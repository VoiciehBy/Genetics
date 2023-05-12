from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA, Color

default_population_size = 4
ferus_caballus_pop = int(default_population_size / 2)
margin_x = 32
margin_y = 80
horse_image_side = 128
windowShape = (1200, 600)
font_size = 16
default_rect_border_radius = 20

windowName = "Genetics by VociehBy"

screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

clearColor = Color("cyan")

s_s_m_m = False

names = ["Equus", "Pony", "Ferus", "Caballus"]  # "Koń"

if(s_s_m_m):
    default_horse_name = "Miku"
else:
    default_horse_name = names[0]


TITLE_THE_INVISIBLE_TXT = " The Invisible"
TITLE_THE_BALD_TXT = " The Bald"
TITLE_THE_STRONG_TXT = " The Strong"
TITLE_THE_WEAK_TXT = " The Weak"

BLACK_HORSE_TXT_PL = "Czarny " + names[0] + ' '
FOUND_TXT_PL = " znaleziony"

ENDING_TXT_PL = ["Czarne Konie Apokalipsy...",
                 "doprowadziły do końca świata jakiego znamy...",
                 "KONIEC", "xDddddddd", "FIN"]

TUTORIAL_LINES_PL = ["Krzyżuj konie dowoli...", "Wybór pierwszego rodzica [LPM]",
                     "Wybór drugiego rodzica [RPM]", "Krzyżuj [Spacja]",
                     "Wyświetl ponownie to okno [P]", "Rozpocznij grę/Wznów grę [ENTER]"]

HORSES_JSON_FILE_NAME = "horses.json"
AI_HORSES_JSON_FILE_NAME = "ai_horses.json"
