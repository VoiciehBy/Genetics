from pygame_utils import drawPygameRect
from pygame import Rect


class indicator:
    def __init__(self, rect, color):
        self.rect = rect
        self.rect = Rect(rect.x + 32, rect.y + 128, int(64), int(64))
        self.color = color

    def draw(self, surface, color=None):
        if(color):
            drawPygameRect(surface, color, self.rect)
        else:
            drawPygameRect(surface, self.color, self.rect)
