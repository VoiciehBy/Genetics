from pygame import Surface, Color, Rect
from constants import font_size, screen
from constants import TUTORIAL_LINES, ENDING_TXT
from constants import PLAYER_WINS_TXT, AI_WINS_TXT
from constants import YOU_SURVIVED_TXT, YOU_BROUGHT_APOCALYPSE_IN_TXT, GENERATIONS_TXT
from draw import drawPygameRect, drawText
from pygame_utils import clear_screen, wait
from update import update
from handleEvents import handleEvents

from Game import Game
from constants import quest_mode
from constants import QUEST_TUTORIAL_LINES,YOU_GAINED_TXT,POINTS_TXT

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
    color_red: Color = Color("red")
    if quest_mode:
        drawScreen(screen, QUEST_TUTORIAL_LINES, color_red)
    else:
        drawScreen(screen, TUTORIAL_LINES, color_red)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndScreen():
    color_white: Color = Color("white")
    drawScreen(screen, ENDING_TXT, color_white)
    update(screen.get_rect())


def drawResultScreen():
    result = Game.result
    generations = str(Game.breedingCounter) + GENERATIONS_TXT
    color_blue: Color = Color("blue")

    if result:
        txt = [AI_WINS_TXT, '', YOU_SURVIVED_TXT, generations]
    else:
        txt = [PLAYER_WINS_TXT, '', YOU_BROUGHT_APOCALYPSE_IN_TXT, generations]

    drawScreen(screen, txt, color_blue)
    update(screen.get_rect())

def drawResultScreenForQuestMode():
    points = str(Game.points) + ' ' + POINTS_TXT
    color_blue: Color = Color("blue")

    txt = [YOU_GAINED_TXT, points]

    drawScreen(screen, txt, color_blue)
    update(screen.get_rect())

def drawEndingScreens():
    if quest_mode is False:
        wait(2000)
    drawEndScreen()
    wait(2000)
    if quest_mode:
        drawResultScreenForQuestMode()
    else:
        drawResultScreen()
    wait(2000)
