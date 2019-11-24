# coding=gbk
"""
hero and block are both 100X100
"""
import pygame
from GameMap import *  # TC


from pygame.locals import *
START_POSITION = 32, 32
SCREEN_SIZE = (800, 600)  # window size # TC
MAP_BOTTOM_CORRECTION = 24
GAME_CAPTION = "Jeff's game"  # TC
MAZE_FILENAME_STR = "maze"  # TC
WIN_FILENAME_STR = "win"  # TC
MAZE_FILE_IMG_TYPE = "png"  # TC
MAZE_FILE_TXT_TYPE = "txt"  # TC
MAZE_NUMBER = "1"  # TC
MOVE_TOLERANCE = 12   # TC how close you have to be to a corridor to go im
CODE_RESOURCES_LOCATION = "../Code_resources/"
MAZE_IMAGE_FILE = CODE_RESOURCES_LOCATION + MAZE_NUMBER + "_"+ MAZE_FILENAME_STR  + "." + MAZE_FILE_IMG_TYPE  # TC
MAZE_WIN_FILE = CODE_RESOURCES_LOCATION + MAZE_NUMBER + "_"+ WIN_FILENAME_STR  + "." + MAZE_FILE_IMG_TYPE  # TC
MAZE_MAP_FILE = CODE_RESOURCES_LOCATION + MAZE_NUMBER + "_"+ MAZE_FILENAME_STR  + "." + MAZE_FILE_TXT_TYPE  # TC
CHAR_IMAGE = "../Code_resources/1_char.png"  # TC
TILE_IMAGE = "../Code_resources/tile.png"  # TC
BLOCK_IMAGE = "../Code_resources/block2.png"  # TC
TILE_SIZE = 32  # TC assume square
WHITE = (0, 255, 255)  # TC

# block_group = []  # block wall group

isOver = False

# maze, 0 no wall, 1 wall
# background_group = [
#     [0,1,1,1,0,0,1],
#     [0,1,0,1,0,0,1],
#     [0,1,1,1,0,0,1],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,1],
#     [0,1,1,1,0,0,1],
#     [0,1,1,1,0,0,0]
# ]


