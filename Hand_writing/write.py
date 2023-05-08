import pygame
from math import floor


pygame.init()
side = 20
increment = 0.03
s = 5


cols, rows = 28, 28
w, h = side * cols, side * rows

screen = pygame.display.set_mode((w, h))

big = True


def draw(g):
    for y1, y in enumerate(g):
        for x1, x in enumerate(y):
            col = int(x * 255)
            pygame.draw.rect(screen, (col, col, col), (x1 * side, y1 * side, side, side))
    pygame.display.update()


def grid_pos(x_, y_):
    return floor(x_ / side), floor(y_ / side)


def edit(g):
    x, y = pygame.mouse.get_pos()
    x, y = grid_pos(x, y)
    if x != 0 or y != 0:
        g[y][x] += increment if g[y][x] + increment < 1. else 1 - g[y][x]
        col = int(g[y][x] * 255)
        pygame.draw.rect(screen, (col, col, col), (x * side, y * side, side, side))
        if big:
            if x > 0:
                g[y][x - 1] += increment / s if g[y][x - 1] + increment < 1. else 1 - g[y][x - 1]
                col = int(g[y][x - 1] * 255)
                pygame.draw.rect(screen, (col, col, col), ((x - 1) * side, y * side, side, side))
            if x < cols - 1:
                g[y][x + 1] += increment / s if g[y][x + 1] + increment < 1. else 1 - g[y][x + 1]
                col = int(g[y][x + 1] * 255)
                pygame.draw.rect(screen, (col, col, col), ((x + 1) * side, y * side, side, side))
            if y > 0:
                g[y - 1][x] += increment / s if g[y - 1][x] + increment < 1. else 1 - g[y - 1][x]
                col = int(g[y - 1][x] * 255)
                pygame.draw.rect(screen, (col, col, col), (x * side, (y - 1) * side, side, side))
            if y < rows - 1:
                g[y + 1][x] += increment / s if g[y + 1][x] + increment < 1. else 1 - g[y + 1][x]
                col = int(g[y + 1][x] * 255)
                pygame.draw.rect(screen, (col, col, col), (x * side, (y + 1) * side, side, side))


def delete():
    screen.fill((0, 0, 0))
    return [[0 for _ in range(h)] for _ in range(w)]


def get_digit():
    drawable = False
    done = False
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawable = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawable = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                grid = delete()
            elif event.type == pygame.KEYDOWN and event.key == 32:
                done = True
                drawable = False
                break

        if drawable:
            edit(grid)
        pygame.display.update()

        if done:
            return grid


print(get_digit())

