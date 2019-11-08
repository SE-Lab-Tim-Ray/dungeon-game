import random, math, pygame
from pygame.locals import *

#print_text function
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#main program begins
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeff's Lair")
font = pygame.font.Font(None, 18)

#load bitmaps
tile = pygame.image.load("../Code_resources/tile.png").convert()

# read file
myfile = open("../Code_resources/maze.txt", "r")

# read the texgt file into list of lines
mazelines = myfile.read().splitlines()
myfile.close()


# getting length of list
linelength = len(mazelines)
current_x = 0
current_y = 0

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(linelength):
    len_j = len(mazelines[i])
    this_line = mazelines[i]
    for j in range(len_j):
        if this_line[j] == "0":
            print_text(font, current_x, current_y, " ")
        else:
            print_text(font, current_x, current_y, "Wall")
            screen.blit(tile, (current_x, current_y))

        current_x += 100
    current_y += 100
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
