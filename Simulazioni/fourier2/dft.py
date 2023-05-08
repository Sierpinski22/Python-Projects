from math import sin, cos, pi, atan2, sqrt


class vector:
    def __init__(self, x, y):
        self.re = x
        self.im = y

    def add(self, c):
        self.re += c.re
        self.im += c.im

    def multiplication(self, c):
        re = self.re * c.re - self.im * c.im
        im = self.re * c.im + self.im * c.re
        return vector(re, im)


def dft(signal):
    complexes = []
    for s in range(len(signal)):
        complexes.append(vector(signal[s][0], signal[s][1]))
    transformed = []
    length = len(complexes)


    for k in range(length):
        total = vector(0, 0)
        for n in range(length):
            angle1 = (pi * 2 * k * n) / length
            c = vector(cos(angle1), -sin(angle1))
            total.add(complexes[n].multiplication(c))

        total.re /= length
        total.im /= length

        phase = atan2(total.im, total.re)
        amplitude = sqrt(total.re * total.re + total.im * total.im)
        frequency = k

        transformed.append([frequency, amplitude, phase])

    return transformed
