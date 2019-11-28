import pygame

"""
GameMap should include(Version 1)
1.making block group for Hero and monsters to move
2.Map drawing
"""

# consist of all the block rect based on the 1_maze.txt
BLOCK_GROUP = []
# each tile size
TILE_SIZE = 32


# block class used to create array of rectangles for walls
class Block:
    def __init__(self, rect):
        self.rect = rect


class GameMap():
    def __init__(self, game_map_img, map_x, map_y):
        """
        :param game_map_img: map img
        :param map_x: map position x
        :param map_y: map position y
        """
        self.game_map_img = game_map_img
        self.map_x = map_x
        self.map_y = map_y

    def draw_map(self, screen):
        screen.blit(self.game_map_img, (self.map_x, self.map_y))

    # global block_group list is for Hero and monsters movement used in their own .py files
    def make_block_group(self, maze_map_file):
        """
        label the block position in block_group list
        """
        global BLOCK_GROUP
        BLOCK_GROUP.clear()

        # read the 1_maze.txt into lines as list
        with open(maze_map_file, 'r') as f:
            maze_lines = f.read().splitlines()

        # getting length of list
        num_lines = len(maze_lines)

        # assume all line lengths are the same as top line(columns)
        maze_map_width = len(maze_lines[0])
        maze_map_height = num_lines

        # based on the list, label the blocks in block_group list
        for i in range(maze_map_height):
            for j in range(maze_map_width):
                if maze_lines[i][j] == str(1):
                    block = Block(pygame.Rect(TILE_SIZE * j, TILE_SIZE * i, TILE_SIZE, TILE_SIZE))
                    BLOCK_GROUP.append(block)
