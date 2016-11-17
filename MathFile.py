import math

#Data

class Point2():                                 #2D - Point
    def __init__(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

    def setCoords(self, x, y):
        self.xCoor = x
        self.yCoor = y
        
class Point3():                                 #3D - Point
    def __init__(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor
    
    def getZ(self):
        return self.zCoor

    def setCoords(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

class Vector2():                                 # 2D - Vector
    def __init__(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

class Vector3():                                 # 3D - Vector
    def __init__(self, x, y, z):
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

    def getZ(self):
        return self.zCoor

    def show(self):
        print(round(self.xCoor, 2))
        print(round(self.yCoor, 2))
        print(round(self.zCoor, 2))
        print()

    def negate(self):
        return Vector3(self.xCoor * -1,self.yCoor * -1,self.zCoor * -1,)

    def showValue(self):
        print(round(math.sqrt(math.sqrt(self.xCoor**2+self.yCoor**2)**2+self.zCoor**2)), 2)
# Methods

class V2Functions():
    # 2D - Functions
    
    def generateVector2(self, point1, point2):
        return Vector2((point2.getX() - point1.getX()), (point2.getY() - point1.getY()))
    
    def addVectors2(self, vec1, vec2):
        return Vector2((vec1.getX() + vec2.getX()), (vec1.getY() + vec2.getY()))

    def addPointAndVector2(self, point, vec):
        return Point2((point.getX() + vec.getX()), (point.getY() + vec.getY()))
        
    def multiplyVector2(self, factor, vec):
        return Vector2(factor * vec.getX(), factor * vec.getY())
    
class V3Functions():

    def generateVector3(self, point1, point2):
        return Vector3((point2.getX() - point1.getX()), (point2.getY() - point1.getY()), (point2.getZ() - point1.getZ()))
    
    def addVectors3(self, vec1, vec2):
        return Vector3((vec1.getX() + vec2.getX()), (vec1.getY() + vec2.getY()), (vec1.getZ() + vec2.getZ()))

    def addPointAndVector3(self, point, vec):
        return Point3((point.getX() + vec.getX()), (point.getY() + vec.getY()), (point.getZ() + vec.getZ()))
        
    def multiplyVector3(self, factor, vec):
        return Vector3(factor * vec.getX(), factor * vec.getY(), factor * vec.getZ())


    # math.

    def rotationTypeX(self, angle, vec):

        X = vec.getX()
        Y = vec.getY()
        Z = vec.getZ()


        newX = X
        newY = math.cos(angle)*Y-math.sin(angle)*Z
        newZ = math.sin(angle)*Y+math.cos(angle)*Z


        return Vector3(newX, newY, newZ)

    def rotationTypeY(self, angle, vec):

        X = vec.getX()
        Y = vec.getY()
        Z = vec.getZ()


        newX = math.cos(angle) * X + math.sin(angle) * Z
        newY = Y
        newZ = -math.sin(angle) * X + math.cos(angle) * Z

        return Vector3(newX, newY, newZ)

    def rotationTypeZ(self, angle, vec):
        X = vec.getX()
        Y = vec.getY()
        Z = vec.getZ()

        newX = math.cos(angle) * X - math.sin(angle) * Y
        newY = math.sin(angle) * X + math.cos(angle) * Y
        newZ = Z

        return Vector3(newX, newY, newZ)


def convertPoint3ToPoint2(ZP, point):
    XLineVector = Vector2(-0, 0)#Vector2(-(0.5/math.sqrt(2)), (0.5/math.sqrt(2)))        # For illustration
    YLineVector = Vector2(1, 0)
    ZLineVector = Vector2(0, 1)

    x = ZP.getX() + point.getX() * XLineVector.getX() + point.getY() * YLineVector.getX() + point.getZ() * ZLineVector.getX()
    y = ZP.getY() + point.getX() * XLineVector.getY() + point.getY() * YLineVector.getY() + point.getZ() * ZLineVector.getY()

    return Point2(x, y)