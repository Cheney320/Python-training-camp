"""
练习一：
写一个用户登录认证的程序，比如用户名是"Albert"，密码是"1"，请用户分别输入
用户名和密码来认证
"""

true_user = 'Albert'
true_pwd = 1
while True:
    user = input("username>>")
    password = input("password>>")
    if user==true_user and password==str(true_pwd):
        print("login successfully!")
        break
    else:
        print("username or password error!please input again!")