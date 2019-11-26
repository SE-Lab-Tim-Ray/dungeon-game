import pygame
from pygame.locals import *
from GameMap import *


tile_width = 32
tile_height = 32

isOver = False
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN_SIZE = (800, 600)
TILE_SIZE = 32


class Sprite:
    """
    used to draw sprites
    """

    @staticmethod
    def draw(screen, source, x, y, cell_x, cell_y, cell_w=32, cell_h=32):
        """
        :param dest: surface,
        :param source: surface,
        :param x: coordination in screen
        :param y: coordination in screen
        :param cell_x: coordination in sprite img
        :param cell_y: coordination in sprite img
        :param cell_w: single sprite width
        :param cell_h: single sprite height
        :return:
        """
        screen.blit(source, (x, y), (cell_x * cell_w, cell_y * cell_h, cell_w, cell_h))


class Hero:
    def __init__(self, hero_fulimg, hero_rect, mx, my):
        self.hero_fulimg = hero_fulimg
        self.hero_img = [self.hero_fulimg.subsurface(Rect((0, 0), (TILE_SIZE, TILE_SIZE)))]
        self.mx = mx
        self.my = my
        self.hero_coordinate_x = mx*32
        self.hero_coordinate_y = my*32
        self.hero_speed = 2
        self.hero_rect = hero_rect
        # data = GameMap.load_walk_file('./resources/maps/maze1.txt')
        # make_block_group(data)



    def draw_hero(self, screen, map_x=0, map_y=0):
        cell_x = 0
        cell_y = 0
        Sprite.draw(screen, self.hero_img, map_x + self.hero_coordinate_x, map_y + self.hero_coordinate_y, cell_x, cell_y)

    def hero_moving(self, screen, press_keys, block_group):
        """
        use the block_group created by GameMap.py
        :param press_keys:
        :return:
        """
        global isOver
        # key press
        if press_keys[K_ESCAPE]:
            exit()
        # key press
        if press_keys[K_LEFT]:
            self.hero_rect.left -= self.hero_speed
            # window conflict with hero
            if self.hero_rect.left <= 0:
                self.hero_rect.left = 0
            # conflict with block
            for n in range(len(block_group)):  # block_group list is all block, last one is end block
                # hero and block conflict
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        if n == len(block_group) - 26:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.hero_rect.left += self.hero_speed  # if so, undo the move

        if press_keys[K_RIGHT]:
            self.hero_rect.left += self.hero_speed  # make the move
            if self.hero_rect.right >= SCREEN_SIZE[0]:
                self.hero_rect.right = SCREEN_SIZE[0]
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        if n == len(block_group) - 26:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.hero_rect.left -= self.hero_speed  # if so, undo the move

        if press_keys[K_UP]:

            self.hero_rect.top -= self.hero_speed
            if self.hero_rect.top <= 0:
                self.hero_rect.top = 0
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.bottom > block_group[n].rect.bottom > self.hero_rect.top:
                        if n == len(block_group) - 26:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.hero_rect.top += self.hero_speed  # if so, undo the move

        if press_keys[K_DOWN]:
            self.hero_rect.top += self.hero_speed
            if self.hero_rect.bottom <= 0:
                self.hero_rect.bottom = 0
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                        if n == len(block_group) - 26:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.hero_rect.top -= self.hero_speed  # if so, undo the move
        screen.blit(self.hero_img[0], self.hero_rect)
        return isOver