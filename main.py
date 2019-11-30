from Hero import *
from GameMap import *

"""
CONSTANTS
"""
# Game constants
WHITE = (255, 255, 255)
GAME_TITLE = "Jeff's Lair"
SCREEN_SIZE = (800, 600)
GAME_SPEED = 60  # game speed in fps

# timer
COUNTER_START = 100  # number of seconds to complete maze
ONE_SECOND = 1000  # number of ticks in a second for timer
TIMER_FONT_SIZE = 24
TIMER_LOCATION = (8, 8)
TIMER_TEXT = "Time remaining: "

# Builing the maze
MAZE_WIN_IMG = "./resources/images/1_win.png"
MAZE_MAP_IMG = "./resources/images/1_maze.png"
MAZE_MAP = "./resources/maps/1_maze.txt"
CHARACTER_IMG = "./resources/images/1_char.png"
WIN_BLOCK_FROM_END = 26  # defines the win square
HERO_TILE_SIZE = 32  # size in px of main player height and width
GAME_TILE_SIZE = 32   # size in px of main grid height and width
PLAYER_BORN_X = 1 * HERO_TILE_SIZE  # x position where hero starts in px
PLAYER_BORN_Y = 1 * HERO_TILE_SIZE  # y position where hero starts in px

class Game:
    def __init__(self, title, screen_width, screen_height, fps=GAME_SPEED):
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
        self.hero_born_x = PLAYER_BORN_X
        self.hero_born_y = PLAYER_BORN_Y
        self.hero_width = HERO_TILE_SIZE
        self.hero_height = HERO_TILE_SIZE

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
        # map
        self.maze_win_img = pygame.image.load(MAZE_WIN_IMG).convert_alpha()
        self.game_map_img = pygame.image.load(MAZE_MAP_IMG).convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)
        self.game_block_group = self.game_map.make_block_group(MAZE_MAP, GAME_TILE_SIZE)
        # hero
        self.hero_fulimg = pygame.image.load(CHARACTER_IMG).convert_alpha()
        self.hero_rect = Rect(self.hero_born_x, self.hero_born_y, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, self.hero_born_x, self.hero_born_y, GAME_TILE_SIZE)
        # others
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)

    def update(self):

        # initialise counter
        counter = COUNTER_START

        # counts time elapsed in ticks
        last_time = 0

        # has the hero won yet ?
        game_over = False

        # main game loop
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
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # draw the map
            self.game_map.draw_map(self.screen)

            # Timer. Check for 1000ms passed since last_time then reduce counter by one
            ticks = pygame.time.get_ticks()
            if ticks > last_time + ONE_SECOND:
                last_time = ticks
                counter -= 1

            # blit Timer to the screen
            text_clock = TIMER_TEXT + str(counter)
            self.screen.blit(self.font.render(text_clock, True, WHITE), TIMER_LOCATION)

            # logic update
            press_keys = pygame.key.get_pressed()
            game_over = self.hero.hero_moving(self.screen, press_keys, self.game_block_group, SCREEN_SIZE[0], SCREEN_SIZE[1], WIN_BLOCK_FROM_END, GAME_TILE_SIZE)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    Game(GAME_TITLE, SCREEN_SIZE[0], SCREEN_SIZE[1])

