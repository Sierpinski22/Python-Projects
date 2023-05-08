from dft import dft
from math import cos, sin, pi
from time import sleep
from snowflake_gen import generate
import pygame

pygame.init()
screen = pygame.display.set_mode((650, 650))
angle = 0
w, h = screen.get_width(), screen.get_height()
wave = []
counter = 0


def restart():
    result1 = dft(generate(8, 8, h / 2))
    buff1 = (pi * 2) / len(result1)
    # result1 = sorted(result1, key=lambda r: r[1], reverse=True)
    print(result1, "\n")
    return result1.copy(), buff1


result, buff = restart()


def draw(x, y):
    for f in range(len(result)):
        px = x
        py = y
        frequency, amplitude, phase = result[f][0], result[f][1], result[f][2]
        x += amplitude * cos(angle * frequency + phase)
        y += amplitude * sin(angle * frequency + phase)
        pygame.draw.circle(screen, (150, 150, 150), (px, py), amplitude, 2)
        pygame.draw.line(screen, (150, 150, 150), (px, py), (x, y), 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    screen.fill((0, 0, 0))
    x1, y1 = draw(w / 2, h / 2)
    wave.append([x1, y1])

    for i in range(1, len(wave)):
        temp = (74, 109, 229) if i % 2 == 0 else (136, 160, 245)
        pygame.draw.line(screen, temp, (wave[i - 1][0], wave[i - 1][1]), (wave[i][0], wave[i][1]), 4)

    pygame.display.update()
    counter += 1

    if counter > len(result):
        sleep(1)
        angle = 0
        counter = 0
        result, buff = restart()
        wave = []
    else:
        angle += buff
        sleep(0.1)
