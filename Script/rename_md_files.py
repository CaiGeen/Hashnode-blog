import os
import re
import yaml

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
    "q龄": "Q 龄",
    # 在此添加其他需要保护的术语...
}

def normalize_title(title):
    """规范化标题：中文与英文/数字间加空格，保护专用名词大小写，保留标点"""
    if not title:
        print("Warning: Empty title provided")
        return ""
    
    original_title = title
    print(f"Debug: Original title: {title}")
    
    # 在中文和英文之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([a-zA-Z])', r'\1 \2', title)
    title = re.sub(r'([a-zA-Z])([\u4e00-\u9fff])', r'\1 \2', title)
    
    # 在中文和数字之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([0-9])', r'\1 \2', title)
    title = re.sub(r'([0-9])([\u4e00-\u9fff])', r'\1 \2', title)
    
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
    """移除 Markdown 图片链接中的 align='center', align='left', align='right', align="center", align="left", 或 align="right" 属性"""
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

# 遍历目录中的所有 .md 文件，排除 readme.md（不区分大小写）
for filename in os.listdir(directory):
    if filename.lower() != "readme.md" and filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        try:
            # 读取 Markdown 文件内容
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # 提取 frontmatter
            frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
            if frontmatter_match:
                try:
                    frontmatter = yaml.safe_load(frontmatter_match.group(1))
                    title = frontmatter.get('title', '')
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
