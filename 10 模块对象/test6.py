# 3 sys.path路径包含的模块

import sys
print(sys.path)

# 如果把spam1.py文件移动到当前目录的x文件夹下
sys.path.append('/Users/huangchen/Documents/Python-training-camp/10 模块对象/x')

print(sys.path)

import spam1

spam1.f1()