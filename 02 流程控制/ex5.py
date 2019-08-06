"""
练习五：
写一个用户猜年龄的游戏，允许用户最多尝试3次，每尝试3次后，
如果还没猜对，就问用户是否还想继续玩，如果回答Y或y，就继续
让其猜3次，以此往复，如果回答N或n，就退出程序。如果猜对了直接退出。
"""

count = 0  # 记录猜测次数
true_age = 21  # 真实年龄

while True:
    age = eval(input("input age>>"))
    count += 1
    if age == true_age:
        print("恭喜你猜对了！")
        break
    elif age > true_age:
        print("猜大了")
    else:
        print("猜小了")
    if count == 3:
        tag = input("已经猜了3次，是否继续玩？")
        if tag == 'Y' or tag == 'y':
            count = 0   # 猜测次数归0
            continue
        if tag == 'N' or tag == 'n':
            break
