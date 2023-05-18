from pygame import Surface, Rect, image
from Individual import Individual
from numpy import array, zeros

from constants import s_s_m_m
from constants import horse_image_side as side
from pygame_colors import *
from constants import margin_x as m_x
from constants import margin_y as m_y
from GSprite import GSprite
from Horse import Horse


def get_horse_image() -> Surface:
    if(s_s_m_m):
        horse_image = image.load("../img/horse_s_s_m_m.png")
    else:
        horse_image = image.load("../img/horse.png")
    return horse_image


def generate_ssmm_horse_image_for_pygame(individual: Individual) -> array:
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


def generate_horse_image_for_pygame(individual: Individual) -> array:
    horse_image = get_horse_image()
    individual_color = individual.color_trait().to_pygame_color()
    inverted_individual_color = individual.color_trait().inverse().to_pygame_color()
    the_color = inverted_individual_color - individual_color

    for i in range(side):
        for j in range(side):
            horse_color = horse_image.get_at((i, j))

            if horse_color == color_brown:
                horse_image.set_at((i, j), individual_color)
            elif horse_color == color_white:
                horse_image.set_at((i, j), inverted_individual_color)

            elif horse_color == color_black:
                pass
            elif horse_color == color_red:
                horse_image.set_at((i, j), color_black)
            elif horse_color == color_green:
                horse_image.set_at((i, j), color_red)
            elif horse_color == color_blue:
                horse_image.set_at((i, j), the_color)
    return horse_image


def generate_horse(individual: Individual, rect: Rect) -> Horse:
    if(s_s_m_m):
        horse_image = generate_ssmm_horse_image_for_pygame(individual)
    else:
        horse_image = generate_horse_image_for_pygame(individual)
    s = GSprite(color_white, rect, horse_image)
    h = Horse(genetics=individual, g_sprite=s)
    return h


def generate_horses_array_with_offset(individuals: array, n=4, margin_x=m_x, margin_y=m_y,
                                      offset=side, offset_1=side) -> array:
    horses = zeros(n, dtype=Horse)

    offset_x = 0
    offset_y = 0
    for i in range(n):
        x = margin_x + offset_x + offset
        y = margin_y + offset_y + 2*offset_1
        rect = Rect([x, y, side, side])
        horses[i] = generate_horse(individuals[i], rect)
        offset_x = offset_x + side
    return horses


def generate_horses_array(individuals: array, n=4) -> array:
    horses = generate_horses_array_with_offset(individuals, n, m_x, m_y, 0, 0)
    return horses
