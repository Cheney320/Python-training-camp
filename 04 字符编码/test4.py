# coding:gbk

# �������Ѿ��л���Python3

x = "��"
print(x)
# unicode===>����encode===>gbk
code_gbk = x.encode('gbk')
code_utf8 = x.encode('utf-8')

print(code_gbk)
print(code_utf8)
print(type(code_gbk))
print(type(code_utf8))

print(code_gbk.decode('gbk'))
print(code_utf8.decode('utf-8'))
