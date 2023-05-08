from graphics import *
import random as r
import math as n

print("Usando numeri troppo grandi le palline si sovrappongono e si incasina tutto")
m = int(input("Quante palline vuoi? > "))
minr = int(input("Raggio minimo? > "))
maxr = int(input("Raggio massimo? > "))
w = GraphWin("Numeri umili ragazzi", 600, 600)
palette = [color_rgb(r.randint(100, 255), r.randint(100, 255), r.randint(100, 255)) for i in range(m)]
w.setBackground(color_rgb(0, 0, 0))


def dist(x, y, x1, y1):
    return int(n.sqrt(n.pow(x - x1, 2) + n.pow(y - y1, 2)))


class palla:
    def __init__(self):
        self.vx = r.random() * 2
        self.vy = r.random() * 2
        self.i = r.randint(0, m)
        self.ragg = r.randint(minr, maxr)
        self.dx = r.randint(self.ragg, w.width - self.ragg)
        self.dy = r.randint(self.ragg, w.width - self.ragg)


    def fix(self):
        for s in cesto:
            if s is not self:
                while self.un_fixed():
                    self.dx = r.randint(self.ragg, w.width - self.ragg)
                    self.dy = r.randint(self.ragg, w.height - self.ragg)


        self.area = Circle(Point(self.dx, self.dy), self.ragg)
        self.area.setFill(palette[self.i % m])
        self.area.draw(w)

    def un_fixed(self):
        for v in cesto:
            if v is not self:
                if dist(self.dx, self.dy, v.dx, v.dy) <= self.ragg + v.ragg:
                    return True
        return False

    def edge(self):
        x = self.area.getCenter().getX()
        y = self.area.getCenter().getY()
        if not self.area.getRadius() < x < w.width - self.area.getRadius():
            self.vx *= -1
            self.i += 1
        if not self.area.getRadius() < y < w.height - self.area.getRadius():
            self.vy *= -1
            self.i += 1


    def collision(self):
        x = self.area.getCenter().getX()
        y = self.area.getCenter().getY()

        for t in cesto:
            if t is not self:
                x1 = t.area.getCenter().getX()
                y1 = t.area.getCenter().getY()

                if dist(x, y, x1, y1) < self.ragg + t.ragg:
                    self.vx *= -1
                    self.vy *= -1
                    self.i += 1

    def run(self):
        self.collision()
        self.edge()

    def bounce(self):
        self.area.setFill(palette[self.i % m])
        self.area.move(self.vx, self.vy)


cesto = [palla() for j in range(m)]

if m > 40 and minr > 30:
    print("Hai esagerato con le dimensioni razza di megalomane!")

for o in cesto:
    o.fix()

while True:
    for p in cesto:
        p.run()
    for p in cesto:
        p.bounce() #prima controllo le posizioni, poi sposto il tutto
