import pygame
from math import sqrt, sin, pi, atan, cos
from random import randrange

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_width(), screen.get_height()
mirror = 6
angle = pi / 3
min_range = -4
max_range = -min_range + 1
solid = [[w / 2, h / 2]]


def distance(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


start_y = h / 2


def special_add(x, y):
    y1 = -(h / 2 - y)
    # prototype = [[x, y1], [x, y]]
    angle1 = atan(y / x)
    angle2 = atan(y1 / x)
    length = distance(x, y, w / 2, h / 2)

    for i in range(mirror):
        solid.append([length * cos(i * angle + angle1) + w / 2, length * sin(i * angle + angle1) + start_y])
        solid.append([length * cos(i * angle + angle2) + w / 2, length * sin(i * angle + angle2) + start_y])


class snowflake:
    def __init__(self, x_=w, y_=start_y, st=False):
        self.x = x_
        self.y = y_
        self.vx = -0.1
        self.stuck = st
        self.radius = 2

    def move(self):
        self.x -= 1
        self.y += randrange(min_range, max_range)
        max_a = h / 2 - (self.x - w / 2) * sin(angle / 2)
        if self.y > h / 2:
            self.y = h / 2
        elif self.y < max_a:
            self.y = max_a

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

    def collision(self, others):
        if not self.stuck:
            for v in others:
                if v is not self and v.stuck:
                    if distance(self.x, self.y, v.x, v.y) <= self.radius + v.radius:
                        self.stuck = True
                        return self.x, self.y
        return None, None


crystal = [snowflake(w / 2, h / 2, True)]
counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    screen.fill((0, 0, 0))

    for c in crystal:
        px, py = c.collision(crystal)
        if not c.stuck:
            c.move()
        else:
            c.show()
        if px is not None:
            special_add(px, py)


        for s in solid:
            pygame.draw.circle(screen, (255, 255, 255), (s[0], s[1]), 2)

    if counter % 100 == 0 and counter < 40000:
        crystal.append(snowflake())
    counter += 1
    pygame.display.update()
