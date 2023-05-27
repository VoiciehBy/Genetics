from pygame import Surface, Color, Rect
from constants import font_size, screen
from constants import TUTORIAL_LINES, ENDING_TXT
from constants import PLAYER_WINS_TXT, AI_WINS_TXT
from constants import YOU_SURVIVED_TXT, YOU_BROUGHT_APOCALYPSE_IN_TXT, GENERATIONS_TXT
from pygame_colors import color_red, color_white, color_blue
from draw import drawPygameRect, drawText
from pygame_utils import clear_screen, wait
from update import update
from handleEvents import handleEvents

from Game import Game


def drawScreen(surface: Surface, lines, color: Color):
    surface_rect = Rect(surface.get_rect())

    rect = Rect(10, 10, surface_rect.width - 20, surface_rect.height - 20)
    drawPygameRect(surface, color, rect)

    left = int(rect.width / 4)
    top = int(rect.height / 8)
    width = int(rect.width / 4)
    height = int(rect.height / 8)

    rect = Rect(left, top, width, height)
    n = len(lines)
    for i in range(n):
        r_rect = Rect(rect.left, rect.top + 2 * i *
                      font_size * 2, rect.width, rect.height)
        drawText(surface, lines[i], r_rect, font_size * 2)


def drawTutorialScreen():
    drawScreen(screen, TUTORIAL_LINES, color_red)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndScreen():
    drawScreen(screen, ENDING_TXT, color_white)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawResultScreen():
    result = Game.result

    generations = str(Game.breedingCounter) + GENERATIONS_TXT
    txt = []

    if result:
        txt.append(AI_WINS_TXT)
        txt.append('')
        txt.append(YOU_SURVIVED_TXT)
        txt.append(generations)
    else:
        txt.append(PLAYER_WINS_TXT)
        txt.append('')
        txt.append(YOU_BROUGHT_APOCALYPSE_IN_TXT)
        txt.append(generations)

    drawScreen(screen, txt, color_blue)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndingScreens():
    wait(2000)
    drawEndScreen()
    wait(2000)
    drawResultScreen()
    wait(2000)
