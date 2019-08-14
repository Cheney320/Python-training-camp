# 2 验证内置模块的查找
import sys

print('time' in sys.modules)  # sys.modules存放内存中被导入的模块

import time  # 内置模块默认在硬盘，导入之后才会进入内存


time.sleep(3)  # 可以用time模块证明：模块查找先查找的内置模块

print('time' in sys.modules)


