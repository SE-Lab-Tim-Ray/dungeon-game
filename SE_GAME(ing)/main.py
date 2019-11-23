from temp_folder.core_code import *
from Board import *
from Timer import *
from Hero import *
from GameMap import *


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
        self.start_board = Board()
        self.start_board.draw_start_board()
        self.game_map_img = pygame.image.load('./resources/images/maze1.png').convert_alpha()
        self.game_map = GameMap(self.game_map_img, 0, 0)

        self.game_map.load_walk_file('./resources/maps/maze1.txt')

        self.timer = Timer()
        self.hero_img = pygame.image.load('./resources/images/char1.png').convert_alpha()
        self.hero_rect = Rect(0, 0, self.hero_width, self.hero_height)
        self.hero = Hero(self.hero_img, self.hero_rect, self.hero_born_x, self.hero_born_y)
        self.leader_board = Board()


        # **************Version 2******************
        self.rat = None
        self.spider = None
        self.bat = None
        self.stone = None


    def update(self):
        while 1:
            self.clock.tick(self.fps)

            # display update
            # draw the map
            self.game_map.draw_map(self.screen)
            # Hero
            self.hero.draw_hero(self.screen, self.game_map.x, self.game_map.y)
            # Timer
            self.timer.draw_timer()

            # game map roll
            self.game_map.map_roll(self.hero.hero_coordinate_x, self.hero.hero_coordinate_y)

            # logic update
            press_keys = pygame.key.get_pressed()
            self.hero.hero_moving(press_keys)

            self.event_handler()
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


if __name__ == "__main__":
    Game("Demo", 800, 600)

