def check_dict(**dic):
    """
    功能:检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    :param dic:字典
    :return:如果存在value不是字符串、列表或元组返回-1,否则返回字典
    """
    try:
        for k in dic:
            assert type(dic[k]) in [list, str, tuple]
            if len(dic[k]) > 2:
                dic[k] = dic[k][:2]
        return dic

    except AssertionError:
        print("字典中的value只能是字符串、列表或元组")
        return -1


dic = {"k1": "abcd", "k2": [11,22,33,44], "k3":(1,2,3,4)}
d = check_dict(**dic)
print(d)