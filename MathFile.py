# -*- coding: utf8 -*-

import math


class Point2:

    # 2D - Point

    def __init__(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def getX(self):
        return round(self.xCoor, 2)

    def getY(self):
        return round(self.yCoor, 2)

    def setCoords(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def toVector(self):
        return Vector2(self.xCoor, self.yCoor)

    def addVec(self, vec):
        return Point2(self.xCoor + vec.getX(), self.yCoor + vec.getY())


class Point3:

    # 3D - Point

    def __init__(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

    def getX(self):
        return round(self.xCoor,2)

    def getY(self):
        return round(self.yCoor,2)
    
    def getZ(self):
        return round(self.zCoor,2)

    def setCoords(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

    def toVector(self):
        return Vector3(self.xCoor, self.yCoor, self.zCoor)

    def addVec(self, vec):
        return Point3(self.xCoor + vec.getX(), self.yCoor + vec.getY(), self.zCoor + vec.getZ())


class Vector2:

    # 2D - Vector

    def __init__(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def getX(self):
        return round(self.xCoor, 2)

    def getY(self):
        return round(self.yCoor, 2)

    def show(self):
        print(round(self.xCoor, 2))
        print(round(self.yCoor, 2))
        print()

    def toPoint(self):
        return Point2(self.xCoor, self.yCoor)

    def negate(self):
        return Vector2(self.xCoor * -1,self.yCoor * -1)

    def addVec(self, vec):
        return Vector2((self.xCoor + vec.getX()),(self.yCoor + vec.getY()))

    def multiply(self, factor):
        return Vector2((self.xCoor * factor), (self.yCoor * factor))

    def showValue(self):
        print(round(math.sqrt(self.xCoor**2+self.yCoor**2), 2))


class Vector3:

    # 3D - Vector

    def __init__(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

    def getX(self):
        return round(self.xCoor, 2)

    def getY(self):
        return round(self.yCoor, 2)

    def getZ(self):
        return round(self.zCoor, 2)

    def show(self):
        print(round(self.xCoor, 2))
        print(round(self.yCoor, 2))
        print(round(self.zCoor, 2))
        print()

    def toPoint(self):
        return Point3(self.xCoor, self.yCoor, self.zCoor)

    def negate(self):
        return Vector3(self.xCoor * -1,self.yCoor * -1,self.zCoor * -1)

    def addVec(self, vec):
        return Vector3((self.xCoor + vec.getX()),(self.yCoor + vec.getY()),(self.zCoor + vec.getZ()))

    def multiply(self, factor):
        return Vector3((self.xCoor * factor), (self.yCoor * factor), (self.zCoor * factor))

    def getValue(self):
        return math.sqrt(self.xCoor**2 + self.yCoor**2 + self.zCoor**2)

    def showValue(self):
        print(round(math.sqrt(self.xCoor**2+self.yCoor**2+self.zCoor**2)), 2)

    def equals(self, vec):
        ret = False
        if self.xCoor == vec.getX():
            if self.yCoor == vec.getY():
                if self.zCoor == vec.getZ():
                    ret = True
        return ret
# Methods


def generateVector2(point1, point2):
    return Vector2((point2.getX() - point1.getX()), (point2.getY() - point1.getY()))


def generateVector3(point1, point2):
    return Vector3((point2.getX() - point1.getX()), (point2.getY() - point1.getY()), (point2.getZ() - point1.getZ()))


def rotationTypeX(angle, vec, ):

    X = vec.getX()
    Y = vec.getY()
    Z = vec.getZ()


    newX = X
    newY = math.cos(angle)*Y-math.sin(angle)*Z
    newZ = math.sin(angle)*Y+math.cos(angle)*Z


    return Vector3(newX, newY, newZ)


def rotationTypeY(angle, vec):

    X = vec.getX()
    Y = vec.getY()
    Z = vec.getZ()

    newX=math.cos(angle)*X+math.sin(angle)*Z
    newY = Y
    newZ =-math.sin(angle)*X+math.cos(angle)*Z

    return Vector3(newX, newY, newZ)


def rotationTypeZ(angle, vec):
    X = vec.getX()
    Y = vec.getY()
    Z = vec.getZ()

    newX = math.cos(angle) * X - math.sin(angle) * Y
    newY = math.sin(angle) * X + math.cos(angle) * Y
    newZ = Z

    return Vector3(newX, newY, newZ)


def rotation3(angle, rVec, oVec):

    normConstant = oVec.getValue()

    rX = rVec.getX()
    rY = rVec.getY()
    rZ = rVec.getZ()

    oX = oVec.getX()/normConstant
    oY = oVec.getY()/normConstant
    oZ = oVec.getZ()/normConstant

    X = ((oX * oX) * (1 - math.cos(angle)) + math.cos(angle))      * rX   + \
        ((oX * oY) * (1 - math.cos(angle)) + oZ * math.sin(angle)) * rY   + \
        ((oX * oZ) * (1 - math.cos(angle)) - oY * math.sin(angle)) * rZ

    Y = ((oY * oX) * (1 - math.cos(angle)) - oZ * math.sin(angle)) * rX + \
        ((oY * oY) * (1 - math.cos(angle)) + math.cos(angle))      * rY + \
        ((oY * oZ) * (1 - math.cos(angle)) + oX * math.sin(angle)) * rZ

    Z = ((oZ * oX) * (1 - math.cos(angle)) + oY * math.sin(angle)) * rX + \
        ((oZ * oY) * (1 - math.cos(angle)) - oX * math.sin(angle)) * rY + \
        ((oZ * oZ) * (1 - math.cos(angle)) + math.cos(angle))      * rZ

    return Vector3(X, Y, Z)

def convertPoint3ToPoint2(point):
    ZP=Point2(200, 250)

    XLineVector = Vector2(-0, 0)#Vector2(-(0.5/math.sqrt(2)), (0.5/math.sqrt(2)))        # For illustration
    YLineVector = Vector2(1, 0)
    ZLineVector = Vector2(0, 1)

    x = ZP.getX() + point.getX() * XLineVector.getX() + point.getY() * YLineVector.getX() + point.getZ() * ZLineVector.getX()
    y = ZP.getY() + point.getX() * XLineVector.getY() + point.getY() * YLineVector.getY() + point.getZ() * ZLineVector.getY()

    return Point2(x, y)