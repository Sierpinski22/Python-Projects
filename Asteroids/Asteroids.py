import pygame
from math import cos, sin, pi, sqrt
from random import uniform, randint

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_width(), screen.get_height()
obstacles = []
score = 0
min_size = 12


def distance(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


class bullet:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = 800
        self.radius = 2
        self.active = True

    def move(self):
        if self.active:
            self.x += self.vx
            self.y += self.vy
            if self.x < 0:
                self.x = w
            elif self.x > w:
                self.x = 0
            if self.y < 0:
                self.y = h
            elif self.y > h:
                self.y = 0
            self.life -= 1
            self.show()

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)


class asteroid:
    def __init__(self, x, y, radius, angle):
        a = 2 * pi / 12
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 6 / self.radius
        self.vertexes = []
        self.vx = self.speed * cos(angle)
        self.vy = self.speed * sin(angle)
        self.active = True

        for i in range(12):
            r = uniform(self.radius / 2, radius)
            self.vertexes.append([r * cos(i * a), r * sin(i * a)])

    def move(self):
        if self.active:
            self.x += self.vx
            self.y += self.vy
            if self.x < 0:
                self.x = w
            elif self.x > w:
                self.x = 0
            if self.y < 0:
                self.y = h
            elif self.y > h:
                self.y = 0
            self.show()

    def show(self):
        for v in range(1, 12):
            pygame.draw.line(screen, (255, 255, 255), (self.vertexes[v][0] + self.x, self.vertexes[v][1] + self.y),
                             (self.vertexes[v - 1][0] + self.x, self.vertexes[v - 1][1] + self.y), 4)
            pygame.draw.line(screen, (255, 255, 255), (self.vertexes[0][0] + self.x, self.vertexes[0][1] + self.y),
                             (self.vertexes[11][0] + self.x, self.vertexes[11][1] + self.y), 4)

    def divide(self, nw):
        if self.active:
            global score
            if self.radius > 18:
                nw.append(asteroid(self.x, self.y, self.radius / 2, uniform(0, 2 * pi)))
                nw.append(asteroid(self.x, self.y, self.radius / 2, uniform(0, 2 * pi)))
                score += self.radius / min_size * 100
                print(score)
        self.active = False


class ship:
    def __init__(self):
        self.x = w / 2
        self.y = h / 2
        self.v = 0.002
        self.vx = 0
        self.vy = 0
        self.angle = -pi / 2
        self.radius = 20
        self.v_max = 0.7
        self.bullets = []
        self.bullet_speed = 1
        self.countdown = 0
        self.recharge = 0

    def show(self):
        pygame.draw.line(screen, (255, 255, 255),
                         (self.x + self.radius * cos(self.angle), self.y + self.radius * sin(self.angle)),
                         (self.x + self.radius * cos(self.angle + 3 * pi / 4),
                          self.y + self.radius * sin(self.angle + 3 * pi / 4)), 5)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.x + self.radius * cos(self.angle + 3 * pi / 4),
                          self.y + self.radius * sin(self.angle + 3 * pi / 4)),
                         (self.x + self.radius / 3 * cos(self.angle + pi),
                          self.y + self.radius / 2 * sin(self.angle + pi)), 5)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.x + self.radius / 3 * cos(self.angle + pi),
                          self.y + self.radius / 2 * sin(self.angle + pi)),
                         (self.x + self.radius * cos(self.angle - 3 * pi / 4),
                          self.y + self.radius * sin(self.angle - 3 * pi / 4)), 5)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.x + self.radius * cos(self.angle - 3 * pi / 4),
                          self.y + self.radius * sin(self.angle - 3 * pi / 4)),
                         (self.x + self.radius * cos(self.angle), self.y + self.radius * sin(self.angle)), 5)

    def move(self):
        self.vx *= 0.999
        self.vy *= 0.999
        self.x += self.vx
        self.y += self.vy
        self.edges()
        for b in self.bullets:
            if b.life > 0:
                b.move()
        self.recharge -= 1
        self.countdown -= 1

    def boost(self):
        self.vx += self.v * cos(self.angle)
        self.vy += self.v * sin(self.angle)
        self.vx = self.vx if self.vx < self.v_max else self.v_max
        self.vy = self.vy if self.vy < self.v_max else self.v_max

    def edges(self):
        if self.x < 0:
            self.x = w
        elif self.x > w:
            self.x = 0
        if self.y < 0:
            self.y = h
        elif self.y > h:
            self.y = 0

    def rotate(self, v):
        self.angle += v

    def shoot(self):
        if self.countdown <= 0:
            self.bullets.append(
                bullet(self.x, self.y, self.bullet_speed * cos(self.angle) + self.vx, self.bullet_speed * sin(self.angle) + self.vy))
            self.countdown = 60

    def warp(self):
        if self.recharge <= 0:
            # pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, 3)
            self.x, self.y = uniform(0, w), uniform(0, h)
            # pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, 3)
            self.recharge = 120

    def impacts(self):
        global obstacles, score
        for ob in obstacles:
            if distance(self.x, self.y, ob.x, ob.y) < self.radius + ob.radius:
                return True
            if len(self.bullets) != 0:
                for b in self.bullets:
                    if distance(b.x, b.y, ob.x, ob.y) < b.radius + ob.radius and (b.active and ob.active):
                        ob.divide(obstacles)
                        score += ob.radius * 3
                        b.active = False
        self.clear()
        return False

    def clear(self):
        global obstacles
        proto_b = self.bullets.copy()
        proto_o = obstacles.copy()
        self.bullets = [b for b in proto_b if b.active and b.life > 0]
        obstacles = [j for j in proto_o if j.active]


s = ship()
counter = 0


def add_asteroid():
    x1, y1 = uniform(0, w), uniform(0, h)
    while distance(s.x, s.y, x1, y1) < 80:
        x1, y1 = uniform(0, w), uniform(0, h)
    obstacles.append(asteroid(x1, y1,  randint(1, 4) * min_size, uniform(0, 2 * pi)))


def restart():
    return ship(), [], 0


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        s.rotate(-0.01)
    elif keys[pygame.K_d]:
        s.rotate(0.01)
    elif keys[pygame.K_SPACE]:
        s.boost()
    elif keys[pygame.K_k]:
        s.shoot()
    elif keys[pygame.K_s]:
        s.warp()
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()

    for o in obstacles:
        o.move()

    if s.impacts():
        s, obstacles, score = restart()
        counter = 0

    if counter % 1500 == 0 and len(obstacles) < 15:
        add_asteroid()

    s.show()
    s.move()
    counter += 1
    pygame.display.update()
