import tkinter as tk

"""
global variables (module scope)
nickname : store the nickname player input and print in the leaderboard
"""
nickname = ''
# Constants
STARTSCREEN_SIZE = "400x300"

"""
The startbox is the function before the main game, the player should input his nickname and click start button to 
start game
The close_the_window function is to connect to the start game button, close the start box and begin the game.
"""
def startbox():
    # inputbox width and height
    startscreen = tk.Tk()

    # title of the inputbox
    startscreen.title("")

    # startscreen.image = background_image     #
    def close_the_window():
        global nickname
        nickname = input_box_text.get()
        #close the start box
        startscreen.destroy()

    # top margin
    input_box_show_var = tk.Label(startscreen, height = 3, width = 50)
    input_box_show_var.pack(side=tk.TOP, expand=tk.NO)
    input_box_show_var["bg"] = "white"

    # show text
    show_var = "Welcome to Jeff's Lair"
    input_box_show_var = tk.Label(startscreen, text=show_var, width = 23, font=(None, 24))
    input_box_show_var.pack(side=tk.TOP, expand=tk.YES)
    input_box_show_var["bg"] = "white"

    # show text
    show_var = "Enter your name: "
    input_box_show_var = tk.Label(startscreen, text=show_var, width = 23, font=(None, 18))
    input_box_show_var.pack(side=tk.TOP, expand=tk.YES)
    input_box_show_var["bg"] = "white"

    # the entry text box
    input_box_text = tk.Entry(startscreen,  font=(None, 18))
    input_box_text.pack(anchor=tk.CENTER, expand=tk.YES)
    input_box_text["bg"] = None

    # padding
    input_box_show_var = tk.Label(startscreen, height = 1, width = 50)
    input_box_show_var.pack(side=tk.TOP, expand=tk.YES)
    input_box_show_var["bg"] = "white"

    # the button to start game
    start_button = tk.Button(startscreen, text="Start", width=20, font=(None, 18), command=lambda: close_the_window())
    start_button.pack(side=tk.TOP, expand=tk.YES)

    # bottom margin
    input_box_show_var = tk.Label(startscreen, height = 3, width = 50)
    input_box_show_var.pack(side=tk.TOP, expand=tk.YES)
    input_box_show_var["bg"] = "white"

    #the box show on the screen continually
    tk.mainloop()
    return nickname
