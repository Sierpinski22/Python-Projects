import pygame
from random import random, randint
from quadtree import *
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_width(), screen.get_height()
side = 150
cl = pygame.time.Clock()
board = False


def distance(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


class particle:
    def __init__(self, x=None, y=None):
        if x is None:
            x = randint(0, w)
        if y is None:
            y = randint(0, h)
        self.x = x
        self.y = y
        self.vx = random() * 2
        self.vy = random() * 2
        self.r = 5

    def move(self):
        if not 0 < self.x < w:
            self.vx *= -1
        if not 0 < self.y < h:
            self.vy *= -1

        self.impact(board)
        self.x += self.vx
        self.y += self.vy

    def impact(self, opt):
        if opt:
            x_, y_ = to_centred(self.x, self.y, 20, 20)
            others = q.query(x_, y_, 20, 20)
            # ygame.draw.rect(screen, (255, 255, 255), (x_, y_, 20, 20), 1)
        else:
            others = particles

        for o in others:
            if distance(self.x, self.y, o.x, o.y) < self.r + o.r and o is not self:
                self.vx *= -1
                self.vy *= -1

    def show(self, colour=(255, 255, 255)):
        pygame.draw.circle(screen, colour, (self.x, self.y), self.r)


particles = [particle() for _ in range(0, 400)]


def convert(array):
    new_array = []
    for a in array:
        new_array.append(element(a, a.x, a.y))
    return new_array


q = quadtree(0, 0, w, h, 3)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board = not board
            elif event.button == 3:
                particles.append(particle())
            elif len(particles):
                particles.pop()

    q.put(convert(particles))

    if board:
        for re in q.show():
            pygame.draw.rect(screen, (0, 255, 0), (re[0], re[1], re[2], re[3]), 1)

        pos = pygame.mouse.get_pos()
        mx, my = pos[0], pos[1]
        nx, ny = to_centred(mx, my, side, side)
        signed = q.query(nx, ny, side, side)
        pygame.draw.rect(screen, (0, 0, 255), (nx, ny, side, side), 5)

    for p in particles:
        p.move()
        if board:
            p.show() if p not in signed else p.show((255, 0, 0))

        else:
            p.show()

    q.reset()
    cl.tick(1000)
    comment = " con " if board else " senza "
    print("fps > circa " + str(round(cl.get_fps())) + comment + 'ottimizzazione')
    pygame.display.update()
