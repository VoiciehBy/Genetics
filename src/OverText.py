from pygame import Rect, Surface
from draw import drawText


class OverText:
    def __init__(self, rect: Rect, txt='', active=False):
        self.rect = rect
        self.rect = Rect(rect.x, rect.y, int(64), int(64))
        self.txt = txt
        self.active = active

    def set_txt(self, txt: str):
        self.txt = txt

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def draw(self, surface: Surface):
        if self.active:
            drawText(surface, self.txt, self.rect)
