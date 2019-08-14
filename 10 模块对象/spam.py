print(__name__)

__all__ = ['money','read1','read2']

print('from the spam.py')

money = 0

def read1():
    print('spam模块.read1:', money)

def read2():
    print("spam模块.read2")
    read1()

def change():
    global money
    money = 1    # 在模块中修改

if __name__ == '__main__':
    print('文件被当做脚本执行了')
    read1()
else:
    print('文件被导入了')