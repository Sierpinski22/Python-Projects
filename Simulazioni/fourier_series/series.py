import pygame
import math
import sys


check = True
max_circle = input("Quanti cerchi vuoi? > ")
sys.setrecursionlimit(2003)
while check:
    try:
        assert 0 <= int(max_circle) < sys.getrecursionlimit() - 2
        check = False
    except AssertionError:
        if int(max_circle) < 0:
            print("Il numero deve essere positivo o nullo! Riprova!")
        else:
            print("Il numero supera la profondità massima di ricorsione! Riprova!")
    except ValueError:
        print("Il numero non può essere una stringa o un carattere! Riprova!")
    finally:
        if check:
            max_circle = input("Quanti cerchi vuoi? > ")

max_circle = int(max_circle)
pygame.init()
size = (1200, 600)
screen = pygame.display.set_mode(size)
colour = (255, 255, 255)
lighter = (155, 0, 0)
w = screen.get_width()
h = screen.get_height()
r = 150
angle = 0
wave = []
max_point = 500
phase = w / 2


class cerchio:
    def __init__(self, radius, n, x_, y_, p=0, parent=None):
        self.parent = parent
        self.child = None
        self.radius = radius
        self.n = n
        self.x = x_
        self.y = y_
        self.phase = p

    def add_child(self, rag=None, freq=None, phi=None):

        if self.child is None:
            if rag is None or freq is None or phi is None:
                rag = r * 4 / ((self.n + 2) * math.pi)
                freq = self.n + 2
                phi = 0
                self.child = cerchio(rag, freq,
                                     self.radius * math.cos(angle * self.n + self.phase) + self.x,
                                     self.radius * math.sin(angle * self.n + self.phase) + self.y, phi, self)
        else:
            self.child.add_child(rag, freq, phi)

    def move(self):
        if self.parent is not None:
            self.x = self.parent.radius * math.cos(angle * self.parent.n + self.parent.phase) + self.parent.x
            self.y = self.parent.radius * math.sin(angle * self.parent.n + self.parent.phase) + self.parent.y

        if self.child is not None:
            self.child.move()

    def show(self):
        if self.child is not None:
            pygame.draw.circle(screen, colour, (self.x, self.y), self.radius, 3)
            self.child.show()
            pygame.draw.line(screen, (100, 100, 100), (self.x, self.y), (self.child.x, self.child.y), 3)
        else:
            pygame.draw.circle(screen, lighter, (self.x, self.y), 4)

    def give(self):
        if self.child is not None:
            return self.child.give()
        else:
            return self.y, self.x


c1 = cerchio(r * 4 / math.pi, 1, w / 5, h / 2)
for f in range(max_circle):
    c1.add_child()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    screen.fill((0, 0, 0))

    angle += 0.01
    c1.show()
    c1.move()
    y, x = c1.give()
    wave.insert(0, y)
    for i in range(1, len(wave)):
        pygame.draw.line(screen, colour, (i - 1 + phase, wave[i - 1]), (i + phase, wave[i]), 3)
    if len(wave) > max_point:
        wave = wave[:max_point].copy()
    pygame.draw.line(screen, lighter, (x, y), (phase, wave[0]), 3)
    pygame.display.update()
