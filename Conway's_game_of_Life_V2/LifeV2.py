import numpy as np
from graphics import *
from random import random

w = GraphWin("Conway's game of Life", 600, 600)
side = 40
cols = int(w.width / side)
rows = int(w.height / side)

tab = np.array([[random() <= 0.5 for i in range(cols)] for j in range(rows)], dtype=bool)


def show():
    for y in range(rows):
        for x in range(cols):
            cell = Rectangle(Point(y * side, x * side), Point(y * side + side, x * side + side))
            if tab[y][x]:
                cell.setFill(color_rgb(255, 255, 255))
                cell.setOutline(color_rgb(255, 255, 255))
            else:
                cell.setFill(color_rgb(0, 0, 0))
                cell.setOutline(color_rgb(0, 0, 0))
            cell.draw(w)

    nextgen(tab.copy())


def nextgen(old_tab):
    for y in range(cols):
        for x in range(rows):
            counter = 0
            for lr in range(y - 1, y + 2):
                for ud in range(x - 1, x + 2):
                    if old_tab[(cols + lr) % cols][(rows + ud) % rows] and (y != lr or x != ud):
                        counter += 1

            if counter == 3:
                tab[y][x] = True
            elif counter < 2 or counter > 3:
                tab[y][x] = False


while True:
    w.setBackground(color_rgb(0, 0, 0))
    show()
    if w.checkMouse():
        break
