import pygame
from boid import *
from quadtree import *

max_boids = int(input("Number of boids > "))
pygame.init()
# screen = pygame.display.set_mode((1000, 700))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
w, h = screen.get_width(), screen.get_height()
init(w, h)
flock = [boid() for _ in range(max_boids)]
q = quadtree(0, 0, w, h)
# c = pygame.time.Clock()
secret = False

def to_element(lis):
    elemented = []
    for thing in lis:
        elemented.append(element(thing, thing.loc.x, thing.loc.y))
    return elemented


while True:
    # c.tick()
    # print(c.get_fps())
    screen.fill((10, 10, 10))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            secret = not secret


    new_flock = to_element(flock)
    q.put(new_flock)

    for a in flock:
        x_, y_ = to_centred(a.loc.x, a.loc.y, a.radius * 2, a.radius * 2)
        a.move(q.query(x_, y_, a.radius * 2, a.radius * 2))
        # pygame.draw.rect(screen, (255, 255, 255), (x_, y_, radius*2, radius*2), 1)
        # pygame.draw.rect(screen, (255, 255, 255), (x_, y_, radius, radius), 1)
        # pygame.draw.circle(screen, (255, 255, 255), (a.loc.x, a.loc.y), radius, 1)
        # errore nella casella di query
    for b in flock:
        pos = b.show()
        pygame.draw.polygon(screen, (180, 180, 180), pos)

    if secret:
        for quad in q.show():
            pygame.draw.rect(screen, (0, 255, 0), (quad['x'], quad['y'], quad['w'], quad['h']), 1)

    pygame.display.update()
    q.reset()
