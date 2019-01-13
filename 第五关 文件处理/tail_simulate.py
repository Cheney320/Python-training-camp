"""练习：基于seek实现tail -f功能"""

import time
with open('test.txt', 'rb') as f:
    f.seek(0, 2)  # 2代表从文件末尾算起
    while True:
        line = f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)
