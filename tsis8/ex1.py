import pygame
import sys
pygame.init()

w, h = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)
BLUE = (0, 0, 255)

sc = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Pygame2")

clock = pygame.time.Clock()
FPS = 60

x = w // 2
y = h // 2
speed = 5

flLeft = flRight = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft = flRight = False

        if flLeft:
            x -= speed
        elif flRight:
            x += speed

    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()