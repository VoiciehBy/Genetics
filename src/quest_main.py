from init import init
from pygame_utils import start_pygame_clock, is_two_pygame_rect_intersects
from draw import drawFPSCounter
from Game import Game
from drawScreen import drawTutorialScreen, drawEndingScreens

from handleEvents import handleEvents
from drawHorses import drawHorses

from generate_enemies import generate_enemies

from quest_objects import bullet, set_delta_time, get_delta_time
from quest_horse_player import horse
from pygame import Rect
from constants import screen
from draw import drawPointsCounter

from update import update

from constants import offset


def quest_main():
    init()
    clock = start_pygame_clock()
    enemies = generate_enemies()

    while 1:
        if Game.is_game_paused():
            drawTutorialScreen()

        if Game.is_game_playing():
            handleEvents()
            if bullet.is_out_off_screen():
                bullet.reset_and_stop()

            n = len(enemies)

            if n == 0:
                enemies = generate_enemies()
            for enemy in enemies:
                enemy.move(-(Game.points / 100 + 1) * get_delta_time() / 4, 0)

                if (is_two_pygame_rect_intersects(horse.sprite_rect(), enemy.sprite_rect())):
                    Game.end_game()

                elif (is_two_pygame_rect_intersects(bullet.bullet_sprite.rect, enemy.sprite_rect())):
                    n = len(enemies)
                    if n == 1:
                        enemies.pop(0)
                    else:
                        for i in range(n - 1):
                            if enemies[i] == enemy:
                                enemies.pop(i)
                    bullet.reset_and_stop()
                    Game.addPoint()

            if bullet.in_motion():
                bullet.rect = horse.sprite_rect()
                bullet.rect = Rect(bullet.rect.left, bullet.rect.top + offset, bullet.rect.width, bullet.rect.height)
                bullet.draw()

                if horse.is_looking_right():
                    bullet.move(-get_delta_time(), 0)
                else:
                    bullet.move(get_delta_time(), 0)

            horses = [horse]
            for enemy in enemies:
                horses.append(enemy)
            drawHorses(horses)

            update(screen.get_rect())
        elif Game.is_it_the_end():
            drawEndingScreens()
            break

        delta_time = clock.tick(60)
        drawFPSCounter(clock)
        drawPointsCounter()
        set_delta_time(delta_time)
