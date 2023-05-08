import pygame
from random import random
from time import sleep
from translator import load

pygame.init()
fc = True
screen = pygame.display.set_mode((400, 400)) if not fc else pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()
side = 10
micro_array = bool(1)

chance = .2
r = 'wall'
s_, b_ = load(r)
square = bool(0)

colors = {'-3': (50, 50, 50), '-2': (100, 50, 20), '-1': (200, 100, 39), '0': (230, 140, 0),
          '1': (100, 230, 100), '2': (0, 230, 0), '3': (0, 150, 0)}
mi, mx = -3, 3

rows, cols = int(h / side), int(w / side)

tab = [[1 if random() < chance else mi for _ in range(cols)] for _ in range(rows)]
old = tab.copy()


def blend(c1, c2):
    c1, c2 = list(c1), list(c2)
    c = [(a + b) / 2 for a, b in zip(c1, c2)]
    return tuple(c)


def update(t, s, b):
    new = [[_ for _ in range(cols)] for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            n = 0
            for x1 in range(x - 1, x + 2):
                for y1 in range(y - 1, y + 2):
                    n += 1 if t[(y1 + rows) % rows][(x1 + cols) % cols] >= 1 and (x != x1 or y != y1) else 0
            if t[y][x] <= 0 and b[n] == 1:  # dead, then alive
                new[y][x] = 1
            elif t[y][x] <= 0 and b[n] == 0:  # dead, then dead
                new[y][x] = t[y][x] - 1 if t[y][x] > mi else mi
            elif t[y][x] >= 1 and s[n] == 1:  # alive, then alive
                new[y][x] = t[y][x] + 1 if t[y][x] < mx else mx
            elif t[y][x] >= 1 and s[n] == 0:  # alive, then dead
                new[y][x] = 0

            if micro_array:
                c = blend(colors[str(new[y][x])], colors[str(t[y][x])])
            else:
                c = colors[str(mi)] if new[y][x] <= 0 else colors['1']
            if not square:
                pygame.draw.circle(screen, c, ((x + .5) * side, (y + .5) * side), (side / 2.7))
            else:
                pygame.draw.rect(screen, c, (x * side, y * side, side, side))

    return new.copy()


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    tab = update(old.copy(), s_, b_)
    old = tab.copy()
    pygame.display.update()
    if side > 6:
        sleep(0.)
