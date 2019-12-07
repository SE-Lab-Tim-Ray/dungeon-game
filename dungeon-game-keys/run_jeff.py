from Code.Hero import *
from Code.GameMap import *
from Code.Startbox import *
from Code.LeaderBoard import *
from Code.Key import *

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
MAZE_WIN_HOLDSCREEN = 3 * ONE_SECOND  # Time to hold win screen
MAZE_LOSE_IMG = "./resources/images/1_lose.png"
NICKNAME_LOCATION = (280, 350)
NICKNAME_FONT_SIZE = 40
NICKNAME_TEXT = "Well done "
NICKNAME_LEADING = 20
MAZE_MAP_IMG = "./resources/images/1_maze.png"
MAZE_MAP = "./resources/maps/1_maze.txt"
CHARACTER_IMG = "./resources/images/1_char.png"
KEY_IMG = "./resources/images/1_key.png"

WIN_BLOCK_FROM_END = 26  # defines the win square
HERO_TILE_SIZE = 32  # size in px of main player height and width
GAME_TILE_SIZE = 32   # size in px of main grid height and width
PLAYER_BORN_X = 1 * HERO_TILE_SIZE  # x position where hero starts in px
PLAYER_BORN_Y = 1 * HERO_TILE_SIZE  # y position where hero starts in px

RAT_IMG = "./resources/images/rat.png"
RAT_BORN_X = 23 * HERO_TILE_SIZE  # x position where rat starts in px
RAT_BORN_Y = 17 * HERO_TILE_SIZE  # y position where rat starts in px
SLOW_RAT = 10  # make rat update every x ms

# Leaderboard
LEADERBOARD_IMG = "./resources/images/leaderboard.png"
LEADER_BOARD_X = 200
LEADER_BOARD_Y = 320
LEADER_BOARD_COLUMN_OFFSET = 350
LEADER_BOARD_FONT_SIZE = 40
LEADER_BOARD_LEADING = 40
LEADER_BOARD_LAST_SCORE_LOCATION_Y = 570
LEADER_BOARD_LAST_TEXT = "Last score: "

