import pygame
from pygame_utils import checkIfMouseOverRect
import handleUserInput as hUI


def onHover(object):
    if checkIfMouseOverRect(object):
        object.set_sprite_over_text_active()
        object.updateName()
        object.flip()
        object.draw()


def handleEvents(horses=None, n=16):
    object = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            hUI.handleUserInputViaKeyboard(event)
        if(horses != None):
            if event.type == pygame.MOUSEBUTTONDOWN:
                object = hUI.handleMouseClick(horses, event, n)
            else:
                for horse in horses:
                    onHover(horse)
    return object
