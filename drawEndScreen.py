from constants import screen
from pygame_utils import drawEnd, clearScreen
from update import update
from handleEvents import handleEvents


def drawEndScreen():
    drawEnd(screen)
    update(screen.get_rect())

    handleEvents()
    clearScreen()
