"""
1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
"""
import os
def change_file(*file, content):  # 完成批量修改文件名
    for f in file:
        num = f.split('.')[0][-1]
        content_list = content.split('.')
        content_list[0] += num
        new_content = content_list[0] + '.txt'
        os.rename(f, new_content)

change_file('test1.txt', 'test2.txt', 'test3.txt', content='modified.txt')

