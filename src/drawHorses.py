from Horse import Horse
from constants import screen
from update import update
from pygame_utils import clear_screen
from constants import default_population_size as pop
from constants import default_wild_pop as wild_pop


def drawHorses(horses, current_horse: Horse):
    update(screen.get_rect())
    clear_screen()

    for horse in horses[:pop]:
        horse.set_sprite_indicator_active()
        if(current_horse):
            if(current_horse == horse):
                horse.set_sprite_color_using_pygame_color(
                    current_horse.sprite_color())
        horse.draw()
        update(horse.sprite_rect())
        update(horse.sprite_indicator_rect())

    for pony in horses[pop:2*pop]:
        pony.draw()
        update(pony.sprite_rect())

    limiter = 2*pop + wild_pop

    for horse in horses[2*pop:limiter]:
        horse.set_sprite_indicator_active()
        horse.draw()
        update(horse.sprite_rect())
        update(horse.sprite_indicator_rect())

    for pony in horses[limiter:]:
        pony.draw()
        update(pony.sprite_rect())
