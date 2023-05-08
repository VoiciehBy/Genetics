from numpy import array, zeros
import color
from pygame import Surface, Rect, image  # , SRCALPHA
import constants as c
from sprite import sprite
from horse import horse


def getHorseImage() -> Surface:
    if(c.s_s_m_m):
        horseImage = image.load("horse_s_s_m_m.png")
    else:
        horseImage = image.load("horse.png")
    return horseImage


def generateHorseSSMMImageForPygame(individual) -> array:
    horseImage = getHorseImage()
    individual_color = individual.color_trait().toPyGameColor()
    inverted_individual_color = individual.color_trait().inverse().toPyGameColor()
    theColor = inverted_individual_color - individual_color
    side = c.horse_image_side

    for i in range(side):
        for j in range(side):
            horse_color = horseImage.get_at((i, j))

            if horse_color == c.color_white:
                horseImage.set_at((i, j), individual_color)
            elif horse_color == c.color_cyan:
                horseImage.set_at((i, j), inverted_individual_color)
            elif horse_color in [c.color_black, c.color_magenta]:
                pass
            elif horse_color == c.color_red:
                horseImage.set_at((i, j), c.color_black)
            elif horse_color == c.color_blue:
                horseImage.set_at((i, j), theColor)
    return horseImage


def generateHorseImageForPygame(individual) -> array:
    horseImage = getHorseImage()
    individual_color = individual.color_trait().toPyGameColor()
    inverted_individual_color = individual.color_trait().inverse().toPyGameColor()
    theColor = inverted_individual_color - individual_color
    side = c.horse_image_side

    for i in range(side):
        for j in range(side):
            horse_color = horseImage.get_at((i, j))

            if horse_color == c.color_brown:
                horseImage.set_at((i, j), individual_color)
            elif horse_color == c.color_white:
                horseImage.set_at((i, j), inverted_individual_color)

            elif horse_color == c.color_black:
                pass
            elif horse_color == c.color_red:
                horseImage.set_at((i, j), c.color_black)
            elif horse_color == c.color_green:
                horseImage.set_at((i, j), c.color_red)
            elif horse_color == c.color_blue:
                horseImage.set_at((i, j), theColor)
    return horseImage


def generateHorse(individual, rect) -> horse:
    if(c.s_s_m_m):
        horseImage = generateHorseSSMMImageForPygame(individual)
    else:
        horseImage = generateHorseImageForPygame(individual)
    s = sprite(color.white, rect, horseImage)
    h = horse(genetics=individual, g_sprite=s)
    return h


def generateHorsesArrayWithOffset(individuals, n=4, margin_x=c.margin_x, margin_y=c.margin_x, offset=c.horse_image_side, offset_1=c.horse_image_side) -> array:
    horses = zeros(n, dtype=horse)
    side = c.horse_image_side

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
    horses = generateHorsesArrayWithOffset(
        individuals, n, c.margin_x, c.margin_y, 0, 0)
    return horses
