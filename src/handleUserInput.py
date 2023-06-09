import pygame
import objects as o
import quest_objects as q_o

from GColor import red, green, blue, magenta
from pygame_utils import is_mouse_over_rect
from generate_horse_populations import generate_horse_populations
from Game import Game
from g_logging import end_json_files

from g_horse_utils import get_horse_parents
from draw import drawParents
from constants import quest_mode, debug_mode

from quest_objects import horse, get_delta_time

switch_A: bool = True


def on_return_pressed():
    Game.start_game()


def on_p_key_pressed():
    Game.pause_game()


def on_space_pressed():
    if quest_mode:
        q_o.bullet.set_active()
    else:
        drawParents(get_horse_parents())
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


def on_left_key_pressed():
    horse.move(-1 * get_delta_time(), 0)
    if horse.is_looking_right() is False:
        horse.flip()


def on_right_key_pressed():
    horse.move(1 * get_delta_time(), 0)
    if horse.is_looking_right():
        horse.flip()


def on_user_input_via_keyboard(event: pygame.event):
    event_key_id: int = event.key
    if event_key_id == pygame.K_RETURN:
        on_return_pressed()
    elif event_key_id == pygame.K_p:
        on_p_key_pressed()
    elif event_key_id == pygame.K_1:
        on_one_key_pressed()
    elif event_key_id == pygame.K_2:
        on_two_key_pressed()
    elif event_key_id == pygame.K_SPACE and Game.is_game_not_paused():
        on_space_pressed()
    elif event_key_id == pygame.K_ESCAPE:
        on_escape_pressed()

    elif event_key_id == pygame.K_LEFT:
        horse.move(-get_delta_time(), 0)
        if horse.is_looking_right() is False:
            horse.flip()
    elif event_key_id == pygame.K_RIGHT:
        horse.move(get_delta_time(), 0)
        if horse.is_looking_right():
            horse.flip()


def on_left_mouse_button_click(objects, i: int):
    if objects[i].is_ai():
        return

    if switch_A:
        o.set_first_parent(objects[i])
        if debug_mode:
            objects[i].set_sprite_color(green)
        return objects[i]
    else:
        o.set_third_parent(objects[i])
        if debug_mode:
            objects[i].set_sprite_color(red)
        return objects[i]


def on_right_mouse_button_click(objects, i: int):
    if objects[i].is_ai():
        return

    if switch_A:
        o.set_second_parent(objects[i])
        if debug_mode:
            objects[i].set_sprite_color(blue)
        return objects[i]
    else:
        o.set_fourth_parent(objects[i])
        if debug_mode:
            objects[i].set_sprite_color(magenta)
        return objects[i]


def on_mouse_click(objects, event: pygame.event, n: int):
    g_object = None
    for i in range(n):
        if is_mouse_over_rect(objects[i]):
            event_button_id: int = event.button
            if event_button_id == 1:
                g_object = on_left_mouse_button_click(objects, i)
            elif event_button_id == 3:
                g_object = on_right_mouse_button_click(objects, i)
    return g_object
