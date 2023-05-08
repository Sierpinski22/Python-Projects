from p5 import *
from random import choice, randint

max_points = int(input("Numero di vertici? > "))
coefficient = float(input("Di quanto si sposta il punto? (min 0, max 1) > "))
randomized = input("Vertici randomizzati? (y, n) > ") == 'y'
restriction = input("Attivare restrizione? (y, n) > ") == 'y'
angle = TWO_PI / max_points
fixed = []
x = y = radius = current = previous = 0
counter = 0
pre = None


def restart():
    x2 = randint(0, width)
    y2 = randint(0, height)

    global radius, x, y
    new_fixed = []

    for k in range(max_points):
        x3 = radius * cos(angle * k + angle / 4) + width / 2 if not randomized else randint(0, width)
        y3 = radius * sin(angle * k + angle / 4) + height / 2 if not randomized else randint(0, height)
        new_fixed.append(Vector(x3, y3))
    x, y = x2, y2
    return Vector(x2, y2).copy(), new_fixed.copy()


def setup():
    size(600, 600)
    background(0, 0, 0)
    global radius
    global current
    global x, y
    radius = 2 * width / 5


def draw():

    global current, x, y, previous, counter, fixed, pre
    no_stroke()

    if counter % 300 == 0:
       
        current, fixed = restart()
        background(0, 0, 0)

    fill(255, 255, 255)

    for v in range(max_points):
        ellipse(fixed[v].x, fixed[v].y, 10, 10)

    for i in range(20):
        extraction = choice(fixed)
        while extraction is previous and restriction:
            extraction = choice(fixed)
        if restriction:
            previous = extraction
        pre = current.copy()
        current.x = lerp(current.x, extraction.x, coefficient)
        current.y = lerp(current.y, extraction.y, coefficient)
        ellipse(current.x, current.y, 1, 1)
        # line((pre.x, pre.y), (current.x, current.y))


    fill(0, 255, 0)
    ellipse(x, y, 6, 6)
    counter += 1

    
run()
