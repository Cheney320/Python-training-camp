# coding:gbk

# 解释器已经切换到Python3

x = "上"
print(x)
# unicode===>编码encode===>gbk
code_gbk = x.encode('gbk')
code_utf8 = x.encode('utf-8')

print(code_gbk)
print(code_utf8)
print(type(code_gbk))
print(type(code_utf8))

print(code_gbk.decode('gbk'))
print(code_utf8.decode('utf-8'))
