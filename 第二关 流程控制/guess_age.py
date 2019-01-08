"""
写一个用户循环猜年龄的游戏，猜对就退出，猜不对就继续猜，猜三次，提示用户是否继续，
用户回答Y或y就继续猜，三次之后再次重复，回答N或者n就结束游戏。
"""

age = 18
count = 0
while True:
    guess_age = eval(input("请猜测年龄:"))
    if guess_age == age:
        print("猜对了！")
        break
    print("猜错了！")
    count += 1
    if count == 3:
        flag = input("已经猜了3次，是否继续？Y或y继续，N或n结束:")
        if flag == 'N' or flag == 'n':
            break
        if flag == 'Y' or flag == 'y':
            count = 0
