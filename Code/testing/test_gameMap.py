from unittest import TestCase

from Code import GameMap as GameMapClass


class TestGameMap(TestCase):
    # the basic class
    gamemap = GameMapClass.GameMap
    def test_0_make_block_group(self):
        blockgroup = self.gamemap.make_block_group(self,"../resources/maps/1_maze.txt", 32)
        # check if there is at least one block
        self.assertIsNotNone(blockgroup[0])  # null blockgroup will fail
        self.assertEqual(blockgroup[0].rect.top,0)  # test there is a block in top left
        self.assertEqual(blockgroup[0].rect.left,0)  # test there is a block in top left
