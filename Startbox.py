import tkinter as tk

"""
global variables
NICKNAME : store the nickname player input and print in the leaderboard
"""
NICKNAME = ''

"""
The startbox is the function before the main game, the player should input his nickname and click start button to 
start game
The close_the_window function is to connect to the start game button, close the start box and begin the game.
"""
def startbox():
    #inputbox width and height
    input_box = tk.Tk()
    # we can add parameters for the position of the box
    input_box.geometry('400x300')
    #title of the inputbox
    input_box.title('Start Game')
    def close_the_window():
        global NICKNAME
        NICKNAME = input_box_text.get()
        #close the start box
        input_box.destroy()
    #text show in the box
    show_var = "Please input your nickname: "
    input_box_show_var = tk.Label(input_box, height = 3, width = 50, text=show_var)
    input_box_show_var.pack(side=tk.TOP, fill=tk.X, expand=tk.NO)
    #the entry text box
    input_box_text = tk.Entry(input_box)
    input_box_text.pack(anchor=tk.CENTER, fill=tk.X, expand=tk.YES)
    #the button to start game
    start_button = tk.Button(input_box, text="Click to Start", width=20, command=lambda: close_the_window())
    start_button.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
    #the box show on the screen continually
    tk.mainloop()