from pygame import Color, Rect
from pygame_utils import drawImageOverRect, mvPygameRect, flipSurfaceHorizontally
import indicator as i
import overText as oT


class sprite:
    def __init__(self, color, rect, texture):
        self.color = Color(color.rgb())
        self.rect = Rect(rect)
        self.texture = texture
        self.overTxt = oT.overText(self.rect)
        self.spriteIndicator = i.indicator(self.rect, self.color)

    def flip(self):
        self.texture = flipSurfaceHorizontally(self.texture)

    def draw(self, surface):
        self.spriteIndicator.draw(surface, self.color)
        self.overTxt.draw(surface)
        drawImageOverRect(surface, self.texture, self.rect)

    def move(self, x, y):
        self.rect = mvPygameRect(self.rect, x, y)

    def set_over_text_txt(self, txt):
        self.overTxt.setTxt(txt)

    def set_over_text_active(self):
        self.overTxt.setActive()

    def set_indicator_active(self):
        self.spriteIndicator.setActive()

    def get_rect(self) -> Rect:
        return self.rect
