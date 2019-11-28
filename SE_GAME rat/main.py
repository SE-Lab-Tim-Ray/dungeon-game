from Hero import *
from GameMap import *
import time

WHITE = (255, 255, 255)
game_over = False
lose_game = False
# timer for counter
last_time = 0
# timer for rat
last_rat_move = 0
counter = 100
class Game:
    def __init__(self, title, screen_width, screen_height, fps=60):
        """
        width of maze is 25 columns, height is 19
        :param title: title of the game
        :param screen_width: screen width
        :param screen_height: screen height
        :param fps: refresh times per second
        """
        self.title = title
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps
        self.screen = None

        # data for game
        self.hero_born_x = 1
        self.hero_born_y = 1
        self.hero_width = 32
        self.hero_height = 32

        self.__init_pygame()
        self.__init_game()
        self.update()

    # private def for init pygame
    def __init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # set a clock
        self.clock = pygame.time.Clock()

    def __init_game(self):
        self.game_map_img = pygame.image.load('./resources/images/maze1.png').convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)
        self.maze_win_img = pygame.image.load('./resources/images/1_win.png').convert_alpha()
        self.maze_lose_img = pygame.image.load('./resources/images/1_lose.png').convert_alpha()

        global block_group
        # global isOver
        self.game_map.make_block_group('./resources/maps/maze1.txt')
        self.hero_fulimg = pygame.image.load('./resources/images/char1.png').convert_alpha()
        self.hero_rect = Rect(32, 32, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, self.hero_born_x, self.hero_born_y)
        self.font = pygame.font.Font(None, 24)

        # rat
        self.rat_fulimg = pygame.image.load('./resources/images/char2.png').convert_alpha()
        # start at space two (harcoded)

        self.rat_rect = Rect(736, 544, 32, 32)
        # pretty sure that the rat_rect includes the x,y for start, not the last 2 params of Hero
        self.rat = Hero(self.rat_fulimg, self.rat_rect, 15, 1)
        # **************Version 2******************
        self.spider = None
        self.bat = None
        self.stone = None

    def collide(self, hero_rect1, hero_rect2):
        isCollision = False
        # hero/monster conflict LEFT
        if hero_rect1.top >= hero_rect2.top - TILE_SIZE and hero_rect1.bottom <= hero_rect2.bottom + TILE_SIZE:
            if hero_rect1.right >= hero_rect2.right >= hero_rect1.left:
                isCollision = True
                print("Collide left")
        # right
        if hero_rect1.top >= hero_rect2.top - TILE_SIZE and hero_rect1.bottom <= hero_rect2.bottom + TILE_SIZE:
            if hero_rect1.left <= hero_rect2.left <= hero_rect1.right:
                isCollision = True
                print("Collide right")

        # up
        if hero_rect1.left >= hero_rect2.left - TILE_SIZE and hero_rect1.right <= hero_rect2.right + TILE_SIZE:
            if hero_rect1.bottom >= hero_rect2.bottom >= hero_rect1.top:
                isCollision = True
                print("Collide up")

        if hero_rect1.left >= hero_rect2.left - TILE_SIZE and hero_rect1.right <= hero_rect2.right + TILE_SIZE:
            if hero_rect1.top <= hero_rect2.top <= hero_rect1.bottom:
                isCollision = True
                print("Collide down")

            #         if self.hero_rect.left > block_group[n].rect.left - TILE_SIZE and self.hero_rect.right < \
            #                 block_group[n].rect.right + TILE_SIZE:
            #             if self.hero_rect.top < block_group[n].rect.top < self.hero_rect.bottom:
            #                 if n == len(block_group) - 26:  # is it the win square?
            #                     isOver = True  # winner
            #                 else:
            #                     self.hero_rect.top -= self.hero_speed  # if so, undo the move


        return isCollision

    def update(self):
        # global isOver
        global game_over, counter, last_time, lose_game, last_rat_move

        while 1:
            if game_over:
                self.screen.blit(self.maze_win_img, (0, 0))  # win bg
                pygame.display.update()
                for m in pygame.event.get():
                    if m.type == QUIT:
                        exit()
                    if m.type == KEYDOWN:
                        exit()
                self.clock.tick(self.fps)
                continue
            if lose_game:
                self.screen.blit(self.maze_lose_img, (0, 0))  # win bg
                pygame.display.update()
                for m in pygame.event.get():
                    if m.type == QUIT:
                        exit()
                    if m.type == KEYDOWN:
                        exit()
                self.clock.tick(self.fps)
                continue
            # game is playing
            # draw the map
            self.game_map.draw_map(self.screen)

            # game map roll
            self.game_map.map_roll(self.hero.hero_coordinate_x, self.hero.hero_coordinate_y)

            for n in pygame.event.get():
                if n.type == QUIT:
                    exit()

            # Timer. Check for 1000ms passed since last_time then reduce counter by one
            ticks = pygame.time.get_ticks()
            if ticks > last_time + 1000:
                last_time = ticks
                counter -= 1

            # blit screen
            textclock = "Time remaining: " + str(counter)
            self.screen.blit(self.font.render(textclock, True, (WHITE)), (10, 5))

            # Only move rat slower every x ms
            move_rat = False
            if ticks > last_rat_move + 10:
                move_rat = True
                last_rat_move = ticks
            self.rat.monster_move(self.screen, self.hero_rect, block_group, move_rat)


            # logic update
            press_keys = pygame.key.get_pressed()
            game_over = self.hero.hero_moving(self.screen, press_keys, block_group)


            # collision detection
            lose_game = self.collide(self.rat_rect, self.hero_rect)


            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    Game("Demo", 800, 600)

