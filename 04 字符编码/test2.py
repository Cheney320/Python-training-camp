# coding:utf-8

# 解释器已经切换到Python2

x = "上"
# print(x.decode('gbk'))  # 使用utf-8编码，使用gbk无法解码
print(x.decode('utf-8'))  # 使用utf-8编码，使用utf-8解码
print([x.decode('utf-8'), ])  # 在列表打印出龟叔没有转换之前的unicode编码