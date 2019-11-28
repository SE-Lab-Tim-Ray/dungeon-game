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
        self.hero_speed = 4
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


    def monster_move(self, screen, hero_rect, block_group, move_rat):
        """
        use the hero_rect for hero. self.hero_rect refers to the monster
        """
        isCaught = False

        # hero conflict with monster
        # if hero_rect.right >= self.hero_rect.left and hero_rect.right:
        #     isCaught = True


        # decide which direction to move in
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        x_offset = self.hero_rect.left - hero_rect.left
        y_offset = self.hero_rect.top - hero_rect.top
        # print(x_offset)

        if x_offset > 0:
            move_left = True
        if x_offset < 0:
            move_right = True

        print("y_offset: ", y_offset)
        # move either up or down
        if y_offset > 0:
            move_up = True
        if y_offset < 0:
            move_down = True

        # MOVING LEFT
        if move_rat and move_left:
            #  was sel.hero_speed
            self.hero_rect.left -= 1
            # window conflict with monster/hero
            if self.hero_rect.left <= 0:
                self.hero_rect.left = 0

            # conflict with block
            for n in range(len(block_group)):  # block_group list is all block
                # hero and block conflict
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    #
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        self.hero_rect.left += 1  # if so, undo the move
        # MOVING RIGHT
        if move_rat and move_right:
            self.hero_rect.left += 1
            # window conflict with hero
            if self.hero_rect.right >= SCREEN_SIZE[0]:
                self.hero_rect.right = SCREEN_SIZE[0]
            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        self.hero_rect.left -= 1  # if so, undo the move
        # MOVIN UP
        if move_rat and move_up:
            self.hero_rect.top -= 1
            if self.hero_rect.top <= 0:
                self.hero_rect.top = 0
            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.bottom > block_group[n].rect.bottom > self.hero_rect.top:
                            self.hero_rect.top += 1  # if so, undo the move
        #
        # Movin DOWN
        if move_rat and move_down:
            self.hero_rect.top += 1
            if self.hero_rect.bottom >= SCREEN_SIZE[1]:
                self.hero_rect.bottom = SCREEN_SIZE[1]
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                            self.hero_rect.top -= 1 # if so, undo the move
        screen.blit(self.hero_img[0], self.hero_rect)
        return isCaught

