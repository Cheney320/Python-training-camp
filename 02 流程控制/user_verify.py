"""
写一个用户认证程序，有三组用户名和密码，每当任意一个用户密码输入错误三次则对该用户
进行限制，禁止登录。
"""

data_dict = {'San': '123', 'Chen': 'e3178', 'Joe': '32ry89'}
ban_user = []
login = False

while True:

    for i in range(3):
        user = input("请输入用户名:")
        if user not in data_dict:
            print("不存在该用户")
            break
        password = input("请输入密码:")
        if data_dict[user] == password and user not in ban_user:
            print("登录成功！")
            login = True
            break
        if data_dict[user] != password:
            print("密码错误！")
        if user in ban_user:
            print("{}密码输入错误三次！禁止登录".format(user))

    else:
        ban_user.append(user)
        print("{}密码输入错误三次！禁止登录".format(user))

    if login == True:
        break
