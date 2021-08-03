"""
海龟画图
@author: keefe
@date: 2020-12-2
@requirement: turtle
@refer: https://www.liaoxuefeng.com/wiki/1016959663602400/1249593505347328
"""

# 导入turtle包的所有内容:
from turtle import *


def draw_rect():
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()


def draw_star_one(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


def draw_star_more(i):
    for x in range(0, 500, int(250 / i)):
        draw_star_one(x, 0)


def draw_tree():
    """ 绘制分形树 """
    def do_draw_tree(l, level):
        global r, g, b
        # save the current pen width
        w = width()

        # narrow the pen width
        width(w * 3.0 / 4.0)
        # set color:
        r = r + 1
        g = g + 2
        b = b + 3
        pencolor(r % 200, g % 200, b % 200)

        l = 3.0 / 4.0 * l

        lt(s)
        fd(l)

        if level < lv:
            do_draw_tree(l, level + 1)
        bk(l)
        rt(2 * s)
        fd(l)

        if level < lv:
            do_draw_tree(l, level + 1)
        bk(l)
        lt(s)

        # restore the previous pen width
        width(w)

    # 初始化： 设置色彩模式是RGB:
    colormode(255)

    lt(90)

    lv = 14
    l = 120
    s = 45

    width(lv)

    # 初始化RGB颜色:
    r = 0
    g = 0
    b = 0
    pencolor(r, g, b)

    penup()
    bk(l)
    pendown()
    fd(l)

    speed("fastest")
    do_draw_tree(l, 4)
    done()

if __name__ == '__main__':
    # draw_rect()
    # draw_star_more(5)
    draw_tree()