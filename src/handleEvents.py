import pygame
from pygame_utils import is_mouse_over_rect
from g_logging import end_json_files
import handleUserInput as hUI


def on_hover(g_object):
    if g_object is None:
        return

    is_g_object_looking_right: bool = g_object.is_looking_right()
    if is_mouse_over_rect(g_object):
        g_object.set_sprite_over_text_active()
        g_object.update_sprite_over_text()
        if is_g_object_looking_right is False:
            g_object.flip()
    else:
        g_object.set_sprite_over_text_inactive()
        if is_g_object_looking_right is True:
            g_object.flip()


def handleEvents(horses=None, n=16):
    g_object = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_json_files()
            exit()
        if event.type == pygame.KEYDOWN:
            hUI.on_user_input_via_keyboard(event)
        if horses is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                g_object = hUI.on_mouse_click(horses, event, n)
            else:
                for horse in horses:
                    on_hover(horse)
    return g_object
