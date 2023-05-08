import pygame
from math import sqrt, tanh
from random import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_size()
balls = []
dt = 0.1
gravity = 0.0001


def dist(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


class ball:
    def __init__(self, x, y, blocked=False):
        self.x, self.y = x, y
        self.vx, self.vy = random(), random()
        self.blocked = blocked
        self.id = random()
        self.tied = []

    def move(self):
        if not self.blocked:
            self.vy += gravity
            for other, spring in self.tied:
                distance = dist(self.x, self.y, other.x, other.y)
                k, rest = spring
                delta_s = distance - rest
                force = k * delta_s  # intensità
                x, y = (other.x - self.x) / distance * force, (other.y - self.y) / distance * force
                c = round(255 * abs(tanh(force * 40)))
                pygame.draw.line(screen, (c, 255 - c, 0), (other.x, other.y), (self.x, self.y))
                other.show()
                self.vx += x * dt
                self.vy += y * dt
            self.vx *= 0.999
            self.vy *= 0.999
            self.edge()
            self.x += self.vx
            self.y += self.vy
            #  self.show()

    def edge(self):
        if self.x < 0 or self.x > w:
            self.vx *= -1
            self.x = 0 if self.x < 0 else w
        if self.y < 0 or self.y > h:
            self.vy *= -1
            self.y = 0 if self.y < 0 else h

    def link(self, other, spring):
        if other not in self.tied:
            for i in self.tied:
                if other.id == i[0].id:
                    return
            self.tied.append((other, spring))
            other.tied.append((self, spring))

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)


def link_all(lis, k, length):
    for li in lis:
        for i in lis:
            if i is not li:
                li.link(i, (k, length))


def link_close(lis, k, length, radius):
    for li in lis:
        for i in lis:
            if i is not li and dist(li.x, li.y, i.x, i.y) <= radius:
                li.link(i, (k, length))


for _ in range(10):
     balls.append(ball(random() * w, random() * h))

link_all(balls, 0.0005, 130)



while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                gravity += 0.0001
            elif event.button == 5:
                gravity -= 0.0001
            else:
                gravity = -gravity
    for b in balls:
        b.move()
        b.show()
    pygame.display.update()
