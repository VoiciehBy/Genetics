from numpy import zeros, uint8
from g_horse_utils import get_horse_image
from pygame import Rect, Surface, Color
from constants import horse_player_rect, horse_image_side, default_population_size, default_chromosome_length, offset
from VSprite import VSprite
from GHorse import GHorse
from Bullet import Bullet
from GPopulation import GPopulation

genes = zeros(default_chromosome_length, dtype=uint8)
horse_image = get_horse_image()
blue = Color("blue")
sprite = VSprite(blue, horse_player_rect, horse_image)
horse: GHorse = GHorse("Koń", genes, sprite, False, False)

bullet_texture = Surface((horse_image_side, default_population_size))
red = Color("red")
bullet_texture.fill(red)
bullet_rect = Rect(horse_player_rect.left, horse_player_rect.top + offset, 1, 1)
sprite_2 = VSprite(red, bullet_rect, bullet_texture)
bullet = Bullet(sprite_2)

ai_population_0 = GPopulation(default_population_size)
ai_population_0.generate_initial_population(default_chromosome_length, default_population_size)

global delta_time
delta_time = 0

def get_ai_population() -> GPopulation:
    return ai_population_0


def set_delta_time(x):
    global delta_time
    delta_time = x


def get_delta_time():
    global delta_time
    return delta_time
