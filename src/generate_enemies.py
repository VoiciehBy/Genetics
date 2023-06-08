from constants import screen, horse_image_side
from pygame import Surface,Color,Rect
from pygame import image

side = 128
from constants import s_s_m_m
from GColor import GColor

from G_Individual import G_Individual
from numpy import array
from G_Horse import G_Horse
from VSprite import VSprite

from generateHorsePopulation import generate_horse_population
from quest_horse_player import horse

color_black = Color("black")
color_white = Color("white")
color_brown = Color(102, 57, 49)
color_red = Color("red")
color_green = Color("green")
color_blue = Color("blue")
color_cyan = Color("cyan")

def get_horse_image() -> Surface:
    return image.load("../img/horse.png")


def generate_horse_image_for_pygame(individual: G_Individual) -> array:
    horse_image: Surface = get_horse_image()
    individual_color: Color = Color(individual.color_trait().to_pygame_color())
    inverted_individual_g_color: GColor = individual.color_trait().inverse()
    inverted_individual_color: Color = Color(inverted_individual_g_color.to_pygame_color())
    the_color: Color = Color(inverted_individual_color - individual_color)

    for i in range(side):
        for j in range(side):
            horse_color: Color = Color(horse_image.get_at((i, j)))
            if horse_color == color_white:
                if s_s_m_m:
                    horse_image.set_at((i, j), individual_color)
                else:
                    horse_image.set_at((i, j), inverted_individual_color)
            elif(s_s_m_m is False and horse_color == color_brown):
                horse_image.set_at((i, j), individual_color)
            elif(s_s_m_m and horse_color == color_cyan):
                horse_image.set_at((i, j), inverted_individual_color)
            elif horse_color == color_red:
                horse_image.set_at((i, j), color_black)
            elif(s_s_m_m and horse_color == color_green):
                horse_image.set_at((i, j), color_red)
            elif horse_color == color_blue:
                horse_image.set_at((i, j), the_color)
    return horse_image


def generate_horse(individual: G_Individual, rect: Rect) -> G_Horse:
    horse_image = generate_horse_image_for_pygame(individual)
    s = VSprite(Color("white"), rect, horse_image)
    return G_Horse(genetics=individual, g_sprite=s)

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