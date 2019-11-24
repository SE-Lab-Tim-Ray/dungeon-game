import random, math, pygame
from pygame.locals import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_NAME = "Jeff's Lair"


#print_text function
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#main program begins
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_NAME)
font = pygame.font.Font(None, 18)

# read file
myfile = open("../code_resources/maze.txt", "r")

# read the texgt file into list of lines
mazelines = myfile.read().splitlines()
myfile.close()


# getting length of list
num_lines = len(mazelines)

# assume all line lengths are the same as top line
maze_pattern_width = len(mazelines[0])
maze_pattern_height = num_lines

# work out tile width and height
tile_width = SCREEN_WIDTH // maze_pattern_width
tile_height = SCREEN_HEIGHT // maze_pattern_height

#load bitmaps
tile = pygame.image.load("../code_resources/plain_tile.png").convert()
tile = pygame.transform.scale(tile, (tile_width, tile_height))

current_x = 0
current_y = 0

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(num_lines):
    len_j = len(mazelines[i])
    this_line = mazelines[i]
    for j in range(len_j):
        if this_line[j] == "1":
            screen.blit(tile, (current_x, current_y))

        current_x += tile_width
    current_y += tile_height
    current_x = 0
# # set y position to zero
# posy = 0
#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        exit()
    #     if press key d, move down
    # if keys[pygame.K_d]:
    #     posy += 100

    #draw background - position y dynamic
    # screen.blit(space, (100,posy))
    # print_text(font, 200, 200, char)
    pygame.display.update()
