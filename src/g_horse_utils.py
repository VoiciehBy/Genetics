from pygame import Surface, Rect, image, Color, transform
from GIndividual import GIndividual
from numpy import array, zeros
from constants import s_s_m_m, quest_mode, window_height
from pygame_utils import flip_surface_horizontally
from constants import horse_image_side
from constants import HORSE_IMAGE_FILE_NAME, HORSE_S_S_M_M_FILE_NAME, default_population_size
from constants import margin_x as m_x
from constants import margin_y as m_y
from VSprite import VSprite
from GHorse import GHorse
from GColor import GColor

import objects as o


def get_horse_image() -> Surface:
    path = HORSE_S_S_M_M_FILE_NAME if s_s_m_m else HORSE_IMAGE_FILE_NAME
    result = flip_surface_horizontally(image.load(path)) if s_s_m_m else image.load(path)
    result = transform.scale(result, (horse_image_side * 2, horse_image_side * 2)) if quest_mode else result
    return result


def generate_horse_image_for_pygame(individual: GIndividual) -> array:
    horse_image: Surface = get_horse_image()
    individual_color: Color = Color(individual.color_trait().to_pygame_color())
    inverted_individual_g_color: GColor = individual.color_trait().inverse()
    inverted_individual_color: Color = Color(inverted_individual_g_color.to_pygame_color())

    horse_image_width: int = horse_image.get_width()
    horse_image_height: int = horse_image.get_height()

    for i in range(horse_image_width):
        for j in range(horse_image_height):
            horse_color: Color = Color(horse_image.get_at((i, j)))
            if horse_color == Color("white"):
                temp_color: Color = individual_color if s_s_m_m else inverted_individual_color
                horse_image.set_at((i, j), temp_color)
            elif horse_color == Color(102, 57, 49):
                horse_image.set_at((i, j), individual_color)
            elif (s_s_m_m and horse_color == Color("cyan")):
                horse_image.set_at((i, j), inverted_individual_color)
            elif horse_color == Color("red"):
                horse_image.set_at((i, j), Color("black"))
            elif (s_s_m_m and horse_color == Color("green")):
                horse_image.set_at((i, j), Color("red"))
    return horse_image


def generate_horse(individual: GIndividual, rect: Rect) -> GHorse:
    horse_image = generate_horse_image_for_pygame(individual)
    s = VSprite(Color("white"), rect, horse_image)
    return GHorse(genetics=individual, g_sprite=s)


def generate_horses_array_with_offset(individuals: array, n=default_population_size, margin_x=m_x, margin_y=m_y,
                                      offset=horse_image_side, offset_1=horse_image_side) -> array:
    horses = zeros(n, dtype=GHorse)
    offset_x = 0
    offset_y = 0
    for i in range(n):
        x = margin_x + offset_x + offset
        y = margin_y + offset_y + 2 * offset_1
        rect = Rect([x, y, horse_image_side, horse_image_side])
        horses[i] = generate_horse(individuals[i], rect)
        offset_x = offset_x + horse_image_side
    return horses


def generate_horses_array(individuals: array, n=default_population_size) -> array:
    horses = generate_horses_array_with_offset(individuals, n, m_x, m_y, int(horse_image_side / 2), 0)
    return horses


def get_horse_parents() -> array:
    horses_parents = zeros(default_population_size, dtype=GHorse)
    horse_parents_genetics = zeros(default_population_size, dtype=GIndividual)

    horse_parents_genetics[0] = o.first_parents[0].genetics
    horse_parents_genetics[1] = o.first_parents[1].genetics
    horse_parents_genetics[2] = o.second_parents[0].genetics
    horse_parents_genetics[3] = o.second_parents[1].genetics

    offset_x = 2 * m_x
    offset_y = int(window_height / 2)
    for i in range(default_population_size):
        x = offset_x + (i % 2) * horse_image_side
        y = offset_y + horse_image_side
        rect = Rect([x, y, horse_image_side, horse_image_side])
        horses_parents[i] = generate_horse(horse_parents_genetics[i], rect)
        offset_y = offset_y + (i % 2) * horse_image_side
    del horse_parents_genetics
    return horses_parents
