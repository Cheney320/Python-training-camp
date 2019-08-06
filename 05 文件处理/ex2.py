"""
练习二
写一个在终端执行拷贝文件的命令，文件不仅限于文本文件，要求是：在终端环境下输入命令：
python(或者python3) Python文件路径 源文件路径 目标文件路径
比如：
python /Users/albert/Desktop/02/02.py /Users/albert/Desktop/02/a.jpg /Users/albert/Desktop/b.jpg
"""

import sys

# 规范输入参数
if len(sys.argv) != 3:
    print("usage:python python_file source_file target_file")
    sys.exit()

source_file, target_file = sys.argv[1], sys.argv[2]
with open(source_file, 'rb') as read_f, open(target_file, 'wb') as write_f:
    for line in read_f:
        write_f.write(line)