from pygame_utils import drawPygameRect
from pygame import Rect


class indicator:
    def __init__(self, rect, color, active=False):
        self.rect = rect
        self.rect = Rect(rect.x + 32, rect.y + 128, int(64), int(64))
        self.color = color
        self.active = active

    def setActive(self):
        self.active = True

    def draw(self, surface, color=None):
        if(self.active):
            if(color):
                drawPygameRect(surface, color, self.rect)
            else:
                drawPygameRect(surface, self.color, self.rect)
