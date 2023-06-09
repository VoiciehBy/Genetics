from VSprite import VSprite
from constants import screen


class Bullet:
    def __init__(self, bullet_sprite=VSprite, is_moving=False):
        self.bullet_sprite = bullet_sprite
        self.rect = bullet_sprite.get_vsprite_rect()
        self.is_moving = is_moving

    def draw(self):
        self.bullet_sprite.draw()

    def move(self, x: int, y: int):
        if self.is_moving:
            self.bullet_sprite.move(x, y)

    def set_active(self, b=True):
        self.is_moving = b

    def stop(self):
        self.set_active(False)

    def reset(self):
        self.bullet_sprite.set_rect(self.rect)

    def in_motion(self) -> bool:
        return bool(self.is_moving)

    def is_out_off_screen(self) -> bool:
        b: bool = self.bullet_sprite.get_vsprite_rect().left < 0
        b = b or self.bullet_sprite.get_vsprite_rect().left > screen.get_rect().width
        return bool(b)

    def reset_and_stop(self):
        self.reset()
        self.stop()
