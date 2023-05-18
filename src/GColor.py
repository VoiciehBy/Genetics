from utils import clamp, rgb_to_hex
from pygame import Color
from constants import COLORS


class GColor:
    def __init__(self, g_red, g_green, g_blue):
        self.bgr = [g_blue, g_green, g_red]
        self.bgr[0] = clamp(self.bgr[0], 0, 255)
        self.bgr[1] = clamp(self.bgr[1], 0, 255)
        self.bgr[2] = clamp(self.bgr[2], 0, 255)

    def __eq__(self, o) -> bool:
        return self.bgr[0:2] == o.bgr[0:2]

    def __add__(self, o):
        self.bgr[0] = clamp(self.bgr[0] + o.bgr[0], 0, 255)
        self.bgr[1] = clamp(self.bgr[1] + o.bgr[1], 0, 255)
        self.bgr[2] = clamp(self.bgr[2] + o.bgr[2], 0, 255)
        return GColor(self.bgr[2], self.bgr[1], self.bgr[0])

    def __sub__(self, o):
        self.bgr[0] = clamp(self.bgr[0] - o.bgr[0], 0, 255)
        self.bgr[1] = clamp(self.bgr[1] - o.bgr[1], 0, 255)
        self.bgr[2] = clamp(self.bgr[2] - o.bgr[2], 0, 255)
        return GColor(self.bgr[2], self.bgr[1], self.bgr[0])

    def rgb(self) -> list:
        rgb = [self.bgr[2], self.bgr[1], self.bgr[0]]
        return list(rgb)

    def inverse(self):
        return GColor(self.bgr[0], self.bgr[1], self.bgr[2])

    def to_pygame_color(self) -> Color:
        return Color(self.bgr[2], self.bgr[1], self.bgr[0])

    def name(self) -> str:
        rgb = (self.rgb()[0], self.rgb()[1], self.rgb()[2])
        try:
            color = rgb_to_hex(rgb)
            return COLORS[str(color)]
        except KeyError:
            return ''

    def __str__(self) -> str:
        rgb = (self.rgb()[0], self.rgb()[1], self.rgb()[2])
        try:
            color = rgb_to_hex(rgb)
            txt = COLORS[str(color)]
        except KeyError:
            txt = ''
        return str(self.rgb) + ' ' + txt


black = GColor(0, 0, 0)
white = GColor(255, 255, 255)
brown = GColor(102, 57, 49)
red = GColor(255, 0, 0)
green = GColor(0, 255, 0)
blue = GColor(0, 0, 255)
magenta = GColor(255, 0, 255)

cyan = GColor(0, 255, 255)
