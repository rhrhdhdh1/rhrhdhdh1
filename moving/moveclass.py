import math
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def PointPrint(self):
        print('현재 위치는({},{})'.format(self.__x, self.__y))

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getXY(self):
        return self.__x, self.__y


class Unit:
    def __init__(self, location = Point2D(), speed = 1):
        self.__location = location
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def getLocation(self):
        return self.__location

    def setSpeed(self, speed):
        self.__speed = speed


    def lenge(self, p1):
        a1 = self.__location.getX()
        a2 = p1.getX()
        b1 = self.__location.getY()
        b2 = p1.getY()

        a = a1 - a2
        b = b1 - b2
        #        c = (a**2 + b**2)**0.5
        #        c = math.sqrt(a**2 + b**2)
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

        return a, a1, b, b1, c

    def move1(self, p1, T):
        a, a1, b, b1, c = self.lenge(p1)
        t = c/self.__speed
        if T < t:
            x = a1 - (a/t*T)
            y = b1 - (b/t*T)

            self.__location.setXY(x, y)

        else:
            x = a1 - a
            y = b1 - b

            self.__location.setXY(x, y)

        self.__location.PointPrint()
    def time(self, p1):
        a, a1, b, b1, c = self.lenge(p1)
        t = c/self.__speed

        return t

    def

class lenge1:

    def __init__(self, u, u1):
        self.u = u
        self.u1 = u1

    def lenge(self):
        a1 = self.u.getX()
        a2 = self.u1.getX()
        b1 = self.u.getY()
        b2 = self.u1.getY()

        a = a1 - a2
        b = b1 - b2
        #        c = (a**2 + b**2)**0.5
        #        c = math.sqrt(a**2 + b**2)
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

        return c



