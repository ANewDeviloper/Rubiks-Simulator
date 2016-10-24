from tkinter import *
import CubeModel

"""For the construction of the Cube"""

class OP():                                 #OP = Orientation Point
    def __init__(self, x, y, side):
        self.xCoor = x
        self.yCoor = y
        self.ID = side

    def getX(self):
        return self.xCoor

    def getY(self):
        return self.yCoor

    def getID(self):
        return self.ID

    
def createOPs():
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


def drawSide(canvas, side, op):
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
    canvas.delete(ALL)
    for i in range(0,6):
       drawSide(canvas, cubeModel.getSideByPosition(CubeModel.SideNames.get(i)), OPList[i])


def drawNewCube(canvas,cubeModel, oPs, method):
    cubeModel.changeCube(method)

    drawCubeFlat(canvas,cubeModel, oPs)
