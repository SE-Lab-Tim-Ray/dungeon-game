#Leaderboard part for the game.
import tkinter as tk
class board:
    '''
    The board will be displayed after the player finish the game. It will shows the nickname of the player
    and the time he used.

    '''
    def __init__(self):


    def draw_start_board(self, self.screen, self.board_x, self.board_y):

class startbox:
    """
    This is the function at the beginning of the game. Pop up a box where players can input his name.
    """

    def __init__(self):
    #inputbox width and height
        input_box = tk.Tk()
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



    def draw_start_board(self, self.screen, self.board_x, self.board_y):
