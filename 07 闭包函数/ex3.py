"""
编写日志装饰器，实现功能：一旦某函数执行，
则将函数执行时间写入到日志文件中，日志文件路径可以指定。
"""

import datetime
import time

def timer(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        res = func(*args, **kwargs)
        with open('log.txt', 'a+') as f:
            f.write('{}:{}\n'.format(func, now.strftime("%Y-%m-%d %H:%M:%S")))
        return res

    return wrapper


@timer
def func1():
    print('welcome to func1')

@timer
def func2():
    print('welcome to func2')

func1()
time.sleep(10)
func2()


