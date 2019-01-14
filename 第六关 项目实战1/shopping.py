"""
#需求:
    用户名和密码存放于文件中，格式为：Albert|Albert123
    启动程序后，先登录，登录成功则让用户选择是否充钱, 然后打印商品列表，失败则重新登录，
    超过三次则退出程序,并将用户名添加到黑名单，再次启动程序登陆该用户名，提示用户禁止登陆
    允许用户根据商品编号购买商品
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
"""

import os

login = False  # 登录状态
login_cnt = {}  # 存放每个用户登录次数
user_money = {}  # 存放每个用户账户余额
user = None  # 当前用户
buy_history = {'购买': [], '余额': []}  # 购买商品和余额

with open('users.txt', encoding='utf-8') as f:
    for line in f:
        if line != '\n':
            login_cnt[line.split('|')[0]] = 0  # 初始化每个用户登录次数为0
            user_money[line.split('|')[0]] = eval(line.split('|')[2])

with open('ban_users.txt') as f:
    ban_users = f.read().split(' ')

while not login:
    while True:
        user = input("请输入用户名：")
        if user in login_cnt.keys() and user not in ban_users:
            break
        if user in ban_users and user != '':
            print('用户名在黑名单，禁止登录！')
        if user not in login_cnt.keys() and user != '':
            print("用户不存在！")
        if user == '':
            print("输入不得为空！")
    password = input("请输入密码：")
    login_cnt[user] += 1
    with open('users.txt', encoding='utf-8') as f_read:
        for line in f_read:
            if line.split('|')[0] == user and line.split('|')[1] == password:
                login = True
                break
    with open('ban_users.txt', 'a+', encoding='utf-8') as f_write:
        if login_cnt[user] > 3:
            print("输入错误超过3次，您已加入黑名单，禁止登录！")
            f_write.write(user+' ')
            break

# 登录状态

while login:
    # 读入商品信息
    with open('products.txt', encoding='utf-8') as f:
        products = f.readlines()
    choice = input("{}登录成功！输入1充钱，输入2开始购物，输入q退出系统：".format(user))
    if choice == '1':
        money = input("请输入金额：(q退出系统)")
        if money == 'q':
            break
        user_money[user] += eval(money)
        print("{}当前余额为{}".format(user, user_money[user]))
        print('*****商品信息*****')
        print(''.join(products))

    if choice == '2':
        print("*****商品信息*****")
        print(''.join(products))

    if choice == 'q':
        break

    flag = 'c'
    while flag == 'c':
        num = input("请输入商品编号：")
        for i in products:
            if num == i.split('|')[0]:
                if user_money[user] >= eval(i.split('|')[2]):
                    user_money[user] -= eval(i.split('|')[2])
                    buy_history['购买'].append(i.split('|')[1])
                else:
                    print("余额不足！")

        flag = input("是否继续购买？q退出，c继续：")
        if flag == 'q':
            break
    if flag == 'q':
        break

# 如果登录过系统则输出购买记录
if login:
    # 打印已购买商品和余额
    buy_history['余额'] = user_money[user]
    print(buy_history)

    # 更新余额信息到users.txt文件
    with open('users.txt') as f_read, open('users.txt.swap', 'w') as f_write:
        for line in f_read:
            if line.split('|')[0] == user:
                line = line.split('|')
                line[2] = str(buy_history['余额'])
                line = '|'.join(line)
            if line != '\n':
                f_write.write(line.strip('\n')+'\n')
    os.remove('users.txt')
    os.rename('users.txt.swap', 'users.txt')









