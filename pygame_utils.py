from pygame import draw, font, Rect, mouse
from constants import font_size, default_rect_border_radius


def drawPygameRect(surface, color, rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface, image, rect):
    surface.blit(image, rect)


def drawText(surface, text, rect):
    txt = font.Font(None, font_size)
    txtSurface = txt.render(text, False, (0, 0, 0))
    surface.blit(txtSurface, rect)


def mvPygameRect(rect, x, y) -> Rect:
    return rect.move(x, y)


def checkIfMouseOverRect(object):
    mousePosition = mouse.get_pos()
    return object.sprite_rect().collidepoint(mousePosition)
