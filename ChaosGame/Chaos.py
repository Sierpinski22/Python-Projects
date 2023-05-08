import pygame
from random import randint, choice
from math import pi, sin, cos

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_height(), screen.get_width()

vertexes = [(w/2 + w/2 * cos(pi/2), h/2 - h/2 * sin(pi/2)),
            (w/2 + w/2 * cos(pi/2+2/3*pi), h/2 - h/2 * sin(pi/2+2/3*pi)),
            (w/2 + w/2 * cos(pi/2+4/3*pi), h/2 - h/2 * sin(pi/2+4/3*pi)),
            (randint(0, w), randint(0, h))]

for p in vertexes:
    pygame.draw.circle(screen, (0, 255, 0), p, 5)

px, py = randint(0, w), randint(0, h)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    px1, py1 = choice(vertexes)
    px = (px + px1) / 2
    py = (py + py1) / 2
    pygame.draw.circle(screen, (255, 255, 255), (px, py), 1)
    pygame.display.update()
