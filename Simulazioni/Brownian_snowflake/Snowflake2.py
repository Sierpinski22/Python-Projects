import pygame
from math import sqrt, sin, pi, atan, cos
from random import randrange, randint, random
from time import sleep


speed = 20
mirror = 6
pygame.init()
screen = pygame.display.set_mode((700, 700))
w, h = screen.get_width(), screen.get_height()
angle = 2 * pi / mirror  # nel mio caso pi / 3
min_range = -4
max_range = (-min_range) + 1
start_y = 0 #sin(angle / 4) * w / 4
start_x = w / 2 - 10
radius = (2, 4)
completed = False


def constrain(x, maxim, minim):
    return max(min(x, maxim), minim)


def distance(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


class snowflake:
    def __init__(self, x=start_x, y=start_y, stuck=False):
        self.x = x
        self.y = y
        self.stuck = stuck
        self.vx = -0.5
        self.radius = randint(*radius)
        r = randint(0, 200)
        if random() > 0: # qui
            if random() > 0: # qui
                self.color = (255 - r, 255 - r, 255)
            else:
                self.color = (55 + r, 100, 50)
        else:
            self.color = (255 - r, 255 - r, 255)

    def move(self):  # per qualche miracolo divino funziona, forse #
        if not self.stuck:
            self.x += self.vx
            self.y += randrange(min_range, max_range)
            self.y = constrain(self.y, self.x * sin(angle / 2), 0)
            # pygame.draw.line(screen, (255, 255, 255), (w / 2, h / 2), (w, h / 2 + self.x * sin(angle / 2)), 3)
            # pygame.draw.line(screen, (255, 255, 255), (w / 2, h / 2), (w, h / 2 - self.x * sin(angle / 2)), 3)

    def collision(self, sn):  # anche questo #
        if not self.stuck:
            for z in sn:
                if z is not self and z.stuck:
                    if distance(self.x, self.y, z.x, z.y) <= self.radius + z.radius:
                        self.stuck = True
                        return special_add(self.x, self.y, self.radius, self.color)


def special_add(x, y, r, c):
    angle1 = atan(y / x)
    radius1 = distance(0, 0, x, y)

    for i in range(mirror):
        x1 = radius1 * cos(angle * i + angle1 + angle / 2) + w / 2
        x2 = radius1 * cos(angle * i - angle1 + angle / 2) + w / 2
        y1 = radius1 * sin(angle * i + angle1 + angle / 2) + h / 2
        y2 = radius1 * sin(angle * i - angle1 + angle / 2) + h / 2

        pygame.draw.circle(screen, c, (x1, y1), r)
        pygame.draw.circle(screen, c, (x2, y2), r)


start = snowflake(0, 0, True)
crystal = [start]
pygame.draw.circle(screen, start.color, (start.x + w / 2, start.y + h / 2), start.radius)
counter = 0
number = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    for s in crystal:
        s.collision(crystal)
        s.move()
        if s.stuck and s.x == start_x and s.y == start_y:
            completed = True

    counter += 1
    if number == 20:
        pygame.quit()
        break

    pygame.display.update()
    if counter % speed == 0 and not completed:
        crystal.append(snowflake())
    elif completed:
        pygame.image.save(screen, f"{number}.jpg")
        number += 1
        print(number)
        sleep(2)
        screen.fill((0, 0, 0))
        start = snowflake(0, 0, True)
        crystal = [start]
        pygame.draw.circle(screen, start.color, (start.x + w / 2, start.y + h / 2), start.radius)
        counter = 0
        completed = False
