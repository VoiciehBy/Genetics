from pygame import draw, font, Rect, mouse, transform, Surface, time
from constants import screen, clearColor, font_size, default_rect_border_radius, TUTORIAL_LINES_PL, ENDING_TXT_PL
from pygame_colors import color_red,color_white

def clearScreen():
    screen.fill(clearColor)


def drawPygameRect(surface: Surface, color, rect: Rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface: Surface, image: Surface, rect: Rect):
    surface.blit(image, rect)


def drawText(surface: Surface, text: str, rect: Rect, text_font_size=font_size):
    txt = font.Font(None, text_font_size)
    txt_surface = txt.render(text, False, (0, 0, 0))
    surface.blit(txt_surface, rect)


def drawTutorial(surface: Surface):
    surface_rect = Rect(surface.get_rect())

    rect = Rect(10, 10, surface_rect.width - 20, surface_rect.height - 20)
    drawPygameRect(surface, color_red, rect)

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

def drawEnd(surface: Surface):
    surface_rect = Rect(surface.get_rect())

    rect = Rect(10, 10, surface_rect.width - 20, surface_rect.height - 20)
    drawPygameRect(surface, color_white, rect)

    left = int(rect.width / 4)
    top = int(rect.height / 8)
    width = int(rect.width / 4)
    height = int(rect.height / 8)

    rect = Rect(left, top, width, height)

    lines = ENDING_TXT_PL

    n = len(lines)
    for i in range(n):
        r_rect = Rect(rect.left, rect.top + 2 * i *
                      font_size * 3, rect.width, rect.height)
        drawText(surface, lines[i], r_rect, font_size * 3)

def mvPygameRect(rect: Rect, x: int, y: int) -> Rect:
    return rect.move(x, y)


def checkIfMouseOverRect(g_object):
    mouse_position = mouse.get_pos()
    return g_object.sprite_rect().collidepoint(mouse_position)


def flipSurface(surface: Surface, horizontally: bool, vertically: bool) -> Surface:
    return transform.flip(surface, horizontally, vertically)


def flipSurfaceHorizontally(surface: Surface) -> Surface:
    return flipSurface(surface, True, False)


def flipSurfaceVertically(surface: Surface) -> Surface:
    return flipSurface(surface, False, True)


def wait(milliseconds: int):
    time.wait(milliseconds)
