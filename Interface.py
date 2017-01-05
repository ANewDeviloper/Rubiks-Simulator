# -*- coding: utf8 -*-

from tkinter import *

import CubeModel
import CoordinateSystem
import Interpreter
import MathFile
import Dicts

rubiksCube = CubeModel.Cube(True)    # Cube you are working with(Currently solved)
perfectCube = CubeModel.perfectCube  # Instance of a solved cube(Constant)

# Window Setup

root = Tk()
root.geometry("1160x550")
root.minsize(1160, 550)
root.maxsize(1160, 550)
root.title("Graphical Interface")

ConstructionFrame = Frame (root, bg = "white")                      # Frame for drawings
ConstructionFrame.place(x=0, y=0, width=800, height=550)

screen = Canvas(ConstructionFrame)
screen.place(x=0, y=0, width=800, height=550)

ControlFrame = Frame(root, bg = "lightblue")                        # Frame for buttons
ControlFrame.place(x=800, y=0, width=360, height=550)

h1 = Label(ControlFrame, text="Cube:", bg="lightblue")
h1.place(x=20, y=0)

# Virtual Cubemodel Setup

offsetY = 0
offsetZ = 0

K = 150

a = 0
b = 0
c = 90

speed = 5

vecX = MathFile.Vector3(1,0,0)
vecY = MathFile.Vector3(0,1,0)
vecZ = MathFile.Vector3(0,0,1)

CS = CoordinateSystem.CS(vecX, vecY, vecZ)

CS.generateCubeVectors(K)
CS.setMVector(offsetY, offsetZ)

CS.setupDict()
CS.rotateCube(a,b,c)

Constructor = Interpreter.Constructor(CS,rubiksCube, screen)

# Control Setup

def addAngle(Index, angle = None):
    global a
    global b
    global c

    global K
    global CS
    if Index == "alpha":
        a = angle
        b = 0
        c = 0
    if Index == "beta":
        a = 0
        b = angle
        c = 0
    if Index == "gamma":
        a = 0
        b = 0
        c = angle
    if Index == "reset":
        a = 0
        b = 0
        c = 0

    CS.rotateCube(a,b,c)

    screen.delete("all")

    Constructor.updateData(CS, rubiksCube)
    Constructor.drawer3D()

def changeCube(methodNameID):
    squareArr = Constructor.generateSquareArray(Dicts.methodIDs.get(methodNameID))
    squares = []
    for i in range(0, 3):
        squares.append(Constructor.generateSquare(squareArr[i]))

    order = Constructor.squareOrder(squares)
    squares.append(squareArr[3])
    squares.append(squareArr[4])

    s1 = list(Dicts.methodToPointDict.get(Dicts.methodIDs.get(methodNameID)))[order[0]]
    s2 = list(Dicts.methodToPointDict.get(Dicts.methodIDs.get(methodNameID)))[order[1]]
    s3 = list(Dicts.methodToPointDict.get(Dicts.methodIDs.get(methodNameID)))[order[2]]

    alpha = 0
    beta = 0
    gamma = 0

    if squares[4] == 1:
        alpha = 3
    if squares[4] == 2:
        beta = 3
    if squares[4] == 3:
        gamma = 3
    if squares[4] == -1:
        alpha = -3
    if squares[4] == -2:
        beta = -3
    if squares[4] == -3:
        gamma = -3

    uOV = Constructor.CS.orientationVectors
    Constructor.CS.setOrientationVectors("cubeVectors")

    for i in range(0, 30):
        Constructor.CS.rotateCube(alpha, beta, gamma, "add")
        screen.update()
        squares[squares[3]] = Constructor.generateSquare(squareArr[squares[3]])

        Constructor.Canvas.delete("all")
        Constructor.drawSquare(squares[order[0]], s1)
        Constructor.drawSquare(squares[order[1]], s2)
        Constructor.drawSquare(squares[order[2]], s3)

        root.update_idletasks()
        root.update()

    Constructor.CS.rotateCube(-alpha * 30,-beta*30, -gamma*30, "add")
    Constructor.CS.setOrientationVectors(uOV)

    rubiksCube.changeCube(Dicts.methodIDs.get(methodNameID))
    Constructor.updateData(CS, rubiksCube)

def key(event):
    global speed
    global offsetY
    global offsetZ
    global CS

    # Rotation-control

    if event.char == '9':
        addAngle("alpha", speed)
    if event.char == '7':
        addAngle("alpha", -1 * speed)
    if event.char == '8':
        addAngle("beta", speed)
    if event.char == '2':
        addAngle("beta", -1 * speed)
    if event.char == '6':
        addAngle("gamma", -1 * speed)
    if event.char == '4':
        addAngle("gamma", speed)

    # Speed-control

    if event.char == '+':
        if speed < 16:
            speed *= 2
    if event.char == '-':
        if speed > 1:
            speed /= 2

    # Offset-control

    if event.char == 'a':
        offsetY -= speed
        CS.setMVector(offsetY, offsetZ)
        Constructor.updateData(CS, rubiksCube)
        screen.delete("all")
        Constructor.drawer3D()
    if event.char == 'd':
        offsetY += speed
        CS.setMVector(offsetY, offsetZ)
        Constructor.updateData(CS, rubiksCube)
        screen.delete("all")
        Constructor.drawer3D()
    if event.char == 'w':
        offsetZ -= speed
        CS.setMVector(offsetY, offsetZ)
        Constructor.updateData(CS, rubiksCube)
        screen.delete("all")
        Constructor.drawer3D()
    if event.char == 's':
        offsetZ += speed
        CS.setMVector(offsetY, offsetZ)
        Constructor.updateData(CS, rubiksCube)
        screen.delete("all")
        Constructor.drawer3D()

    # Axis-control

    if event.char == 'c':
        if CS.orientationVectors == "systemVectors":
            var = "cubeVectors"
        else:
            var = "systemVectors"
        CS.setOrientationVectors(var)
        Constructor.updateData(CS, rubiksCube)

root.bind_all('<Key>', key)

# Button Setup (Former Buttonland)

xCoor = 30
yCoor = 40
for i in range (0, 24):
    buttonTCR = Button(ControlFrame, text=Dicts.methodIDs.get(i), command=(lambda d: lambda:changeCube(d))(i), bg ="#0000FF")
    buttonTCR.place(x = xCoor, y = yCoor, width = 150, height = 25)
    i+=1
    if i%2 == 1:
        xCoor += 170
    else:
        xCoor -= 170
        yCoor += 35


# Final Setup

Constructor.drawer3D()

root.mainloop()
