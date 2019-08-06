"""
练习三
写一个修改文件的程序，要求是原来的内容不能覆盖，修改之后字符之间的空格不能变化(4个空格)
源文件内容如下：
马一特    18    male
刘德华    50    male
林志玲    20    female
修改后的文件：
马一特[Albert)]    18    male
刘德华    50    male
林志玲    20    female
"""

import os

with open('source.txt', 'r') as read_f, \
    open('.source.temp.txt', 'w+') as write_f:

    for line in read_f:
        l = line.split(' '*4)
        if l[0] == '马一特':
            l[0] = '马一特[Albert]'
        line = (' '*4).join(l)
        write_f.write(line)

os.remove('source.txt')
os.rename('.source.temp.txt', 'source.txt')