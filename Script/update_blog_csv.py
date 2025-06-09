import os
import csv
from datetime import datetime
import yaml
import re
from dateutil.parser import parse
from dateutil.tz import tzutc, tzoffset

# 专用名词库
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

# 清理日期字符串，移除括号内的描述性文本
def clean_date_string(date_str):
    if not date_str:
        return date_str
    # 移除括号及其内容，例如 "(Coordinated Universal Time)"
    cleaned = re.sub(r'\s*\([^)]+\)', '', date_str).strip()
    print(f"Debug: Cleaned date from '{date_str}' to '{cleaned}'")
    return cleaned

# 获取脚本所在目录（Script 目录）
script_dir = os.path.dirname(os.path.abspath(__file__))
# 根目录
root_dir = os.path.dirname(script_dir)
print(f"Debug: Root directory: {root_dir}")
# CSV 文件路径（相对于根目录）
CSV_FILE = os.path.join(root_dir, "Table", "Archive of 涂俊杰JunJie blog.csv")
print(f"Debug: CSV file path: {CSV_FILE}")
# 验证 CSV 文件是否存在
print(f"Debug: CSV file exists: {os.path.exists(CSV_FILE)}")
# Markdown 文件在根目录
POSTS_DIR = root_dir

print(f"Debug: Scanning directory: {POSTS_DIR}")
print(f"Debug: Found files: {os.listdir(POSTS_DIR)}")

# 读取现有 CSV 文件内容，避免重复
existing_entries = {}
if os.path.exists(CSV_FILE):
    print(f"Debug: Reading CSV file: {CSV_FILE}")
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳过标题行
        for row in reader:
            if row:
                existing_entries[row[1]] = row  # 以文章链接作为唯一标识
    print(f"Debug: Existing entries: {len(existing_entries)}")
    print(f"Debug: Existing entries content: {existing_entries}")
else:
    print(f"Debug: CSV file does not exist, will create it.")

# 遍历根目录下的 Markdown 文件
new_entries = []
for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        filepath = os.path.join(POSTS_DIR, filename)
        print(f"Debug: Processing file: {filename}")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                # 提取 front matter（YAML 格式）
                front_matter = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
                if front_matter:
                    try:
                        metadata = yaml.safe_load(front_matter.group(1))
                        title = metadata.get("title", "")
                        slug = metadata.get("slug", "")
                        date_published = metadata.get("datePublished", "")

                        print(f"Debug: Extracted title: {title}")
                        print(f"Debug: Extracted slug: {slug}")
                        print(f"Debug: Extracted datePublished: {date_published}")

                        # 规范化标题
                        clean_title = normalize_title(title)

                        # 生成文章链接
                        article_link = f"https://blog.tujunjie.com/{slug}"
                        print(f"Debug: Generated article_link: {article_link}")

                        # 转换日期为 UTC+8 并格式化为 YYYY/MM/DD
                        if date_published:
                            cleaned_date = clean_date_string(date_published)
                            dt = parse(cleaned_date)
                            dt = dt.astimezone(tzoffset(None, 8 * 3600))  # UTC+8 偏移 8 小时
                            pub_date = dt.strftime("%Y/%m/%d")
                        else:
                            pub_date = ""

                        # 检查文章链接是否在 CSV 中
                        if article_link:
                            if article_link in existing_entries:
                                existing_entries[article_link] = [clean_title, article_link, pub_date]
                                print(f"Debug: Updated entry: {existing_entries[article_link]}")
                            else:
                                new_entries.append([clean_title, article_link, pub_date])
                                print(f"Debug: New entry: {new_entries[-1]}")

                    except yaml.YAMLError as e:
                        print(f"Error: Invalid YAML in frontmatter of {filename}: {e}")
                else:
                    print(f"Error: No frontmatter found in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# 强制写入 CSV 文件（调试用）
print(f"Debug: New entries: {new_entries}")
print(f"Debug: Updated existing entries: {[(k, v) for k, v in existing_entries.items() if v[0] != [r for r in existing_entries.values() if r[1] == k][0][0]]}")
if new_entries or any(existing_entries[link][0] != row[0] for link, row in existing_entries.items()):
    print(f"Debug: Writing to CSV with {len(new_entries)} new entries and updated existing entries")
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link", "Date"])
        for entry in existing_entries.values():
            writer.writerow(entry)
        for entry in new_entries:
            writer.writerow(entry)
    print(f"Updated CSV with {len(new_entries)} new entries and updated existing entries")
else:
    print("No new or updated entries to add.")
