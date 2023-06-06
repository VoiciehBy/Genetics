from constants import screen
from update import update

from pygame_utils import clear_screen
from constants import default_population_size as pop
from constants import default_wild_pop as wild_pop

from constants import debug_mode


def drawHorses(horses):
    update(screen.get_rect())
    clear_screen()

    for horse in horses[:pop]:
        horse.set_sprite_indicator_active()
        horse.draw()
        update(horse.sprite_rect())
        if debug_mode:
            update(horse.sprite_indicator_rect())

    for pony in horses[pop:2*pop]:
        pony.draw()
        update(pony.sprite_rect())

    limiter = 2*pop + wild_pop

    for horse in horses[2*pop:limiter]:
        horse.set_sprite_indicator_active()
        horse.draw()
        update(horse.sprite_rect())
        if debug_mode:
            update(horse.sprite_indicator_rect())

    for pony in horses[limiter:]:
        pony.draw()
        update(pony.sprite_rect())
