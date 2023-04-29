from individual import individual
from sprite import sprite
from pygame import Rect
from constants import clearColor, screen, default_horse_name
from color import color, green, blue, black, red

# Names: #Koń# Pony #Ferus #Equus #Caballus


class horse():
    def __init__(self, name=default_horse_name, genetics=individual, sprite=sprite):
        self.name = name
        self.genetics = genetics
        self.sprite = sprite
        self.sprite.text = self.name

    def __eq__(self, o) -> bool:
        return self.genetics == o.genetics

    def set_sprite_color(self, color):
        self.sprite.color = color.toPyGameColor()

    def set_sprite_color_green(self):
        self.set_sprite_color(green)

    def set_sprite_color_blue(self):
        self.set_sprite_color(blue)

    def update_sprite_overText(self):
        self.sprite.overText.txt = self.name

    def set_sprite_over_text_active(self, b=True):
        self.sprite.set_over_text_active(b)

    def draw(self, surface=screen):
        self.sprite.draw(surface)

    def move(self, x, y):
        self.sprite.move(x, y)

    def rect(self) -> Rect:
        return Rect(self.sprite.rect)

    def sprite_rect(self) -> Rect:
        return self.sprite.rect

    def coat_color(self) -> color:
        return self.genetics.color_trait()

    def mane_color(self) -> color:
        return self.coat_color().inverse()

    def eye_color(self) -> color:
        return self.coat_color().inverse() - self.coat_color()

    def nose_color(self) -> color:
        return c.red

    def foot_color(self) -> color:
        return c.black

    def invisible(self) -> bool:
        return clearColor == self.coat_color().toPyGameColor()

    def bald(self) -> bool:
        return clearColor == self.mane_color().toPyGameColor()

    def strong(self) -> bool:
        return self.fitness() >= 5

    def weak(self) -> bool:
        return self.fitness() <= 2

    def parents(self) -> list:
        if(self.genetics.parents != None):
            return list(self.genetics.parents)

    def fitness(self) -> int:
        return int(self.genetics.fitness())

    def debug_lines(self) -> list:
        lines = []
        if(self.parents() != None):
            lines.append(str("parent:") + str(self.parents()[0]))
            lines.append(str("parent:") + str(self.parents()[1]))

        lines.append(str("genes:") + str(self.genetics))
        lines.append(str("coat color:") + str(self.coat_color()))
        lines.append(str("mane color:") + str(self.mane_color()))
        lines.append(str("eye color:") + str(self.eye_color()))
        lines.append(str("nose color:") + str(self.nose_color()))
        lines.append(str("foot color:") + str(self.foot_color()))
        lines.append(str("invisible:") + str(self.invisible()))
        lines.append(str("bald:") + str(self.bald()))
        return lines

    def updateTitles(self):
        titles = []
        if(str(self.coat_color().name())):
            titles.append(str(self.coat_color().name()).capitalize())
        if(self.invisible()):
            titles.append(" The Invisible")
        elif(self.bald()):
            titles.append(" The Bald")
        elif(self.strong()):
            titles.append(" The Strong")
        elif(self.weak()):
            titles.append(" The Weak")

        name = ''
        for title in titles:
            name = name + str(title)
        name = self.name + ' ' + name
        self.name = name

    def updateName(self):
        self.updateTitles()
        self.update_sprite_overText()

    def __str__(self) -> str:
        self.updateTitles()
        lines = []
        lines.append(str("name:") + str(self.name))
        self.update_sprite_overText()
        #debug = False
        # if(debug):
        #    lines.append(self.debug_lines())

        result = ''
        for line in lines:
            result = result + str(line + "\n")
        return str(result)
