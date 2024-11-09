#!/usr/bin/env python3

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Walking Square")

square_size = 50
speed = 2.7

x_position = (WIDTH - square_size) // 2
y_position = (HEIGHT - square_size) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_position > 0:
        x_position -= speed
    if keys[pygame.K_RIGHT] and x_position < WIDTH - square_size:
        x_position += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x_position, y_position, square_size, square_size))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
