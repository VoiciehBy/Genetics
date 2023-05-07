from constants import screen
from pygame_utils import drawTutorial
from update import update
from handleEvents import handleEvents
from clearScreen import clearScreen

def drawTutorialScreen():
    drawTutorial(screen)
    update(screen.get_rect())

    handleEvents()
    clearScreen()