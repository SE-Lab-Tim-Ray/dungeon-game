from unittest import TestCase
from GameMap import *
from RunGameMap import *  # for the constants that define the
import pygame

"""
 Test for the create map map function creates the block group correctly. Very specific to the current maze1
 This will need extra cases when we change this from a constant to a variable
"""
class TestCreate_maze_map(TestCase):
    def test_create_maze_map(self):

        # create the block group using the constants in RunGameMap
        block_group = create_maze_map(MAZE_MAP_FILE, TILE_SIZE, pygame)

        # test that the first block left is at 0
        rect_left_pos = block_group[0].rect.left
        self.assertEqual(rect_left_pos, 0)

        # test that the first block top is at 0
        rect_top_pos = block_group[0].rect.top
        self.assertEqual(rect_top_pos, 0)

        # # test that the last block left is at 768 - this is the win block
        print(len(block_group))
        rect_left_pos = block_group[len(block_group)-1].rect.left
        self.assertEqual(rect_left_pos, 768)

        # test that the last block top is at 544 - this is the win block
        rect_top_pos = block_group[len(block_group)-1].rect.top
        self.assertEqual(rect_top_pos, 544)

