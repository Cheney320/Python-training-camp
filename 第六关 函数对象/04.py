"""
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""

def assert_len(alist):

    if len(alist) > 2:
        alist = alist[:2]

    return alist

l = [i for i in range(10)]
new_l = assert_len(l)
print(new_l)

    