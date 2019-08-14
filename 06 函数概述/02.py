def count_str(string):
    """
    功能：计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
    :param string:字符串
    :return:无返回值
    """
    num = 0
    letters = 0
    space = 0
    others = 0

    for c in string:
        if c.isdigit():
            num += 1
        elif c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        else:
            others += 1

    print("{}中有{}个数字，{}个字母，{}个空格，{}个其他字符".format(string, num, letters, space, others))

count_str('fhewio43252  ￥@*&fjwie45')