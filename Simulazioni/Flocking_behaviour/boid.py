from vector import *
from random import randint

w, h = 0, 0
max_speed = 4
radius = 40
max_force = 0.7
min_force = max_force / 7
coefficient_co, coefficient_al, coefficient_sep = 0.5, 0.8, 2.4


def init(width, height):
    global w, h
    w, h = width, height


class boid:
    def __init__(self, x=None, y=None):
        self.coh_radius = radius
        self.ali_radius = radius
        self.sep_radius = 2 * radius / 3
        self.radius = radius

        if x is not None:
            self.loc = vector(x, y)
        else:
            self.loc = vector(randint(0, w), randint(0, h))
        self.vel = vector(rand=True)
        self.acc = vector()
        self.pseudo_loc = self.loc.copy()
        self.dir = self.vel.heading()

    def move(self, neighbours):

        # self.acc += self.cohesion(neighbours) * coefficient_co
        # self.acc += self.alignment(neighbours) * coefficient_al
        # self.acc += self.separation(neighbours) * coefficient_sep
        force = self.behave(neighbours)
        if force.mag() > min_force:
            self.acc += self.behave(neighbours)
        self.vel += self.acc
        self.vel.limit(max_speed)
        self.pseudo_loc += self.vel
        self.edge()
        self.acc.mult(0)
        self.dir = self.vel.heading()

    def edge(self):
        self.pseudo_loc.x = (self.pseudo_loc.x + w) % w
        self.pseudo_loc.y = (self.pseudo_loc.y + h) % h

    def show(self):
        self.loc = self.pseudo_loc.copy()
        angle = self.vel.heading()
        return (self.loc.x + self.radius / 5 * cos(angle), self.loc.y + self.radius / 5 * sin(angle)), \
               (self.loc.x + self.radius / 5 * cos(angle + 3 / 4 * pi),
                self.loc.y + self.radius / 5 * sin(angle + 3 / 4 * pi)), \
               (self.loc.x + self.radius / 15 * cos(angle + pi), self.loc.y + self.radius / 15 * sin(angle + pi)), \
               (self.loc.x + self.radius / 5 * cos(angle + 5 / 4 * pi),
                self.loc.y + self.radius / 5 * sin(angle + 5 / 4 * pi))


    def behave(self, flock):
        alignment = vector(0, 0)
        separation = vector(0, 0)
        cohesion = vector(0, 0)
        ali_count = 0
        sep_count = 0
        coh_count = 0

        for other in flock:
            if other is not self:
                d = self.loc.dist(other.loc)

                if d < self.coh_radius:
                    cohesion.add(other.loc)
                    coh_count += 1
                if d < self.ali_radius:
                    alignment.add(other.vel)
                    ali_count += 1
                if 0 < d < self.sep_radius:
                    difference = self.loc - other.loc
                    difference.div(d)
                    separation.add(difference)
                    sep_count += 1

        if coh_count != 0:
            cohesion.div(coh_count)
            cohesion.sub(self.loc)
            cohesion.limit(max_force)

        if ali_count != 0:
            alignment.set_mag(self.vel.mag())
            alignment.sub(self.vel)
            alignment.limit(max_force)

        if sep_count != 0:
            separation.div(sep_count)
            separation.limit(max_force)

        return cohesion * coefficient_co + alignment * coefficient_al + separation * coefficient_sep

    #  ====================================LA CLASSE FINISCE QUI=====================================================

    def cohesion(self, flock):  # verso il punto medio
        steer = vector(0, 0)
        counter = 0
        for other in flock:
            if other is not self:
                # print(self.loc.dist(other.loc), self.loc.x, self.loc.y, other.loc.x, other.loc.y)
                if self.loc.dist(other.loc) < self.radius:
                    steer.add(other.loc)
                    counter += 1

        if counter != 0:
            steer.div(counter)
            steer.sub(self.loc)
            steer.limit(max_force)
        return steer

    def alignment(self, flock):  # cambio di direzione, ossia di angolo
        steer = vector(0, 0)
        counter = 0
        for other in flock:
            if other is not self:
                if self.loc.dist(other.loc) < self.radius:
                    steer.add(other.vel)
                    counter += 1

        if counter != 0:
            steer.set_mag(self.vel.mag())
            steer.sub(self.vel)
            steer.limit(max_force)
        return steer

    def separation(self, flock):
        steer = vector(0, 0)
        counter = 0
        for other in flock:
            if other is not self:
                d = self.loc.dist(other.loc)
                if 0 < d < self.radius / 2:
                    difference = self.loc - other.loc
                    difference.div(d * 2)
                    steer.add(difference)
                    counter += 1

        if counter != 0:
            steer.div(counter)
            steer.limit(max_force)
        return steer
