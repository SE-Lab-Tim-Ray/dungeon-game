#Leaderboard part for the game.
import tkinter as tk
import sys, pygame
from Timer import TIMER, player_time
from pexpect import screen

global NICKNAME
leader_board_filename = "leader_board.txt"
class board:
    """
    The board will be displayed after the player finish the game. It will shows the nickname of the player
    and the time he used.
    board_get_result : You should input the nickname and player_time. The function will write the results to leaderboard
    draw_leader_board : It will print the leaderboard on the screen.
    """
    def board_get_result(self,board_nickname='NoName', board_time=player_time):
        board_nickname = NICKNAME
        board_time = TIMER - player_time
        leader_board = open(leader_board_filename,'a')
        leader_board.write(board_nickname+'    '+board_time)
        leader_board.write('\n')
        leader_board.close()

    def print_text(font, x, y, text, color=(0, 0, 0)):

        imgText = font.render(text, True, (0, 0, 0))
        screen.blit(imgText, (x - 2, y - 2))
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x, y))

    def draw_leader_board(self, self.screen, self.board_x, self.board_y):
        leader_board = open(leader_board_filename, 'r')
        read = leader_board.readlines()
        for i in read:
            print_text(pygame.font.Font(None,24),i)



class startbox:
    """
    This is the function at the beginning of the game. Pop up a box where players can input his name.
    """

    def __init__(self):
    #inputbox width and height
        input_box = tk.Tk()
    # we can add parameters for the position of the box
        input_box.geometry('400x300')
    #title of the inputbox
        input_box.title('Start Game')
    #text show in the box
        show_var = "Please input your nickname: "
        input_box_show_var = tk.Label(input_box, height = 3, width = 50, text=show_var)
        input_box_show_var.pack(side=tk.TOP, fill=tk.X, expand=tk.NO)
    #the entry text box
        input_box_text = tk.Entry(input_box)
        input_box_text.pack(anchor=tk.CENTER, fill=tk.X, expand=tk.YES)
    #the button to start game
        start_button = tk.Button (input_box, text = "Start", width = 20, command = self.get_name)
        start_button.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
    #the box show on the screen continually
        tk.mainloop()
    def get_name(self):
        NICKNAME = self.input_box_text.get()


    def draw_start_board(self, self.screen, self.board_x, self.board_y):
