from constants import font_size, screen
from pygame import Color, Rect, Surface
from pygame_utils import move_pygame_rect, flip_surface_horizontally
from draw import drawImageOverRect
from Indicator import Indicator
from OverText import OverText

from constants import debug_mode


class VSprite:
    def __init__(self, color: Color, rect: Rect, texture: Surface):
        self.color = Color(color)
        self.rect = Rect(rect)
        self.texture = texture
        over_text_rect = Rect(self.rect.left, self.rect.top -
                              font_size, self.rect.width, self.rect.height)
        self.overTxt = OverText(over_text_rect)
        self.spriteIndicator = Indicator(self.rect, self.color)

    def flip(self):
        self.texture = flip_surface_horizontally(self.texture)

    def draw(self, surface=screen):
        if debug_mode:
            self.spriteIndicator.draw(surface, self.color)
        self.overTxt.draw(surface)
        drawImageOverRect(surface, self.texture, self.rect)

    def move(self, x: int, y: int):
        self.rect = move_pygame_rect(self.rect, x, y)

    def set_color(self, color: Color):
        self.color = Color(color)

    def set_rect(self, rect: Rect):
        self.rect = rect

    def set_over_text_txt(self, txt=''):
        self.overTxt.set_txt(txt)

    def set_over_text_active(self):
        self.overTxt.set_active()

    def set_over_text_inactive(self):
        self.overTxt.set_inactive()

    def set_indicator_active(self):
        self.spriteIndicator.set_active()

    def get_g_sprite_rect(self) -> Rect:
        return Rect(self.rect)

    def get_indicator_rect(self) -> Rect:
        return Rect(self.spriteIndicator.get_indicator_rect())

    def get_color(self):
        return Color(self.color)
