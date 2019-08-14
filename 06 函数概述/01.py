def modify_files(**kwargs):
    """
    功能：用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
    使用方式：modify_files(**{file1:content1, file2:content2,...})
    :param kwargs:字典(文件名与对应修改内容)
    :return:无返回值
    """
    for file in kwargs:
        with open(file, 'w') as f:
            f.write(kwargs[file])

modify_files(**{'file1.txt':'a', 'file2.txt':'b', 'file3.txt':'c'})






