"""
程序实现功能：用户猜测年龄，根据输出提示进行猜测，
            直到猜对了为止，但是猜测次数不能超
            过6次，超过6次，程序退出，game over~
"""

age = 21
count = 0
while True:
    guess_age = eval(input("请输入年龄:"))
    if guess_age > age:
        print("年龄猜大了")
    if guess_age < age:
        print("年龄猜小了")
    if guess_age == age:
        print("恭喜你，猜对了！")
        break
    count += 1
    if count > 6:
        print("猜测次数超过6次，game over...")
        break
