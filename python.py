# 打开源文件并读取内容
with open('dns.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 去除重复内容并保持顺序，确保完整行内容比较
unique_lines = []
seen = set()
for line in lines:
    line = line.rstrip()  # 去掉行尾多余的换行符
    if line not in seen:  # 如果该行未被记录为重复，添加到结果中
        unique_lines.append(line)
        seen.add(line)  # 标记该行已经出现过

# 将去重后的内容写入一个新的文件
with open('dns_cleaned.txt', 'w', encoding='utf-8') as new_file:
    new_file.write('\n'.join(unique_lines))

print("重复内容已去除，结果已保存到 'dns_cleaned.txt' 文件中。")
