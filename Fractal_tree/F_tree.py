import pygame
from math import cos, sin, pi
from time import sleep
import numpy as np

pygame.init()
screen = pygame.display.set_mode((700, 700))
w, h, = screen.get_size()
side1 = h / 4
max_level = 7
array = np.concatenate((np.linspace(0, 2 * pi / 3, 100), np.linspace(2 * pi / 3, 0, 100)))
save = False


def tree(x, y, angle, side, level, increment):
    if level < max_level:
        side /= 2
        x1 = x + side * cos(angle)
        y1 = y - side * sin(angle)
        pygame.draw.line(screen, (255, 153, 0), (x, y), (x1, y1), 2)
        tree(x1, y1, angle, side, level + 1, increment)
        x1 = x + side * cos(angle - increment)
        y1 = y - side * sin(angle - increment)
        pygame.draw.line(screen, (0, 0, 255), (x, y), (x1, y1), 2)
        tree(x1, y1, angle - increment, side, level + 1, increment)
        x1 = x + side * cos(angle + increment)
        y1 = y - side * sin(angle + increment)
        pygame.draw.line(screen, (230, 230, 230), (x, y), (x1, y1), 2)
        tree(x1, y1, angle + increment, side, level + 1, increment)


i = 0
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    tree(w / 2, h / 2 + sin(pi / 3) * side1 / 2, pi / 2, 2 * side1, 0, array[i % len(array)])

    pygame.display.update()
    if array[i % len(array)] == 2 * pi / 3 and save:
        pygame.image.save(screen, 'colored_tree.jpg')
        print('done!')
    sleep(0.025)
    i += 1
