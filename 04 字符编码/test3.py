# coding:gbk

# �������Ѿ��л���Python2

x = "��"
print(type(x))  # str����
print([x, ])  # ��gbk���뱣��
print([x.decode('gbk'), ])  # ��������unicode�������汣����ַ�����һ��

y = u'��'  # �����ַ�����ʱ��ǰ���"u"
print(type(y))  # unicode����
print([y, ])  # ��unicode���뱣��