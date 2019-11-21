# coding=gbk
"""
hero and block are both 100X100
"""
import pygame

from pygame.locals import *

size = (700, 700)  # window size

white = (255, 255, 255)

block_group = []  # block wall group

isOver = False

# maze, 0 no wall, 1 wall
background_group = [
    [0,1,1,1,0,0,1],
    [0,1,0,1,0,0,1],
    [0,1,1,1,0,0,1],        #
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1],
    [0,1,1,1,0,0,1],
    [0,1,1,1,0,0,0]
]


# character hero
class Hero:
    # 初始化类
    def __init__(self, img, rect, speed):

        # full_img is whole pic，imgs is surface
        # rect is hero rect，speed is moving speed of hero
        self.ful_img = img
        self.imgs = [self.ful_img.subsurface(Rect((0, 0), (100, 100)))]

        self.rect = rect
        self.speed = speed
        self.num = 0

    def update(self, screen, press_keys):
        global isOver

        if press_keys[K_ESCAPE]:
            exit()
        # key press
        if press_keys[K_LEFT]:
            # rect(left, top, width, height)
            self.rect.left -= self.speed
            # window conflict with hero
            if self.rect.left <= 0:
                self.rect.left = 0
            # conflict with block
            for n in range(len(block_group)-1):     # block_group list is all block, last one is end block
                # hero and block conflict
                if self.rect.top > block_group[n].rect.top - 100 and self.rect.bottom < block_group[n].rect.bottom + 100:
                    if self.rect.right > block_group[n].rect.right > self.rect.left:
                        self.rect.left += self.speed
                        break   # conflict happen

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            if self.rect.right >= 700:
                self.rect.right = 700
            for n in range(len(block_group)-1):
                if self.rect.top > block_group[n].rect.top - 100 and self.rect.bottom < block_group[n].rect.bottom + 100:
                    if self.rect.left < block_group[n].rect.left < self.rect.right:
                        self.rect.left -= self.speed
                        break
            # win
            if self.rect.top > block_group[len(block_group) - 1].rect.top - 100 and self.rect.bottom < block_group[len(block_group) - 1].rect.bottom + 100:
                if self.rect.left < block_group[len(block_group) - 1].rect.left < self.rect.right:
                    isOver = True

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 100 and self.rect.right < block_group[n].rect.right + 100:
                    if self.rect.bottom > block_group[n].rect.bottom > self.rect.top:
                        self.rect.top += self.speed
                        break

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            if self.rect.bottom >= 700:
                self.rect.bottom = 700
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 100 and self.rect.right < block_group[n].rect.right + 100:
                    if self.rect.top < block_group[n].rect.top < self.rect.bottom:
                        self.rect.top -= self.speed
                        break
            # win?
            if self.rect.left > block_group[len(block_group)-1].rect.left - 100 and self.rect.right < block_group[len(block_group)-1].rect.right + 100:
                if self.rect.top < block_group[len(block_group)-1].rect.top < self.rect.bottom:
                    isOver = True

        # draw hero
        screen.blit(self.imgs[0], self.rect)

        return 0


# block class
class Block:
    def __init__(self, img, rect):
        self.img = img
        self.rect = rect

    # draw block
    def draw(self, screen):
        screen.blit(self.img, self.rect)

# draw bg
def drawBackground(screen):
    # init list
    block_group.clear()

    # load block img
    block1_img = pygame.image.load('image/tile.png').convert_alpha()

    # 通draw maze
    for i in range(7):
        for j in range(7):
            if background_group[i][j] == 1:
                block = Block(block1_img, Rect(100*j, 100*i, 100, 100))
                block.draw(screen)  # draw block
                block_group.append(block)  # append block into block group

    # end block
    block_final = Block(pygame.image.load('image/block2.png').convert_alpha(), Rect(630, 630, 100, 100))
    block_final.draw(screen)
    block_group.append(block_final)


def game():
    # moving speed
    hero_speed = 10
    # interval time for loop
    dwTime = 60
    # hero rect
    hero_rect = Rect(0, 0, 100, 100)
    # init game
    pygame.init()
    # since the last time of anime
    clock = pygame.time.Clock()
    # sreen
    screen = pygame.display.set_mode(size, 0, 32)
    # bg
    background1 = pygame.image.load('image/background1.jpg').convert()
    # hero img load
    hero = pygame.image.load('image/char.png').convert_alpha()
    # hero object
    Andr = Hero(hero, hero_rect, hero_speed)
    # game caption
    pygame.display.set_caption("Demo")

    # main loop
    while 1:
        # game over
        if isOver:
            screen.blit(pygame.image.load('image/over.jpg').convert(), (0, 0))  # win bg
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
        screen.fill(white)
        # bg on screen
        screen.blit(background1, (0, 0))

        drawBackground(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # key press, update
        press_keys = pygame.key.get_pressed()
        Andr.update(screen, press_keys)
        pygame.display.update()

        # frame of game
        clock.tick(dwTime)


if __name__ == "__main__":
    game()
