from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA, Color

default_population_size = 4
default_wild_pop = int(default_population_size / 2)

horse_image_side = 128

margin_x = int(horse_image_side/4)
margin_y = horse_image_side - 48

font_size = int(horse_image_side/8)

default_rect_border_radius = font_size

windowShape = (1200, 600)

windowName = "Genetics by VociehBy"

screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

clearColor = Color("cyan")

s_s_m_m = False

names = ["Equus", "Pony", "Ferus", "Caballus", "Miku"]  # "Koń"

if(s_s_m_m):
    default_horse_name = names[4]
else:
    default_horse_name = names[0]

TITLE_THE_INVISIBLE_TXT_ENG = " The Invisible"
TITLE_THE_BALD_TXT_ENG = " The Bald"
TITLE_THE_STRONG_TXT_ENG = " The Strong"
TITLE_THE_WEAK_TXT_ENG = " The Weak"

BLACK_HORSE_TXT_ENG = "Black Horse" + ' '
FOUND_TXT_ENG = " found"

ENDING_TXT_ENG = ["Black Horses of Apocalypse...",
                  "ended the world that we used to know...",
                  "THE END", "xDddddddd", "FIN"]

TUTORIAL_LINES_ENG = ["Breed horses at your own pace...", "Choose first breeding mate [LMB]",
                      "Choose second breeding mate [RMB]", "Init Breeding [Space]",
                      "Display this window again [P]", "Start/Resume Game [ENTER]"]


TITLE_THE_INVISIBLE_TXT_PL = " Niewidzialny"
TITLE_THE_BALD_TXT_PL = " Łysy"
TITLE_THE_STRONG_TXT_PL = " Silny"
TITLE_THE_WEAK_TXT_PL = " Słaby"

BLACK_HORSE_TXT_PL = "Czarny " + names[0] + ' '
FOUND_TXT_PL = " znaleziony"

ENDING_TXT_PL = ["Czarne Konie Apokalipsy...",
                 "doprowadziły do końca świata jakiego znamy...",
                 "KONIEC", "xDddddddd", "FIN"]

TUTORIAL_LINES_PL = ["Krzyżuj konie dowoli...", "Wybór pierwszego rodzica [LPM]",
                     "Wybór drugiego rodzica [RPM]", "Krzyżuj [Spacja]",
                     "Wyświetl ponownie to okno [P]", "Rozpocznij grę/Wznów grę [ENTER]"]

HORSES_JSON_FILE_NAME = "../horses.json"
AI_HORSES_JSON_FILE_NAME = "../ai_horses.json"
