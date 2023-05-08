from math import sin, cos, pi
from Systems import s, initialize
from time import sleep
import pygame

pygame.init()
w, h = (1000, 700)
initialize(w, h)
screen = pygame.display.set_mode((w, h))


def f(co):
    x, y = co[-1][0] + side * cos(co[-1][2]), co[-1][1] - side * sin(co[-1][2])
    pygame.draw.line(screen, (255, 255, 255), (co[-1][0], co[-1][1]), (x, y))
    co[-1] = [x, y, co[-1][2]]  # !
    return co


def g(co):
    x, y = co[-1][0] + side * cos(co[-1][2]), co[-1][1] - side * sin(co[-1][2])
    pygame.draw.line(screen, (255, 255, 255), (co[-1][0], co[-1][1]), (x, y))
    co[-1] = [x, y, co[-1][2]]  # !
    return co


def x_(co):
    return co


def end(co):
    x, y = co[-1][0] + side * cos(co[-1][2]), co[-1][1] - side * sin(co[-1][2])
    pygame.draw.line(screen, (255, 255, 255), (co[-1][0], co[-1][1]), (x, y))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
    co[-1] = [x, y, co[-1][2]]  # !
    return co


def plus(co):
    co[-1] = [co[-1][0], co[-1][1], co[-1][2] + angle]
    return co


def minus(co):
    co[-1] = [co[-1][0], co[-1][1], co[-1][2] - angle]
    return co


def l_par(co):
    co.append(co[-1])
    return co


def r_par(co):
    co = co[:len(co) - 1]
    return co


class l_system:
    def __init__(self, V, omega, P, start=None):
        if start is None:
            start = [w / 2, h / 2, pi / 2]  #

        self.V = V
        self.omega = omega  # axiom
        self.P = P

        self.coordinates = [start]

    def update(self, string=None):
        if string is None:
            string = self.omega
        new_string = ''
        coordinates = self.coordinates.copy()
        for letter in list(string):
            new_string += self.P[letter] if letter in self.P.keys() else letter
            try:
                coordinates = self.V[str(letter)](coordinates.copy())
            except KeyError:
                coordinates = self.V['-'](coordinates.copy())
                # a volte '-' non è '-'?????????????????????????
        return new_string

    def cycle(self, n):
        omegas = [self.omega]
        for i in range(n):
            screen.fill((0, 0, 0))
            omegas.append(self.update(omegas[-1]))
            if i + 1 == n:
                pygame.display.update()
        return omegas


def unpack(choice):
    axiom, rules, location, angle_, iterations, side_ = s()[choice]
    return axiom, rules, location, angle_, iterations, side_


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    a, r, l_, angle, it_, side = unpack('fern')
    v = {'f': f, '+': plus, '-': minus, '[': l_par, ']': r_par, '0': end, 'g': g, 'x': x_}
    lsys = l_system(v, a, r, l_)

    for t in range(1, it_ + 1):
        o = lsys.cycle(t)
        print(f"{f'{t - 1}:':<3}{o[-1]}")
        sleep(1)
