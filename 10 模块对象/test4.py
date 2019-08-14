"""
模块搜索查找的顺序
1、内存中已经加载的模块
2、内置模块
3、sys.path路径中包含的模块
"""

# 1 验证先查找内存中加载的模块
import time

from x import spam1

spam1.f1()

time.sleep(15)  # 15秒时间从硬盘删除spam1.py

spam1.f1()



