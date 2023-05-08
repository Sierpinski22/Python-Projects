import pygame
from random import randint
from time import sleep

pygame.init()
screen = pygame.display.set_mode((600, 600))
w, h = screen.get_size()
side = 20
previous_x, previous_y = 0, 0
snake = [[randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]]
pygame.draw.rect(screen, (0, 255, 0), (snake[0][0] * side, snake[0][1] * side, side, side))
fruit = [randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]
while fruit in snake:
    fruit = [randint(0, int(w / side)), randint(0, int(h / side))]
pygame.draw.rect(screen, (255, 0, 0), (fruit[0] * side, fruit[1] * side, side, side))


def move(x, y):
    global previous_x, previous_y, fruit
    if not (len(snake) > 1 and previous_x + x == 0 and previous_y + y == 0):
        previous_x, previous_y = x, y
    else:
        x, y = previous_x, previous_y
    new_x, new_y = snake[0][0] + x, snake[0][1] + y
    if [new_x, new_y] in snake and (x != 0 or y != 0):
        return True
    elif not [new_x, new_y] == fruit:
        pygame.draw.rect(screen, (0, 0, 0), (snake[-1][0] * side, snake[-1][1] * side, side, side))
        snake.pop(-1)
    else:
        fruit = [randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]
        while fruit in snake or fruit == [new_x - 1, new_y - 1]:
            fruit = [randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]
            print(1)
        pygame.draw.rect(screen, (255, 0, 0,), (fruit[0] * side, fruit[1] * side, side, side))

    snake.insert(0, [(new_x + w / side) % (w / side), (new_y + h / side) % (h / side)])
    pygame.draw.rect(screen, (0, 255, 0), (snake[0][0] * side, snake[0][1] * side, side, side))
    return False


def reset():
    screen.fill((0, 0, 0))
    global previous_x, previous_y, snake, fruit
    previous_x, previous_y = 0, 0
    snake = [[randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]]
    pygame.draw.rect(screen, (0, 255, 0), (snake[0][0] * side, snake[0][1] * side, side, side))
    fruit = [randint(0, int(w / side) - 1), randint(0, int(h / side) - 1)]
    while fruit in snake:
        fruit = [randint(0, int(w / side)), randint(0, int(h / side))]
    pygame.draw.rect(screen, (255, 0, 0), (fruit[0] * side, fruit[1] * side, side, side))


while True:
    sleep(0.07)
    dx, dy = previous_x, previous_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_w:
                dx, dy = 0, -1
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            elif event.key == pygame.K_d:
                dx, dy = 1, 0
            elif event.key == pygame.K_s:
                dx, dy = 0, 1
    if move(dx, dy):
        reset()
    pygame.display.update()
