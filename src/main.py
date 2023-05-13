from constants import HORSES_JSON_FILE_NAME, AI_HORSES_JSON_FILE_NAME

from init import init
from g_logging import start_json_file, end_json_file
from pygame_utils import wait
from generate_four_populations import generate_four_populations
from Game import Game
from drawScreen import drawTutorialScreen, drawEndScreen

from constants import default_population_size as pop
from constants import default_wild_pop as wild_pop

from handleEvents import handleEvents

from pygame_colors import color_white

from drawHorses import drawHorses

import pygame


def main():
    start_json_file(HORSES_JSON_FILE_NAME)
    start_json_file(AI_HORSES_JSON_FILE_NAME)
    init()
    clock = pygame.time.Clock()

    horses = generate_four_populations()
    while(1):
        if(Game.is_game_paused()):
            drawTutorialScreen()
        elif(Game.is_in_breeding_state()):
            horses = generate_four_populations()
            Game.stop_breeding_state()
        elif(Game.is_game_playing()):
            current_horse = handleEvents(horses, n=2*pop + 2*wild_pop)
            drawHorses(horses, current_horse)
            if(current_horse):
                wait(64)
                current_horse.set_sprite_color_using_pygame_color(color_white)
        elif(Game.is_it_the_end()):
            drawEndScreen()
            wait(2000)

            end_json_file(HORSES_JSON_FILE_NAME)
            end_json_file(AI_HORSES_JSON_FILE_NAME)

            break
        clock.tick(60)
        print(clock.get_fps())


main()
