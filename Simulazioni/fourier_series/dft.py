import math
import cmath

def dft(signal):
    transformed = []
    length = len(signal)
    for k in range(length):
        total = complex(0, 0)
        for i in range(length):
            angle1 = (math.pi * 2 * k * i) / length
            c = complex(signal[i][0], signal[i][1])
            a = complex(math.cos(angle1), -math.sin(angle1))
            total += c * a

        aver = complex(total.real / length, total.imag / length)
        amplitude, phase = cmath.polar(aver)
        frequency = k
        transformed.append([amplitude, frequency, phase])
    print(transformed)
    return transformed

