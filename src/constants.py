import json
from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA, Color
from languages_strings import *

default_population_size = 4
default_wild_pop = int(default_population_size / 2)

horse_image_side = 128
margin_x = int(horse_image_side/4)
margin_y = horse_image_side - 48
font_size = int(horse_image_side/8)
default_rect_border_radius = font_size


windowName = "Genetics by VociehBy"
window_width = 1200
window_height = 600
windowShape = (window_width, window_height)
screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

clearColor = Color("cyan")

with open("config.jini", "r", encoding="utf-8") as file:
    config_dict = json.loads(file.read())
    s_s_m_m = config_dict["s_s_m_m"]
    names = config_dict["names"]
    LANGUAGE = config_dict["language"]

if(s_s_m_m):
    default_horse_name = names[4]
else:
    default_horse_name = names[0]

HORSES_JSON_FILE_NAME = "../horses.json"
AI_HORSES_JSON_FILE_NAME = "../ai_horses.json"

if(LANGUAGE == "pl"):
    TITLE_THE_INVISIBLE_TXT = TITLE_THE_INVISIBLE_TXT_PL
    TITLE_THE_BALD_TXT = TITLE_THE_BALD_TXT_PL
    TITLE_THE_STRONG_TXT = TITLE_THE_STRONG_TXT_PL
    TITLE_THE_WEAK_TXT = TITLE_THE_WEAK_TXT_PL

    BLACK_HORSE_TXT = BLACK_HORSE_TXT_PL
    FOUND_TXT = FOUND_TXT_PL
    ENDING_TXT = ENDING_TXT_PL
    TUTORIAL_LINES = TUTORIAL_LINES_PL
else:
    TITLE_THE_INVISIBLE_TXT = TITLE_THE_INVISIBLE_TXT_ENG
    TITLE_THE_BALD_TXT = TITLE_THE_BALD_TXT_ENG
    TITLE_THE_STRONG_TXT = TITLE_THE_STRONG_TXT_ENG
    TITLE_THE_WEAK_TXT = TITLE_THE_WEAK_TXT_ENG

    BLACK_HORSE_TXT = BLACK_HORSE_TXT_ENG
    FOUND_TXT = FOUND_TXT_ENG
    ENDING_TXT = ENDING_TXT_ENG
    TUTORIAL_LINES = TUTORIAL_LINES_ENG
