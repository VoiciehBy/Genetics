from populationsGetters import getPopulation_0, getPopulation_1, getPopulation_2, getPopulation_3
from horse_utils import generateHorsesArray, generateHorsesArrayWithOffset
from numpy import array
from init import init
from clearScreen import clearScreen
from update import update
from constants import screen, margin_x, margin_y
from handleEvents import handleEvents


def generateFourPopulations():
    side = 128

    pop_0 = getPopulation_0().pop
    pop_1 = getPopulation_1().pop
    pop_2 = getPopulation_2().pop
    pop_3 = getPopulation_3().pop

    horses = generateHorsesArray(pop_0)
    ponies = generateHorsesArrayWithOffset(pop_1)
    horses_1 = generateHorsesArrayWithOffset(
        pop_2, margin_x=0, margin_y=0, offset=side*4 + margin_x, offset_1=margin_y/2)

    ponies_1 = generateHorsesArrayWithOffset(
        pop_3, offset=side*4 + 3*margin_x, offset_1=side)

    for pony in ponies:
        pony.name = "Pony"

    for horse in horses_1:
        horse.name = "Equus"

    for pony in ponies:
        pony.name = "Pony"

    for pony in ponies_1:
        pony.name = "Caballus"

    result = list(horses) + list(ponies) + list(horses_1) + list(ponies_1)
    return array(result)


def main():
    init()
    clearScreen()
    update(screen.get_rect())

    while(1):
        horses = generateFourPopulations()
        side = 128

        h = handleEvents(horses, n=16)
        clearScreen()

        for horse in horses[:4]:
            if(h):
                if(h == horse):
                    horse.sprite.color = h.sprite.color
            horse.draw()
            update(horse.sprite.rect)
            update(horse.sprite.indicator.rect)

        for pony in horses[4:8]:
            pony.draw()
            update(pony.sprite.rect)

        for horse in horses[8:12]:
            horse.draw()
            update(horse.sprite.rect)
            update(horse.sprite.indicator.rect)

        for pony in horses[12:]:
            pony.draw()
            update(pony.sprite.rect)


main()
