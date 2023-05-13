from GColor import GColor
from constants import clearColor
from constants import TITLE_THE_INVISIBLE_TXT_ENG, TITLE_THE_BALD_TXT_ENG, TITLE_THE_STRONG_TXT_ENG, TITLE_THE_WEAK_TXT_ENG


def surname(color: GColor) -> str:
    result = color.name()
    if(result):
        return str(color.name()).capitalize()
    else:
        return ''


def strong_weak(fitness: int) -> str:
    if(fitness >= 5):
        return str(TITLE_THE_STRONG_TXT_ENG)
    elif(fitness <= 2):
        return str(TITLE_THE_WEAK_TXT_ENG)
    else:
        return str('')


def invisible_bald(coat_color: GColor) -> str:
    mane_color = coat_color.inverse().to_pygame_color()
    coat_color = coat_color.to_pygame_color()
    if(clearColor == coat_color):
        return str(TITLE_THE_INVISIBLE_TXT_ENG)
    elif(clearColor == mane_color):
        return str(TITLE_THE_BALD_TXT_ENG)
    else:
        return str('')
