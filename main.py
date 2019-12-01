from Hero import *
from GameMap import *
from Startbox import *

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

# Building the maze
MAZE_WIN_IMG = "./resources/images/1_win.png"
MAZE_LOSE_IMG = "./resources/images/1_lose.png"
NICKNAME_LOCATION = (280, 350)
NICKNAME_FONT_SIZE = 40
NICKNAME_TEXT = "Well done "
NICKNAME_LEADING = 20
MAZE_MAP_IMG = "./resources/images/1_maze.png"
MAZE_MAP = "./resources/maps/1_maze.txt"
CHARACTER_IMG = "./resources/images/1_char.png"

WIN_BLOCK_FROM_END = 26  # defines the win square
HERO_TILE_SIZE = 32  # size in px of main player height and width
GAME_TILE_SIZE = 32   # size in px of main grid height and width
PLAYER_BORN_X = 1 * HERO_TILE_SIZE  # x position where hero starts in px
PLAYER_BORN_Y = 1 * HERO_TILE_SIZE  # y position where hero starts in px

RAT_IMG = "./resources/images/rat.png"
RAT_BORN_X = 23 * HERO_TILE_SIZE  # x position where rat starts in px
RAT_BORN_Y = 17 * HERO_TILE_SIZE  # y position where rat starts in px
SLOW_RAT = 10  # make rat update every x ms


class Game:
    def __init__(self, title, screen_width, screen_height, nickname, fps=GAME_SPEED):
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
        self.nickname = nickname

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
        # initialise map
        self.maze_win_img = pygame.image.load(MAZE_WIN_IMG).convert_alpha()
        self.maze_lose_img = pygame.image.load(MAZE_LOSE_IMG).convert_alpha()
        self.game_map_img = pygame.image.load(MAZE_MAP_IMG).convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)
        self.game_block_group = self.game_map.make_block_group(MAZE_MAP, GAME_TILE_SIZE)
        # initialise hero
        self.hero_fulimg = pygame.image.load(CHARACTER_IMG).convert_alpha()
        self.hero_rect = Rect(self.hero_born_x, self.hero_born_y, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, GAME_TILE_SIZE)
        # others
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)

        # initialise rat
        self.rat_fulimg = pygame.image.load(RAT_IMG).convert_alpha()

        # start rat at particular space
        self.rat_rect = Rect(RAT_BORN_X, RAT_BORN_Y, GAME_TILE_SIZE, GAME_TILE_SIZE)

        # pretty sure that the rat_rect includes the x,y for start, not the last 2 params of Hero
        self.rat = Hero(self.rat_fulimg, self.rat_rect, GAME_TILE_SIZE)


    def collide(self, hero_rect1, hero_rect2, GAME_TILE_SIZE):
        is_collision = False
        # hero/monster conflict LEFT
        if hero_rect1.top >= hero_rect2.top - GAME_TILE_SIZE and hero_rect1.bottom <= hero_rect2.bottom + GAME_TILE_SIZE:
            if hero_rect1.right >= hero_rect2.right >= hero_rect1.left:
                is_collision = True
        # right
        if hero_rect1.top >= hero_rect2.top - GAME_TILE_SIZE and hero_rect1.bottom <= hero_rect2.bottom + GAME_TILE_SIZE:
            if hero_rect1.left <= hero_rect2.left <= hero_rect1.right:
                is_collision = True

        # up
        if hero_rect1.left >= hero_rect2.left - GAME_TILE_SIZE and hero_rect1.right <= hero_rect2.right + GAME_TILE_SIZE:
            if hero_rect1.bottom >= hero_rect2.bottom >= hero_rect1.top:
                is_collision = True

        if hero_rect1.left >= hero_rect2.left - GAME_TILE_SIZE and hero_rect1.right <= hero_rect2.right + GAME_TILE_SIZE:
            if hero_rect1.top <= hero_rect2.top <= hero_rect1.bottom:
                is_collision = True
        return is_collision


    def update(self):

        # initialise counter
        counter = COUNTER_START

        # counts time elapsed in ticks
        last_time = 0

        # counter to delay rat moves
        last_rat_move = 0

        # is the game over yet ?
        game_over = False
        lose_game = False

        # main game loop
        while 1:
            if game_over:
                # show the win background
                self.screen.blit(self.maze_win_img, (0, 0))
                # show the winner name and time remaining
                self.screen.blit(self.font.render(NICKNAME_TEXT + self.nickname, True, WHITE), NICKNAME_LOCATION)
                self.screen.blit(self.font.render(text_clock, True, WHITE), (NICKNAME_LOCATION[0], NICKNAME_LOCATION[1]+NICKNAME_LEADING))
                # print(self.nickname)
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

            # Only move rat slower every x ms
            move_rat = False
            if ticks > last_rat_move + SLOW_RAT:
                move_rat = True
                last_rat_move = ticks
            self.rat.monster_move(self.screen, self.hero_rect, self.game_block_group, move_rat, GAME_TILE_SIZE)

            # logic update
            press_keys = pygame.key.get_pressed()
            game_over = self.hero.hero_moving(self.screen, press_keys, self.game_block_group, SCREEN_SIZE[0], SCREEN_SIZE[1], WIN_BLOCK_FROM_END, GAME_TILE_SIZE)

            # collision detection
            lose_game = self.collide(self.rat_rect, self.hero_rect, GAME_TILE_SIZE)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":

    Game(GAME_TITLE, SCREEN_SIZE[0], SCREEN_SIZE[1], nickname = startbox())

