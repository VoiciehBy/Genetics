from utils import generate_id
from Individual import Individual
from GSprite import GSprite
from pygame import Rect, Color
from constants import clearColor, screen, default_horse_name
from constants import TITLE_THE_INVISIBLE_TXT, TITLE_THE_BALD_TXT, TITLE_THE_STRONG_TXT, TITLE_THE_WEAK_TXT
from GColor import GColor, green, blue, black, red


class Horse:
    def __init__(self, name=default_horse_name, genetics=Individual, g_sprite=GSprite):
        self.id = generate_id()
        self.name = name
        self.genetics = genetics
        self.horseSprite = g_sprite
        self.horseSprite.text = self.name

    def __eq__(self, o) -> bool:
        return self.id == o.id and self.name == o.name and self.genetics == o.genetics

    def set_sprite_color(self, sprite_color):
        self.horseSprite.set_color(sprite_color.to_pygame_color())

    def set_sprite_color_using_pygame_color(self, sprite_color):
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

    def invisible(self) -> bool:
        return clearColor == self.coat_color().to_pygame_color()

    def bald(self) -> bool:
        return clearColor == self.mane_color().to_pygame_color()

    def fitness(self) -> int:
        return int(self.genetics.fitness())

    def strong(self) -> bool:
        return self.fitness() >= 5

    def weak(self) -> bool:
        return self.fitness() <= 2

    def parents(self) -> list:
        result = self.genetics.get_parents()
        if(result):
            return list(result)

    def update_titles(self):
        name = ''
        if(str(self.coat_color().name())):
            name += str(self.coat_color().name()).capitalize()
        if(self.invisible()):
            name += TITLE_THE_INVISIBLE_TXT
        elif(self.bald()):
            name += TITLE_THE_BALD_TXT
        elif(self.strong()):
            name += TITLE_THE_STRONG_TXT
        elif(self.weak()):
            name += TITLE_THE_WEAK_TXT
        self.name = self.name + ' ' + name

    def set_name(self, name):
        self.name = name
        self.update_titles()

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)
