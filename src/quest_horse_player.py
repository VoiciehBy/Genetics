from generate_ai_genetic_population import generate_ai_genetic_population
from g_horse_utils import get_horse_image
from pygame import Rect, Color
from VSprite import VSprite
from GHorse import GHorse


genes = generate_ai_genetic_population()[0].genes()
horse_image = get_horse_image()
rect = Rect(0, 0, 128, 128)
blue = Color("blue")
sprite = VSprite(blue, rect, horse_image)
horse: GHorse = GHorse("Koń", genes, sprite, False, False)
