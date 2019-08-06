# coding:gbk

# 解释器已经切换到Python2

x = "上"
print(type(x))  # str类型
print([x, ])  # 以gbk编码保存
print([x.decode('gbk'), ])  # 解码后就是unicode，与下面保存的字符编码一致

y = u'上'  # 定义字符串的时候前面加"u"
print(type(y))  # unicode类型
print([y, ])  # 以unicode编码保存