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


def changeCube(canvas,cubeModel, oPs, method):
    if method == "TCR":
        cubeModel.turnCubeRight()
    if method == "TCL":
        cubeModel.turnCubeLeft()
    if method == "TCU":
        cubeModel.turnCubeUp()
    if method == "TCD":
        cubeModel.turnCubeDown()
    if method == "RCR":
        cubeModel.rotateCubeRight()
    if method == "RCL":
        cubeModel.rotateCubeLeft()
        
    if method == "TLPU":
        cubeModel.turnLeftPartUp()
    if method == "TLPD":
        cubeModel.turnLeftPartDown()
    if method == "TVMPU":
        cubeModel.turnVerticalMiddlePartUp()
    if method == "TVMPD":
        cubeModel.turnVerticalMiddlePartDown()
    if method == "TRPU":
        cubeModel.turnRightPartUp()
    if method == "TRPD":
        cubeModel.turnRightPartDown()

    if method == "TFPR":
        cubeModel.turnFrontPartRight()
    if method == "TFPL":
        cubeModel.turnFrontPartLeft()
    if method == "TOMPR":
        cubeModel.turnOtherMiddlePartRight()
    if method == "TOMPL":
        cubeModel.turnOtherMiddlePartLeft()
    if method == "TBPR":
        cubeModel.turnBackPartRight()
    if method == "TBPL":
        cubeModel.turnBackPartLeft()

    if method == "TUPR":
        cubeModel.turnUpperPartRight()
    if method == "TUPL":
        cubeModel.turnUpperPartLeft()
    if method == "THMPR":
        cubeModel.turnHorizontalMiddlePartRight()
    if method == "THMPL":
        cubeModel.turnHorizontalMiddlePartLeft()
    if method == "TDPR":
        cubeModel.turnLowerPartRight()
    if method == "TDPL":
        cubeModel.turnLowerPartLeft()
    else:
        pass

    drawCubeFlat(canvas,cubeModel, oPs)
