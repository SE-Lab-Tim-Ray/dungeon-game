from Hero import *
from GameMap import *

GAME_OVER = False
WHITE = (255, 255, 255)
last_time = 0
counter = 100


class Game:
    def __init__(self, title, screen_width, screen_height, fps=60):
        """
        25 columns width and 19 columns height
        :param title: title of the game
        :param screen_width: screen width
        :param screen_height: screen height
        :param fps: refresh times per second
        """
        # data for pygame
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

        # run functions below
        self.__init_pygame()
        self.__init_game()
        self.update()

    def __init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

    def __init_game(self):
        global BLOCK_GROUP
        self.maze_win_img = pygame.image.load('./resources/images/1_win.png').convert_alpha()
        self.game_map_img = pygame.image.load('./resources/images/1_maze.png').convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)
        self.game_map.make_block_group('./resources/maps/1_maze.txt')
        self.hero_fulimg = pygame.image.load('./resources/images/1_char.png').convert_alpha()
        self.hero_rect = Rect(32, 32, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, self.hero_born_x, self.hero_born_y)
        self.font = pygame.font.Font(None, 24)

    def update(self):
        global GAME_OVER, counter, last_time

        while 1:
            if GAME_OVER:
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
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # draw the map
            self.game_map.draw_map(self.screen)

            # Timer. Check for 1000ms passed since last_time then reduce counter by one
            ticks = pygame.time.get_ticks()
            if ticks > last_time + 1000:
                last_time = ticks
                counter -= 1

            # blit Timer to the screen
            text_clock = "Time remaining: " + str(counter)
            self.screen.blit(self.font.render(text_clock, True, WHITE), (10, 5))

            # logic update
            press_keys = pygame.key.get_pressed()
            GAME_OVER = self.hero.hero_moving(self.screen, press_keys, BLOCK_GROUP)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    Game("Demo", 800, 600)

