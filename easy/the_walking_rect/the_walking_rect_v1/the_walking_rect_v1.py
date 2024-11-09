#!/usr/bin/env python

import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (250, 250, 250)
BLUE = (0, 0, 250)

x_position = WIDTH/2
y_position = HEIGHT/2

square_size = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.rect(
        surface=screen,
        color=BLUE,
        rect=pygame.Rect(x_position, y_position, square_size, square_size), width=5)

    pygame.display.flip()
