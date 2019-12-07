# from unittest import TestCase
# from Code.Hero import Hero
# import pygame
# from pygame.locals import *
#
#
# class TestHero(TestCase):
#
#     def setUp(self):
#         # pygame.init()
#         # self.screen = pygame.display.set_mode((800,600))
#         # hero_fulimg = pygame.image.load(self, "../resources/images/1_char.png").convert_alpha()
#         # hero_rect = Rect(1, 1, 32, 32)
#         # self.hero = Hero(hero_fulimg, hero_rect, 32)
#         # pygame.display.update()
#
#     def test_hero_moving(self):
#         pass
#         # block_group = []
#         # press_keys = pygame.key.get_pressed()
#         # # self.assertEqual(press_keys, K_DOWN)
#         # is_over = Hero.hero_moving(self.hero, self.screen, press_keys, block_group, 800, 600, 26, 32)
#         # self.assertTrue(is_over)
#     #
#     # def test_monster_move(self):
#     #     pass



from unittest import TestCase
from Code import GameMap as GameMapClass
class TestHero(TestCase):
    # the basic class
    gamemap = GameMapClass.GameMap
    def test_0_make_block_group(self):
        blockgroup = self.gamemap.make_block_group(self, "../resources/maps/1_maze.txt", 32)
        # check if there is at least one block
        self.assertIsNotNone(blockgroup[0])  # null blockgroup will fail
        self.assertEqual(blockgroup[0].rect.top,0)  # test there is a block in top left
        self.assertEqual(blockgroup[0].rect.left,0)  # test there is a block in top left