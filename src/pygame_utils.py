from pygame import draw, font, Surface, Color, Rect, mouse, transform, time
from constants import screen, clearColor, font_size, default_rect_border_radius


def clear_screen():
    screen.fill(clearColor)


def drawPygameRect(surface: Surface, color: Color, rect: Rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface: Surface, image: Surface, rect: Rect):
    surface.blit(image, rect)


def drawText(surface: Surface, text: str, rect: Rect, text_font_size=font_size):
    txt = font.Font(None, text_font_size)
    txt_surface = txt.render(text, False, (0, 0, 0))
    surface.blit(txt_surface, rect)


def move_pygame_rect(rect: Rect, x: int, y: int) -> Rect:
    return rect.move(x, y)


def is_mouse_over_rect(g_object) -> bool:
    mouse_position = mouse.get_pos()
    rect_to_check = g_object.sprite_rect()
    result = rect_to_check.collidepoint(mouse_position)
    return result


def flip_surface(surface: Surface, horizontally: bool, vertically: bool) -> Surface:
    return transform.flip(surface, horizontally, vertically)


def flip_surface_horizontally(surface: Surface) -> Surface:
    return flip_surface(surface, True, False)


def flip_surface_vertically(surface: Surface) -> Surface:
    return flip_surface(surface, False, True)


def wait(milliseconds: int):
    time.wait(milliseconds)


def start_pygame_clock():
    return time.Clock()
