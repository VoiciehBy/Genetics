from pygame import Color, Rect
from pygame_utils import drawImageOverRect, mvPygameRect, flipSurfaceHorizontally
from Indicator import Indicator
from OverText import OverText


class GSprite:
    def __init__(self, color, rect, texture):
        self.color = Color(color.rgb())
        self.rect = Rect(rect)
        self.texture = texture
        self.overTxt = OverText(self.rect)
        self.spriteIndicator = Indicator(self.rect, self.color)

    def flip(self):
        self.texture = flipSurfaceHorizontally(self.texture)

    def draw(self, surface):
        self.spriteIndicator.draw(surface, self.color)
        self.overTxt.draw(surface)
        drawImageOverRect(surface, self.texture, self.rect)

    def move(self, x, y):
        self.rect = mvPygameRect(self.rect, x, y)

    def set_over_text_txt(self, txt):
        self.overTxt.set_txt(txt)

    def set_over_text_active(self):
        self.overTxt.set_active()

    def set_indicator_active(self):
        self.spriteIndicator.set_active()

    def get_rect(self) -> Rect:
        return self.rect

    def get_indicator_rect(self) -> Rect:
        return Rect(self.spriteIndicator.get_rect())
