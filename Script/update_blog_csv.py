import os
import csv
from datetime import datetime
import yaml
import re
from dateutil.parser import parse
from dateutil.tz import tzutc, tzoffset

# 获取脚本所在目录（Script 目录）
script_dir = os.path.dirname(os.path.abspath(__file__))
# 根目录
root_dir = os.path.dirname(script_dir)
# CSV 文件路径（相对于根目录）
CSV_FILE = os.path.join(root_dir, "Table", "Archive of 涂俊杰JunJie blog.csv")
# Markdown 文件在根目录
POSTS_DIR = root_dir

# 读取现有 CSV 文件内容，避免重复
existing_entries = {}
if os.path.exists(CSV_FILE):
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳过标题行
        for row in reader:
            if row:
                existing_entries[row[1]] = row  # 以文章链接作为唯一标识

# 遍历根目录下的 Markdown 文件
new_entries = []
for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            # 提取 front matter（YAML 格式）
            front_matter = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
            if front_matter:
                metadata = yaml.safe_load(front_matter.group(1))
                title = metadata.get("title", "")
                slug = metadata.get("slug", "")
                date_published = metadata.get("datePublished", "")

                # 生成文章链接
                article_link = f"https://blog.tujunjie.com/{slug}"

                # 转换日期为 UTC+8 并格式化为 YYYY/MM/DD
                if date_published:
                    # 解析日期（UTC 时间）
                    dt = parse(date_published)
                    # 转换为 UTC+8
                    dt = dt.astimezone(tzoffset(None, 8 * 3600))  # UTC+8 偏移 8 小时
                    pub_date = dt.strftime("%Y/%m/%d")
                else:
                    pub_date = ""

                # 如果文章链接不在现有 CSV 中，添加新条目
                if article_link and article_link not in existing_entries:
                    new_entries.append([title, article_link, pub_date])

# 如果有新文章，追加到 CSV 文件
if new_entries:
    with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for entry in new_entries:
            writer.writerow(entry)
    print(f"Added {len(new_entries)} new entries to {CSV_FILE}")
else:
    print("No new entries to add.")
