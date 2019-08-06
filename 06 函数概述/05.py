"""
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""

def getOddElement(obj):
    l = []
    for i, value in enumerate(obj):
        if i % 2 == 1:
            l.append(value)

    return l

l1 = getOddElement([i for i in range(10)])
print(l1)

l2 = getOddElement((1,2,3,4,5,6))
print(l2)
