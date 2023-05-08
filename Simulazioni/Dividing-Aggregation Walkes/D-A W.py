import pygame
from math import sin, cos, pi
from random import randint, random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()
particles = []
f = pygame.time.Clock()

#  parameters
n = 5
radius = 3
speed = radius
increase = pi / n
turn_chance = 0.02
split_chance = turn_chance


# parameters


class walker:
    def __init__(self, x, y, a=None):
        if x is None or y is None:
            x, y = randint(0, w), randint(0, h)
        self.x, self.y = x, y
        self.px, self.py = x, y
        self.immune = [1, 1, 1]
        self.blocked = False
        if a is None:
            self.angle = randint(0, 2*n - 1)
        else:
            self.angle = a
            while abs(a - self.angle) == 4 or a - self.angle == 0:
                self.angle = randint(0, 2*n - 1)
        self.vx, self.vy = 0, 0
        self.velocity()


    def velocity(self):
        self.vx, self.vy = speed * cos(self.angle * increase), speed * sin(self.angle * increase)

    def move(self):  # nuovo mod per vedere la velocità?
        c = None
        if random() < turn_chance and not 1 in self.immune:
            self.angle += 1 if random() < 0.5 else -1
            self.angle = (self.angle + 2*n) % (2*n)
            self.velocity()
        self.px += self.vx
        self.py += self.vy
        jump = self.edge()
        if not screen.get_at((round(self.px), round(self.py))) != (0, 0, 0, 255) or 1 in self.immune:
            if len(self.immune) > 0:
                self.immune.pop()
            if not jump:
                pygame.draw.line(screen, (255, 255, 255), (self.px, self.py), (self.x, self.y), radius)
            if random() < split_chance:
                c = walker(self.x, self.y, self.angle)
                # pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), radius)
            self.x, self.y = self.px, self.py

        else:
            self.blocked = True
            if not jump:
                pygame.draw.line(screen, (255, 255, 255), (self.px, self.py), (self.x, self.y), radius)
        return c

    def edge(self):
        j = False
        if self.px < 1:
            self.px = w - 1
            j = True
        elif self.px > w - 1:
            self.px = 1
            j = True

        if self.py < 1:
            j = True
            self.py = h - 1
        elif self.py > h - 1:
            self.py = 1
            j = True
        return j


for i in range(n):
    # particles.append(walker(w / 2, h))
    particles.append(walker(w / 2 + w / 3 * cos(i * increase * 2), h / 2 + h / 3 * sin(i * increase * 2)))

while True:
    s = pygame.Surface((w, h))
    s.set_alpha(1)
    s.fill((0, 0, 0))
    if len(particles) > 0:
        screen.blit(s, (0, 0))
    new_particles = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    for p in particles:
        child = p.move()
        if not p.blocked:
            new_particles.append(p)
            if child is not None:
                new_particles.append(child)
    particles = new_particles.copy()
    pygame.display.update()
