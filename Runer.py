import tkinter as tk
import os
    

def Human():
    os.system('python Snakegame.py')

def AI():
    os.system('python ai_version.py')

def SuperFast():
    os.system('python SuperFastSnakeGame.py')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()




button = tk.Button(frame, 
                   text="Ai version",
                   command=AI)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Human",
                   command=Human)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                    text="Super fast Human",
                    command=SuperFast)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Quit",
                   fg="red",
                   command=quit)
slogan.pack(side=tk.BOTTOM)


root.mainloop()