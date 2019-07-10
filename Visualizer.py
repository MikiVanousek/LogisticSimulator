from tkinter import *
from Model.Map import *
basic_size = 100
road_size = 25
background_color='#33a300'
road_color='#455862'



def draw(map):
    master = Tk()
    canvas = Canvas(master, width=map.size.x * basic_size, height=map.size.y * basic_size)
    canvas.configure(background=background_color)
    canvas.pack()
    canvas.create_line(0, 100, 200, 100, fill=road_color)
    for road in map.roads:
        end = road.road.plus(road.start)
        canvas.create_rectangle(road.start.x * basic_size, road.start.y * basic_size, end.x * basic_size, end.y * basic_size, fill=road_color, width=road_size)
    mainloop()
