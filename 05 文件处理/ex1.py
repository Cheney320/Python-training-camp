"""
练习一
写一个程序在要保持文件内容的顺序不变的前提下，去除文件中重复的行
"""

# 读取文件，去除重复行用列表保存
with open('text.txt', 'r', encoding='utf-8') as f:
    new_lines = []
    for line in f:
        if line not in new_lines:
            new_lines.append(line)

# 将列表内容重写入文件
with open('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)