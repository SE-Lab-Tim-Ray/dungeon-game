from GameMap import *
from pygame.locals import *

ISOVER = False
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN_SIZE = (800, 600)
TILE_SIZE = 32
WIN_BLOCK_FROM_END = 26


class Hero:
    def __init__(self, hero_fulimg, hero_rect, mx, my):
        # the full sprite img of hero
        self.hero_fulimg = hero_fulimg
        # single sprite img of hero
        self.hero_img = [self.hero_fulimg.subsurface(Rect((0, 0), (TILE_SIZE, TILE_SIZE)))]
        self.hero_rect = hero_rect
        self.mx = mx
        self.my = my
        self.hero_coordinate_x = mx * 32
        self.hero_coordinate_y = my * 32
        self.hero_speed = 4

    def hero_moving(self, screen, press_keys, block_group):
        """
        use the block_group list created by GameMap.py
        :param screen: game screen
        :param press_keys: keyboard pressed
        :param block_group: labeled block_group list by GameMap.py
        :return: ISOVER: True if hero hits the win block
        """
        global ISOVER
        if press_keys[K_ESCAPE]:
            exit()

        # moving key pressed
        if press_keys[K_LEFT]:
            self.hero_rect.left -= self.hero_speed
            # window conflict with hero
            if self.hero_rect.left <= 0:
                self.hero_rect.left = 0
            # block conflict with hero
            for n in range(len(block_group)):
                # hero and block conflict
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        # hit win block
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            # win
                            ISOVER = True
                        else:
                            # hit the normal block
                            self.hero_rect.left += self.hero_speed

        if press_keys[K_RIGHT]:
            self.hero_rect.left += self.hero_speed
            if self.hero_rect.right >= SCREEN_SIZE[0]:
                self.hero_rect.right = SCREEN_SIZE[0]
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            ISOVER = True
                        else:
                            self.hero_rect.left -= self.hero_speed

        if press_keys[K_UP]:
            self.hero_rect.top -= self.hero_speed
            if self.hero_rect.top <= 0:
                self.hero_rect.top = 0
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.bottom > block_group[n].rect.bottom > self.hero_rect.top:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            ISOVER = True
                        else:
                            self.hero_rect.top += self.hero_speed

        if press_keys[K_DOWN]:
            self.hero_rect.top += self.hero_speed
            if self.hero_rect.bottom <= 0:
                self.hero_rect.bottom = 0
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            ISOVER = True  # winner
                        else:
                            self.hero_rect.top -= self.hero_speed

        screen.blit(self.hero_img[0], self.hero_rect)
        return ISOVER