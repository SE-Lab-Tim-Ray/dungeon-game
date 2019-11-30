from pygame.locals import *

class Hero:
    def __init__(self, hero_fulimg, hero_rect, mx, my, GAME_TILE_SIZE):
        # the full sprite img of hero
        self.hero_fulimg = hero_fulimg

        # single sprite img of hero
        self.hero_img = [self.hero_fulimg.subsurface(Rect((0, 0), (GAME_TILE_SIZE, GAME_TILE_SIZE)))]
        self.hero_rect = hero_rect
        self.mx = mx
        self.my = my
        self.hero_coordinate_x = mx * GAME_TILE_SIZE
        self.hero_coordinate_y = my * GAME_TILE_SIZE
        self.hero_speed = 4

    def hero_moving(self, screen, press_keys, block_group, window_x, window_y, WIN_BLOCK_FROM_END, GAME_TILE_SIZE):
        """
        use the block_group list created by GameMap.py
        :param screen: game screen
        :param press_keys: keyboard pressed
        :param block_group: labeled block_group list by GameMap.py
        :return: ISOVER: True if hero hits the win block
        """

        is_over = False
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
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        # hit win block
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            # win
                            is_over = True
                        else:
                            # hit the normal block
                            self.hero_rect.left += self.hero_speed

        if press_keys[K_RIGHT]:
            self.hero_rect.left += self.hero_speed
            if self.hero_rect.right >= window_x:
                self.hero_rect.right = window_x
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            is_over = True
                        else:
                            self.hero_rect.left -= self.hero_speed

        if press_keys[K_UP]:
            self.hero_rect.top -= self.hero_speed
            if self.hero_rect.top <= 0:
                self.hero_rect.top = 0
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - GAME_TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + GAME_TILE_SIZE:
                    if self.hero_rect.bottom > block_group[n].rect.bottom > self.hero_rect.top:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            is_over = True
                        else:
                            self.hero_rect.top += self.hero_speed

        if press_keys[K_DOWN]:
            self.hero_rect.top += self.hero_speed
            if self.hero_rect.bottom >= window_y:
                self.hero_rect.bottom = window_y
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - GAME_TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + GAME_TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            is_over = True  # winner
                        else:
                            self.hero_rect.top -= self.hero_speed

        screen.blit(self.hero_img[0], self.hero_rect)
        return is_over