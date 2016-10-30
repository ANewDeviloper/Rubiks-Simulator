from tkinter import *
import MathFile
import CubeModel
import Solver
import InterfaceMethods

"""Give this thing a Level-UP"""

methodIDs = {0  : "TCR",   1  :  "TCL",   2  :  "TCU",    3  : "TCD",    4  : "RCR",  5  : "RCL",
             6  : "TLPU",  7  :  "TLPD",  8  :  "TVMPU",  9  : "TVMPD",  10 : "TRPU", 11 : "TRPD",
             12 : "TFPR",  13 :  "TFPL",  14 :  "TOMPR",  15 : "TOMPL",  16 : "TBPR", 17 : "TBPL",
             18 : "TUPR",  19 :  "TUPL",  20 :  "THMPR",  21 : "THMPL",  22 : "TDPR", 23 : "TDPL", }


rubiksCube = CubeModel.Cube(True)  # Cube you are working with(Currently solved)
perfectCube = CubeModel.perfectCube # Instance of a solved cube(Constant)

root = Tk()
root.geometry("1160x550")
root.minsize(1160, 550)
root.maxsize(1160, 550)
root.title("Graphical Interface")

ConstructionFrame = Frame (root, bg = "white")
ConstructionFrame.place(x = 0, y = 0, width = 800, height = 550)

screen = Canvas(ConstructionFrame)
screen.place(x = 0, y = 0, width = 800, height = 550)

ControlFrame = Frame(root, bg = "lightblue")
ControlFrame.place(x = 800, y = 0, width = 360, height = 550)

h1 = Label(ControlFrame, text="Cube:", bg = "lightblue")
h1.place(x = 20, y = 0)

Constructor = InterfaceMethods.Constructor(screen, "Isometric", rubiksCube)
V2Functions = MathFile.V2Functions()

# Arguments for the Cube

OP = MathFile.Point2(125, 175) # Position of the Cube

Vector1 = MathFile.Vector2(150, 100) # Width(for Flat)
Vector2 = MathFile.Vector2(0, 150) # Height(for Flat)
Vector3 = MathFile.Vector2(150, -100)

#First Draw
Constructor.drawCubeIsometric(OP, Vector1, Vector2, Vector3)

##########################################
# WARNING | You are entering Buttonland! #
##########################################

i = 0

buttonTCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TCR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTCR.place(x = 30, y = 40, width = 150, height = 25)
i+=1

buttonTCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TCL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTCL.place(x = 200, y = 40, width = 150, height = 25)
i+=1

buttonTCU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TCU", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTCU.place(x = 30, y = 75, width = 150, height = 25)
i+=1

buttonTCD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TCD", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTCD.place(x = 200, y = 75, width = 150, height = 25)
i+=1

buttonRCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("RCR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonRCR.place(x = 30, y = 110, width = 150, height = 25)
i+=1

buttonRCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("RCL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonRCL.place(x = 200, y = 110, width = 150, height = 25)
i+=1



buttonTLPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TLPU", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTLPU.place(x = 30, y = 145, width = 150, height = 25)
i+=1

buttonTLPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TLPD", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTLPD.place(x = 200, y = 145, width = 150, height = 25)
i+=1

buttonTVMPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TVMPU", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTVMPU.place(x = 30, y = 180, width = 150, height = 25)
i+=1

buttonTVMPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TVMPD", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTVMPD.place(x = 200, y = 180, width = 150, height = 25)
i+=1

buttonTRPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TRPU", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTRPU.place(x = 30, y = 215, width = 150, height = 25)
i+=1

buttonTRPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TRPD", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTRPD.place(x = 200, y = 215, width = 150, height = 25)
i+=1



buttonTFPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TFPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTFPR.place(x = 30, y = 250, width = 150, height = 25)
i+=1

buttonTFPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TFPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTFPL.place(x = 200, y = 250, width = 150, height = 25)
i+=1

buttonTOMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TOMPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTOMPR.place(x = 30, y = 285, width = 150, height = 25)
i+=1

buttonTOMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TOMPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTOMPL.place(x = 200, y = 285, width = 150, height = 25)
i+=1

buttonTBPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TBPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTBPR.place(x = 30, y = 320, width = 150, height = 25)
i+=1

buttonTBPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TBPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTBPL.place(x = 200, y = 320, width = 150, height = 25)
i+=1



buttonTUPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TUPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTUPR.place(x = 30, y = 355, width = 150, height = 25)
i+=1

buttonTUPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TUPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTUPL.place(x = 200, y = 355, width = 150, height = 25)
i+=1

buttonTHMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("THMPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTHMPR.place(x = 30, y = 390, width = 150, height = 25)
i+=1

buttonTHMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("THMPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTHMPL.place(x = 200, y = 390, width = 150, height = 25)
i+=1

buttonTDPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TDPR", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTDPR.place(x = 30, y = 425, width = 150, height = 25)
i+=1

buttonTDPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:Constructor.drawNewCube("TDPL", OP, Vector1, Vector2, Vector3), bg = "lightblue")
buttonTDPL.place(x = 200, y = 425, width = 150, height = 25)
i+=1

buttonSolve = Button(ControlFrame, text="Solve",command=lambda: Solver.solveByTrying(rubiksCube, perfectCube), bg = "lightblue")
buttonSolve.place(x = 30, y = 460, width = 150, height = 25)

"""
buttonChangeDrawMethod = Button(ControlFrame, text="Change Drawing",command=lambda: currentDrawMethod.update(screenFC, rubiksCube, oPs, None), bg = "lightblue")
buttonChangeDrawMethod.place(x = 200, y = 460, width = 150, height = 25)
i+=1
"""
#Buttonland border


root.mainloop()
