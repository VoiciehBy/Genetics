import pygame
from pygame_utils import checkIfMouseOverRect
import handleUserInput as hUI


def onHover(object):
    if checkIfMouseOverRect(object):
        object.set_sprite_over_text_active()
        object.updateName()
        object.draw()


def handleEvents(horses, n=4):
    object = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            hUI.handleUserInputViaKeyboard(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            object = hUI.handleMouseClick(horses, event, n)
        else:
            for horse in horses:
                onHover(horse)
    return object
