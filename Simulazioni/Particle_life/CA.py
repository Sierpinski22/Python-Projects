import pygame
from random import uniform, randint
from vector import *
from quadtree import *

pygame.init()
screen = pygame.display.set_mode((1300, 650))
w, h = screen.get_size()

#  idee: interazione, salvataggio schemi interessanti, nuovo modo di originare

secret = False
max_particles = 600
n_ = 6

size = 7
max_radius = size / 2 * 7
min_radius = size / 2 * 4
max_force = 5
min_force = max_force / 6
limit = 3.5
speed = 2.7
friction = 0.84
simulation = []
q = quadtree(0, 0, w, h)
sep_coefficient = 1.7


def rules(n):  # ok
    rule = [[] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            rule[i].append(speed * uniform(-max_force, max_force))
    return rule


def quality(n):  # min e max radius, max speed
    attributes = []
    for i in range(n):
        m_r = uniform(min_radius / limit, min_radius)
        attributes.append([m_r, uniform(max_radius / limit, max_radius), max_force / limit,
                           uniform(max_force / limit, max_force)])
    return attributes


def colours(n):
    colors = []
    for i in range(n):
        colors.append((randint(50, 150), randint(25, 200), randint(0, 100)))
    return colors


class particle:  # max radius e min radius sono separati
    def __init__(self, diplomacy, qualities, colour, index=None, loc=None):
        self.index = index if index is not None else randint(0, n_ - 1)
        self.loc = loc if loc is not None else vector(randint(size, w - size), randint(size, h - size))
        self.vel = vector(0, 0)
        self.col = colour[self.index]
        self.rules = diplomacy[self.index]
        self.min_radius = qualities[self.index][0]
        self.max_radius = qualities[self.index][1]
        self.max_force = qualities[self.index][2]
        self.max_repulsion = qualities[self.index][3]

    def edges(self):
        if self.loc.x > w:
            self.loc.x = 0
        elif self.loc.x < 0:
            self.loc.x = w
        if self.loc.y > h:
            self.loc.y = 0
        elif self.loc.y < 0:
            self.loc.y = h

    def move(self, neigh=None):
        if neigh is None:
            neigh = simulation

        acceleration = self.interactions(neigh)
        if acceleration.mag() > min_force:
            self.vel += acceleration
        self.vel *= friction
        self.loc += self.vel
        self.edges()

    def interactions(self, neigh):
        diff = vector(0, 0)
        sep = vector(0, 0)
        for other in neigh:
            d = self.loc.dist(other.loc)
            if d > self.min_radius:
                if d < self.min_radius + self.max_radius:
                    per = 1 / abs(self.max_radius / 2 - (d - self.min_radius))  # qui
                    diff += ((other.loc - self.loc) * per * self.rules[other.index])


            elif 0 < d < min_radius:
                sep += (self.loc - other.loc) / (d * d) * sep_coefficient

        sep *= sep_coefficient
        diff.limit(self.max_force)
        return diff + sep

    def show(self):
        pygame.draw.circle(screen, self.col, (self.loc.x, self.loc.y), size / 2)


r = rules(n_)
a = quality(n_)
c = colours(n_)

for _ in range(max_particles):
    simulation.append(particle(r, a, c))


def to_element(lis):
    element_ed = []
    for thing in lis:
        element_ed.append(element(thing, thing.loc.x, thing.loc.y))
    return element_ed


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    q.put(to_element(simulation))
    for p in simulation:
        p.show()
        r = (p.min_radius + p.max_radius) * 2
        x_, y_ = to_centred(p.loc.x, p.loc.y, r, r)
        p.move(q.query(x_, y_, r, r))

    if secret:
        for s in q.show():
            pygame.draw.rect(screen, (0, 255, 0), s, 1)

    pygame.display.update()
    q.reset()
