from math import pi

w, h = 0, 0


def initialize(x, y):
    global w, h
    w, h = x, y


def s():
    return {'tree': ('0', {'f': 'ff', '0': 'f[+0-]-0'}, [w / 2, h, pi / 2], pi/4, 7, 10),
            'sier': ('f-g-g', {'f': 'f−g+f+g−f', 'g': 'gg'}, [w/2, w/9, -pi/3], 2*pi/3, 7, 10),
            's1er': ('f', {'f': 'g−f−g', 'g': 'f+g+f'}, [w/5, 7*h/8, 0], pi/3, 7, 10),
            'drag': ('f', {'f': 'f+g', 'g': 'f-g'}, [w/3, 2*h/3, pi], -pi/2, 13, 7),
            'fern': ('x', {'x': 'F+[[X]-X]-F[-FX]+X'.lower(), 'f': 'ff'}, [0, h, pi/4], pi * 25 / 180, 7, 6)}
