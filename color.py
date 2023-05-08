from utils import clamp
from pygame import Color
import webcolors


class color:
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
        return color(self.bgr[2], self.bgr[1], self.bgr[0])

    def __sub__(self, o):
        self.bgr[0] = clamp(self.bgr[0] - o.bgr[0], 0, 255)
        self.bgr[1] = clamp(self.bgr[1] - o.bgr[1], 0, 255)
        self.bgr[2] = clamp(self.bgr[2] - o.bgr[2], 0, 255)
        return color(self.bgr[2], self.bgr[1], self.bgr[0])

    def rgb(self) -> list:
        rgb = [self.bgr[2], self.bgr[1], self.bgr[0]]
        return list(rgb)

    def inverse(self):
        return color(self.bgr[0], self.bgr[1], self.bgr[2])

    def toPyGameColor(self) -> Color:
        return Color(self.bgr[2], self.bgr[1], self.bgr[0])

    def name(self) -> str:
        rgb = (self.rgb()[0], self.rgb()[1], self.rgb()[2])
        try:
            return webcolors.rgb_to_name(rgb)
        except ValueError:
            return ""

    def __str__(self) -> str:
        rgb = (self.rgb()[0], self.rgb()[1], self.rgb()[2])
        try:
            txt = webcolors.rgb_to_name(rgb)
        except ValueError:
            txt = "Unknown"
        return str(self.rgb) + ' ' + txt


black = color(0, 0, 0)
white = color(255, 255, 255)
brown = color(102, 57, 49)
red = color(255, 0, 0)
green = color(0, 255, 0)
blue = color(0, 0, 255)
magenta = color(255, 0, 255)
#yellow = color(255, 255, 0)
cyan = color(0, 255, 255)
