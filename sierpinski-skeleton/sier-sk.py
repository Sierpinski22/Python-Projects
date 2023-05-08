import pygame
from math import sin, cos, pi

pygame.init()
screen = pygame.display.set_mode((600, 600))
actual_max = 7
w, h = screen.get_width(), screen.get_width()


def skeleton(x, y, side):
    if side > 3:
        x1, y1 = x, y - side
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x1, y1))
        skeleton(x1, y1, side / 2)
        x1, y1 = x + side * cos(-pi / 6), y - side * sin(-pi / 6)
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x1, y1))
        skeleton(x1, y1, side / 2)
        x1, y1 = x + side * cos(pi + pi / 6), y - side * sin(pi + pi / 6)
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x1, y1))
        skeleton(x1, y1, side / 2)


skeleton(w / 2, h / 2, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.display.update()
