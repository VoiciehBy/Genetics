from utils import generate_id
from Individual import Individual
from GSprite import GSprite
from pygame import Rect, Color
from constants import screen, default_horse_name

from GColor import GColor, green, blue, black, red

from trait_utils import surname, strong_weak, invisible_bald


class Horse:
    def __init__(self, name=default_horse_name, genetics=Individual, g_sprite=GSprite):
        self.id = generate_id()
        self.name = name
        self.genetics = genetics
        self.horseSprite = g_sprite
        self.horseSprite.text = self.name

    def __eq__(self, o) -> bool:
        return self.id == o.id and self.name == o.name and self.genetics == o.genetics

    def set_sprite_color(self, sprite_color: GColor):
        self.horseSprite.set_color(sprite_color.to_pygame_color())

    def set_sprite_color_using_pygame_color(self, sprite_color: GColor):
        self.horseSprite.set_color(sprite_color)

    def set_sprite_color_green(self):
        self.set_sprite_color(green)

    def set_sprite_color_blue(self):
        self.set_sprite_color(blue)

    def update_sprite_over_text(self):
        self.horseSprite.set_over_text_txt(self.name)

    def set_sprite_over_text_active(self):
        self.horseSprite.set_over_text_active()

    def set_sprite_indicator_active(self):
        self.horseSprite.set_indicator_active()

    def sprite_color(self) -> Color:
        return self.horseSprite.get_color()

    def flip(self):
        self.horseSprite.flip()

    def draw(self, surface=screen):
        self.horseSprite.draw(surface)

    def move(self, x, y):
        self.horseSprite.move(x, y)

    def sprite_rect(self) -> Rect:
        return self.horseSprite.get_rect()

    def sprite_indicator_rect(self) -> Rect:
        return self.horseSprite.get_indicator_rect()

    def coat_color(self) -> GColor:
        return self.genetics.color_trait()

    def mane_color(self) -> GColor:
        return self.coat_color().inverse()

    def eye_color(self) -> GColor:
        return self.coat_color().inverse() - self.coat_color()

    @staticmethod
    def nose_color() -> GColor:
        return red

    @staticmethod
    def foot_color() -> GColor:
        return black

    def fitness(self) -> int:
        return int(self.genetics.fitness())

    def parents(self) -> list:
        result = self.genetics.get_parents()
        if(result):
            return list(result)

    def set_name(self, name: str):
        self.name = name
        titles = ''
        titles += surname(self.coat_color())
        titles += invisible_bald(self.coat_color())
        titles += strong_weak(self.fitness())
        self.name = self.name + ' ' + titles

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)
