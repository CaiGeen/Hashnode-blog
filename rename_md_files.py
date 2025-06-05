import os
import re
import yaml

# 设置目录为仓库根目录
directory = "./"
# 指定要处理的文件
target_file = "clbc9kt1o000508mn3x6gdpup.md"

# 检查目标文件是否存在
filepath = os.path.join(directory, target_file)
if os.path.exists(filepath) and filepath.endswith(".md"):
    try:
        # 读取 Markdown 文件的 frontmatter
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # 提取 frontmatter（假设 frontmatter 以 --- 开头和结尾）
            frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
            if frontmatter_match:
                frontmatter = yaml.safe_load(frontmatter_match.group(1))
                title = frontmatter.get('title', '')
                
                # 清理标题以用作文件名（移除非法字符并替换空格）
                if title:
                    clean_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-').lower()
                    new_filename = f"{clean_title}.md"
                    new_filepath = os.path.join(directory, new_filename)
                    
                    # 检查是否需要重命名（避免覆盖同名文件）
                    if new_filename != target_file:
                        if os.path.exists(new_filepath):
                            # 如果文件已存在，添加后缀以避免冲突
                            base, ext = os.path.splitext(new_filename)
                            counter = 1
                            while os.path.exists(new_filepath):
                                new_filename = f"{base}-{counter}{ext}"
                                new_filepath = os.path.join(directory, new_filename)
                                counter += 1
                        
                        # 重命名文件
                        os.rename(filepath, new_filepath)
                        print(f"Renamed {target_file} to {new_filename}")
                    else:
                        print(f"No rename needed for {target_file}: already matches title")
            else:
                print(f"No frontmatter found in {target_file}")
    except Exception as e:
        print(f"Error processing {target_file}: {e}")
else:
    print(f"File {target_file} not found or is not a .md file")
