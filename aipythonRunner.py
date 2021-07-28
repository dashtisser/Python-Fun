import tkinter as tk
import os


def AIsnake():
    os.system('python ai_version.py')

def DIno():
    os.system('python game.py')

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()
window.title("PYTHON AI FUN")



button = tk.Button(frame, 
                   text="Ai snake",
                   command=AIsnake)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                    text="Chrome Dino AI",
                    command=DIno)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Quit",
                   fg="darkblue",
                   command=quit)
slogan.pack(side=tk.BOTTOM)


window.mainloop()