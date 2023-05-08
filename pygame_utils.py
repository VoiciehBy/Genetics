from pygame import draw, font, Rect, mouse, transform, Surface
from constants import screen, clearColor, font_size, default_rect_border_radius, TUTORIAL_LINES_PL


def clearScreen():
    screen.fill(clearColor)


def drawPygameRect(surface, color, rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface, image, rect):
    surface.blit(image, rect)


def drawText(surface, text, rect, text_font_size=font_size):
    txt = font.Font(None, text_font_size)
    txtSurface = txt.render(text, False, (0, 0, 0))
    surface.blit(txtSurface, rect)


def drawTutorial(surface):
    surfaceRect = surface.get_rect()

    rect = Rect(10, 10,
                surfaceRect.width - 20, surfaceRect.height - 20)
    drawPygameRect(surface, (255, 0, 0), rect)

    left = int(rect.width/4)
    top = int(rect.height/8)
    width = int(rect.width/4)
    height = int(rect.height/8)

    rect = Rect(left, top, width, height)

    lines = TUTORIAL_LINES_PL

    n = len(lines)
    for i in range(n):
        r_rect = Rect(rect.left, rect.top + 2*i *
                      font_size*3, rect.width, rect.height)
        drawText(surface, lines[i], r_rect, font_size*3)


def mvPygameRect(rect, x, y) -> Rect:
    return rect.move(x, y)


def checkIfMouseOverRect(g_object):
    mousePosition = mouse.get_pos()
    return g_object.sprite_rect().collidepoint(mousePosition)


def flipSurface(surface, horizontally, vertically) -> Surface:
    return transform.flip(surface, horizontally, vertically)


def flipSurfaceHorizontally(surface) -> Surface:
    return flipSurface(surface, True, False)


def flipSurfaceVertically(surface) -> Surface:
    return flipSurface(surface, False, True)
