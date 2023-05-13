from pygame import Surface, Color, Rect
from constants import font_size, screen, TUTORIAL_LINES_ENG, ENDING_TXT_ENG
from pygame_colors import color_red, color_white
from pygame_utils import drawPygameRect, drawText, clear_screen
from update import update
from handleEvents import handleEvents


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
                      font_size * 3, rect.width, rect.height)
        drawText(surface, lines[i], r_rect, font_size * 3)


def drawTutorialScreen():
    drawScreen(screen, TUTORIAL_LINES_ENG, color_red)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndScreen():
    drawScreen(screen, ENDING_TXT_ENG, color_white)
    update(screen.get_rect())

    handleEvents()
    clear_screen()
