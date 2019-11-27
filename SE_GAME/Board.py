import tkinter as tk

def startbox():
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
    start_button = tk.Button (input_box, text = "Start", width = 20, command=update())
    start_button.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
    #the box show on the screen continually
    tk.mainloop()

    return input_box_text.get()