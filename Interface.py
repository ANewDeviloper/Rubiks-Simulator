from tkinter import *
import CubeModel
import Solver
import InterfaceMethods

"""Give this thing a Level-UP"""

class drawMethod:

    def __init__(self, method):
        self.drawMethod = method

    def update(self, canvas, cube, OPS, method):
        self.drawMethod += 1
        if self.drawMethod > 1:
            self.drawMethod = 0
        InterfaceMethods.drawNewCube(self.drawMethod, canvas, cube, OPS, method)
        
    def get(self):
        
        return self.drawMethod

methodIDs = {0  : "TCR",   1  :  "TCL",   2  :  "TCU",    3  : "TCD",    4  : "RCR",  5  : "RCL",
             6  : "TLPU",  7  :  "TLPD",  8  :  "TVMPU",  9  : "TVMPD",  10 : "TRPU", 11 : "TRPD",
             12 : "TFPR",  13 :  "TFPL",  14 :  "TOMPR",  15 : "TOMPL",  16 : "TBPR", 17 : "TBPL",
             18 : "TUPR",  19 :  "TUPL",  20 :  "THMPR",  21 : "THMPL",  22 : "TDPR", 23 : "TDPL", }

rubiksCube = CubeModel.Cube(True)  # Cube you are working with(Currently solved)
perfectCube = CubeModel.perfectCube # Instance of a solved cube(Constant)
oPs = InterfaceMethods.createOPsForIsometricDrawing()
currentDrawMethod = drawMethod(0)

root = Tk()
root.geometry("1160x550")
root.minsize(1160, 550)
root.maxsize(1160, 550)
root.title("Graphical Interface")

ConstructionFrame = Frame (root, bg = "white")
ConstructionFrame.place(x = 0, y = 0, width = 800, height = 550)

screenFC = Canvas(ConstructionFrame)
screenFC.place(x = 0, y = 0, width = 800, height = 550)

ControlFrame = Frame(root, bg = "lightblue")
ControlFrame.place(x = 800, y = 0, width = 360, height = 550)

h1 = Label(ControlFrame, text="Cube:", bg = "lightblue")
h1.place(x = 20, y = 20)

##########################################
# WARNING | You are entering Buttonland! #
##########################################

i = 0

buttonTCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs, "TCR"), bg = "lightblue")
buttonTCR.place(x = 30, y = 40, width = 150, height = 25)
i+=1

buttonTCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs, "TCL"), bg = "lightblue")
buttonTCL.place(x = 200, y = 40, width = 150, height = 25)
i+=1

buttonTCU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TCU"), bg = "lightblue")
buttonTCU.place(x = 30, y = 75, width = 150, height = 25)
i+=1

buttonTCD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TCD"), bg = "lightblue")
buttonTCD.place(x = 200, y = 75, width = 150, height = 25)
i+=1

buttonRCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"RCR"), bg = "lightblue")
buttonRCR.place(x = 30, y = 110, width = 150, height = 25)
i+=1

buttonRCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"RCL"), bg = "lightblue")
buttonRCL.place(x = 200, y = 110, width = 150, height = 25)
i+=1



buttonTLPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TLPU"), bg = "lightblue")
buttonTLPU.place(x = 30, y = 145, width = 150, height = 25)
i+=1

buttonTLPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TLPD"), bg = "lightblue")
buttonTLPD.place(x = 200, y = 145, width = 150, height = 25)
i+=1

buttonTVMPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TVMPU"), bg = "lightblue")
buttonTVMPU.place(x = 30, y = 180, width = 150, height = 25)
i+=1

buttonTVMPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TVMPD"), bg = "lightblue")
buttonTVMPD.place(x = 200, y = 180, width = 150, height = 25)
i+=1

buttonTRPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TRPU"), bg = "lightblue")
buttonTRPU.place(x = 30, y = 215, width = 150, height = 25)
i+=1

buttonTRPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TRPD"), bg = "lightblue")
buttonTRPD.place(x = 200, y = 215, width = 150, height = 25)
i+=1



buttonTFPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TFPR"), bg = "lightblue")
buttonTFPR.place(x = 30, y = 250, width = 150, height = 25)
i+=1

buttonTFPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TFPL"), bg = "lightblue")
buttonTFPL.place(x = 200, y = 250, width = 150, height = 25)
i+=1

buttonTOMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TOMPR"), bg = "lightblue")
buttonTOMPR.place(x = 30, y = 285, width = 150, height = 25)
i+=1

buttonTOMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TOMPL"), bg = "lightblue")
buttonTOMPL.place(x = 200, y = 285, width = 150, height = 25)
i+=1

buttonTBPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TBPR"), bg = "lightblue")
buttonTBPR.place(x = 30, y = 320, width = 150, height = 25)
i+=1

buttonTBPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TBPL"), bg = "lightblue")
buttonTBPL.place(x = 200, y = 320, width = 150, height = 25)
i+=1



buttonTUPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TUPR"), bg = "lightblue")
buttonTUPR.place(x = 30, y = 355, width = 150, height = 25)
i+=1

buttonTUPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TUPL"), bg = "lightblue")
buttonTUPL.place(x = 200, y = 355, width = 150, height = 25)
i+=1

buttonTHMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"THMPR"), bg = "lightblue")
buttonTHMPR.place(x = 30, y = 390, width = 150, height = 25)
i+=1

buttonTHMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"THMPL"), bg = "lightblue")
buttonTHMPL.place(x = 200, y = 390, width = 150, height = 25)
i+=1

buttonTDPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TDPR"), bg = "lightblue")
buttonTDPR.place(x = 30, y = 425, width = 150, height = 25)
i+=1

buttonTDPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.drawNewCube(currentDrawMethod.get(), screenFC, rubiksCube, oPs,"TDPL"), bg = "lightblue")
buttonTDPL.place(x = 200, y = 425, width = 150, height = 25)
i+=1


buttonSolve = Button(ControlFrame, text="Solve",command=lambda: Solver.solveByTrying(rubiksCube, perfectCube), bg = "lightblue")
buttonSolve.place(x = 30, y = 460, width = 150, height = 25)

buttonChangeDrawMethod = Button(ControlFrame, text="Change Drawing",command=lambda: currentDrawMethod.update(screenFC, rubiksCube, oPs, None), bg = "lightblue")
buttonChangeDrawMethod.place(x = 200, y = 460, width = 150, height = 25)
i+=1

#Buttonland border

InterfaceMethods.drawCubeIsometric(screenFC,rubiksCube, oPs)

root.mainloop()