leader_board_content = []
count = 0

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

        # key
        self.key1_x = KEY1_BORN_X
        self.key1_y = KEY1_BORN_Y
        self.key2_x = KEY2_BORN_X
        self.key2_y = KEY2_BORN_Y
        self.key3_x = KEY3_BORN_X
        self.key3_y = KEY3_BORN_Y
        self.key4_x = KEY4_BORN_X
        self.key4_y = KEY4_BORN_Y

        self.key_width = 32
        self.key_height = 32

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
        self.maze_leaderboard_img = pygame.image.load(LEADERBOARD_IMG).convert_alpha()
        self.game_map_img = pygame.image.load(MAZE_MAP_IMG).convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)
        self.game_block_group = self.game_map.make_block_group(MAZE_MAP, GAME_TILE_SIZE)
        # initialise hero
        self.hero_fulimg = pygame.image.load(CHARACTER_IMG).convert_alpha()
        self.hero_rect = Rect(self.hero_born_x, self.hero_born_y, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_fulimg, self.hero_rect, GAME_TILE_SIZE)
        # Set font size
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)

        # initialise rat
        self.rat_fulimg = pygame.image.load(RAT_IMG).convert_alpha()

        # start rat at particular space
        self.rat_rect = Rect(RAT_BORN_X, RAT_BORN_Y, GAME_TILE_SIZE, GAME_TILE_SIZE)

        # pretty sure that the rat_rect includes the x,y for start, not the last 2 params of Hero
        self.rat = Hero(self.rat_fulimg, self.rat_rect, GAME_TILE_SIZE)

        # key
        self.key_fulimg = pygame.image.load(KEY_IMG).convert_alpha()
        # key 1
        self.key1_rect = Rect(self.key1_x, self.key1_y, self.key_width, self.key_height)
        self.key1 = Key(self.key_fulimg, self.key1_rect, GAME_TILE_SIZE)
        # key 2
        self.key2_rect = Rect(self.key2_x, self.key2_y, self.key_width, self.key_height)
        self.key2 = Key(self.key_fulimg, self.key2_rect, GAME_TILE_SIZE)
        # key 3
        self.key3_rect = Rect(self.key3_x, self.key3_y, self.key_width, self.key_height)
        self.key3 = Key(self.key_fulimg, self.key3_rect, GAME_TILE_SIZE)
        # key 4
        self.key4_rect = Rect(self.key4_x, self.key4_y, self.key_width, self.key_height)
        self.key4 = Key(self.key_fulimg, self.key4_rect, GAME_TILE_SIZE)


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
        win_time = 0

        get_key1 = False
        get_key2 = False
        get_key3 = False
        get_key4 = False
        key1_num = 1
        key2_num = 2
        key3_num = 3
        key4_num = 4

        key1_count = 0
        key2_count = 0
        key3_count = 0
        key4_count = 0


        # main game loop
        while 1:
            if game_over and key1_count == 1 and key2_count == 1 and key3_count == 1 and key4_count == 1:
                global count, leader_board_content
                # hold the win screen
                if win_time == 0:
                    win_time = pygame.time.get_ticks()
                    # show the win background
                    self.screen.blit(self.maze_win_img, (0, 0))
                    # show the winner name and time remaining
                    self.screen.blit(self.font.render(NICKNAME_TEXT + self.nickname, True, WHITE), NICKNAME_LOCATION)
                    self.screen.blit(self.font.render(text_clock, True, WHITE), (NICKNAME_LOCATION[0], NICKNAME_LOCATION[1]+ NICKNAME_LEADING))

                now = pygame.time.get_ticks()
                if win_time > 0 and now > (win_time + MAZE_WIN_HOLDSCREEN):

                    # position of each line of the leaderboard
                    # show the leaderboard background
                    self.screen.blit(self.maze_leaderboard_img, (0, 0))

                    # Set font size
                    self.font = pygame.font.Font(None, LEADER_BOARD_FONT_SIZE)
                    x = LEADER_BOARD_X
                    y = LEADER_BOARD_Y

                    # position the leaderboard names and scores
                    for i in leader_board_list_of_strings:
                        lb_name_and_score = i.split(",")
                        lb_name = lb_name_and_score[0]
                        lb_score = lb_name_and_score[1][:-1]
                        self.screen.blit(self.font.render(lb_name, True, WHITE), (x, y))
                        self.screen.blit(self.font.render(lb_score, True, WHITE), (x+LEADER_BOARD_COLUMN_OFFSET, y))
                        y += LEADER_BOARD_LEADING
                    # put last score below in case its not on the leaderboard
                    last_score_txt = self.font.render(LEADER_BOARD_LAST_TEXT + self.nickname + ", " + text_clock, True, WHITE)
                    last_score_txt_rect = last_score_txt.get_rect(center=(SCREEN_SIZE[0]/2, LEADER_BOARD_LAST_SCORE_LOCATION_Y))
                    self.screen.blit(last_score_txt, last_score_txt_rect)
                pygame.display.update()
                self.clock.tick(self.fps)


                for m in pygame.event.get():
                    if m.type == QUIT:
                        exit()
                    if m.type == KEYDOWN:
                        exit()
                # get the result and write into txt file
                if(count == 0):
                    # leader_board_content = LeaderBoard.board_input_result(self.nickname, int(counter))
                    leader_board_list_of_strings = LeaderBoard.board_input_result(self.nickname, int(counter))
                    count += 1

                pygame.display.update()
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

            # draw key
            if not get_key1:
                self.key1.draw_keys(self.screen, key1_num)
            if not get_key2:
                self.key2.draw_keys(self.screen, key2_num)
            if not get_key3:
                self.key3.draw_keys(self.screen, key3_num)
            if not get_key4:
                self.key4.draw_keys(self.screen, key4_num)

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
            game_over, has_got_key1, has_got_key2, has_got_key3, has_got_key4 = self.hero.hero_moving(self.screen, press_keys, self.game_block_group, SCREEN_SIZE[0], SCREEN_SIZE[1], WIN_BLOCK_FROM_END, GAME_TILE_SIZE)
            if not get_key1:
                get_key1 = has_got_key1
                key1_count = 0
            if get_key1:
                key1_count = 1

            if not get_key2:
                get_key2 = has_got_key2
                key2_count = 0
            if get_key2:
                key2_count = 1

            if not get_key3:
                get_key3 = has_got_key3
                key3_count = 0
            if get_key3:
                key3_count = 1

            if not get_key4:
                get_key4 = has_got_key4
                key4_count = 0
            if get_key4:
                key4_count = 1

            # collision detection
            lose_game = self.collide(self.rat_rect, self.hero_rect, GAME_TILE_SIZE)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":

    Game(GAME_TITLE, SCREEN_SIZE[0], SCREEN_SIZE[1], nickname = startbox())
