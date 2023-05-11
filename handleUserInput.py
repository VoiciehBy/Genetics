import pygame
import gettersAndSetters as gAS

from pygame_utils import checkIfMouseOverRect
from generateHorsePopulations import generate_horse_populations
from Game import Game


def on_space_pressed():
    generate_horse_populations()


def handleUserInputViaKeyboard(event: pygame.event):
    if(event.key == pygame.K_RETURN):
        Game.start_game()
    elif(event.key == pygame.K_p):
        Game.pause_game()
    elif(event.key == pygame.K_SPACE):
        print("Ok")
        Game.start_breeding_state()
        on_space_pressed()
    elif(event.key == pygame.K_ESCAPE):
        exit()


def on_left_mouse_button_click(objects, i: int):
    second_parent = gAS.get_second_parent()
    if(second_parent):
        if(objects[i] != second_parent):
            gAS.set_first_parent(objects[i])
            objects[i].set_sprite_color_green()
            return objects[i]


def on_right_mouse_button_click(objects, i: int):
    first_parent = gAS.get_first_parent()
    if(first_parent):
        if(objects[i] != first_parent):
            gAS.set_second_parent(objects[i])
            objects[i].set_sprite_color_blue()
            return objects[i]


def on_mouse_click(objects, event: pygame.event, n: int):
    g_object = None
    for i in range(n):
        if checkIfMouseOverRect(objects[i]):
            if event.button == 1:
                g_object = on_left_mouse_button_click(objects, i)
            if event.button == 3:
                g_object = on_right_mouse_button_click(objects, i)
    return g_object
