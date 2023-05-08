import pygame
from math import pi, sin, cos
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
ter_chance = 0
turn_angle = pi / 3
thickness = 0.7

path = []
particles = []
q = quadtree(0, 0, w, h, sensitivity=30)


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
        self.speed = 5
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
                split = False

                if random() < split_chance:
                    split = True
                    if random() < 0.5:
                        self.angle += turn_angle
                    else:
                        self.angle -= turn_angle
                    self.vx, self.vy = self.speed * cos(self.angle), self.speed * sin(self.angle)

                self.px, self.py = self.x, self.y
                self.x += self.vx
                self.y += self.vy
                jump, px2, py2 = self.edge()

                if jump:
                    return {'x': px2, 'y': py2,
                            'x1': self.x, 'y1': self.y,
                            'mx': (self.px + self.x) / 2, 'my': (self.py + self.y) / 2}, child
                else:
                    return {'x': self.px, 'y': self.py,
                            'x1': self.x, 'y1': self.y,
                            'mx': (self.px + self.x) / 2, 'my': (self.py + self.y) / 2}, child
        return None, None


    def edge(self):
        jump = False
        x1 = self.x
        y1 = self.y
        if self.x > w:
            self.x = 0
            x1 = w
            jump = True
        elif self.x < 0:
            self.x = w
            x1 = 0
            jump = True

        if self.y > h:
            self.y = 0
            jump = True
            y1 = h
        elif self.y < 0:
            self.y = h
            jump = True
            y1 = 0
        return jump, x1, y1

    def collision(self, place):  # le linee non funzionano quando si teletrasporta
        for p in place:
            try:
                slope = (p['y'] - p['y1']) / (p['x'] - p['x1'])
                if slope * (self.x - p['x']) + thickness >= (self.y - p['y1']) > slope * (self.x - p['x']) - thickness:
                    return True
            except ZeroDivisionError:
                print(1)
                if thickness + min(p['x'], p['x1']) < self.x < thickness + max(p['x'], p['x1']) and min(p['y'], p[
                    'y1']) + thickness < self.y < max(p['y'], p['y1']) + thickness:
                    return True

        return False

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


for i in range(0, 1):
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
                path.append(element(z, z['mx'], z['my']))
            if new_p is not None:
                new_gen.append(new_p)
            if not par.blocked:
                new_gen.append(par)
    # for re in q.show():
    #   pygame.draw.rect(screen, (0, 255, 0), (re[0], re[1], re[2], re[3]), 1)
    particles = new_gen
    cl.tick(60)
    pygame.display.update()
    q.reset()

{'x': self.px, 'y': self.py,
 'x1': self.x, 'y1': self.y,
 'mx': (self.px + self.x) / 2, 'my': (self.py + self.y) / 2}, child
