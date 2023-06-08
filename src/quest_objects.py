from pygame import Rect, Color, Surface

from constants import offset

from VSprite import VSprite
from Bullet import Bullet

from G_Population import G_Population

rect = Rect(0, 0, 128, 128)
t = Surface((128 * 2, 4))
t.fill(Color("red"))
rect_2 = Rect(rect.left, rect.top + offset, 1, 1)
sprite_2 = VSprite(Color("red"), rect_2, t)
bullet = Bullet(sprite_2)

global delta_time
delta_time = 0

ai_population_0 = G_Population(4)
ai_population_0.generate_initial_population(8, 4)


def get_ai_population() -> G_Population:
    return ai_population_0


def set_delta_time(x):
    global delta_time
    delta_time = x


def get_delta_time():
    global delta_time
    return delta_time
