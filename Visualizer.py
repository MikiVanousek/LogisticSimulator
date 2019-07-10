from tkinter import *
from Model.Map import *

canvas_width = 1500
canvas_height = 900

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()
w.create_rectangle(50, 50, 200, 100, fill='#476042')
w.create_line(0, canvas_height/2, canvas_width, canvas_height/2)
mainloop()

def draw(self, map):
