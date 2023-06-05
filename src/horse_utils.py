from pygame import Surface, Rect, image, Color
from Individual import Individual
from numpy import array, zeros

from constants import s_s_m_m, window_height
from constants import horse_image_side as side
from pygame_colors import color_white, color_brown, color_cyan, color_red, color_black, color_green, color_blue
from constants import margin_x as m_x
from constants import margin_y as m_y
from GSprite import GSprite
from Horse import Horse

from GColor import GColor

import objects as o


def get_horse_image() -> Surface:
    if s_s_m_m:
        return image.load("../img/horse_s_s_m_m.png")
    else:
        return image.load("../img/horse.png")


def generate_horse_image_for_pygame(individual: Individual) -> array:
    horse_image: Surface = get_horse_image()
    individual_color: Color = Color(individual.color_trait().to_pygame_color())
    inverted_individual_g_color: GColor = individual.color_trait().inverse()
    inverted_individual_color: Color = Color(inverted_individual_g_color.to_pygame_color())
    the_color: Color = Color(inverted_individual_color - individual_color)

    for i in range(side):
        for j in range(side):
            horse_color: Color = Color(horse_image.get_at((i, j)))
            if horse_color == color_white:
                if s_s_m_m:
                    horse_image.set_at((i, j), individual_color)
                else:
                    horse_image.set_at((i, j), inverted_individual_color)
            elif(s_s_m_m is False and horse_color == color_brown):
                horse_image.set_at((i, j), individual_color)
            elif(s_s_m_m and horse_color == color_cyan):
                horse_image.set_at((i, j), inverted_individual_color)
            elif horse_color == color_red:
                horse_image.set_at((i, j), color_black)
            elif(s_s_m_m and horse_color == color_green):
                horse_image.set_at((i, j), color_red)
            elif horse_color == color_blue:
                horse_image.set_at((i, j), the_color)
    return horse_image


def generate_horse(individual: Individual, rect: Rect) -> Horse:
    horse_image = generate_horse_image_for_pygame(individual)
    s = GSprite(color_white, rect, horse_image)
    return Horse(genetics=individual, g_sprite=s)


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
    horses = generate_horses_array_with_offset(
        individuals, n, m_x, m_y, int(side/2), 0)
    return horses


def get_horse_parents() -> array:
    n = 4
    horses_parents = zeros(n, dtype=Horse)
    horse_parents_genetics = zeros(n, dtype=Individual)
    horse_parents_genetics[0] = o.first_parents[0].genetics
    horse_parents_genetics[1] = o.first_parents[1].genetics
    horse_parents_genetics[2] = o.second_parents[0].genetics
    horse_parents_genetics[3] = o.second_parents[1].genetics

    offset_x = 2 * m_x
    offset_y = int(window_height/2)
    for i in range(n):
        x = offset_x + (i % 2) * side
        y = offset_y + side
        rect = Rect([x, y, side, side])
        horses_parents[i] = generate_horse(horse_parents_genetics[i], rect)
        offset_y = offset_y + (i % 2) * side
    del horse_parents_genetics
    return horses_parents
