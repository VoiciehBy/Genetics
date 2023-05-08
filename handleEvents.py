import pygame
from pygame_utils import checkIfMouseOverRect
import handleUserInput as hUI


def onHover(g_object):
    if checkIfMouseOverRect(g_object):
        g_object.set_sprite_over_text_active()
        g_object.updateName()
        g_object.flip()
        g_object.draw()


def handleEvents(horses=None, n=16):
    g_object = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            hUI.handleUserInputViaKeyboard(event)
        if(horses is not None):
            if event.type == pygame.MOUSEBUTTONDOWN:
                g_object = hUI.handleMouseClick(horses, event, n)
            else:
                for horse in horses:
                    onHover(horse)
    return g_object
