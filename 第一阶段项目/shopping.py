"""
需求：
    用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
        已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
                登录过程中，用户密码输入超过三次则退出程序，
                并将用户名添加到黑名单，再次启动程序登录该用户名，提示用户禁止登录
        未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
                注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
    1  iPhone
    2  macbook
    3  bike
    用户选择商品后，检测余额是否够，够就直接扣款，修改文件中用户余额，不够就提醒可随时退出，
    退出时，打印已购买商品和余额。
"""

import os

tag = True
count = {}   # 记录用户密码输入次数
products = {'iPhone':5000, 'macbook':13000, 'bike':8000}
id_to_products = {}  # 将编号与商品对应
current_account = {}   # 存储当前用户余额
buying_list = {}   # 已购商品
login = False   # 记录登录状态
all_users = []   # 保存所有用户名，为注册判断是否重名

print("欢迎进入购物商城".center(50, '='))

while tag:
    global user
    print("1: 登录    2:注册")
    choice = input("请选择:>>").strip()
    try:
        assert choice in ['1','2']
    except:
        print("输入错误!")
        continue
    if choice == '1':
        print("欢迎进入登录程序".center(30, '*'))
        while tag:
            user = input("请输入用户名:>>").strip()
            pwd = input("请输入密码:>>").strip()

            if user == '' or pwd == '':
                print("输入不能为空!")
                continue

            with open('ban_users.txt', 'a+') as f:
                f.seek(0)
                ban_list = f.readlines()
                ban_list = [i.strip('\n') for i in ban_list]
                if user in ban_list:
                    print("您已在黑名单!禁止登录!")
                    tag = False
                    break
                if user in count:
                    count[user] += 1
                else:
                    count[user] = 1

                if count[user] == 3:
                    print("登录次数已达3次，您已经加入黑名单!")
                    f.write(user+'\n')
                    tag = False
                    break

            with open('users.txt', 'a+', encoding='utf-8') as f:
                f.seek(0)
                for line in f:
                    name = line.split('|')[0]
                    all_users.append(name)
                    if user == name:
                        if pwd == line.split('|')[1]:
                            print(("{}登录成功！开始购物之旅吧！".format(user)).center(30, '*'))
                            login = True
                            current_account[user] = eval(line.split('|')[2])
                            break
                        else:
                            print("密码错误!")
                            break

                else:
                    print("{}用户不存在,请先注册!".format(user))
                    break

            if login:break

        if login:
            while tag:
                # 打印商品信息
                for k, i in zip(products, range(len(products))):
                    print("{}{}{}".format(i + 1, ' ' * 5, k))
                    id_to_products[i + 1] = k
                try:
                    id = input("请输入商品编号:>>").strip()
                    num = input("请输入购买数量:>>").strip()
                    product = id_to_products[eval(id)]
                    price = products[product] * eval(num)
                    if price <= current_account[user]:
                        current_account[user] -= price
                        print("购买成功!")
                        if product not in buying_list:
                            buying_list[product] = eval(num)
                        else:
                            buying_list[product] += eval(num)

                    else:
                        print("余额不足!")
                        while tag:
                            flag = input("充值输入y,q退出系统:>>").strip()
                            if flag == 'y':
                                break
                            elif flag == 'q':
                                tag = False
                                break
                            else:
                                continue
                        if not tag: break
                        while tag:
                            try:
                                money = input("请输入充值金额:>>").strip()
                                assert eval(money) > 0
                                current_account[user] += eval(money)
                                print("充值成功!余额:{}元".format(current_account[user]))
                                break
                            except:
                                print("输入错误!")
                                continue

                    while tag:
                        flag = input("是否继续购买(y继续,q退出):>>")
                        if flag == 'q':
                            tag = False
                            break
                        elif flag == 'y':
                            break
                        else:
                            print("输入错误!")
                            continue
                except:
                    print("输入错误!")
                    continue

    if choice == '2':
        print("欢迎进入注册程序".center(30, '*'))
        info = []   # 存储注册信息
        while tag:
            user = input("请输入用户名:>>")
            pwd = input("请输入密码:>>")
            verified_pwd = input("请再次输入密码:>>")
            if user in all_users:
                print("该用户名已存在！")
                continue
            if user == '' or pwd == '':
                print("输入不能为空")
                continue
            if pwd == verified_pwd:
                info.extend([user, pwd])
                break

        while tag:
            money = input("请输入充值金额:>>")
            try:
                assert eval(money) > 0
            except:
                print("输入错误!")
                continue
            info.append(money)
            break
        # 将注册信息写入文件
        with open('users.txt','a+', encoding='utf-8') as f:
            f.write('|'.join(info)+'\n')
        print("注册成功！")


print("欢迎下次光临!".center(50,'='))

if login:
    print("已购商品清单".center(30, '-'))
    print("商品{}数量".format(' '*27))

    user = None
    account = None
    for k in buying_list:
        l = len("{}{}".format(k, buying_list[k]))
        print("{}{}{}".format(k, ' '*(33-l), buying_list[k]), end='\n')

    for k in current_account:
        user = k
        account = current_account[k]

    print('-'*33)
    print("{},您的余额:{}元".format(user, account))

    # 修改users.txt中的余额
    with open('users.txt', 'r') as f_read, \
        open('.users_temp.txt', 'w') as f_write:
        for line in f_read:
            info = line.split('|')
            if info[0] == user:
                info[2] = str(account)+'\n'
                line = '|'.join(info)
            f_write.write(line)
    os.remove('users.txt')
    os.rename('.users_temp.txt','users.txt')














