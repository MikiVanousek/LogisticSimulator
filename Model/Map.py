import random

class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, anotherVector):
        return Vector(self.x + anotherVector.x, self.y + anotherVector.y)

class Road:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Car:
    def __init__(self, position):
        self.position = position


class Package:
    def __init__(self, position, destinatino):
        self.position = position
        self.destination = destinatino

class Map:
    def __init__(self, w, h):
        self.size = Vector(w, h)
        self.car = Car(self.getRandomVectorOnMap())
        self.packages = []
        self.roads = []


        self.fillWithRoads()


    def fillWithRoads(self):
        up = Vector(1, 0)
        right = Vector(0, 1)
        for x in range(self.size.x):
            for y in range(self.size.y):
                position = Vector(x, y)
                if x != self.size.x:
                    self.roads.append(Road(position, position.plus(right)))
                if y != self.size.y:
                    self.roads.append(Road(position, position.plus(up)))

    def generatePackage(self):
        self.packages.append(Package(self.getRandomVectorOnMap(), self.getRandomVectorOnMap()))

    def getRandomVectorOnMap(self):
        return Vector(random.randint(0, self.size.x), random.randint(0, self.size.y))