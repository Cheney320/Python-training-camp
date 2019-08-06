"""
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
"""

def check_dict(dic):
    try:
        for k in dic:
            assert type(dic[k]) == list or type(dic[k]) == str
            if len(dic[k]) > 2:
                dic[k] = dic[k][:2]
        return dic

    except AssertionError:
        print("字典中的value只能是字符串或列表")
        return -1


dic = {"k1": "v1v1", "k2": [11,22,33,44], "k3":42}
d = check_dict(dic)
print(d)