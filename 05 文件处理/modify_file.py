"""
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

2. 修改文件内容，把文件中的mac都替换成linux
"""

import os

with open('a.txt', 'r') as read_f, open('.a.txt.swap', 'w+') as write_f:
    s = 0
    for line in read_f:
        tmp = line.split(' ')
        s += eval(tmp[1]) * eval(tmp[2])
        if 'mac' in line:
            line = line.replace('mac', 'linux')
        write_f.write(line)
    print("总钱数:{}元".format(s))

os.remove('a.txt')
os.rename('.a.txt.swap', 'a.txt')
