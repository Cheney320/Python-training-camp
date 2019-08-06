import sys
import time


class Tail():
    def __init__(self, file_name, callback=sys.stdout.write):
        self.file_name = file_name
        self.callback = callback

    def follow(self, n=10):
        try:
            # 打开文件
            with open(self.file_name) as f:
                self._file = f
                self._file.seek(0, 2)
                # 存储文件的字符长度
                self.file_length = self._file.tell()
                # 打印最后10行
                self.showLastLine(n)
                # 持续读文件 打印增量
                while True:
                    line = self._file.readline()
                    if line:
                        self.callback(line)
                    time.sleep(1)
        except Exception:
            print('打开文件失败')

    def showLastLine(self, n):
        # 一行大概100个吧 这个数改成1或者1000都行
        len_line = 100
        # n默认是10，也可以follow的参数传进来
        read_len = len_line * n
        # 用last_lines存储最后要处理的内容
        while True:
            # 如果要读取的1000个字符，大于之前存储的文件长度
            # 读完文件，直接break
            if read_len > self.file_length:
                self._file.seek(0)
                last_lines = self._file.read().split('\n')[-n:]
                break
            # 先读1000个 然后判断1000个字符里换行符的数量
            self._file.seek(-read_len, 2)
            last_words = self._file.read(read_len)
            # count是换行符的数量
            count = last_words.count('\n')

            if count >= n:
                # 换行符数量大于10 很好处理，直接读取
                last_lines = last_words.split('\n')[-n:]
                break
            # 换行符不够10个
            else:
                # break
                # 不够十行
                # 如果一个换行符也没有，那么我们就认为一行大概是100个
                if count == 0:

                    len_perline = read_len
                # 如果有4个换行符，我们认为每行大概有250个字符
                else:
                    len_perline = read_len / count
                # 要读取的长度变为2500，继续重新判断
                read_len = len_perline * n
        for line in last_lines:
            self.callback(line + '\n')


if __name__ == '__main__':
    py_tail = Tail('test.txt')
    py_tail.follow(20)
