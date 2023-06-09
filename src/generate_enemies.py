from constants import screen, horse_image_side
from pygame import Rect
from g_horse_utils import generate_horse
from generate_horse_population_for_quest_mode import generate_horse_population
from quest_horse_player import horse

def generate_enemies():
    individuals = generate_horse_population()
    n = len(individuals)
    enemies = []
    for i in range(n):
        rect = Rect(screen.get_rect().width + i*horse_image_side, horse.sprite_rect().top, horse_image_side, horse_image_side),
        enemy = generate_horse(individuals[i], rect)
        enemy.flip()
        enemies.append(enemy)
    return enemies