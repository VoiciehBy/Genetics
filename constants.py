from color import black, white, brown, red, green, blue, magenta, cyan
from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA

margin_x = 40
margin_y = 80
horse_image_side = 128
windowShape = (1200, 600)
font_size = 16

windowName = "Genetics by VociehBy"

screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

color_black = black.toPyGameColor()
color_white = white.toPyGameColor()
color_brown = brown.toPyGameColor()
color_red = red.toPyGameColor()
color_green = green.toPyGameColor()
color_blue = blue.toPyGameColor()
color_magenta = magenta.toPyGameColor()
#color.yellow = yellow.toPyGameColor()
color_cyan = cyan.toPyGameColor()

clearColor = color_cyan

s_s_m_m = False

# Names: #Koń# Pony #Ferus #Equus #Caballus

if(s_s_m_m):
    default_horse_name = "Miku"
else:
    default_horse_name = "Ferus"


TITLE_THE_INVISIBLE_TXT = "The Invisible"
TITLE_THE_BALD_TXT = "The Bald"
TITLE_THE_STRONG_TXT = "The Strong"
TITLE_THE_WEAK_TXT = "The Weak"
