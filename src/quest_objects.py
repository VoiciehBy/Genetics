from pygame import Rect, Surface, Color
from constants import default_population_size, default_chromosome_length, offset
from VSprite import VSprite
from Bullet import Bullet
from GPopulation import GPopulation

red = Color("red")
rect = Rect(0, 0, 128, 128)

t = Surface((128 * 2, 4))
t.fill(red)

rect_2 = Rect(rect.left, rect.top + offset, 1, 1)
sprite_2 = VSprite(red, rect_2, t)
bullet = Bullet(sprite_2)

ai_population_0 = GPopulation(default_population_size)
ai_population_0.generate_initial_population(default_chromosome_length, default_population_size)


def get_ai_population() -> GPopulation:
    return ai_population_0


def set_delta_time(x):
    global delta_time
    delta_time = x


def get_delta_time():
    global delta_time
    return delta_time
