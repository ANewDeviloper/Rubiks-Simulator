class Point2():                                 #OP = Orientation Point
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

class Vector2():                                 #OP = Orientation Point
    def __init__(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

class V2Functions():
    
    def generateVector2(self, point1, point2):
        return Vector2((point2.getX() - point1.getX()), (point2.getY() - point1.getY()))
    
    def addVectors2(self, vec1, vec2):
        return Vector2((vec1.getX() + vec2.getX()), (vec1.getY() + vec2.getY()))

    def addPointAndVector2(self, point, vec):
        return Point2((point.getX() + vec.getX()), (point.getY() + vec.getY()))
        
    def multiplyVector2(self, factor, vec):
        return Vector2(factor * vec.getX(), factor * vec.getY())
