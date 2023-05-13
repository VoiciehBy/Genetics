from pygame_utils import drawPygameRect
from pygame import Rect, Color, Surface


class Indicator:
    def __init__(self, rect: Rect, color: Color, active=False):
        self.rect = rect
        self.rect = Rect(rect.x + 32, rect.y + 128, int(64), int(64))
        self.color = color
        self.active = active

    def set_active(self):
        self.active = True

    def get_rect(self) -> Rect:
        return Rect(self.rect)

    def draw(self, surface: Surface, color=None):
        if(self.active):
            if(color):
                drawPygameRect(surface, color, self.rect)
            else:
                drawPygameRect(surface, self.color, self.rect)