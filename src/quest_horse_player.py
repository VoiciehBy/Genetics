from generate_horse_population_for_quest_mode import generate_horse_population
from g_horse_utils import get_horse_image
from pygame import Rect, Color
from VSprite import VSprite
from GHorse import GHorse


genes = generate_horse_population()[0].genes()
horse_image = get_horse_image()
rect = Rect(0, 0, 128, 128)
sprite = VSprite(Color("blue"), rect, horse_image)
horse: GHorse = GHorse("Koń", genes, sprite, False, False)
