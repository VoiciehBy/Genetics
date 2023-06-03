from utils import clamp, rgb_to_hex
from pygame import Color
from constants import COLORS


class GColor:
    color_names: dict = COLORS

    def __init__(self, g_red, g_green, g_blue):
        self.red: int = clamp(g_red, 0, 255)
        self.green: int = clamp(g_green, 0, 255)
        self.blue: int = clamp(g_blue, 0, 255)

    def __eq__(self, o) -> bool:
        b = self.red == o.red
        b = b and self.green == o.green
        b = b and self.blue == o.blue
        return b

    def __add__(self, o):
        g_red: int = clamp(self.red + o.red, 0, 255)
        g_green: int = clamp(self.green + o.green, 0, 255)
        g_blue: int = clamp(self.blue + o.blue, 0, 255)
        return GColor(g_red, g_green, g_blue)

    def __sub__(self, o):
        g_red: int = clamp(self.red - o.red, 0, 255)
        g_green: int = clamp(self.green - o.green, 0, 255)
        g_blue: int = clamp(self.blue - o.blue, 0, 255)
        return GColor(g_red, g_green, g_blue)

    def to_rgb(self) -> list:
        return list([self.red, self.green, self.blue])

    def inverse(self):
        return GColor(self.blue, self.green, self.red)

    def to_pygame_color(self) -> Color:
        return Color(self.red, self.green, self.blue)

    def name(self) -> str:
        try:
            color = rgb_to_hex(self.to_rgb())
            return COLORS[str(color)]
        except KeyError:
            return ''

    def __str__(self) -> str:
        rgb = self.to_rgb()
        try:
            color = rgb_to_hex(rgb)
            txt = self.color_names[str(color)]
        except KeyError:
            txt = ''
        return str(rgb) + ' ' + txt


black = GColor(0, 0, 0)
white = GColor(255, 255, 255)
brown = GColor(102, 57, 49)
red = GColor(255, 0, 0)
green = GColor(0, 255, 0)
blue = GColor(0, 0, 255)
magenta = GColor(255, 0, 255)

cyan = GColor(0, 255, 255)
