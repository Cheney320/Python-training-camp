# 装饰器的使用

"""
强调装饰器的原则：
    1 不修改被装饰对象的源代码
    2 不修改被装饰对象的调用方式
装饰器的目标：
    在遵循1和2的前提下，为被装饰对象添加上新功能
"""

# 无参装饰器
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

@timmer
def foo():
    time.sleep(3)
    print('from foo')
# foo()

"""
不修改原来代码只在代码头部加上@timer，从而完成了程序功能的拓展，
如果新加的代码有问题，只需要把这行注释掉即可，源代码随即恢复
"""

# 有参装饰器
def auth(driver='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            name=input("user: ")
            pwd=input("pwd: ")

            if driver == 'file':
                if name == 'albert' and pwd == '123':
                    print('login successful')
                    res=func(*args,**kwargs)
                    return res
            elif driver == 'ldap':
                print('ldap')
        return wrapper
    return auth2

@auth(driver='file')
def foo(name):
    print(name)

# foo('albert')
"""
有参装饰器就是在原来无参装饰器的基础上，在装饰器外层再次加入一层闭包函数。
"""

# 装饰器的语法
"""
被装饰函数的正上方，单独一行
        @deco1
        @deco2
        @deco3
        def foo():
            pass

        foo=deco1(deco2(deco3(foo)))
"""

"""
在被装饰函数的正上方单独一行添加@装饰器名字，
如果多个装饰器叠加，最先起作用的装饰器距离函数最近，后装饰的装饰器距离函数最远。
"""

from functools import wraps

def deco(func):
    @wraps(func) #加在最内层函数正上方
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@deco
def index():
    '''哈哈哈哈'''
    print('from index')

# print(index.__doc__)

"""
说明：装饰器使用的是闭包函数的原理，返回的是和原来函数同名字的函数地址，再加上()就能调用这个函数，
所以给我们的感觉是原来的函数没有变化，却添加了新的功能，其实已经不是原来的函数了，你可以把以上代码
的第四行注释掉，运行代码，打印结果为None，就是因为你运行的函数已经不是原来的函数了，所以这其实是一
个伪装饰器，要想让装饰器真的是装饰器，调用别人写好的包，返回结果还是原函数，以上写法就是。
"""

# 叠加多个装饰器
# 1. 加载顺序(outter函数的调用顺序):自下而上
# 2. 执行顺序(wrapper函数的执行顺序):自上而下

def outter1(func1): #func1=wrapper2的内存地址
    print('加载了outter1')
    def wrapper1(*args,**kwargs):
        print('执行了wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def outter2(func2): #func2=wrapper3的内存地址
    print('加载了outter2')
    def wrapper2(*args,**kwargs):
        print('执行了wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def outter3(func3): # func3=最原始的那个index的内存地址
    print('加载了outter3')
    def wrapper3(*args,**kwargs):
        print('执行了wrapper3')
        res3=func3(*args,**kwargs)
        return res3
    return wrapper3

@outter1 # outter1(wrapper2的内存地址)======>index=wrapper1的内存地址
@outter2 # outter2(wrapper3的内存地址)======>wrapper2的内存地址
@outter3 # outter3(最原始的那个index的内存地址)===>wrapper3的内存地址
def index():
    print('from index')

print('======================================================')
index()