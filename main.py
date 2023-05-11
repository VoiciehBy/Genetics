from objects import get_population_0, get_population_1
from Population import Population
from horse_utils import generate_horses_array, generate_horses_array_with_offset
from numpy import array
from init import init
from pygame_utils import clearScreen, wait
from pygame_colors import color_white
from update import update
from constants import horse_image_side as side
from constants import default_population_size as pop
from constants import names, screen, margin_x, margin_y
from handleEvents import handleEvents

from Game import Game
from drawTutorialScreen import drawTutorialScreen
from drawEndScreen import drawEndScreen

population_2 = Population(pop)
population_2.generate_initial_population(8, pop)

population_3 = Population(pop)
population_3.generate_initial_population(8, pop)


def generateFourPopulations() -> array:
    pop_0 = get_population_0().get_pop()
    pop_1 = get_population_1().get_pop()

    pop_2 = population_2.get_pop()
    pop_3 = population_3.get_pop()

    horses = generate_horses_array(pop_0)
    ponies = generate_horses_array_with_offset(pop_1)

    horses_1 = generate_horses_array_with_offset(
        pop_2, margin_x=0, margin_y=0, offset=side*4 + margin_x, offset_1=margin_y/2)

    ponies_1 = generate_horses_array_with_offset(
        pop_3, offset=side*4 + 4*margin_x, offset_1=side)

    for i in range(4):
        ponies[i].set_name(names[1])
        horses[i].set_name(names[2])
        horses_1[i].set_name(names[3])
        ponies_1[i].set_name(names[4])

    result = list(horses) + list(ponies) + list(horses_1) + list(ponies_1)
    return array(result)


def drawHorses(horses, current_horse):
    update(screen.get_rect())
    clearScreen()

    for horse in horses[:4]:
        horse.set_sprite_indicator_active()
        if(current_horse):
            if(current_horse == horse):
                horse.set_sprite_color_using_pygame_color(
                    current_horse.sprite_color())
        horse.draw()
        update(horse.sprite_rect())
        update(horse.sprite_indicator_rect())

    for pony in horses[4:8]:
        pony.draw()
        update(pony.sprite_rect())

    for horse in horses[8:12]:
        horse.set_sprite_indicator_active()
        horse.draw()
        update(horse.sprite_rect())
        update(horse.sprite_indicator_rect())

    for pony in horses[12:]:
        pony.draw()
        update(pony.sprite_rect())


def main():
    with open("horses.json", "w", encoding="utf-8") as file:
        file.write("{\n\"horses\" : [\n")
    with open("ai_horses.json", "w", encoding="utf-8") as file:
        file.write("{\n\"horses\" : [\n")
    init()
    clearScreen()
    horses = generateFourPopulations()
    while(1):
        if(Game.is_game_paused()):
            drawTutorialScreen()
        elif(Game.is_in_breeding_state()):
            horses = generateFourPopulations()
            Game.stop_breeding_state()
        elif(Game.is_game_playing()):
            current_horse = handleEvents(horses, n=16)
            drawHorses(horses, current_horse)
            if(current_horse):
                wait(64)
                current_horse.set_sprite_color_using_pygame_color(color_white)
        elif(Game.is_it_the_end()):
            drawEndScreen()
            wait(2000)
            with open("ai_horses.json", "a", encoding="utf-8") as file:
                file.write(']\n}')
            txt = ''
            with open("ai_horses.json", "r", encoding="utf-8") as file:
                txt = file.read()
                n = len(txt)
                txt = txt[:n-5] + txt[n-4:]
            with open("ai_horses.json", "w", encoding="utf-8") as file:
                file.write(txt)
            break


main()
