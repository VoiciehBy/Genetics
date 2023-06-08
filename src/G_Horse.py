from G_Individual import G_Individual
from VSprite import VSprite
from pygame import Rect, Color
from constants import default_horse_name, FITNESS_TXT

from GColor import GColor

from trait_utils import surname, strong_weak, invisible_bald


class G_Horse:
    def __init__(self, name=default_horse_name, genetics=G_Individual, g_sprite=VSprite, looking_right=False, ai=False):
        self.name = name
        self.genetics = genetics
        self.horseSprite = g_sprite
        self.looking_right = looking_right
        self.ai = ai

    def set_name(self, name: str):
        self.name = name
        titles = ''
        titles += surname(self.coat_color())
        titles += invisible_bald(self.coat_color())
        titles += strong_weak(self.fitness())
        self.name = self.name + ' ' + titles

    def set_sprite_color(self, sprite_color: GColor):
        new_color: Color = Color(sprite_color.to_pygame_color())
        self.horseSprite.set_color(new_color)

    def set_sprite_color_using_pygame_color(self, sprite_color: GColor):
        self.horseSprite.set_color(sprite_color)

    def set_sprite_color_white_using_pygame_color(self):
        color_white: Color = Color("white")
        self.horseSprite.set_color(color_white)

    def update_sprite_over_text(self):
        self.horseSprite.set_over_text_txt(
            self.name + ' ' + FITNESS_TXT + ": " + str(self.fitness()))

    def set_sprite_over_text_active(self):
        self.horseSprite.set_over_text_active()

    def set_sprite_over_text_inactive(self):
        self.horseSprite.set_over_text_inactive()

    def set_sprite_indicator_active(self):
        self.horseSprite.set_indicator_active()

    def set_ai(self, b: bool):
        self.ai = b

    def flip(self):
        self.looking_right = not(self.looking_right)
        self.horseSprite.flip()

    def draw(self):
        self.horseSprite.draw()

    def move(self, x: int, y: int):
        self.horseSprite.move(x, y)

    def sprite_rect(self) -> Rect:
        return Rect(self.horseSprite.get_g_sprite_rect())

    def sprite_indicator_rect(self) -> Rect:
        return self.horseSprite.get_indicator_rect()

    def is_looking_right(self) -> bool:
        return self.looking_right

    def coat_color(self) -> GColor:
        return self.genetics.color_trait()

    def fitness(self) -> int:
        return int(self.genetics.individual_fitness())

    def parents(self) -> list:
        result = self.genetics.get_parents()
        if result:
            return list(result)

    def is_ai(self) -> bool:
        return bool(self.ai)