# character hero
class Hero:
    # 初始化类
    def __init__(self, img, rect, speed):

        # full_img is whole pic，imgs is surface
        # rect is hero rect，speed is moving speed of hero
        self.ful_img = img
        self.imgs = [self.ful_img.subsurface(Rect((0, 0), (TILE_SIZE, TILE_SIZE)))]

        self.rect = rect
        self.speed = speed
        self.num = 0

    def update(self, screen, press_keys, block_group):
        global isOver

        if press_keys[K_ESCAPE]:
            exit()
        # key press
        if press_keys[K_LEFT]:

            self.rect.left -= self.speed
            # window conflict with hero
            if self.rect.left <= 0:
                self.rect.left = 0
            # conflict with block
            for n in range(len(block_group)):     # block_group list is all block, last one is end block
                # hero and block conflict
                if self.rect.top > block_group[n].rect.top - TILE_SIZE and self.rect.bottom < block_group[n].rect.bottom + TILE_SIZE:
                    if self.rect.right > block_group[n].rect.right > self.rect.left:
                        if n == len(block_group)-1:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.rect.left += self.speed  # if so, undo the move

        if press_keys[K_RIGHT]:
            self.rect.left += self.speed # make the move
            if self.rect.right >= SCREEN_SIZE[0]:
                self.rect.right = SCREEN_SIZE[0]
            for n in range(len(block_group)):
                if self.rect.top > block_group[n].rect.top - TILE_SIZE and self.rect.bottom < block_group[n].rect.bottom + TILE_SIZE: # is it on the right row?
                    if self.rect.left < block_group[n].rect.left < self.rect.right:  # does it conflict with x position?
                        if n == len(block_group)-1:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.rect.left -= self.speed  # if so, undo the move


        if press_keys[K_UP]:

            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
            for n in range(len(block_group)):
                if self.rect.left > block_group[n].rect.left - TILE_SIZE and self.rect.right < block_group[n].rect.right + TILE_SIZE:
                    if self.rect.bottom > block_group[n].rect.bottom > self.rect.top:
                        if n == len(block_group)-1:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.rect.top += self.speed  # if so, undo the move

        if press_keys[K_DOWN]:
            self.rect.top += self.speed
            if self.rect.bottom <= 0:
                self.rect.bottom = 0
            for n in range(len(block_group)):
                if self.rect.left > block_group[n].rect.left - TILE_SIZE and self.rect.right < block_group[n].rect.right + TILE_SIZE:
                    if self.rect.top < block_group[n].rect.top < self.rect.bottom:
                        if n == len(block_group)-1:  # is it the win square?
                            isOver = True  # winner
                        else:
                            self.rect.top -= self.speed  # if so, undo the move

            # next_location = self.rect.top + self.speed  # make the move
            #
            # if next_location >= SCREEN_SIZE[1]-MAP_BOTTOM_CORRECTION-TILE_SIZE:  # if outside screen undo move
            #     next_location = SCREEN_SIZE[1]-MAP_BOTTOM_CORRECTION-TILE_SIZE
            #
            # for n in range(len(block_group)):
            #     if (self.rect.left) > (block_group[n].rect.left - TILE_SIZE) and (self.rect.right) < (block_group[n].rect.right + TILE_SIZE):  # is it on the right row exactly?
            #
            #
            #         if self.rect.top < block_group[n].rect.top < self.rect.bottom:   # does it conflict with x position?
            #             if n == len(block_group)-1:  # is it the win square?
            #                 isOver = True  # winner
            #             else:
            #                 next_location = self.rect.top - self.speed  # if not, undo the move
            #     else:    # there is no wall to stop. You're close enough. Move down, but correct the left co-ordinate
            #
            #         if (self.rect.left) > (block_group[n].rect.left - TILE_SIZE - MOVE_TOLERANCE) and (
            #                 self.rect.right) < (
            #                 block_group[n].rect.right + TILE_SIZE + MOVE_TOLERANCE):  # is it on the right row with extra tolerance?
            #
            #                 self.rect.left = (round(self.rect.left / TILE_SIZE)*(TILE_SIZE))  # go down corridor
            #
            # self.rect.top = next_location

        # draw hero
        screen.blit(self.imgs[0], self.rect)

        return 0



def game():
    # moving speed
    hero_speed = 1
    # interval time for loop
    dwTime = 60
    # hero rect
    hero_rect = Rect(START_POSITION[0], START_POSITION[1], TILE_SIZE, TILE_SIZE)
    # init game
    pygame.init()
    # since the last time of anime
    clock = pygame.time.Clock()
    # screen
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)  # TC use constant


    # # bg
    # background1 = pygame.image.load(MAP_IMAGE).convert() # TC remove
    # hero img load
    hero = pygame.image.load(CHAR_IMAGE).convert_alpha()
    # hero object
    andr = Hero(hero, hero_rect, hero_speed)
    # game caption
    pygame.display.set_caption(GAME_CAPTION)

    block_group = create_maze_map(MAZE_MAP_FILE, TILE_SIZE, pygame)

    # main loop
    while 1:
        # game over
        if isOver:
            screen.blit(pygame.image.load(MAZE_WIN_FILE).convert(), (0, 0))  # win bg
            pygame.display.update()
            # any key pressed to exit
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    exit()
            clock.tick(60)
            continue

        # not game over，isOver is False
        # screen fill up with white
        screen.fill(WHITE)  # TC
        # bg on screen
        # screen.blit(background1, (0, 0))
        draw_maze_to_screen(screen, MAZE_IMAGE_FILE, pygame)  # TC

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # key press, update
        press_keys = pygame.key.get_pressed()
        andr.update(screen, press_keys, block_group)

        pygame.display.update()

        # frame of game
        clock.tick(dwTime)

# to ensure only run as main program
if __name__ == "__main__":
    game()
