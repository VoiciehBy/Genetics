from pygame.display import set_mode
from pygame import DOUBLEBUF, SRCALPHA, Color

default_population_size = 4
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

names = ["Koń", "Pony", "Ferus", "Equus", "Caballus"]

if(s_s_m_m):
    default_horse_name = "Miku"
else:
    default_horse_name = names[2]


TITLE_THE_INVISIBLE_TXT = "The Invisible"
TITLE_THE_BALD_TXT = "The Bald"
TITLE_THE_STRONG_TXT = "The Strong"
TITLE_THE_WEAK_TXT = "The Weak"

TUTORIAL_LINES_PL = ["Krzyżuj konie dowoli...", "Wybór pierwszego rodzica [LPM]",
                     "Wybór drugiego rodzica [RPM]", "Krzyżuj [Spacja]",
                     "Wyświetl ponownie to okno [P]", "Rozpocznij grę/Wznów grę [ENTER]"]
