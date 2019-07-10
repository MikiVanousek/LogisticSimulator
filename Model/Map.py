class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Road:
    def __init__(self, startVector, roadVector):
        self.start = startVector
        self.road = roadVector


class Map:
    size = Vector(0, 0)
    roads = []

    def __init__(self, w, h):
        size = Vector(w, h)
        self.fillWithRoads()

    def fillWithRoads(self):
        up = Vector(1, 0)
        down = Vector(-1, 0)
        right = Vector(0, 1)
        left = Vector(0, -1)
        for x in range(self.size.x):
            for y in range(self.size.y):
                position = Vector(x, y)

                if x != self.size.x:
                    self.roads.append(Road(position, up))
                if x != 0:
                    self.roads.append(Road(position, down))
                if y != self.size.y:
                    self.roads.append(Road(position, right))
                if y != 0:
                    self.roads.append(Road(position, left))

class Car:
    def __init__(self):