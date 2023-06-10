from constants import horse_player_rect, horse_image_side, default_population_size, default_chromosome_length, offset
from GPopulation import GPopulation
from g_horse_utils import generate_horses_array
from numpy import zeros, uint8
from g_horse_utils import get_horse_image
from pygame import Rect, Surface, Color
from VSprite import VSprite
from GHorse import GHorse
from Bullet import Bullet

population_0 = GPopulation(default_population_size)
population_0.generate_initial_population(default_chromosome_length, default_population_size)

population_1 = GPopulation(default_population_size)
population_1.generate_initial_population(default_chromosome_length, default_population_size)

pop_0 = population_0.get_pop()
horses = generate_horses_array(pop_0)

first_parents = [horses[0], horses[1]]
second_parents = [horses[2], horses[3]]

genes = zeros(default_chromosome_length, dtype=uint8)
horse_image = get_horse_image()
blue = Color("blue")
sprite = VSprite(blue, horse_player_rect, horse_image)
horse: GHorse = GHorse("Koń", genes, sprite, False, False)

bullet_texture = Surface((horse_image_side, default_population_size))
red = Color("red")
bullet_texture.fill(red)
bullet_rect = Rect(horse_player_rect.left + 3*offset, horse_player_rect.top + offset, 1, 1)
sprite_2 = VSprite(red, bullet_rect, bullet_texture)
bullet = Bullet(sprite_2)

global delta_time


def get_population_0() -> GPopulation:
    return population_0


def get_population_1() -> GPopulation:
    return population_1


def get_delta_time():
    global delta_time
    return delta_time


def set_first_parent(g_object):
    first_parents[0] = g_object


def set_second_parent(g_object):
    first_parents[1] = g_object


def set_third_parent(g_object):
    second_parents[0] = g_object


def set_fourth_parent(g_object):
    second_parents[1] = g_object


def set_delta_time(x):
    global delta_time
    delta_time = x
