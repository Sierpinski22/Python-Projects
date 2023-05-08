import pygame
from random import randint, random

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_width(), screen.get_height()
n = 20 * 3
K = 20
G = 10
dampening = 0.9
density = 1 / 125


class proton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = (random() - 0.5) * 2
        self.vy = (random() - 0.5) * 2
        self.ax = 0
        self.ay = 0
        self.r = 8
        self.m = 1
        self.q = 1

    @staticmethod
    def distance(x, y, x1, y1):
        return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

    def normalize(self, fx, fy):
        mod = self.distance(fx, fy, 0, 0)
        return (fx / mod, fy / mod) if mod != 0 else (0, 0)

    def attract(self, lis):
        for par in lis:
            if not (par is self):
                r = self.distance(self.x, self.y, par.x, par.y)
                fx = par.x - self.x
                fy = par.y - self.y
                fx, fy = self.normalize(fx, fy)
                if r < self.r + par.r:
                    mod = self.distance(self.vx, self.vy, 0, 0)
                    self.applyForce(-fx * mod * dampening, -fy * mod * dampening)
                else:
                    f = K * -(self.q * par.q) / (r ** 2)
                    self.applyForce(fx * f, fy * f)
                    f = G * (self.m * par.m) / (r ** 2)
                    self.applyForce(fx * f, fy * f)

    def edges(self):
        if self.x > w:
            self.x = w
            self.vx *= -1 * dampening
        elif self.x < 0:
            self.x = 0
            self.vx *= -1 * dampening

        if self.y > h:
            self.y = h
            self.vy *= -1 * dampening
        elif self.y < 0:
            self.y = 0
            self.vy *= -1 * dampening

    def applyForce(self, fx, fy):
        self.ax += fx / self.m
        self.ay += fy / self.m

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        self.ax = 0
        self.ay = 0
        self.edges()

    def show(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.r)


class electron(proton):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.r = 5
        self.m = 1
        self.q = -1

    def show(self):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.r)


class neutron(proton):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.r = 8
        self.m = 1
        self.q = 0

    def show(self):
        pygame.draw.circle(screen, (200, 200, 200), (self.x, self.y), self.r)


particles = []

for i in range(n):
    if i % 3 == 0:
        particles.append(proton(randint(0, w), randint(0, h)))
    elif i % 3 == 1:
        particles.append(electron(randint(0, w), randint(0, h)))
    else:
        particles.append(neutron(randint(0, w), randint(0, h)))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    [p.attract(particles) for p in particles]

    for p in particles:
        p.move()
        p.show()
    pygame.display.update()
