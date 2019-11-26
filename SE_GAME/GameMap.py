import pygame
from pygame.locals import *

block_group = []
TILE_SIZE = 32

class Array2D:
    """
    two dimension list for maze file
    """

    def __init__(self, w, h, default=0):
        self.w = w
        self.h = h
        self.data = [[y for y in range(h)] for x in range(w)]

    def show_array2d(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end='')
            # print("")

    def __getitem__(self, item):
        return self.data[item]

# block class used to create array of rectangles for walls
class Block:
    def __init__(self, rect):  # TC remove image
        # self.img = img # TC remove image
        self.rect = rect

class GameMap(Array2D):
    """
    create map
    """

    def __init__(self, game_map_img, x, y):
        w = int(game_map_img.get_width() / 32) + 1
        h = int(game_map_img.get_height() / 32) + 1

        super().__init__(w, h)
        self.map_width = game_map_img.get_width()
        self.map_height = game_map_img.get_height()
        self.game_map_img = game_map_img
        # self.screen_width = screen_width
        # self.screen_height = screen_height
        self.x = x
        self.y = y


    def draw_map(self, screen):
        # This is draw the whole map as a png
        screen.blit(self.game_map_img, (self.x, self.y))

    # roll the map(partial view)
    def map_roll(self, role_x, role_y):
        pass

    def load_walk_file(self, path):
        """
        read the maze file
        output the 0101 list
        """
        self.make_block_group(path)


    def make_block_group(self, maze_map_file):
        """
        mark the block position in block_group list
        :return: block_group list
        """
        global block_group
        # initialise list
        block_group.clear()

        # read file
        with open(maze_map_file, 'r') as f:
            mazelines = f.read().splitlines()

        # getting length of list
        num_lines = len(mazelines)

        # assume all line lengths are the same as top line
        maze_map_width = len(mazelines[0])
        maze_map_height = num_lines

        # load maze map
        for i in range(maze_map_height):  #
            for j in range(maze_map_width):  #
                if mazelines[i][j] == str(1):
                    block = Block(pygame.Rect(TILE_SIZE * j, TILE_SIZE * i, TILE_SIZE, TILE_SIZE))
                    block_group.append(block)  # append block into block group

        # create winning square bottom right
        # block_final = Block(pygame.Rect((maze_map_width * TILE_SIZE) - TILE_SIZE, (maze_map_height * TILE_SIZE) - TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # add wining square to group
        # block_group.append(block_final)