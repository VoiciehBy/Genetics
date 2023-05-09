from numpy import array, zeros
import color
from pygame import Surface, Rect, image  # , SRCALPHA
from constants import s_s_m_m
from constants import horse_image_side as side
from pygame_colors import *
from constants import margin_x as m_x
from constants import margin_y as m_y
from sprite import sprite
from horse import horse


def get_horse_image() -> Surface:
    if(s_s_m_m):
        horse_image = image.load("horse_s_s_m_m.png")
    else:
        horse_image = image.load("horse.png")
    return horse_image


def generate_ssmm_horse_image_for_pygame(individual) -> array:
    horse_image = get_horse_image()
    individual_color = individual.color_trait().to_pygame_color()
    inverted_individual_color = individual.color_trait().inverse().to_pygame_color()
    the_color = inverted_individual_color - individual_color

    for i in range(side):
        for j in range(side):
            horse_color = horse_image.get_at((i, j))

            if horse_color == color_white:
                horse_image.set_at((i, j), individual_color)
            elif horse_color == color_cyan:
                horse_image.set_at((i, j), inverted_individual_color)
            elif horse_color in [color_black, color_magenta]:
                pass
            elif horse_color == color_red:
                horse_image.set_at((i, j), color_black)
            elif horse_color == color_blue:
                horse_image.set_at((i, j), the_color)
    return horse_image


def generateHorseImageForPygame(individual) -> array:
    horseImage = get_horse_image()
    individual_color = individual.color_trait().to_pygame_color()
    inverted_individual_color = individual.color_trait().inverse().to_pygame_color()
    theColor = inverted_individual_color - individual_color

    for i in range(side):
        for j in range(side):
            horse_color = horseImage.get_at((i, j))

            if horse_color == color_brown:
                horseImage.set_at((i, j), individual_color)
            elif horse_color == color_white:
                horseImage.set_at((i, j), inverted_individual_color)

            elif horse_color == color_black:
                pass
            elif horse_color == color_red:
                horseImage.set_at((i, j), color_black)
            elif horse_color == color_green:
                horseImage.set_at((i, j), color_red)
            elif horse_color == color_blue:
                horseImage.set_at((i, j), theColor)
    return horseImage


def generateHorse(individual, rect) -> horse:
    if(s_s_m_m):
        horseImage = generate_ssmm_horse_image_for_pygame(individual)
    else:
        horseImage = generateHorseImageForPygame(individual)
    s = sprite(color.white, rect, horseImage)
    h = horse(genetics=individual, g_sprite=s)
    return h


def generateHorsesArrayWithOffset(individuals, n=4, margin_x=m_x, margin_y=m_y, offset=side, offset_1=side) -> array:
    horses = zeros(n, dtype=horse)

    offset_x = 0
    offset_y = 0
    for i in range(n):
        x = margin_x + offset_x + offset
        y = margin_y + offset_y + 2*offset_1
        rect = Rect([x, y, side, side])
        horses[i] = generateHorse(individuals[i], rect)
        offset_x = offset_x + side
    return horses


def generateHorsesArray(individuals, n=4) -> array:
    horses = generateHorsesArrayWithOffset(individuals, n, m_x, m_y, 0, 0)
    return horses
