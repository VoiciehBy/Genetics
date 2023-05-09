from pygame_utils import drawText
from pygame import Rect


class OverText:
    def __init__(self, rect, txt='', active=False):
        self.rect = rect
        self.rect = Rect(rect.x, rect.y, int(64), int(64))
        self.txt = txt
        self.active = active

    def set_txt(self, txt):
        self.txt = txt

    def set_active(self):
        self.active = True

    def draw(self, surface):
        if(self.active):
            drawText(surface, self.txt, self.rect)
