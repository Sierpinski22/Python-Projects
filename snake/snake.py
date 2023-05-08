from math import floor
from random import randint
from time import sleep
import pygame

pygame.init()
screen = pygame.display.set_mode((700, 600))
w, h = screen.get_width(), screen.get_height()
side = 20
cols, rows = floor(w / side), floor(h / side)
snake_color = pygame.Color(255, 255, 255)
fruit_color = pygame.Color(255, 50, 50)
tim = 0.06


def restart():
    s = [(randint(0, cols - 1), randint(0, rows - 1))]
    f = (randint(0, cols - 1), randint(0, rows - 1))
    x, y = 0, 0
    while f in s:
        f = (randint(0, cols - 1), randint(0, rows - 1))
    return s, f, x, y


def check_direction(pdx, pdy):
    if len(snake) > 1:
        return not (snake[0][0] + pdx == snake[1][0] and snake[0][1] + pdy == snake[1][1])
    else:
        return True


def check_contact():  # 1 => aggiungi segmento e frutto 0 => non fare nulla 2 => hai perso
    if snake[0] == fruit:
        return 1
    if not (0 <= snake[0][0] < cols and 0 <= snake[0][1] < rows) or snake[0] in snake[1:]:
        return 2
    return 0


def move():
    if token:
        snake.append(snake[len(snake) - 1])
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    snake[0] = (snake[0][0] + vx, snake[0][1] + vy)


snake, fruit, vx, vy = restart()


def show():
    pygame.draw.rect(screen, fruit_color, (fruit[0] * side, fruit[1] * side, side, side))
    for coordinates in snake:
        pygame.draw.rect(screen, snake_color, (coordinates[0] * side, coordinates[1] * side, side, side))


while True:
    sleep(tim)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_SPACE]:
                pygame.quit()
            if event.key == pygame.K_w:
                dx, dy = 0, -1
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            elif event.key == pygame.K_d:
                dx, dy = 1, 0
            elif event.key == pygame.K_s:
                dx, dy = 0, 1
            else:
                dx, dy = vx, vy

            if check_direction(dx, dy):
                vx, vy = dx, dy

    screen.fill((0, 0, 0))

    c = check_contact()
    token = c == 1

    if c == 2:
        print("Hai totalizzato " + str(len(snake) - 1) + " punti!")
        snake, fruit, vx, vy = restart()
    else:
        if token:
            while fruit in snake:
                fruit = (randint(0, cols - 1), randint(0, rows - 1))
        move()
        show()
        token = False

    pygame.display.update()
