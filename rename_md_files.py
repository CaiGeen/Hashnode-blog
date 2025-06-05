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
    # 在此添加其他需要保护的术语...
}

def normalize_title(title):
    """规范化标题：中文与英文/数字间加空格，保护专用名词大小写"""
    if not title:
        print("Warning: Empty title provided")
        return ""
    
    original_title = title
    
    # 先在中文和英文之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([a-zA-Z])', r'\1 \2', title)
    title = re.sub(r'([a-zA-Z])([\u4e00-\u9fff])', r'\1 \2', title)
    
    # 在中文和数字之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([0-9])', r'\1 \2', title)
    title = re.sub(r'([0-9])([\u4e00-\u9fff])', r'\1 \2', title)
    
    print(f"Debug: After adding spaces: {title}")
    
    # 构建专用名词替换的正则表达式
    terms = sorted(PROPER_NOUNS.keys(), key=len, reverse=True)  # 按长度降序
    pattern = re.compile(
        r'(?:^|\s|[\u4e00-\u9fff\p{P}])(?:' + '|'.join(re.escape(term) for term in terms) + r')(?:$|\s|[\u4e00-\u9fff\p{P}])',
        re.IGNORECASE | re.UNICODE
    )
    
    def replace_term(match):
        # 提取匹配的术语（去除前后边界）
        matched = match.group(0)
        # 查找术语（忽略大小写）
        for term in PROPER_NOUNS:
            if matched.lower().strip(' \t\n\r,.?!;:/').startswith(term):
                replaced = PROPER_NOUNS[term]
                print(f"Debug: Replaced term '{matched.strip()}' with '{replaced}'")
                return matched[0] + replaced + matched[-1] if len(matched) > len(term) else replaced
        print(f"Debug: No replacement for term '{matched}'")
        return matched
    
    title = pattern.sub(replace_term, title)
    
    # 如果标题未改变，说明已符合规范
    if title == original_title:
        print(f"Debug: Title already normalized: {title}")
    else:
        print(f"Debug: Normalized title from {original_title} to {title}")
    
    return title

# 设置目录为仓库根目录
directory = "./"

# 遍历目录中的所有 .md 文件，排除 readme.md（不区分大小写）
for filename in os.listdir(directory):
    if filename.lower() != "readme.md" and filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        try:
            # 读取 Markdown 文件的 frontmatter
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # 提取 frontmatter（假设 frontmatter 以 --- 开头和结尾）
                frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
                if frontmatter_match:
                    try:
                        frontmatter = yaml.safe_load(frontmatter_match.group(1))
                        title = frontmatter.get('title', '')
                        if not title:
                            print(f"Warning: No title found in frontmatter of {filename}")
                            continue
                        
                        print(f"Debug: Processing title: {title}")
                        # 规范化标题
                        clean_title = normalize_title(title)
                        if clean_title:
                            new_filename = f"{clean_title}.md"
                            current_base = os.path.splitext(filename)[0]
                            
                            # 标准化比较（忽略大小写和空格）
                            def normalize_for_comparison(s):
                                return re.sub(r'\s+', '', s).lower()
                            
                            current_normalized = normalize_for_comparison(current_base)
                            auto_normalized = normalize_for_comparison(clean_title)
                            
                            # 如果文件名与标题标准化后相等，认为是人工修改，跳过
                            if current_normalized == auto_normalized:
                                print(f"Skipping {filename}: filename matches normalized title '{clean_title}'")
                                continue
                            
                            new_filepath = os.path.join(directory, new_filename)
                            
                            # 检查是否需要重命名（避免覆盖同名文件）
                            if new_filename != filename:
                                if os.path.exists(new_filepath):
                                    base, ext = os.path.splitext(new_filename)
                                    counter = 2
                                    while os.path.exists(new_filepath):
                                        new_filename = f"{base}({counter}){ext}"
                                        new_filepath = os.path.join(directory, new_filename)
                                        counter += 1
                                    
                                # 重命名文件
                                os.rename(filepath, new_filepath)
                                print(f"Renamed {filename} to {new_filename}")
                            else:
                                print(f"No rename needed for {filename}: already matches title")
                        else:
                            print(f"Warning: Empty normalized title for {filename}")
                    except yaml.YAMLError as e:
                        print(f"Error: Invalid YAML in frontmatter of {filename}: {e}")
                else:
                    print(f"Error: No frontmatter found in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
