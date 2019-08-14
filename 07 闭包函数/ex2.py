"""
编写装饰器，为多个函数加上认证功能，要求登录成功一次，
在超过时间内无需重复登录，超过了超时时间，则必须重新登录
"""

import time


current_user = {'username':None}

with open('user.txt', 'r') as f:
    user_dict = eval(f.read())


def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print('已经登录过了')
            res = func(*args, **kwargs)
            return res

        start_time = time.time()
        name = input("用户名>>:").strip()
        pwd = input("密码>>:").strip()
        end_time = time.time()

        spend_time = end_time - start_time

        if name == user_dict['name'] and pwd == user_dict['password'] \
            and spend_time <= 10:
            current_user['username'] = name
            res = func(*args, **kwargs)
            return res

        else:
            print('登录失败!')

    return wrapper

@auth
def func1():
    print('welcome to func1')

@auth
def func2():
    print('welcome to func2')

@auth
def func3():
    print('welcome to func3')

func1()
func2()
func3()
