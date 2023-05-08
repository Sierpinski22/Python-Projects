import pygame
from random import randint
from math import pi, sin, cos

pygame.init()  # inzializza
screen = pygame.display.set_mode((600, 600))  # imposta uno schermo
w, h = screen.get_width(), screen.get_height()  # dimensioni dello schermo

maxDepth = 6
inc = 0
d = 0


def fractal(x, y, length, angle, depth):

    if depth == maxDepth:
        return
    else:

        x0 = x + length * cos(angle + inc / 2)
        y0 = y - length * sin(angle + inc / 2)
        col = (0, randint(0, 255), 0)
        pygame.draw.line(screen, col, (x, y), (x0, y0))
        fractal(x0, y0, length / 2, angle + inc / 2, depth + 1)

        x0 = x + length * cos(angle - inc / 2)
        y0 = y - length * sin(angle - inc / 2)
        col = (0, randint(0, 255), 0)
        pygame.draw.line(screen, col, (x, y), (x0, y0))
        fractal(x0, y0, length / 2, angle - inc / 2, depth + 1)

        x0 = x + length * cos(angle + inc + inc / 2)
        y0 = y - length * sin(angle + inc + inc / 2)
        col = (0, randint(0, 255), 0)
        pygame.draw.line(screen, col, (x, y), (x0, y0))
        fractal(x0, y0, length / 2, angle + inc + inc / 2, depth + 1)

        x0 = x + length * cos(angle - inc - inc / 2)
        y0 = y - length * sin(angle - inc - inc / 2)
        col = (0, randint(0, 255), 0)
        pygame.draw.line(screen, col, (x, y), (x0, y0))
        fractal(x0, y0, length / 2, angle - inc - inc / 2, depth + 1)

        # x0 = x+length*cos(angle+inc*2)
        # y0 = y-length*sin(angle+inc*2)
        # pygame.draw.line(screen, (255, 255, 255), (x, y), (x0, y0))
        # fractal(x0, y0, length / 2, angle+inc*2, depth+1)

        # x0 = x+length*cos(angle-inc*2)
        # y0 = y-length*sin(angle-inc*2)
        # pygame.draw.line(screen, (255, 255, 255), (x, y), (x0, y0))
        # fractal(x0, y0, length / 2, angle-inc*2, depth+1)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    fractal(w / 2, h / 2, 150, pi / 2, 0)
    d = 0
    inc += 0.01 if inc < 1000000 else -inc
    pygame.display.update()
