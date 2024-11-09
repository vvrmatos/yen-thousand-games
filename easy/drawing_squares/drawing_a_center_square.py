#!/usr/bin/env python3

import sys
import pygame

# INITIALIZE PYGAME
pygame.init()

# PYGAME VARIABLES
WIDTH, HEIGHT = 600, 400
BLUE = (0, 0, 250)
WHITE = (250, 250, 250)

square_size = 40
initial_x_position = x_position = WIDTH/2
y_position = HEIGHT/2
speed = 2.7

# SCREEN CONFIGURATION
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Center Square")

# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # KEY PRESSED DETECTION
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_position > 0:
        x_position -= speed
    if keys[pygame.K_RIGHT] and x_position < WIDTH - square_size:
        x_position += speed
    if keys[pygame.K_SPACE]:
        x_position = initial_x_position

    # SCREEN INTERACTION
    screen.fill(WHITE)
    pygame.draw.rect(surface=screen, color=BLUE, rect=(x_position, y_position, square_size, square_size), width=5)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
