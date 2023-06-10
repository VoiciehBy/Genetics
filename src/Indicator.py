from pygame import Rect, Color, Surface
from draw import drawPygameRect
from constants import horse_image_side, debug_mode


class Indicator:
    def __init__(self, rect: Rect, color: Color, active=False):
        self.rect = rect
        self.rect = Rect(rect.x + int(horse_image_side/4), rect.y + horse_image_side, int(horse_image_side/2), int(horse_image_side/2))
        self.color = color
        self.active = active

    def set_active(self):
        self.active = True

    def get_indicator_rect(self) -> Rect:
        return Rect(self.rect)

    def get_color(self) -> Color:
        return self.color

    def draw(self, surface: Surface, color=None):
        if self.active and debug_mode:
            if color:
                drawPygameRect(surface, color, self.rect)
            else:
                drawPygameRect(surface, self.color, self.rect)
