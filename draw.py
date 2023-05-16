import pygame
from pygame.locals import *
import sys, os
# import time
pygame.init()
pygame.display.set_caption('Paintme')

mouse = pygame.mouse
FPS = 60

width = 1440
height = 1024

window = pygame.display.set_mode((width, height))
screen = window.copy()

BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)

bg = pygame.image.load("images/background.png")
screen.blit(bg, (0, 0))


while True:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        window.fill(WHITE)
        window.blit(screen, (0, 0))
        pygame.draw.circle(window, BLACK, (pygame.mouse.get_pos()), 5)
        pygame.display.update()

        if left_pressed:
            pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()),5)
        