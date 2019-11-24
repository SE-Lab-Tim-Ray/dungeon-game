# block class used to create array of rectangles for walls
class Block:
    def __init__(self, rect):  # TC remove image
        # self.img = img # TC remove image
        self.rect = rect


# load the maze image to the screen
def draw_maze_to_screen(screen, map_image, pygame):
    # bg on screen
    screen.blit(pygame.image.load(map_image).convert(), (0, 0))


def create_maze_map(maze_map_file, tile_size, pygame):
    # create temp list
    block_group_local = []

    # initialise list
    block_group_local.clear()

    # read file
    my_maze_file = open(maze_map_file, "r")

    # read the texgt file into list of lines
    mazelines = my_maze_file.read().splitlines()
    my_maze_file.close()

    # getting length of list
    num_lines = len(mazelines)

    # assume all line lengths are the same as top line
    maze_map_width = len(mazelines[0])
    maze_map_height = num_lines

    # load maze map
    for i in range(maze_map_height): #
        for j in range(maze_map_width): #
            if mazelines[i][j] == str(1):
                block = Block(pygame.Rect(tile_size * j, tile_size * i, tile_size, tile_size))
                block_group_local.append(block)  # append block into block group


    # create winning square bottom right
    block_final = Block(pygame.Rect((maze_map_width * tile_size)-tile_size , (maze_map_height * tile_size)-tile_size , tile_size, tile_size))

    # add wining square to group
    block_group_local.append(block_final)

    return block_group_local
