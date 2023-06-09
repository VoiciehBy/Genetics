from utils import make_data_directory
from g_logging import start_json_files, end_json_files
from init import init
from constants import default_population_size, default_wild_pop, quest_mode, offset, screen
from pygame_utils import start_pygame_clock, is_two_pygame_rect_intersects, wait
from generate_four_populations import generate_four_populations
from g_horse_utils import get_horse_parents
from generate_enemies import generate_enemies
from Game import Game
from drawScreen import drawTutorialScreen, drawEndingScreens
from handleEvents import handleEvents
from quest_objects import bullet, set_delta_time, get_delta_time, horse
from pygame import Rect
from drawHorses import drawHorses
from update import update
from GHorse import GHorse
from draw import drawParents, drawFPSCounter, drawPointsCounter, drawTurnCounter, drawParentsNumbers

def main():
    make_data_directory()
    start_json_files()
    init()

    n_n = 2 * default_population_size + 2 * default_wild_pop
    clock = start_pygame_clock()

    horses = generate_four_populations()
    horses_parents = get_horse_parents()

    enemies = generate_enemies()

    while 1:
        if Game.is_game_paused():
            drawTutorialScreen()
        elif Game.is_game_playing():
            if quest_mode:
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
                    bullet.rect = Rect(bullet.rect.left, bullet.rect.top + offset, bullet.rect.width,
                                       bullet.rect.height)
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
            else:
                current_horse: GHorse = handleEvents(horses, n=n_n)
                drawHorses(horses)

                if current_horse:
                    horses_parents = get_horse_parents()
                    current_horse.set_sprite_color_white_using_pygame_color()

                drawParents(horses_parents)
        elif Game.is_in_breeding_state():
            horses = generate_four_populations()
            horses_parents = get_horse_parents()
            drawParents(horses_parents)

            Game.stop_breeding_state()

        elif Game.is_it_the_end():
            if quest_mode is False:
                wait(500)

                horses = generate_four_populations()
                drawHorses(horses)

                horses_parents = get_horse_parents()
                drawParents(horses_parents)

            drawEndingScreens()
            end_json_files()
            break
        delta_time = clock.tick(60)
        drawFPSCounter(clock)
        if quest_mode:
            drawPointsCounter()
            set_delta_time(delta_time)
        else:
            drawTurnCounter()
            drawParentsNumbers(horses_parents)
main()