from constants import screen
from pygame_utils import drawTutorial, drawEnd, clearScreen
from update import update
from handleEvents import handleEvents


def drawTutorialScreen():
    drawTutorial(screen)
    update(screen.get_rect())

    handleEvents()
    clearScreen()


def drawEndScreen():
    drawEnd(screen)
    update(screen.get_rect())

    handleEvents()
    clearScreen()
