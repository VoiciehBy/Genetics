from constants import screen
from pygame_utils import drawTutorial, drawEnd, clear_screen
from update import update
from handleEvents import handleEvents


def drawTutorialScreen():
    drawTutorial(screen)
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndScreen():
    drawEnd(screen)
    update(screen.get_rect())

    handleEvents()
    clear_screen()
