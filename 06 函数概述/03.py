def assert_length(obj):
    """
    功能:判断用户传入的对象（字符串、列表、元组）长度是否大于5。
    :param obj:对象(字符串、列表、元组)
    :return:无返回值
    """
    try:
        assert len(obj) > 5

    except AssertionError:
        print("长度不大于5")

    else:
        print("长度大于5")

assert_length([1,2,3,4,5,6])

assert_length('fhewj')

assert_length((1,2,3,4,5,6))
