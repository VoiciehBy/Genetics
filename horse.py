from utils import generateId
from individual import individual
from sprite import sprite
from pygame import Rect
from constants import clearColor, screen, default_horse_name
from constants import TITLE_THE_INVISIBLE_TXT, TITLE_THE_BALD_TXT, TITLE_THE_STRONG_TXT, TITLE_THE_WEAK_TXT
from color import color, green, blue, black, red


class horse:
    def __init__(self, name=default_horse_name, genetics=individual, g_sprite=sprite):
        self.id = generateId()
        self.name = name
        self.genetics = genetics
        self.horseSprite = g_sprite
        self.horseSprite.text = self.name

    def __eq__(self, o) -> bool:
        return self.id == o.id and self.name == o.name and self.genetics == o.genetics

    def set_sprite_color(self, sprite_color):
        self.horseSprite.color = sprite_color.toPyGameColor()

    def set_sprite_color_green(self):
        self.set_sprite_color(green)

    def set_sprite_color_blue(self):
        self.set_sprite_color(blue)

    def update_sprite_overText(self):
        name = self.name
        self.horseSprite.set_over_text_txt(name)

    def set_sprite_over_text_active(self):
        self.horseSprite.set_over_text_active()

    def set_sprite_indicator_active(self):
        self.horseSprite.set_indicator_active()

    def flip(self):
        self.horseSprite.flip()

    def draw(self, surface=screen):
        self.horseSprite.draw(surface)

    def move(self, x, y):
        self.horseSprite.move(x, y)

    def rect(self) -> Rect:
        return Rect(self.horseSprite.get_rect())

    def sprite_rect(self) -> Rect:
        return self.horseSprite.get_rect()

    def coat_color(self) -> color:
        return self.genetics.color_trait()

    def mane_color(self) -> color:
        return self.coat_color().inverse()

    def eye_color(self) -> color:
        return self.coat_color().inverse() - self.coat_color()

    @staticmethod
    def nose_color() -> color:
        return red

    @staticmethod
    def foot_color() -> color:
        return black

    def invisible(self) -> bool:
        return clearColor == self.coat_color().toPyGameColor()

    def bald(self) -> bool:
        return clearColor == self.mane_color().toPyGameColor()

    def fitness(self) -> int:
        return int(self.genetics.fitness())

    def strong(self) -> bool:
        return self.fitness() >= 5

    def weak(self) -> bool:
        return self.fitness() <= 2

    def parents(self) -> list:
        result = self.genetics.getParents()
        if(result):
            return list(result)

    def updateTitles(self):
        titles = []
        if(str(self.coat_color().name())):
            colorTitle = str(self.coat_color().name()).capitalize()
            titles.append(colorTitle)
        if(self.invisible()):
            titles.append(' ' + TITLE_THE_INVISIBLE_TXT)
        elif(self.bald()):
            titles.append(' ' + TITLE_THE_BALD_TXT)
        elif(self.strong()):
            titles.append(' ' + TITLE_THE_STRONG_TXT)
        elif(self.weak()):
            titles.append(' ' + TITLE_THE_WEAK_TXT)

        name = ''
        for title in titles:
            name += str(title)
        name = self.name + ' ' + name
        self.name = name

    def updateName(self):
        self.updateTitles()
        self.update_sprite_overText()
