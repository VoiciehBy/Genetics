from numpy import array, zeros
import color
from pygame import Surface, Rect, image  # , SRCALPHA
from constants import s_s_m_m
from constants import horse_image_side as side
from constants import color_white, color_cyan, color_black
from constants import color_magenta, color_red, color_blue, color_brown, color_green
from constants import margin_x as m_x
from constants import margin_y as m_y
from sprite import sprite
from horse import horse


def getHorseImage() -> Surface:
    if(s_s_m_m):
        horseImage = image.load("horse_s_s_m_m.png")
    else:
        horseImage = image.load("horse.png")
    return horseImage


def generateHorseSSMMImageForPygame(individual) -> array:
    horseImage = getHorseImage()
    individual_color = individual.color_trait().toPyGameColor()
    inverted_individual_color = individual.color_trait().inverse().toPyGameColor()
    theColor = inverted_individual_color - individual_color

    for i in range(side):
        for j in range(side):
            horse_color = horseImage.get_at((i, j))

            if horse_color == color_white:
                horseImage.set_at((i, j), individual_color)
            elif horse_color == color_cyan:
                horseImage.set_at((i, j), inverted_individual_color)
            elif horse_color in [color_black, color_magenta]:
                pass
            elif horse_color == color_red:
                horseImage.set_at((i, j), color_black)
            elif horse_color == color_blue:
                horseImage.set_at((i, j), theColor)
    return horseImage


def generateHorseImageForPygame(individual) -> array:
    horseImage = getHorseImage()
    individual_color = individual.color_trait().toPyGameColor()
    inverted_individual_color = individual.color_trait().inverse().toPyGameColor()
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
        horseImage = generateHorseSSMMImageForPygame(individual)
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
