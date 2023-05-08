import pygame
from math import sin, cos, pi

screen = pygame.display.set_mode((600, 600))
w, h = screen.get_size()


def to_d(x, n=1.):
    return float(x) / n * 2 ** 0.5


def square(xc, yc, diagonal, angle=0, color=(255, 255, 255)):
    points = []
    for i in range(4):
        points.append((xc + diagonal * cos(angle + i * pi / 2 - pi / 4),
                       yc - diagonal * sin(angle + i * pi / 2 - pi / 4)))
    pygame.draw.polygon(screen, color, points)


def menger(x, y, side, angle, depth, max_depth):
    c = int((255 / max_depth) * (max_depth - depth))
    square(x, y, to_d(side) / 2, angle, (c, c, c))
    if depth < max_depth:
        for i in range(8):  # angles
            ns = to_d(side) if i % 2 == 1 else side
            menger(x + ns * cos(angle + i * pi/4), y - ns * sin(angle + i * pi/4),
                   side / 3, angle, depth + 1, max_depth)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    side = 300
    menger(w / 2, h / 2, side / 3, 0, 0, 4) # gli passi un terzo
    pygame.draw.rect(screen, (0, 255, 0), (w/2-side/2, h/2-side/2, side, side), 1)
    pygame.display.update()