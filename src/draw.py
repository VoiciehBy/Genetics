from Game import Game
from constants import screen, turn_counter_rect, d_font_size, default_rect_border_radius, font_size
from pygame import Surface, Color, Rect, draw, font


def drawTurnCounter():
    turn_str = "T: " + str(Game.breedingCounter)
    drawText(screen, turn_str, turn_counter_rect, d_font_size)


def drawFPSCounter(clock):
    drawText(screen, str(int(clock.get_fps())), screen.get_rect())


def drawUIParentsTxt(rect, n=1):
    _str = "P#" + str(n)
    rect = Rect(rect.left, rect.top, rect.width, rect.height)
    drawText(screen, _str, rect, d_font_size*2)


def drawPygameRect(surface: Surface, color: Color, rect: Rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface: Surface, image: Surface, rect: Rect):
    surface.blit(image, rect)


def drawText(surface: Surface, text: str, rect: Rect, text_font_size=font_size):
    txt = font.Font(None, text_font_size)
    txt_surface = txt.render(text, False, (0, 0, 0))
    surface.blit(txt_surface, rect)


def drawParents(horse_parents):
    for horse in horse_parents:
        horse.draw()
