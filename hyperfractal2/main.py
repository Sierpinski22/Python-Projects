import pygame
from math import pi, sin, cos
from c_rainbow import test

s = 1500
pygame.init()
screen = pygame.display.set_mode((s, s))
w, h = screen.get_size()
coefficient = 2
rainbow = True


def to_d(x, n=1.):
    return float(x) / n * 2 ** 0.5


def to_s(x, n=1):
    return float(x) * 2 / 2 ** 0.5


def square(xc, yc, diagonal, angle=0, color=(255, 255, 255)):
    points = []
    for i in range(4):
        points.append((xc + diagonal * cos(angle + i * pi / 2 - pi / 4),
                       yc - diagonal * sin(angle + i * pi / 2 - pi / 4)))
    pygame.draw.polygon(screen, color, points)


def menger(x, y, side, angle, depth, max_depth):
    if rainbow:
        c = test(depth, max_depth) if depth + 1 < max_depth else (0, 0, 0)
    else:
        c = int((255 / max_depth) * (max_depth - depth))
    square(x, y, to_d(side) / 2, angle, (c, c, c) if not rainbow else c)
    if depth < max_depth:
        for i in range(8):  # angles
            ns = to_d(side) if i % 2 == 1 else side
            menger(x + ns * cos(angle + i * pi / 4), y - ns * sin(angle + i * pi / 4),
                   side / 3, angle, depth + 1, max_depth)


def fractal(xc, yc, side, angle, max_depth, depth, directions=None):  # side è la diagonale / 2!
    if directions is None:
        directions = [True, True, True, True]

    # square(xc, yc, to_d(side), angle)
    menger(xc, yc, 2 * side / 3, angle, depth, max_depth)  # un terzo del lato

    ns = to_d(side) + to_d(side, coefficient)
    if depth < max_depth:
        if directions[0]:  # up
            fractal(xc + ns * cos(angle + pi / 4), yc - ns * sin(angle + pi / 4),
                    side / coefficient, angle, max_depth, depth + 1, directions=[True, True, False, True])

        if directions[1]:  # right
            fractal(xc + ns * cos(angle - pi / 4), yc - ns * sin(angle - pi / 4),
                    side / coefficient, angle, max_depth, depth + 1, directions=[True, True, True, False])

        if directions[2]:  # right
            fractal(xc + ns * cos(angle - pi / 2 - pi / 4), yc - ns * sin(angle - pi / 2 - pi / 4),
                    side / coefficient, angle, max_depth, depth + 1, directions=[False, True, True, True])

        if directions[3]:  #
            fractal(xc + ns * cos(angle + pi - pi / 4), yc - ns * sin(angle + pi - pi / 4),
                    side / coefficient, angle, max_depth, depth + 1, directions=[True, False, True, True])
    else:
        return


first = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    if first:
        fractal(w / 2, h / 2, w / 6, 0, 6, 0)
        pygame.display.update()
        pygame.image.save(screen, 'hf2.png')
        first = False
