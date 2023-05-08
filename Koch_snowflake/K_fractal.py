import pygame
from math import sqrt, sin, cos, pi

pygame.init()
size = 700  # int(input("Lato della finestra (in pixel) > "))
actual_max = 5  # int(input("Livello massimo? (con numeri troppo alti potrebbe non funzionare) > "))  # 5
tri_part = False
screen = pygame.display.set_mode((size, size))
w, h = screen.get_width(), screen.get_height()
start_x = w / 10
start_side = w - 2 * start_x
start_y = h / 2 + 1 / (2 * sqrt(3)) * start_side
phi = pi / 3
max_level = 0
col = int(255 / actual_max)


def distance(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


def sierpinski(x, y, side, angle, depth, max_depth, level):
    if depth == max_depth:
        c = col * level
        pygame.draw.polygon(screen, (c, c, c), ((x, y), (x + side * cos(angle), y - side * sin(angle)),
                                                (x + side * cos(angle + phi),
                                                 y - side * sin(angle + phi))))
    else:
        side /= 2 if not tri_part else 3
        sierpinski(x, y, side, angle, depth + 1, max_depth, level)
        sierpinski(x + side * cos(angle + phi), y - side * sin(angle + phi), side, angle, depth + 1, max_depth, level)
        sierpinski(x + side * cos(angle), y - side * sin(angle), side, angle, depth + 1, max_depth, level)  #

        if tri_part:
            sierpinski(x + 2 * side * cos(angle + phi), y - 2 * side * sin(angle + phi), side, angle, depth + 1,
                       max_depth,
                       level)
            sierpinski(x + 2 * side * cos(angle), y - 2 * side * sin(angle), side, angle, depth + 1, max_depth,
                       level)
            sierpinski(x + side * cos(angle) + side * cos(angle + phi),
                       y - side * sin(angle) - side * sin(angle + phi), side, angle, depth + 1, max_depth,
                       level)


def koch(x, y, x1, y1, side, angle, level):
    if level == max_level:
        # pygame.draw.line(screen, ((actual_max - level) * col, (actual_max - level) * col, (actual_max - level) * col),
        # (x, y), (x1, y1))
        return
    else:
        side /= 3
        sierpinski(x + side * cos(angle), y - side * sin(angle), side, angle, 0, max_level - (level + 1),
                   actual_max - (level + 1))

        koch(x, y, x + side * cos(angle), y - side * sin(angle), side, angle, level + 1)
        koch(x + side * cos(angle), y - side * sin(angle),  
             x + side * cos(angle + phi) + side * cos(angle),
             y - side * sin(angle + phi) - side * sin(angle), side, angle + phi, level + 1)

        koch(x + 2 * side * cos(angle), y - 2 * side * sin(angle), x + side * 3 * cos(angle), y - side * 3 * sin(angle),
             side, angle, level + 1)
        koch(x + side * cos(angle + 2 * phi) + 2 * side * cos(angle),
             y - side * sin(angle + 2 * phi) - 2 * side * sin(angle),
             x + 2 * side * cos(angle),
             y - 2 * side * sin(angle),
             side, angle - phi, level + 1)


koch(w - start_x, start_y, start_x, start_y, start_side, pi, 0)
koch(start_x, start_y, w / 2, start_y - start_side * sin(phi), start_side, phi, 0)
koch(w / 2, start_y - start_side * sin(phi), w - start_x, start_y, start_side, -phi, 0)
sierpinski(start_x, start_y, start_side, 0, 0, 0, actual_max)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            max_level = max_level + 1 if max_level < actual_max else 0
            # col = int(255 / max_level) if max_level != 0 else 255
            koch(w - start_x, start_y, start_x, start_y, start_side, pi, 0)
            koch(start_x, start_y, w / 2, start_y - start_side * sin(phi), start_side, phi, 0)
            koch(w / 2, start_y - start_side * sin(phi), w - start_x, start_y, start_side, -phi, 0)
            sierpinski(start_x, start_y, start_side, 0, 0, max_level, actual_max)

    #if max_level == actual_max:
     #   pygame.image.save(screen, "Iper_fractal_2.jpg")
    pygame.display.update()
