from utils import make_data_directory
from g_logging import start_json_files, end_json_files
from init import init
from pygame_utils import start_pygame_clock, wait
from generate_four_populations import generate_four_populations
from Game import Game
from drawScreen import drawTutorialScreen, drawEndScreen, drawResultScreen
from constants import default_population_size, default_wild_pop
from handleEvents import handleEvents
from drawHorses import drawHorses


def main():
    make_data_directory()
    start_json_files()
    init()
    clock = start_pygame_clock()
    horses = generate_four_populations()
    while(1):
        if(Game.is_game_paused()):
            drawTutorialScreen()
        elif(Game.is_in_breeding_state()):
            horses = generate_four_populations()
            Game.stop_breeding_state()
        elif(Game.is_game_playing()):
            current_horse = handleEvents(
                horses, n=2*default_population_size + 2*default_wild_pop)
            drawHorses(horses, current_horse)
            if(current_horse):
                wait(64)
                current_horse.set_sprite_color_white_using_pygame_color()
        elif(Game.is_it_the_end()):
            drawEndScreen()
            wait(2000)
            drawResultScreen()
            wait(2000)
            end_json_files()
            break
        clock.tick(60)
        print(clock.get_fps())


main()
