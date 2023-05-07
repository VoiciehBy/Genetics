from constants import screen
from pygame_utils import drawTutorial, clearScreen
from update import update
from handleEvents import handleEvents


def drawTutorialScreen():
    drawTutorial(screen)
    update(screen.get_rect())

    handleEvents()
    clearScreen()
