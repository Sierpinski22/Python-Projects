import pygame
from math import pi, sin, cos, sqrt
from random import uniform, randint, random
from quadtree import *

#  usare una linea al posto dei quadratini
pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_size()

cl = pygame.time.Clock()

split_chance = 0.01
turn_chance = 0.1
div_chance = turn_chance / 10
ter_chance = div_chance / 10
turn_angle = pi / 3
thickness = 0.8

path = []
particles = []
q = quadtree(0, 0, w, h, sensitivity=30)


def distance(x, y, x1, y1):
    n = sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return n


def to_element(lis):
    e = []
    for li in lis:
        e.append(element(li, li['x'], li['y']))
    return e


class walker:
    def __init__(self, x=None, y=None):
        if x is None:
            x = randint(0, w)
            y = randint(0, h)

        self.px, self.py = x, y
        self.speed = 1
        self.angle = uniform(0, 2 * pi)
        self.vx, self.vy = self.speed * cos(self.angle), self.speed * sin(self.angle)
        self.x, self.y = x + self.vx, y + self.vy
        self.blocked = False

    def move(self, place=None):
        if place is None:
            place = path
        if not self.blocked:
            if not self.collision(place):
                child = None
                if random() < split_chance:
                    if random() < 0.5:
                        self.angle += turn_angle
                    else:
                        self.angle -= turn_angle
                    self.vx, self.vy = self.speed * cos(self.angle), self.speed * sin(self.angle)
                self.px, self.py = self.x, self.y
                self.x += self.vx
                self.y += self.vy

                if random() < div_chance:
                    child = walker(x=self.x, y=self.y)

                if not self.edge():
                    pygame.draw.circle(screen, (255, 255, 255), (self.px, self.py), 1)
                    return {'x': self.px, 'y': self.py}, child
                else:
                    return None, child
            else:
                self.blocked = True
                return None, None

    def edge(self):
        jump = False
        if self.x > w:
            self.x = 0
            jump = True
        elif self.x < 0:
            self.x = w
            jump = True

        if self.y > h:
            self.y = 0
            jump = True
        elif self.y < 0:
            self.y = h
            jump = True
        return jump

    def collision(self, place):
        for p in place:
            if distance(p['x'], p['y'], self.x, self.y) < thickness:
                return True
        return False

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


for i in range(0, 20):
    particles.append(walker())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    new_gen = []
    q.put(path)
    for par in particles:
        if random() > ter_chance:
            nx, ny = to_centred(par.x, par.y, thickness * 3, thickness * 3, rounded=False)
            close = q.query(nx, ny, thickness, thickness)
            z, new_p = par.move(close)

            if z is not None:
                path.append(element(z, z['x'], z['y']))
            if new_p is not None:
                new_gen.append(new_p)
            if not par.blocked:
                new_gen.append(par)
    # for re in q.show():
    #    pygame.draw.rect(screen, (0, 255, 0), (re[0], re[1], re[2], re[3]), 1)
    particles = new_gen
    pygame.display.update()
    q.reset()
