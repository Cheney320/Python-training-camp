"""练习：基于seek实现tail -f功能"""

"""
该程序将光标定位到文件末尾，然后监测文件最后一行的输入，打开文件在末尾追加一行保存，
程序将实时打印出新增的一行，在mac系统下无法打印输出，在windows系统下正常输出。可
能是因为机器硬件的处理方式不同，windows会动态再去读取硬盘中的数据到内存。

"""
import time
with open('test.txt', 'rb') as f:
    f.seek(0, 2)  # 2代表从文件末尾算起
    while True:
        line = f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)
