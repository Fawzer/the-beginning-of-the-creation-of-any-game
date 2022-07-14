import pygame
import sys


def events(screen):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update(image, screen):
    """обновление экрана"""
    screen.blit(image, (0, 0))
    screen.draw()
    pygame.display.flip()

