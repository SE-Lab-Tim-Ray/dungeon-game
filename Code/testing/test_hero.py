from unittest import TestCase
import pygame


from Code.Hero import *

class TestHero(TestCase):
    def test_hero(self):
        self.hero_fulimg = pygame.image.load("../resources/images/1_char.png").convert_alpha()
        self.assertIsNone(self.hero_fulimg) # load img successfully
        self.hero_rect = Rect(32, 32, 32, 32)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, 32)
        self.assertIsInstance(self.hero, Hero)  # hero instantiate successfully



