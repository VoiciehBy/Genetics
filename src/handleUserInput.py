import pygame
import objects as o

from pygame_utils import is_mouse_over_rect
from generateHorsePopulations import generate_horse_populations
from Game import Game
from g_logging import end_json_files

switch_A = True


def on_return_pressed():
    Game.start_game()


def on_p_key_pressed():
    Game.pause_game()


def on_space_pressed():
    print("Ok")
    Game.start_breeding_state()
    generate_horse_populations()


def on_one_key_pressed():
    global switch_A
    switch_A = True


def on_two_key_pressed():
    global switch_A
    switch_A = False


def on_escape_pressed():
    end_json_files()
    exit()


def on_user_input_via_keyboard(event: pygame.event):
    if(event.key == pygame.K_RETURN):
        on_return_pressed()
    elif(event.key == pygame.K_p):
        on_p_key_pressed()
    elif(event.key == pygame.K_1):
        on_one_key_pressed()
    elif (event.key == pygame.K_2):
        on_two_key_pressed()
    elif(event.key == pygame.K_SPACE and Game.is_game_not_paused()):
        on_space_pressed()
    elif(event.key == pygame.K_ESCAPE):
        on_escape_pressed()


def on_left_mouse_button_click(objects, i: int):
    if switch_A:
        o.set_first_parent(objects[i])
        objects[i].set_sprite_color_green()
        return objects[i]
    else:
        o.set_third_parent(objects[i])
        objects[i].set_sprite_color_red()
        return objects[i]


def on_right_mouse_button_click(objects, i: int):
    if switch_A:
        o.set_second_parent(objects[i])
        objects[i].set_sprite_color_blue()
        return objects[i]
    else:
        o.set_fourth_parent(objects[i])
        objects[i].set_sprite_color_magenta()
        return objects[i]


def on_mouse_click(objects, event: pygame.event, n: int):
    g_object = None
    for i in range(n):
        if is_mouse_over_rect(objects[i]):
            if event.button == 1:
                g_object = on_left_mouse_button_click(objects, i)
            elif event.button == 3:
                g_object = on_right_mouse_button_click(objects, i)
    return g_object
