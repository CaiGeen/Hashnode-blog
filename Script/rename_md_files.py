import os
import re
import yaml

# 专用名词库（保持不变）
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
    "TTS": "TTS",
    "ema": "EMA",
}

def normalize_title(title):
    """规范化标题：中文与英文/数字间加空格，保护专用名词大小写，保留标点"""
    if not title:
        print("Warning: Empty title provided")
        return ""
    
    # 移除文件名中不安全的字符，例如 '/', ':', '?' 等
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    
    original_title = title
    
    # 在中文和英文/数字之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([a-zA-Z0-9])', r'\1 \2', title)
    title = re.sub(r'([a-zA-Z0-9])([\u4e00-\u9fff])', r'\1 \2', title)
    
    # 专用名词替换
    for term, replacement in PROPER_NOUNS.items():
        pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
        title = pattern.sub(replacement, title)
        
    print(f"Debug: Normalized '{original_title}' to '{title}'")
    return title

def clean_image_links(content):
    """移除 Markdown 图片链接中的 align 属性"""
    # 这个函数逻辑没问题，保持原样
    pattern = re.compile(r'!\[(.*?)\]\((https?://[^\s)]+)(?:\s+align=(?:\"(?:center|left|right)\"|\'(?:center|left|right)\'))?\)')
    
    def replace_image(match):
        alt, url = match.group(1), match.group(2)
        return f'![{alt}]({url})'
        
    cleaned_content = pattern.sub(replace_image, content)
    return cleaned_content

# --- 主逻辑开始 ---

directory = "./"
operations = [] # 存储计划的操作
target_filenames = {} # 跟踪目标文件名，用于检测冲突

# --- Pass 1: Scan and Plan ---
print("--- Starting Pass 1: Scanning files and planning operations ---")
for filename in os.listdir(directory):
    if filename.lower() == "readme.md" or not filename.endswith(".md"):
        continue

    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            print(f"Warning: No frontmatter found in {filename}. Skipping.")
            continue

        frontmatter = yaml.safe_load(frontmatter_match.group(1))
        title = frontmatter.get('title', '')
        
        if not title:
            print(f"Warning: No title found in frontmatter of {filename}. Skipping.")
            continue
            
        clean_title = normalize_title(str(title)) # 确保 title 是字符串
        if not clean_title:
            print(f"Warning: Normalization resulted in an empty title for {filename}. Skipping.")
            continue

        new_filename = f"{clean_title}.md"
        
        # 检查目标文件名是否已计划用于其他文件
        if new_filename in target_filenames:
            print(f"ERROR: Duplicate title detected! Both '{filename}' and '{target_filenames[new_filename]}' want to be renamed to '{new_filename}'. Please resolve the title conflict.")
            # 决定是中止还是跳过，这里选择跳过当前文件
            continue
        else:
            target_filenames[new_filename] = filename

        # 计划文件操作
        operations.append({
            'original_filename': filename,
            'original_filepath': filepath,
            'new_filename': new_filename,
            'new_filepath': os.path.join(directory, new_filename),
            'original_content': content
        })

    except Exception as e:
        print(f"Error processing {filename} in Pass 1: {e}")


# --- Pass 2: Execute Operations ---
print("\n--- Starting Pass 2: Executing planned operations ---")
for op in operations:
    try:
        # 清理图片链接
        cleaned_content = clean_image_links(op['original_content'])
        
        # 检查是否需要重命名
        if op['original_filename'] == op['new_filename']:
            print(f"No rename needed for {op['original_filename']}.")
            # 如果内容有变动，仍需写回文件
            if cleaned_content != op['original_content']:
                with open(op['original_filepath'], 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)
                print(f"Updated image links in {op['original_filename']}.")
        else:
            # 执行重命名和内容写入
            print(f"Renaming {op['original_filename']} to {op['new_filename']}")
            
            # 先写入新文件，再删除旧文件，更安全
            with open(op['new_filepath'], 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            os.remove(op['original_filepath'])
            
            print(f"Successfully renamed and updated {op['original_filename']} to {op['new_filename']}.")
            
    except Exception as e:
        print(f"Error executing operation for {op['original_filename']}: {e}")

print("\n--- Script finished ---")
