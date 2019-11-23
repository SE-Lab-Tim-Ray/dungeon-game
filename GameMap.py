import pygame
from pygame.locals import *

data_list = []
block_group = []

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
        # read file of the map
        with open("./resources/maps/maze1.txt", "r") as map_file:
            mazelines = map_file.read().splitlines()

        num_lines = len(mazelines)
        # assume all line lengths are the same as top line
        maze_pattern_width = len(mazelines[0])
        maze_pattern_height = num_lines
        # work out tile width and height
        tile_width = 800 // maze_pattern_width
        tile_height = 600 // maze_pattern_height
        # load bitmaps, change the tile size flexibly
        tile = pygame.image.load("./resources/images/plain_tile.png").convert_alpha()
        tile = pygame.transform.scale(tile, (tile_width, tile_height))
        current_x = 0
        current_y = 0

        for i in range(num_lines):
            len_j = len(mazelines[i])
            this_line = mazelines[i]
            for j in range(len_j):
                if this_line[j] == "1":
                    screen.blit(tile, (current_x, current_y))

                current_x += tile_width
            current_y += tile_height
            current_x = 0

        # This is draw the whole map as a png
        # screen.blit(self.game_map_img, (self.x, self.y))

    # roll the map(partial view)
    def map_roll(self, role_x, role_y):
        pass

    def load_walk_file(self, path):
        """
        read the maze file
        """
        with open(path, 'r') as file:
            for x in range(self.w):
                for y in range(self.h):
                    pass
        self.make_block_group()
        # print(data_list)
        # return data_list

    def make_block_group(self):
        """
        mark the block position
        :return:
        """
        pass