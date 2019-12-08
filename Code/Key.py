from pygame.locals import *
from run_jeff import HERO_TILE_SIZE

KEY1_X = 3
KEY1_Y = 1
KEY2_X = 5
KEY2_Y = 6
KEY3_X = 7
KEY3_Y = 7
KEY4_X = 9
KEY4_Y = 9

KEY1_BORN_X = KEY1_X * HERO_TILE_SIZE
KEY1_BORN_Y = KEY1_Y * HERO_TILE_SIZE

KEY2_BORN_X = KEY2_X * HERO_TILE_SIZE
KEY2_BORN_Y = KEY2_X * HERO_TILE_SIZE

KEY3_BORN_X = KEY3_X * HERO_TILE_SIZE
KEY3_BORN_Y = KEY3_X * HERO_TILE_SIZE

KEY4_BORN_X = KEY4_X * HERO_TILE_SIZE
KEY4_BORN_Y = KEY4_X * HERO_TILE_SIZE

class Key:
    def __init__(self, key_fulimg, key_rect, GAME_TILE_SIZE):
        # Key image
        self.key_fulimg = key_fulimg

        # attach image to surface
        self.key_img = [self.key_fulimg.subsurface(Rect((0, 0), (GAME_TILE_SIZE, GAME_TILE_SIZE)))]
        self.key_rect = key_rect

    def draw_keys(self, screen, key_num):
        if(key_num == 1):
            screen.blit(self.key_img[0], self.key_rect)
        if(key_num == 2):
            screen.blit(self.key_img[0], self.key_rect)
        if(key_num == 3):
            screen.blit(self.key_img[0], self.key_rect)
        if(key_num == 4):
            screen.blit(self.key_img[0], self.key_rect)



