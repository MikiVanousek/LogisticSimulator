import random

class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, anotherVector):
        return Vector(self.x + anotherVector.x, self.y + anotherVector.y)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Vector):
            return False
        return o.x == self.x and o.y == self.y


class Road:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Road):
            return False;
        return self.start == o.start and self.end == o.end or self.start == o.end and self.end == o.start


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

    def isRoad(self, position: Vector, direction: Vector) -> bool:
        road = Road(position, position.plus(direction))
        return road in self.roads

    def moveCar(self, move: Vector):
        move = Vector(1, 0)
        if self.isRoad(self.car.position, move):
            self.car.position = self.car.position.plus(move)
