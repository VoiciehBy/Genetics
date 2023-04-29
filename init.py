import pygame
from constants import windowName


def init():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(windowName)
    pygame.event.set_allowed(
        [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
