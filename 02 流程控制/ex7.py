"""
练习七：
打印如下金字塔图形，下图为等腰三角形，上面一行
内容永远比下面少两颗星星且位于下面一行的正上方
    *       空格 4， * 1
   ***      空格 3， * 3
  *****     空格 2， * 5
 *******    空格 1， * 7
*********   空格 0， * 9
"""

max_layers = 5
for l in range(1, max_layers+1):
    for i in range(5-l):
        print(' ', end='')
    for j in range(2*l-1):
        print('*', end='')
    print()
