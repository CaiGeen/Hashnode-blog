import os
import re
import yaml

# 新增：专用名词库（全大写或特定大小写的术语）
PROPER_NOUNS = {
    "chatgpt": "ChatGPT",
    "ai": "AI",
    "llm": "LLM",
    "atimelogger": "aTimeLogger",
    # 可在此添加更多专用名词...
}

def normalize_title(title):
    """规范化标题：处理空格并保护专用名词的大小写"""
    if not title:
        print("Warning: Empty title provided")
        return ""

    # 保存原始标题用于比较
    original_title = title

    # 新增：保护专用名词的大小写
    for lowercase_term, correct_term in PROPER_NOUNS.items():
        title = re.sub(
            re.compile(rf'\b{lowercase_term}\b', re.IGNORECASE),
            correct_term,
            title
        )

    # 在中文和英文之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([a-zA-Z])', r'\1 \2', title)
    title = re.sub(r'([a-zA-Z])([\u4e00-\u9fff])', r'\1 \2', title)

    # 在中文和数字之间添加空格
    title = re.sub(r'([\u4e00-\u9fff])([0-9])', r'\1 \2', title)
    title = re.sub(r'([0-9])([\u4e00-\u9fff])', r'\1 \2', title)

    if title == original_title:
        print(f"Debug: Title already normalized: {title}")
    else:
        print(f"Debug: Normalized title from {original_title} to {title}")

    return title

# 其余代码保持不变...
directory = "./"

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
                        if not title:
                            print(f"Warning: No title found in frontmatter of {filename}")
                            continue

                        print(f"Debug: Processing title: {title}")
                        clean_title = normalize_title(title)
                        if clean_title:
                            new_filename = f"{clean_title}.md"
                            current_base = os.path.splitext(filename)[0]

                            def normalize_for_comparison(s):
                                return re.sub(r'\s+', '', s.lower())

                            current_normalized = normalize_for_comparison(current_base)
                            auto_normalized = normalize_for_comparison(clean_title)

                            if current_normalized == auto_normalized:
                                print(f"Skipping {filename}: filename already matches a normalized version of the title")
                                continue

                            new_filepath = os.path.join(directory, new_filename)
                            if new_filename != filename:
                                if os.path.exists(new_filepath):
                                    base, ext = os.path.splitext(new_filename)
                                    counter = 2
                                    while os.path.exists(new_filepath):
                                        new_filename = f"{base}({counter}){ext}"
                                        new_filepath = os.path.join(directory, new_filename)
                                        counter += 1

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
