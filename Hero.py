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


    def monster_move(self, screen, hero_rect, block_group, move_rat, GAME_TILE_SIZE):
        """
        use the hero_rect for hero. self.hero_rect refers to the monster
        """
        isCaught = False


        # decide which direction to move in
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        x_offset = self.hero_rect.left - hero_rect.left
        y_offset = self.hero_rect.top - hero_rect.top


        if x_offset > 0:
            move_left = True
        if x_offset < 0:
            move_right = True

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
            # if self.hero_rect.left <= 0:
            #     self.hero_rect.left = 0

            # conflict with block
            for n in range(len(block_group)):  # block_group list is all block
                # hero and block conflict
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    #
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        self.hero_rect.left += 1  # if so, undo the move
        # MOVING RIGHT
        if move_rat and move_right:
            self.hero_rect.left += 1
            # window conflict with hero
            # if self.hero_rect.right >= SCREEN_SIZE[0]:
            #     self.hero_rect.right = SCREEN_SIZE[0]
            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        self.hero_rect.left -= 1  # if so, undo the move
        # MOVIN UP
        if move_rat and move_up:
            self.hero_rect.top -= 1
            # if self.hero_rect.top <= 0:
            #     self.hero_rect.top = 0
            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - GAME_TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + GAME_TILE_SIZE:
                    if self.hero_rect.bottom > block_group[n].rect.bottom > self.hero_rect.top:
                        self.hero_rect.top += 1  # if so, undo the move
        #
        # Movin DOWN
        if move_rat and move_down:
            self.hero_rect.top += 1
            # if self.hero_rect.bottom >= SCREEN_SIZE[1]:
            #     self.hero_rect.bottom = SCREEN_SIZE[1]
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - GAME_TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + GAME_TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                        self.hero_rect.top -= 1 # if so, undo the move
        screen.blit(self.hero_img[0], self.hero_rect)
        return isCaught

