from math import cos, sin, pi
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
angle = pi / 4
min_length = 200
max_length = 500
w, h = screen.get_width(), screen.get_height()
spess = 4
radius = 40
col = (170, 170, 170)
screen.fill((15, 15, 15))
offset = angle / 2


def av_point(x, y, x1, y1) -> tuple:
    return (x + x1) / 2, (y + y1) / 2


for i in range(9):
    p = (cos(angle * i + offset) * min_length + w / 2, sin(angle * i + offset) * min_length + h / 2)
    a = (cos(angle * i + angle / 2 + offset) * max_length + w / 2, sin(angle * i + angle / 2 + offset) * max_length + h / 2)
    b = (cos(angle * (i+1)+ offset) * min_length + w / 2, sin(angle * (i+1)+ offset) * min_length + h / 2)
    m = (cos(angle * i + angle / 2+ offset) * min_length + w / 2, sin(angle * i + angle / 2+ offset) * min_length + h / 2)
    m3 = (cos(angle * i + angle / 2+ offset) * min_length * 2 + w / 2, sin(angle * i + angle / 2+ offset) * min_length * 2 + h / 2)
    m6 = (cos(angle * i + angle / 2+ offset) * max_length / 4 + w / 2, sin(angle * i + angle / 2+ offset) * max_length / 4 + h / 2)
    m1 = av_point(p[0], p[1], a[0], a[1])
    m2 = av_point(b[0], b[1], a[0], a[1])
    m4 = av_point(m1[0], m1[1], a[0], a[1])
    m5 = av_point(m2[0], m2[1], a[0], a[1])
    pygame.draw.line(screen, col, (w / 2, h / 2), p, spess)
    pygame.draw.line(screen, col, p, a, spess)
    pygame.draw.line(screen, col, (w / 2, h / 2), b, spess)
    pygame.draw.line(screen, col, b, a, spess)
    pygame.draw.line(screen, col, (w / 2, h / 2), m, spess)
    pygame.draw.line(screen, col, m, m1, spess)
    pygame.draw.line(screen, col, m, m2, spess)
    pygame.draw.line(screen, col, m3, m4, spess)
    pygame.draw.line(screen, col, m3, m5, spess)
    pygame.draw.line(screen, col, m, m3, spess)
    pygame.draw.line(screen, col, m6, p, spess)
    pygame.draw.line(screen, col, m6, b, spess)
    colour = (255, 0, 0) if i < 5 else (0, 255, 0)
    col2 = (100, 00, 0) if i < 5 else (0, 100, 0)
    pygame.draw.circle(screen, colour, a, radius)
    pygame.draw.circle(screen, col2, a, radius, 5)
    pygame.draw.circle(screen, (150, 150, 150), (w / 2, h / 2), radius)
    pygame.draw.circle(screen, (100, 100, 100), (w / 2, h / 2), radius, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    pygame.display.update()
    pygame.image.save(screen, "logo.jpg")
    break

