import pygame
from math import sin, cos, pi, sqrt
from time import sleep
import c_rainbow

pygame.init()
screen = pygame.display.set_mode((1000, 700))
w, h = screen.get_size()
max_d = 10
a = 0
s = 90
n = 400
interval = pi / 2 / n




def build(x, y, angle, side, depth):  # trovo i punti
    if depth < max_d:
        tx = x + cos(angle + pi / 2) * side
        ty = y - sin(angle + pi / 2) * side

        x1 = tx + cos(angle + a) * cos(a) * side
        y1 = ty - sin(angle + a) * cos(a) * side

        pygame.draw.polygon(screen, c_rainbow.test(depth, max_d), [(x, y), (tx, ty),
                                                                           (
                                                                            x + sqrt(2) * side * cos(angle + pi / 4),
                                                                            y - sqrt(2) * side * sin(
                                                                                angle + pi / 4)),
                                                                           (x + side * cos(angle),
                                                                            y - side * sin(angle))])

        build(tx, ty, angle + a, side * cos(a), depth + 1)
        build(x1, y1, angle + a + pi + pi / 2, side * sin(a), depth + 1)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    for j in range(0, n):
        screen.fill((0, 0, 0))
        a = j * interval
        build(w / 2 - s / 2, h, 0, s, 0)
        pygame.display.update()
        sleep(0.01)
