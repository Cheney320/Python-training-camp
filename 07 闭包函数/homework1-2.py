import time
import random

# 编写装饰器，为函数加上统计时间的功能
def timmer(func):
    def wrapper():
        start_time = time.time()
        res = func()
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return res
    return wrapper

# 编写函数，函数执行的时间是随机的
@timmer
def fun():
    time.sleep(random.randint(1,10))

fun()