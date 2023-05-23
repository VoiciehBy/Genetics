from constants import font_size
from pygame import Color, Rect, Surface
from pygame_utils import drawImageOverRect, move_pygame_rect, flip_surface_horizontally
from Indicator import Indicator
from OverText import OverText


class GSprite:
    def __init__(self, color: Color, rect: Rect, texture):
        self.color = Color(color)
        self.rect = rect
        self.texture = texture
        overTextRect = Rect(self.rect.left, self.rect.top -
                            font_size, self.rect.width, self.rect.height)
        self.overTxt = OverText(overTextRect)
        self.spriteIndicator = Indicator(self.rect, self.color)

    def flip(self):
        self.texture = flip_surface_horizontally(self.texture)

    def draw(self, surface: Surface):
        self.spriteIndicator.draw(surface, self.color)
        self.overTxt.draw(surface)
        drawImageOverRect(surface, self.texture, self.rect)

    def move(self, x: int, y: int):
        self.rect = move_pygame_rect(self.rect, x, y)

    def set_color(self, color):
        self.color = color

    def set_over_text_txt(self, txt):
        self.overTxt.set_txt(txt)

    def set_over_text_active(self):
        self.overTxt.set_active()

    def set_over_text_inactive(self):
        self.overTxt.set_inactive()

    def set_indicator_active(self):
        self.spriteIndicator.set_active()

    def get_rect(self) -> Rect:
        return self.rect

    def get_indicator_rect(self) -> Rect:
        return Rect(self.spriteIndicator.get_rect())

    def get_color(self):
        return Color(self.color)
