"""
八皇后问题:该问题是国际西洋棋棋手马克斯·贝瑟尔于1848年提出：
在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个
皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。
"""

def conflict(state, nextX):
    """
    功能:在当前行的8个位置摆放棋子时，检查是否与已摆放的棋子是否冲突。
    :param state:已摆放的棋子位置,比如(1,3,0),1代表第一行棋子所在列,3代表第二行棋子所在列,0代表第3行棋子所在列
    :param nextX:当前摆放棋子所在列
    :return:True or False
    """
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    """
    :param num:棋盘行数
    :param state:已摆放棋子的列数汇总
    :return:
    """
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

result = queens()
print(list(result))



