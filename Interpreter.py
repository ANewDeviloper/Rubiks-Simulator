# -*- coding: utf8 -*-

import Dicts
from MathFile import convertPoint3ToPoint2, generateVector3, generateVector2


class Constructor:
    def __init__(self, cs, cubeModel, canvas):
        self.CS = cs
        self.Cube = cubeModel
        self.Canvas = canvas

    # Basic drawing methods

    def drawLine2(self, point, vector, color="black"):
        self.Canvas.create_line(point.getX(), point.getY(),  # Start-XY
                                point.addVec(vector).getX(),  # End-X
                                point.addVec(vector).getY(),  # End-Y
                                fill=color, width=3)

    def drawSquare2(self, point1, point2, point3, point4, color="black"):
        self.Canvas.create_polygon(point1.getX(), point1.getY(),  #
                                   point2.getX(), point2.getY(),  # Color and Form
                                   point3.getX(), point3.getY(),  # of the
                                   point4.getX(), point4.getY(),  # polygon
                                   fill=color)  #

        self.drawLine2(point1, generateVector2(point1, point2))  #
        self.drawLine2(point2, generateVector2(point2, point3))  # Outline of the
        self.drawLine2(point3, generateVector2(point3, point4))  # polygon
        self.drawLine2(point4, generateVector2(point4, point1))  #

    def drawLine3(self, point, vector, color="black"):
        startPoint2 = convertPoint3ToPoint2(point)  # Get 2D start-point
        endPoint2 = convertPoint3ToPoint2(point.addVec(vector))  # Get 2D end-point

        newVec = generateVector2(startPoint2, endPoint2)  # Generate the Vector

        self.drawLine2(startPoint2, newVec, color)  # Call drawLine2

    def drawSquare3(self, point1, point2, point3, point4, color="black"):
        # Draws a 3D Square
        point1 = convertPoint3ToPoint2(point1)  #
        point2 = convertPoint3ToPoint2(point2)  # Convert all 3DPoints
        point3 = convertPoint3ToPoint2(point3)  # to 2DPoints
        point4 = convertPoint3ToPoint2(point4)  #

        self.drawSquare2(point1, point2, point3, point4, color)  # Call drawSquare2

    # Cube drawing methods

    def generateDict3D(self):
        ret = {}
        var = 0
        for i in range (0,8):
            ret.update({i : self.CS.getPoint(3*i + var)})
            if i == 3:
                var = 24
        return ret

    def findSmallX(self, dict):

        # Returns the smallest x found in the given dict (Dict consists of Points)

        searchedValue = None

        for key in dict:
            cuValue = dict.get(key).getX()

            if searchedValue == None:
                searchedValue = cuValue
            elif cuValue < searchedValue:
                searchedValue = cuValue

        return searchedValue

    def generateUnallowedArray(self, x, dict):
        ret = []
        for key in dict:
            if dict.get(key).getX() == x:
                ret.append(key)

        return ret

    def drawer3D(self):
        points = self.generateDict3D()
        unallowed = self.generateUnallowedArray(self.findSmallX(points), points)

        for i in range(0, 6):
            if \
            Dicts.pointDict.get(i)[0] not in unallowed and Dicts.pointDict.get(i)[1] not in unallowed and \
            Dicts.pointDict.get(i)[2] not in unallowed and Dicts.pointDict.get(i)[3] not in unallowed:
                OP = points.get(Dicts.pointDict.get(i)[0])
                cuOP = OP
                vec1 = generateVector3(cuOP, points.get(Dicts.pointDict.get(i)[1]))
                vec2 = generateVector3(cuOP, points.get(Dicts.pointDict.get(i)[3]))
                for d in range(0, 9):
                    P1 = cuOP.addVec(vec1.multiply(1 / 3))
                    P2 = P1.addVec(vec2.multiply(1 / 3))
                    P3 = cuOP.addVec(vec2.multiply(1 / 3))
                    self.drawSquare3(cuOP, P1, P2, P3,
                                     self.Cube.getSideByPosition(Dicts.SideNames.get(i)).Content.get(d))
                    if (d + 1) % 3 == 0:
                        OP = OP.addVec(vec2.multiply(1 / 3))
                        cuOP = OP
                    else:
                        cuOP = cuOP.addVec(vec1.multiply(1 / 3))

    # Animation methods

    def generateSquare(self, arr):
        ret = {}
        for i in range(0, len(arr)):
            ret.update({i: self.CS.getPoint(arr[i])})
        return ret

    def generateSquareArray(self, method):
        var = list(Dicts.methodToPointDict.get(method))
        ret = var
        for i in range(0, 3):
            ret[i] = Dicts.partSquareDict.get(var[i])
        return ret

    def squareOrder(self, squareArr):
        ret = []
        squares = [0, 1, 2]
        for d in range(0, 3):
            square = squares[0]
            for i in range(0, len(squares)):
                if squareArr[squares[i]].get(0).getX() <= squareArr[square].get(0).getX():
                    square = squares[i]


            ret.append(square)
            squares.remove(square)

        return ret

    def drawSquare(self, square, ID):
        points = square
        unallowed = self.generateUnallowedArray(self.findSmallX(points), points)

        for i in range(0, 6):
            count = -1
            if \
            Dicts.pointDict.get(i)[0] not in unallowed and Dicts.pointDict.get(i)[1] not in unallowed and \
            Dicts.pointDict.get(i)[2] not in unallowed and Dicts.pointDict.get(i)[3] not in unallowed:
                OP = points.get(Dicts.pointDict.get(i)[0])
                cuOP = OP
                vec1 = generateVector3(cuOP, points.get(Dicts.pointDict.get(i)[1]))
                vec2 = generateVector3(cuOP, points.get(Dicts.pointDict.get(i)[3]))
                f1 = 3
                f2 = 3

                if vec1.getValue() < self.CS.cubeX.getValue():
                    f1 =1
                else:
                    vec1 = vec1.multiply(1/3)
                if vec2.getValue() < self.CS.cubeX.getValue():
                    f2 =1
                else:
                    vec2 = vec2.multiply(1/3)

                count1 = 0
                count2 = 0

                while count2 < f2:
                    count1 += 1
                    P1 = cuOP.addVec(vec1)
                    P2 = P1.addVec(vec2)
                    P3 = cuOP.addVec(vec2)
                    count += 1
                    self.drawSquare3(cuOP, P1, P2, P3,
                                        self.Cube.getSideByPosition(Dicts.SideNames.get(i)).getContent().get(list(Dicts.partSquareC.get(ID).get(i))[count]))
                    cuOP = cuOP.addVec(vec1)

                    if count1==f1:
                        count1 = 0
                        count2 +=1
                        cuOP = OP.addVec(vec2.multiply(count2))


    # Squares are not Cubes...

    # Other methods

    def updateData(self, cs, cubeModel):
        self.CS = cs
        self.Cube = cubeModel