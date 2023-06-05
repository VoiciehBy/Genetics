from utils import make_data_directory
from g_logging import start_json_files, end_json_files
from init import init
from pygame_utils import start_pygame_clock
from draw import drawTurnCounter, drawFPSCounter, drawParents, drawUIParentsTxt
from generate_four_populations import generate_four_populations
from Game import Game
from drawScreen import drawTutorialScreen, drawEndingScreens
from constants import default_population_size, default_wild_pop
from handleEvents import handleEvents


from horse_utils import get_horse_parents
from drawHorses import drawHorses

from Horse import Horse


def main():
    make_data_directory()
    start_json_files()
    init()

    n_n = 2 * default_population_size + 2 * default_wild_pop
    clock = start_pygame_clock()
    horses = generate_four_populations()
    horses_parents = get_horse_parents()

    while 1:
        if Game.is_game_paused():
            drawTutorialScreen()

        elif Game.is_game_playing():
            current_horse: Horse = handleEvents(horses, n=n_n)
            drawHorses(horses)
            if current_horse:
                horses_parents = get_horse_parents()
                current_horse.set_sprite_color_white_using_pygame_color()
            drawParents(horses_parents)

        elif Game.is_in_breeding_state():
            horses = generate_four_populations()
            horses_parents = get_horse_parents()
            drawParents(horses_parents)
            Game.stop_breeding_state()

            horses_parents = get_horse_parents()
            drawParents(horses_parents)

        elif Game.is_it_the_end():
            drawHorses(horses)
            horses_parents = get_horse_parents()
            drawParents(horses_parents)

            drawEndingScreens()
            end_json_files()
            break

        # lock frame rate to 60 FPS
        clock.tick(60)
        drawFPSCounter(clock)
        drawTurnCounter()
        _n = len(horses_parents)
        for i in range(_n):
            drawUIParentsTxt(horses_parents[i].sprite_rect(), i)


main()
