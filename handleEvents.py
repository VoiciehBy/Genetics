import pygame
from pygame_utils import checkIfMouseOverRect
import handleUserInput as hUI


def on_hover(g_object):
    if checkIfMouseOverRect(g_object):
        g_object.set_sprite_over_text_active()
        g_object.update_sprite_over_text()
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
                g_object = hUI.on_mouse_click(horses, event, n)
            else:
                for horse in horses:
                    on_hover(horse)
    return g_object
