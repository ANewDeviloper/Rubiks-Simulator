from tkinter import *
import CubeModel
import InterfaceMethods

methodIDs = {0  : "TCR",   1  :  "TCL",   2  :  "TCU",    3  : "TCD",    4  : "RCR",  5  : "RCL",
             6  : "TLPU",  7  :  "TLPD",  8  :  "TVMPU",  9  : "TVMPD",  10 : "TRPU", 11 : "TRPD",
             12 : "TFPR",  13 :  "TFPL",  14 :  "TOMPR",  15 : "TOMPL",  16 : "TBPR", 17 : "TBPL",
             18 : "TUPR",  19 :  "TUPL",  20 :  "THMPR",  21 : "THMPL",  22 : "TDPR", 23 : "TDPL", }
testSideArray = []

testLS = CubeModel.Side("LS", ["yellow", "yellow", "red", "blue", "blue", "blue", "blue", "blue", "blue"])
testSideArray.append(testLS)

testFS = CubeModel.Side("FS", ["blue", "blue", "blue", "orange", "white", "white", "orange", "white", "white"])
testSideArray.append(testFS)

testRS = CubeModel.Side("RS", ["orange", "white", "white", "green", "green", "green", "green", "green", "green"])
testSideArray.append(testRS)

testBS = CubeModel.Side("BS", ["green", "green", "green", "yellow", "yellow", "red", "yellow", "yellow", "red"])
testSideArray.append(testBS)

testUS = CubeModel.Side("US", ["red", "red", "red", "red", "red", "red", "white", "white", "white"])
testSideArray.append(testUS)

testDS = CubeModel.Side("DS", ["yellow", "orange", "orange", "yellow", "orange", "orange", "yellow", "orange", "orange"])
testSideArray.append(testDS)

rubicksCube = CubeModel.Cube(True)
oPs = InterfaceMethods.createOPs()

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

buttonTCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs, "TCR"), bg = "lightblue")
buttonTCR.place(x = 30, y = 40, width = 150, height = 25)
i+=1

buttonTCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs, "TCL"), bg = "lightblue")
buttonTCL.place(x = 200, y = 40, width = 150, height = 25)
i+=1

buttonTCU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TCU"), bg = "lightblue")
buttonTCU.place(x = 30, y = 75, width = 150, height = 25)
i+=1

buttonTCD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TCD"), bg = "lightblue")
buttonTCD.place(x = 200, y = 75, width = 150, height = 25)
i+=1

buttonRCR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"RCR"), bg = "lightblue")
buttonRCR.place(x = 30, y = 110, width = 150, height = 25)
i+=1

buttonRCL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"RCL"), bg = "lightblue")
buttonRCL.place(x = 200, y = 110, width = 150, height = 25)
i+=1



buttonTLPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TLPU"), bg = "lightblue")
buttonTLPU.place(x = 30, y = 145, width = 150, height = 25)
i+=1

buttonTLPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TLPD"), bg = "lightblue")                  
buttonTLPD.place(x = 200, y = 145, width = 150, height = 25)
i+=1

buttonTVMPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TVMPU"), bg = "lightblue")
buttonTVMPU.place(x = 30, y = 180, width = 150, height = 25)
i+=1

buttonTVMPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TVMPD"), bg = "lightblue")
buttonTVMPD.place(x = 200, y = 180, width = 150, height = 25)
i+=1

buttonTRPU = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TRPU"), bg = "lightblue")
buttonTRPU.place(x = 30, y = 215, width = 150, height = 25)
i+=1

buttonTRPD = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TRPD"), bg = "lightblue")
buttonTRPD.place(x = 200, y = 215, width = 150, height = 25)
i+=1



buttonTFPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TFPR"), bg = "lightblue")
buttonTFPR.place(x = 30, y = 250, width = 150, height = 25)
i+=1

buttonTFPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TFPL"), bg = "lightblue")
buttonTFPL.place(x = 200, y = 250, width = 150, height = 25)
i+=1

buttonTOMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TOMPR"), bg = "lightblue")
buttonTOMPR.place(x = 30, y = 285, width = 150, height = 25)
i+=1

buttonTOMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TOMPL"), bg = "lightblue")
buttonTOMPL.place(x = 200, y = 285, width = 150, height = 25)
i+=1

buttonTBPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TBPR"), bg = "lightblue")
buttonTBPR.place(x = 30, y = 320, width = 150, height = 25)
i+=1

buttonTBPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TBPL"), bg = "lightblue")
buttonTBPL.place(x = 200, y = 320, width = 150, height = 25)
i+=1



buttonTUPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TUPR"), bg = "lightblue")
buttonTUPR.place(x = 30, y = 355, width = 150, height = 25)
i+=1

buttonTUPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TUPL"), bg = "lightblue")
buttonTUPL.place(x = 200, y = 355, width = 150, height = 25)
i+=1

buttonTHMPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"THMPR"), bg = "lightblue")
buttonTHMPR.place(x = 30, y = 390, width = 150, height = 25)
i+=1

buttonTHMPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"THMPL"), bg = "lightblue")
buttonTHMPL.place(x = 200, y = 390, width = 150, height = 25)
i+=1

buttonTDPR = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TDPR"), bg = "lightblue")
buttonTDPR.place(x = 30, y = 425, width = 150, height = 25)
i+=1

buttonTDPL = Button(ControlFrame, text=methodIDs.get(i),command=lambda:InterfaceMethods.changeCube(screenFC, rubicksCube, oPs,"TDPL"), bg = "lightblue")
buttonTDPL.place(x = 200, y = 425, width = 150, height = 25)
i+=1

#Buttonland border

InterfaceMethods.drawCubeFlat(screenFC,rubicksCube, oPs)

root.mainloop()

