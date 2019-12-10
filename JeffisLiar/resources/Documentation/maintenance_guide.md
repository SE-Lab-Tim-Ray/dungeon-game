**Jeff’s Lair - Maintenance Guide**

**Introduction**
Jeff's lair is a dungeon maze game built using the pygame module https://www.pygame.org

**Module: Main.py**\
This is the main code needed to run the game. 
 
**Constants**\
All global constants held here to fix resource locations and gameplay defaults

**Class: Game**\
Main game object built here

**.\_\_init\_\_**\
Sets up the game with given parameters:
• Screen size: 800x600 (global constants)
• How big the tiles on the maze are in px: 32px (global constants)
• Title on maze window: Jeff's Lair (global constants)
• Where the character will be placed at start: 32,32px (global constants)

Runs __init_pygame\
Runs __init_game
runs .update

**.__init_pygame**\
Loads pygame module\
• Sets the timer

**.__init_game**\
• Initialises the map\
• Initialised hero and rat

**.collide**\
Works out if 2 rectangles have hit each other, returns true if they do.

**.update**\
This is the main game loop\
2 possible ways to finish: 

**game_over== True**\  
Player finished maze, display win image and show score and nickname. Hold until quit/escape.

**lose_game == True**\
Player caught by rat, display lose image. Hold until quit/escape.

• Make the clock update every second 
• Make the clock tick
• detect collisions

**Module: Hero.py**

**Class: Hero**
Can be either hero or monster (rat)

**.hero_moving**\
Moves the character left right up and down checking for screen edges, walls and winning square.

Checks for touching the rat and returns True if caught.

**.monster_move**\
Moves the monster towards the character, returns True if caught.

**Module: GameMap.py**\

**Class: Block**\
A rectangle to form the list of rectangles that represent maze walls.

**Class: GameMap**\
Creates the logical game map from text file

**.draw_map**
Put map on screen.

**.make_block_group**
Returns a list of rectangles that represent maze walls.

**Module: Startbox.py**

**Function: Startbox**\
Creates a start screen for the user to enter their name and start the main game. Returns nickname.


 



















