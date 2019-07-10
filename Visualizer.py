from tkinter import *
from Model.Map import *

basic_size = 100
road_size = 25
car_size = 35
background_color = '#33a300'
road_color = '#455862'
car_color = '#4DA6FF'
master = Tk()


class Visulaizer:
    def __init__(self, map):
        self.canvas = Canvas(master, width=map.size.x * basic_size, height=map.size.y * basic_size)
        self.canvas.configure(background=background_color)
        self.canvas.pack()
        for road in map.roads:
            self.drawRoad(road)

    def upadte(self, map):
        self.drawCar(map.car)

    def drawRoad(self, road):

        self.canvas.create_rectangle(road.start.x * basic_size, road.start.y * basic_size, road.end.x * basic_size,
                                road.end.y * basic_size, fill=road_color, width=road_size)

    def drawCar(self, car):
        self.canvas.create_rectangle(car.position.x * basic_size - car_size, car.position.y * basic_size - car_size, car.position.x * basic_size + car_size, car.position.y * basic_size + car_size, fill=car_color)
        self.canvas.mainloop()