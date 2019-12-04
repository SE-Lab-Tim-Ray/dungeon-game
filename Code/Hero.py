from pygame.locals import *

class Hero:
    def __init__(self, hero_fulimg, hero_rect, GAME_TILE_SIZE):
        # Hero image
        self.hero_fulimg = hero_fulimg

        # attach image to surface
        self.hero_img = [self.hero_fulimg.subsurface(Rect((0, 0), (GAME_TILE_SIZE, GAME_TILE_SIZE)))]
        self.hero_rect = hero_rect
        self.hero_speed = 4

    def hero_moving(self, screen, press_keys, block_group, window_x, window_y, WIN_BLOCK_FROM_END, GAME_TILE_SIZE):
        """
        use the block_group list created by GameMap.py
        :param screen: game screen
        :param press_keys: keys pressed on keyboard
        :param block_group: list of rectangles where wall squares are
        :return: is_over: True if hero hits the win block
        """
        #  assume the game is not over until proved otherwise
        is_over = False

        # end game on hitting escape
        if press_keys[K_ESCAPE]:
            exit()

        # if left arrow key pressed move to left by speed factor
        if press_keys[K_LEFT]:
            self.hero_rect.left -= self.hero_speed
            # has the character hit the edge of the screen, if so dont let past
            if self.hero_rect.left <= 0:
                self.hero_rect.left = 0
            # has the player hit a wall (in block group)
            for n in range(len(block_group)):
                # hero and block conflict
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    if self.hero_rect.right > block_group[n].rect.right > self.hero_rect.left:
                        # If the character has hit a block - is it the win block?
                        if n == len(block_group) - WIN_BLOCK_FROM_END:
                            # set variable to return function game over
                            is_over = True
                        else:
                            # hit a normal block so undo the move
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
        Move the monster in the direction of the character
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

        # move either left or right
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

            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.top > block_group[n].rect.top - GAME_TILE_SIZE and self.hero_rect.bottom < \
                        block_group[n].rect.bottom + GAME_TILE_SIZE:
                    if self.hero_rect.left < block_group[n].rect.left < self.hero_rect.right:
                        self.hero_rect.left -= 1  # if so, undo the move
        # MOVIN UP
        if move_rat and move_up:
            self.hero_rect.top -= 1

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

            # conflict with block
            for n in range(len(block_group)):
                if self.hero_rect.left > block_group[n].rect.left - GAME_TILE_SIZE and self.hero_rect.right < \
                        block_group[n].rect.right + GAME_TILE_SIZE:
                    if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
                        self.hero_rect.top -= 1 # if so, undo the move

        # transfer new position of hero
        screen.blit(self.hero_img[0], self.hero_rect)

        # if the monster has touched the character, then return function as true
        return isCaught

