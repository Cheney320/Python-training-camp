"""
编写装饰器，为多个函数加上认证的功能(用户的账号密码来源于文件)。
要求：登录成功一次，后续的函数都无需要再输入用户名和密码。
"""

current_user = {'username':None}

with open('user.txt', 'r') as f:
    user_dict = eval(f.read())

def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print("已经登录过了")
            res = func(*args, **kwargs)
            return res

        name = input("用户名>>:").strip()
        pwd = input("密码>>:").strip()
        if name == user_dict['name'] and pwd == user_dict['password']:
            print("登录成功")
            current_user['username'] = name
            res = func(*args, **kwargs)
            return res
        else:
            print("用户名或密码错误")

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

