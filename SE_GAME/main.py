from Hero import *
from GameMap import *
import time

WHITE = (0, 255, 255)
game_over = False
last_time = 0
counter = 10
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
        global block_group
        # global isOver
        self.game_map.make_block_group('./resources/maps/maze1.txt')
        self.hero_fulimg = pygame.image.load('./resources/images/char1.png').convert_alpha()
        self.hero_rect = Rect(32, 32, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, self.hero_born_x, self.hero_born_y)
        self.font = pygame.font.Font(None, 40)

        # **************Version 2******************
        self.rat = None
        self.spider = None
        self.bat = None
        self.stone = None

    def update(self):
        # global isOver
        global game_over, counter, last_time
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

            # game is playing
            # draw the map
            self.game_map.draw_map(self.screen)

            # game map roll
            self.game_map.map_roll(self.hero.hero_coordinate_x, self.hero.hero_coordinate_y)

            for n in pygame.event.get():
                if n.type == QUIT:
                    exit()
            # Timer
            ticks = pygame.time.get_ticks()
            if ticks > last_time + 1000:
                last_time = ticks
                counter -= 1
                textclock = str(counter)
                # print(counter)
                self.screen.blit(self.font.render(textclock, True, (0, 0, 0)), (0, 0))

            # logic update
            press_keys = pygame.key.get_pressed()
            game_over = self.hero.hero_moving(self.screen, press_keys, block_group)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    Game("Demo", 800, 600)

