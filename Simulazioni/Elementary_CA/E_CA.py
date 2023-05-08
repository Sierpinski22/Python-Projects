import pygame
from random import random
from time import sleep
from Network import *

is_training = True


pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_size()
screen.fill((255, 255, 255))
pygame.display.update()
side = 10
cols, rows = int(w / side), int(h / side)

# ---------------------------------#
model, optimizer = build_model(cols)
# -------------------------------- #

rand = False
clear = False
r = 3
dec = [[111, 0], [110, 1], [101, 2], [100, 3], [11, 4], [10, 5], [1, 6], [0, 7]]

rules = [[0, 1, 1, 1, 1, 1, 1, 0],  # 0: sierpinski
         [0, 0, 1, 0, 1, 1, 0, 1],  # 1: parete rocciosa
         [0, 1, 0, 1, 0, 1, 1, 0],  # 2: conchiglia
         [0, 1, 0, 0, 1, 0, 0, 1]   # 3: storto
         ]

seed = [round(random()) for _ in range(cols)] if rand else [int(i == int(cols / 2)) for i in range(cols)]
ro = -1


def decoder(build):
    for b, index in dec:
        if build == b:
            return index
    print('errore')


def update(line, rule):
    newline = [0 for _ in range(len(line))]
    for i in range(cols):
        build = 100 * line[(i - 1 + cols) % cols] + 10 * line[i] + line[(i + 1 + cols) % cols]
        result = rule[decoder(build)]
        newline[i] = result
    return newline


if not is_training:
    print('Loaded')
    load(model)

k = 0

while True:
    k += 1
    if k == 60 * 10 and is_training:
        save(model)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    ro = (ro + 1) % rows

    s = update(seed, rules[r]).copy()
    if is_training:
        out = train(model, optimizer, seed, s)
    else:
        out = generate(model, seed, False)
    seed = s.copy()

    for i, c in enumerate(out):
        color = (255 - round(255 * c))
        pygame.draw.rect(screen, (color, color, color), (i * side, ro * side, side, side))


    if clear:
        cl = (ro + 1) % rows
        pygame.draw.rect(screen, (255, 255, 255), (0, cl * side, w, side))
        cl = (ro + 2) % rows
        pygame.draw.rect(screen, (255, 255, 255), (0, cl * side, w, side))

    pygame.display.update()
    sleep(0.0)

