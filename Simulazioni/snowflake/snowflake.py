import pygame
from math import cos, sin, pi
import random

vertex = []
pygame.init()
screen = pygame.display.set_mode((600, 600))
max_vertexes = 5
max_mirror = 10
max_angle = pi * 2 / max_mirror
max_increment = max_angle / max_vertexes
max_radius = 200
angle = 0
w, h = screen.get_width(), screen.get_height()

for f in range(max_vertexes):
    r = random.randint(0, max_radius)
    vertex.append([r, f * max_increment])


def rotation():
    for g in range(1, max_mirror):
        for k in range(max_vertexes):
            vertex.append([vertex[k][0], vertex[k][1] + max_angle * g])


def to_cartesian(polar):
    transf = []
    r1 = polar[0][0]
    a1 = polar[0][1]
    x1 = r1 * cos(a1)
    y1 = r1 * sin(a1
                  )
    for d in polar:
        radius = d[0]
        a = d[1]
        transf.append([radius * cos(a) + w / 2, radius * sin(a) + h / 2])
    transf.append([x1+w/2, y1+h/2])

    return transf


def draw():
    for i in range(1, len(vertex)):
        pygame.draw.line(screen, (255, 255, 255), (vertex[i - 1][0], vertex[i - 1][1]), (vertex[i][0], vertex[i][1]), 3)


rotation()
vertex = to_cartesian(vertex).copy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        draw()
        pygame.display.update()
