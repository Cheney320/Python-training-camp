"""
练习四：
写一个循环验证用户登录的程序，用户验证登录成功后，输入"q"退出程序，
用户认证失败后重复让用户执行登录操作，当用户重复次数超过3次仍没有登录成功，则退出程序
"""

count = 0  # 记录用户输入次数
true_user = "Chen"
true_pwd = '123'

while count < 3:
    user = input("username>>")
    password = input("password>>")
    count += 1
    if user == true_user and password == true_pwd:
        print("login successfully!")
        flag = input("input q to quit>>")
        if flag == 'q':
            break
else:
    print("login unsuccessfully!")