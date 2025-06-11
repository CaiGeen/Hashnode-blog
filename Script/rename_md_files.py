import os
import re
import yaml
from datetime import datetime

# 专用名词库（全大写或特定大小写的术语）
PROPER_NOUNS = {
    "ai": "AI",
    "chatgpt": "ChatGPT",
    "llm": "LLM",
    "atimelogger": "aTimeLogger",
    "qq": "QQ",
    "roi": "ROI",
    "ted": "TED",
    "gafata": "GAFATA",
    "TradingView": "TradingView",
    "Claude": "Claude",
    "SEO": "SEO",
    "Xmind": "Xmind",
    "SergeiZaplitny": "Sergei Zaplitny",
    "404 KIDS SEE GHOSTS": "404 KIDS SEE GHOSTS",
    "CNZZ": "CNZZ",
}

def normalize_title(title):
    """规范化标题：中文与英文/数字间加空格，保护专用名词大小写，保留标点"""
    if not title:
        print("Warning: Empty title provided")
        return ""
    
    original_title = title
    print(f"Debug: Original title: {title}")
    
    # 在中文和英文之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])(?=[a-zA-Z])', r'\1 ', title)
    title = re.sub(r'([a-zA-Z])(?=[\u4e00-\u9fff])', r'\1 ', title)
    
    # 在中文和数字之间添加空格，仅当直接相邻
    title = re.sub(r'([\u4e00-\u9fff])(?=\d)', r'\1 ', title)
    title = re.sub(r'(\d)(?=[\u4e00-\u9fff])', r'\1 ', title)
    
    print(f"Debug: After adding spaces: {title}")
    
    # 专用名词替换，使用词边界确保精确匹配
    for term, replacement in PROPER_NOUNS.items():
        pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
        matches = pattern.finditer(title)
        for match in matches:
            print(f"Debug: Found term '{match.group(0)}' at position {match.start()}-{match.end()}")
        title = pattern.sub(replacement, title)
    
    print(f"Debug: After proper noun replacement: {title}")
    
    # 如果标题未改变，说明已符合规范
    if title == original_title:
        print(f"Debug: Title already normalized: {title}")
    else:
        print(f"Debug: Normalized title from {original_title} to {title}")
    
    return title

def clean_image_links(content):
    """移除 Markdown 图片链接中的 align='center', align='left', align='right', align=\"center\", align=\"left\", 或 align=\"right\" 属性"""
    pattern = re.compile(r'!\[(.*?)\]\((https?://[^\s)]+)(?:\s+align=(?:\"(?:center|left|right)\"|\'(?:center|left|right)\'))?\)')
    
    def replace_image(match):
        alt = match.group(1)
        url = match.group(2)
        original = match.group(0)
        cleaned = f'![{alt}]({url})'
        print(f"Debug: Cleaned image link from '{original}' to '{cleaned}'")
        return cleaned
    
    cleaned_content = pattern.sub(replace_image, content)
    
    if cleaned_content == content:
        print("Debug: No image links with align='center', align='left', align='right', align=\"center\", align=\"left\", or align=\"right\" found in content")
    
    return cleaned_content

# 设置目录为仓库根目录
directory = "./"

# 收集所有 .md 文件的元数据
md_files = []
for filename in os.listdir(directory):
    if filename.lower() != "readme.md" and filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
                if frontmatter_match:
                    try:
                        frontmatter = yaml.safe_load(frontmatter_match.group(1))
                        title = frontmatter.get('title', '')
                        date_published = frontmatter.get('datePublished', '')
                        if date_published:
                            # 提取日期部分 "Fri Jul 28 2023 05:42:08"
                            date_match = re.match(r'(\w{3} \w{3} \d{2} \d{4} \d{2}:\d{2}:\d{2})', date_published)
                            if date_match:
                                date_str = date_match.group(1)
                                date = datetime.strptime(date_str, '%a %b %d %Y %H:%M:%S')
                                formatted_date = date.strftime('%Y/%m/%d %H:%M:%S')
                                print(f"Debug: Collected {filename} with date {date_published} parsed as {formatted_date}")
                            else:
                                date = None
                                print(f"Debug: Collected {filename} with date {date_published} parsing failed, using None")
                        else:
                            date = None
                            print(f"Debug: Collected {filename} with no datePublished")
                        md_files.append((filepath, title, date))
                    except yaml.YAMLError as e:
                        print(f"Error: Invalid YAML in frontmatter of {filename}: {e}")
                else:
                    print(f"Error: No frontmatter found in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# 按 datePublished 降序排序，空日期置后
md_files.sort(key=lambda x: x[2] if x[2] else None, reverse=True)

# 按排序结果处理文件
for filepath, title, date in md_files:
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
            if frontmatter_match:
                try:
                    frontmatter = yaml.safe_load(frontmatter_match.group(1))
                    cuid = frontmatter.get('cuid', '')
                    
                    if not title:
                        print(f"Warning: No title found in frontmatter of {filename}")
                        continue
                    
                    if not cuid:
                        print(f"Warning: No cuid found in frontmatter of {filename}")
                    
                    print(f"Debug: Processing file: {filename}")
                    print(f"Debug: Processing title: {title}")
                    
                    # 规范化标题
                    clean_title = normalize_title(title)
                    if clean_title:
                        new_filename = f"{clean_title}.md"
                        
                        # 检测文件名是否为人为修改（不匹配 cuid 且不匹配规范化 title）
                        base_filename = os.path.splitext(filename)[0]
                        if cuid and base_filename.lower() != cuid.lower() and base_filename.lower() != clean_title.lower():
                            print(f"Skipping rename for {filename}: filename does not match cuid {cuid} or normalized title {clean_title}")
                            # 仍需清理图片链接
                            cleaned_content = clean_image_links(content)
                            if cleaned_content != content:
                                with open(filepath, 'w', encoding='utf-8') as file:
                                    file.write(cleaned_content)
                                print(f"Updated image links in {filename}")
                            continue
                        
                        # 检查是否需要重命名（直接比较文件名）
                        if new_filename != filename:
                            new_filepath = os.path.join(directory, new_filename)
                            
                            # 避免文件名冲突
                            if os.path.exists(new_filepath):
                                base, ext = os.path.splitext(new_filename)
                                counter = 2
                                while os.path.exists(new_filepath):
                                    new_filename = f"{base}({counter}){ext}"
                                    new_filepath = os.path.join(directory, new_filename)
                                    counter += 1
                            
                            # 清理图片链接
                            cleaned_content = clean_image_links(content)
                            
                            # 重命名文件并写入清理后的内容
                            with open(new_filepath, 'w', encoding='utf-8') as file:
                                file.write(cleaned_content)
                            os.remove(filepath)
                            print(f"Renamed {filename} to {new_filename} and updated image links")
                        else:
                            print(f"No rename needed for {filename}: already matches title")
                            # 仍需清理图片链接
                            cleaned_content = clean_image_links(content)
                            if cleaned_content != content:
                                with open(filepath, 'w', encoding='utf-8') as file:
                                    file.write(cleaned_content)
                                print(f"Updated image links in {filename}")
                    else:
                        print(f"Warning: Empty normalized title for {filename}")
                except yaml.YAMLError as e:
                    print(f"Error: Invalid YAML in frontmatter of {filename}: {e}")
            else:
                print(f"Error: No frontmatter found in {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
