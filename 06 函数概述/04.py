def assert_len(l):
    """
    功能:检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    :param l:列表
    :return:如果列表长度大于2返回前两个长度内容，否则返回原列表
    """
    if len(l) > 2:
        l = l[:2]

    return l

l = [i for i in range(10)]
new_l = assert_len(l)
print(new_l)

    