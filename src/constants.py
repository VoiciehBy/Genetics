import json
import webcolors
from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA, Color, Rect

default_population_size = 4
default_wild_pop = int(default_population_size / 2)
default_chromosome_length = 8
default_goal_evaluation_value = 3

horse_image_side = 128
margin_x = int(horse_image_side/4)
margin_y = horse_image_side
font_size = int(horse_image_side/8)
d_font_size = font_size * 2
default_rect_border_radius = font_size
default_mutation_rate = 0.1


windowName = "Genetics by VociehBy"
window_width = 1366
window_height = 768
turn_counter_rect = Rect(window_width - 3 * d_font_size,
                         window_height - 2 * d_font_size, d_font_size, d_font_size)
windowShape = (window_width, window_height)
screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

clearColor = Color(153, 229, 80)

with open("../config.json", "r", encoding="utf-8") as file:
    config_dict = json.loads(file.read())
    s_s_m_m = config_dict["s_s_m_m"]
    names = config_dict["names"]
    LANGUAGE = config_dict["language"]

debug_mode = False

if s_s_m_m:
    default_horse_name = names[4]
else:
    default_horse_name = names[0]

BACKGROUND_IMAGE_FILE_NAME = "../img/background.png"
HORSE_IMAGE_FILE_NAME = "../img/horse.png"
HORSE_S_S_M_M_FILE_NAME = "../img/horse_s_s_m_m.png"

HORSES_JSON_FILE_NAME = "../data/horses.json"
AI_HORSES_JSON_FILE_NAME = "../data/ai_horses.json"

if LANGUAGE == "pl":
    filename = "../locals_pl.json"
else:
    filename = "../locals_eng.json"
with open(filename, "r", encoding="utf-8") as file:
    locals_dict = json.loads(file.read())
    TITLE_THE_INVISIBLE_TXT = locals_dict["TITLE_THE_INVISIBLE_TXT"]
    TITLE_THE_BALD_TXT = locals_dict["TITLE_THE_BALD_TXT"]
    TITLE_THE_STRONG_TXT = locals_dict["TITLE_THE_STRONG_TXT"]
    TITLE_THE_WEAK_TXT = locals_dict["TITLE_THE_WEAK_TXT"]
    FITNESS_TXT = locals_dict["FITNESS_TXT"]

    TURN_TXT = locals_dict["TURN_TXT"]

    BLACK_HORSE_TXT = locals_dict["BLACK_HORSE_TXT"]
    FOUND_TXT = locals_dict["FOUND_TXT"]
    ENDING_TXT = locals_dict["ENDING_TXT"]
    TUTORIAL_LINES = locals_dict["TUTORIAL_LINES"]
    PLAYER_WINS_TXT = locals_dict["PLAYER_WINS_TXT"]
    AI_WINS_TXT = locals_dict["AI_WINS_TXT"]
    YOU_BROUGHT_APOCALYPSE_IN_TXT = locals_dict["YOU_BROUGHT_APOCALYPSE_IN_TXT"]
    YOU_SURVIVED_TXT = locals_dict["YOU_SURVIVED_TXT"]
    GENERATIONS_TXT = locals_dict["GENERATIONS_TXT"]

COLORS = dict(webcolors.HTML4_HEX_TO_NAMES)
COLORS.update(webcolors.CSS3_HEX_TO_NAMES)
