import pygame
import gettersAndSetters as gAS

from pygame_utils import checkIfMouseOverRect
from generateHorsePopulations import generateHorsePopulations

from game import game


def on_space_pressed():
    generateHorsePopulations()


def handleUserInputViaKeyboard(event):
    if(event.key == pygame.K_RETURN):
        game.start_game()
    elif(event.key == pygame.K_p):
        game.pause_game()
    elif(event.key == pygame.K_SPACE):
        print("Ok")
        on_space_pressed()
    elif(event.key == pygame.K_ESCAPE):
        exit()


def handleLeftMouseButtonClick(objects, i):
    first_parent = gAS.getFirstParent()
    second_parent = gAS.getSecondParent()

    if(second_parent):
        if(objects[i] != second_parent):
            gAS.setFirstParent(objects[i])
            gAS.setFirstParentId(i)
            objects[i].set_sprite_color_green()
            return objects[i]


def handleRightMouseButtonClick(objects, i):
    first_parent = gAS.getFirstParent()
    if(first_parent):
        if(objects[i] != first_parent):
            gAS.setSecondParent(objects[i])
            gAS.setSecondParentId(i)
            objects[i].set_sprite_color_blue()
            return objects[i]


def handleMouseClick(objects, event, n):
    g_object = None
    for i in range(n):
        if checkIfMouseOverRect(objects[i]):
            if event.button == 1:
                g_object = handleLeftMouseButtonClick(objects, i)
            if event.button == 3:
                g_object = handleRightMouseButtonClick(objects, i)
    return g_object
