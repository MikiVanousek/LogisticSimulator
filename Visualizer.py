from tkinter import *
from Model.Map import *
basic_size = 30
road_size = 5
background_color='#33a300'
road_color='#455862'



def draw(map):
    master = Tk()
    canvas = Canvas(master, width=map.size.x * basic_size, height=map.size.y * basic_size)
    canvas.configure(background=background_color)
    canvas.pack()
    for road in map.roads:
        canvas.create_rectangle(road.start.x, road.start.y, road.road.x, road.road.y, fill=road_color)
    mainloop()
