from math import sin, cos, pi, atan2, sqrt
from random import uniform


def rand_coordinates():
    angle = uniform(-pi, pi)
    return cos(angle), sin(angle)


def distance(x, y, x1, y1):
    return sqrt(((x - x1) ** 2) + ((y - y1) ** 2))


class vector:
    def __init__(self, x=0, y=0, rand=False):
        if not rand:
            self.x = x
            self.y = y
        else:
            self.x, self.y = rand_coordinates()

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return vector(self.x / other, self.y / other)

    def set(self, x, y):
        self.x, self.y = x, y

    def heading(self):
        return atan2(self.y, self.x)

    def copy(self):
        return vector(self.x, self.y, False)

    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        normalized = self / self.mag()
        self.x = normalized.x
        self.y = normalized.y

    def set_mag(self, number):
        self.normalize()
        multiplied = self * number
        self.x = multiplied.x
        self.y = multiplied.y

    def dist(self, other):
        return distance(self.x, self.y, other.x, other.y)

    def limit(self, number):
        if self.mag() > number:
            self.set_mag(number)

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y

    def mult(self, number):
        self.x *= number
        self.y *= number

    def div(self, number):
        self.x /= number
        self.y /= number


