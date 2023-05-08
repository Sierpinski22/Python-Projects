from math import cos, sin, pi
import random


def rotation(to_rotate, max_m, max_v, max_a):
    for g in range(1, max_m):
        for k in range(max_v):
            to_rotate.append([to_rotate[k][0], to_rotate[k][1] + max_a * g])
    return to_rotate


def to_cartesian(polar):
    transformed = []
    r1 = polar[0][0]
    a1 = polar[0][1]
    x1 = r1 * cos(a1)
    y1 = r1 * sin(a1)
    for d in polar:
        radius = d[0]
        a = d[1]
        transformed.append([radius * cos(a), radius * sin(a)])
    transformed.append([x1, y1])

    return transformed


def generate(nv, ns, r):
    max_vertexes = nv
    max_mirror = ns
    max_angle = pi * 2 / max_mirror
    max_increment = max_angle / max_vertexes
    max_radius = r
    vertex = []

    for f in range(max_vertexes):
        r = random.randint(0, max_radius)
        vertex.append([r, f * max_increment])

    vertex = rotation(vertex, max_mirror, max_vertexes, max_angle).copy()
    vertex = to_cartesian(vertex).copy()
    print(vertex)
    return vertex.copy()
