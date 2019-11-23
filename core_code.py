import pygame
from pygame import *


class Sprite:
    """
    用于绘制精灵图的工具类
    """

    @staticmethod
    def draw(dest, source, x, y, cell_x, cell_y, cell_w=100, cell_h=100):
        """
        绘制精灵图中，指定x,y的图像
        :param dest: surface类型，要绘制到的目标surface
        :param source: surface类型，来源surface
        :param x: 绘制图像在dest中的坐标
        :param y: 绘制图像在dest中的坐标
        :param cell_x: 在精灵图中的格子坐标
        :param cell_y: 在精灵图中的格子坐标
        :param cell_w: 单个精灵的宽度
        :param cell_h: 单个精灵的高度
        :return:
        """
        dest.blit(source, (x, y), (cell_x * cell_w, cell_y * cell_h, cell_w, cell_h))

class CharWalk:
    """
    charator walk class
    """
    def __init__(self, hero_surf, rect, hero_width, hero_height, mx, my, hero_speed):
        """
        :param hero_surf: 精灵图的surface
        :param mx: 角色所在的小格子坐标
        :param my: 角色所在的小格子坐标
        """
        self.hero_surf = hero_surf
        self.mx = mx
        self.my = my
        self.block_group = []  # block wall group
        self.imgs = [self.hero_surf.subsurface(Rect((0, 0), (hero_width, hero_height)))]
        self.rect = rect
        self.speed = hero_speed
        # self.frame = 1  # 角色当前帧

        self.x = mx * 100  # 角色相对于地图的坐标
        self.y = my * 100

    def draw(self,screen_surf, map_x, map_y):
        cell_x = 0
        cell_y = 0
        Sprite.draw(screen_surf, self.hero_surf, map_x + self.x, map_y + self.y, cell_x, cell_y)

    def moving(self, screen_surf, press_keys):
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
            for n in range(len(self.block_group) - 1):  # block_group list is all block, last one is end block
                # hero and block conflict
                if self.rect.top > self.block_group[n].rect.top - 100 and self.rect.bottom < self.block_group[n].rect.bottom + 100:
                    if self.rect.right > self.block_group[n].rect.right > self.rect.left:
                        self.rect.left += self.speed
                        break  # conflict happen

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            if self.rect.right >= 700:
                self.rect.right = 700
            for n in range(len(self.block_group) - 1):
                if self.rect.top > self.block_group[n].rect.top - 100 and self.rect.bottom < self.block_group[n].rect.bottom + 100:
                    if self.rect.left < self.block_group[n].rect.left < self.rect.right:
                        self.rect.left -= self.speed
                        break
            # # win
            # if self.rect.top > self.block_group[len(self.block_group) - 1].rect.top - 100 and self.rect.bottom < self.block_group[
            #     len(self.block_group) - 1].rect.bottom + 100:
            #     if self.rect.left < self.block_group[len(self.block_group) - 1].rect.left < self.rect.right:

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
            for n in range(len(self.block_group) - 1):
                if self.rect.left > self.block_group[n].rect.left - 100 and self.rect.right < self.block_group[n].rect.right + 100:
                    if self.rect.bottom > self.block_group[n].rect.bottom > self.rect.top:
                        self.rect.top += self.speed
                        break

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            if self.rect.bottom >= 700:
                self.rect.bottom = 700
            for n in range(len(self.block_group) - 1):
                if self.rect.left > self.block_group[n].rect.left - 100 and self.rect.right < self.block_group[n].rect.right + 100:
                    if self.rect.top < self.block_group[n].rect.top < self.rect.bottom:
                        self.rect.top -= self.speed
                        break

        # draw hero
        screen_surf.blit(self.imgs[0], self.rect)

