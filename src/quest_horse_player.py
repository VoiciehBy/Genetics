from pygame.image import load as image_load
from pygame import Rect, Color

from VSprite import VSprite

from G_Horse import G_Horse

from generateHorsePopulation import generate_horse_population

genes = generate_horse_population()[0].genes()

horse_image = image_load("../img/horse.png")
rect = Rect(0, 0, 128, 128)

sprite = VSprite(Color("blue"), rect, horse_image)
horse: G_Horse = G_Horse("Koń", genes, sprite, False, False)
