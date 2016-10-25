from tkinter import *
import CubeModel

"""For the construction of the Cube"""

class OP():                                 #OP = Orientation Point
    def __init__(self, x, y, side = None):
        self.xCoor = x
        self.yCoor = y
        self.ID = side

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

    def getID(self):
        return self.ID
    
class Vector():                                 #OP = Orientation Point
    def __init__(self, OP1, OP2):
        self.xCoor = (OP2.getX() - OP1.getX())
        self.yCoor = (OP2.getY() - OP1.getY())

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor


    
def createOPsForFlatDrawing():
    ret = []
    cuX = 100   #CurrentX
    chX = 150   #ChangeX
    cuY = 200   #CurrentY
    chY = 0     #ChangeY
    for i in range(0, 6):
        ret.append(OP(cuX, cuY, CubeModel.SideNames.get(i)))
        cuX += chX
        cuY += chY
        if (i+1)%4 == 0:
            cuX = 250
            chX = 0
            cuY = 50
            chY = 300
    return ret

def createOPsForIsometricDrawing():
    
    OP0 = OP(275, 275)
    OP1 = OP(275, 440)
    OP2 = OP(400, 330)
    OP3 = OP(400, 220)

    ret = [OP0, OP1, OP2, OP3]
    
    return ret
    
def drawSideFlat(canvas, side, op):
    xCoor = op.getX()
    yCoor = op.getY()
    Content = side.getContent()

    for key in Content:
        canvas.create_rectangle(xCoor, yCoor, (xCoor + 50), (yCoor + 50), fill=Content.get(key))
        xCoor += 50
        if (key+1)%3 == 0:
            xCoor = op.getX()
            yCoor += 50

def drawCubeFlat(canvas,cubeModel, OPList):
    for i in range(0,6):
       drawSideFlat(canvas, cubeModel.getSideByPosition(CubeModel.SideNames.get(i)), OPList[i])

def drawCubeIsometric(canvas,cubeModel, OPList):
    xCoor0 = OPList[0].getX()
    yCoor0 = OPList[0].getY()
    xCoor1 = OPList[1].getX()
    yCoor1 = OPList[1].getY()
    xCoor2 = OPList[2].getX()
    yCoor2 = OPList[2].getY()
    xCoor3 = OPList[3].getX()
    yCoor3 = OPList[3].getY()
    
    vec1 = Vector(OPList[0], OPList[1])
    vec2 = Vector(OPList[0], OPList[2])
    vec3 = Vector(OPList[0], OPList[3])
    
    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec1.getX()),(yCoor0 + vec1.getY()))
    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec2.getX()),(yCoor0 + vec2.getY()))
    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec3.getX()),(yCoor0 + vec3.getY()))
    canvas.create_line(xCoor1, yCoor1, (xCoor1 + vec2.getX()),(yCoor1 + vec2.getY()))
    

    xCoor0 += 2 * (xCoor3 - xCoor0)
    xCoor1 += 2 * (xCoor3 - xCoor1)

    vec1 = Vector(OP(xCoor0, yCoor0), OP(xCoor1, yCoor1))
    vec2 = Vector(OP(xCoor0, yCoor0), OPList[2])
    vec3 = Vector(OP(xCoor0, yCoor0), OPList[3])

    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec1.getX()),(yCoor0 + vec1.getY()))
    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec2.getX()),(yCoor0 + vec2.getY()))
    canvas.create_line(xCoor0, yCoor0, (xCoor0 + vec3.getX()),(yCoor0 + vec3.getY()))
    canvas.create_line(xCoor1, yCoor1, (xCoor1 + vec2.getX()),(yCoor1 + vec2.getY()))

    canvas.create_line(xCoor2, yCoor2, (xCoor2 + vec1.getX()),(yCoor2 + vec1.getY()))


def drawNewCube(drawMethodSetter, canvas,cubeModel, oPs, method):
    canvas.delete(ALL)
    cubeModel.changeCube(method)
    if drawMethodSetter == 0:
        drawCubeFlat(canvas,cubeModel, oPs)
    if drawMethodSetter == 1:
        drawCubeIsometric(canvas,cubeModel, oPs)
