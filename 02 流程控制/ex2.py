"""
练习二：
写一个打印用户权限的程序，请用户输入用户名来验证
"""

user = input("username>>")
if user == "Albert":
    print("超级管理员")
elif user == "tom":
    print("普通管理员")
elif user in ['jack','rain']:
    print("业务主管")
else:
    print("普通用户")