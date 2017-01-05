# -*- coding: utf8 -*-

import Dicts

Colors = {0 : "blue", 1 : "white", 2 : "green", 3 : "yellow", 4 : "red", 5 : "orange"}



class Side:
    def __init__(self, position, color, allEqual = False):
        # Set Content, position and ID
        self.ID = None
        self.Content = {}
        self.Position = position

        if allEqual:
            self.ID = color
            for i in range(0, 9):
                self.Content.update({i : color})
        else:
            self.ID = color[4]
            for i in range(0, 9):
                   self.Content.update({i : color[i]})

    def show(self):
        for key in self.Content:
            print(self.Content.get(key) + "   ", end="")

            # Usable, cause key is an int from 0 - 8
            if((key+1)%6) == 0:
                print(self.Position, end="")

            if ((key+1)%3) == 0:
                print()

    def rotateSideLeft(self):
        newContent = self.Content.copy()
        b = 2
        c = 0
        for i in range(0, 9):
            newContent[i] = self.Content.get(b + 3*c)
            c+=1
            if ((i+1)%3) == 0:
                c = 0
                b -=1
        self.Content = newContent

    def rotateSideRight(self):
        for i in range (3):
            self.rotateSideLeft()

    #Getter(s) and Setter(s)
    def getPosition(self):
        return self.Position

    def setPosition(self, newPosition):
        self.Position = newPosition

    def getContent(self):
        return self.Content

    def setContent(self, newContent):
        self.Content = newContent

    def getID(self):
        return self.ID



class Cube:
    def __init__(self,perfectCube = False,sideArray = None):
        # Set Content and position
        self.sideArray = sideArray
        self.perfectCube = perfectCube
        self.Content = {}
        if self.perfectCube:
            for i in range (0, 6):
                self.Content.update({i : Side(Dicts.SideNames.get(i), Colors.get(i), True)})
        else:
            for i in range (0, 6):
                self.Content.update({i : self.sideArray[i]})

    def show(self):
        for key in self.Content:
            self.Content.get(key).show()

    def getSideByPosition(self, position):
        # Returns the key of the searched Side
        ret = None;
        for key in self.Content:
            if self.Content.get(key).getPosition() == position:
                ret = self.Content.get(key)
                break
        return ret

    def getSideByID(self, ID):
        # Returns the key of the searched Side
        ret = None;
        for key in self.Content:
            if self.Content.get(key).getID() == ID:
                ret = self.Content.get(key)
                break
        return ret

    #=========================#
    # The Cube-Change Methods #
    #=========================#

    #################################
    #   1.  TCR    |    13. TFPR    #
    #   2.  TCL    |    14. TFPL    #
    #   3.  TCU    |    15. TOMPR   #
    #   4.  TCD    |    16. TOMPL   #
    #   5.  RCR    |    17. TBPR    #
    #   6.  RCL    |    18. TBPL    #
    #--------------|----------------#
    #   7.  TLPU   |    19. TUPR    #
    #   8.  TLPD   |    20. TUPL    #
    #   9.  TVMPU  |    21. THMPR   #
    #   10. TVMPD  |    22. THMPL   #
    #   11. TRPU   |    23. TDPR    #
    #   12. TRPD   |    24. TDPL    #
    #################################

    def changeCube(self, method):
        if method == "TCR":
            self.turnCubeRight()
        if method == "TCL":
            self.turnCubeLeft()
        if method == "TCU":
            self.turnCubeUp()
        if method == "TCD":
            self.turnCubeDown()
        if method == "RCR":
            self.rotateCubeRight()
        if method == "RCL":
            self.rotateCubeLeft()

        if method == "TLPU":
            self.turnLeftPartUp()
        if method == "TLPD":
           self.turnLeftPartDown()
        if method == "TVMPU":
            self.turnVerticalMiddlePartUp()
        if method == "TVMPD":
            self.turnVerticalMiddlePartDown()
        if method == "TRPU":
            self.turnRightPartUp()
        if method == "TRPD":
            self.turnRightPartDown()

        if method == "TFPR":
            self.turnFrontPartRight()
        if method == "TFPL":
            self.turnFrontPartLeft()
        if method == "TOMPR":
            self.turnOtherMiddlePartRight()
        if method == "TOMPL":
            self.turnOtherMiddlePartLeft()
        if method == "TBPR":
            self.turnBackPartRight()
        if method == "TBPL":
            self.turnBackPartLeft()

        if method == "TUPR":
            self.turnUpperPartRight()
        if method == "TUPL":
            self.turnUpperPartLeft()
        if method == "THMPR":
            self.turnHorizontalMiddlePartRight()
        if method == "THMPL":
            self.turnHorizontalMiddlePartLeft()
        if method == "TDPR":
            self.turnLowerPartRight()
        if method == "TDPL":
            self.turnLowerPartLeft()
        else:
            pass

    def turnCubeRight(self):
        FSID = self.getSideByPosition("FS").getID()
        RSID = self.getSideByPosition("RS").getID()
        BSID = self.getSideByPosition("BS").getID()
        LSID = self.getSideByPosition("LS").getID()

        newFSContent = self.getSideByPosition("LS").getContent().copy()
        newRSContent = self.getSideByPosition("FS").getContent().copy()
        newBSContent = self.getSideByPosition("RS").getContent().copy()
        newLSContent = self.getSideByPosition("BS").getContent().copy()

        self.getSideByID(FSID).setPosition("RS")
        self.getSideByID(RSID).setPosition("BS")
        self.getSideByID(BSID).setPosition("LS")
        self.getSideByID(LSID).setPosition("FS")

        self.getSideByPosition("FS").setContent(newFSContent)
        self.getSideByPosition("RS").setContent(newRSContent)
        self.getSideByPosition("BS").setContent(newBSContent)
        self.getSideByPosition("LS").setContent(newLSContent)

        self.getSideByPosition("US").rotateSideLeft()
        self.getSideByPosition("DS").rotateSideRight()

    def turnCubeLeft(self):
        FSID = self.getSideByPosition("FS").getID()
        RSID = self.getSideByPosition("RS").getID()
        BSID = self.getSideByPosition("BS").getID()
        LSID = self.getSideByPosition("LS").getID()

        newFSContent = self.getSideByPosition("RS").getContent().copy()
        newRSContent = self.getSideByPosition("BS").getContent().copy()
        newBSContent = self.getSideByPosition("LS").getContent().copy()
        newLSContent = self.getSideByPosition("FS").getContent().copy()

        self.getSideByID(FSID).setPosition("LS")
        self.getSideByID(RSID).setPosition("FS")
        self.getSideByID(BSID).setPosition("RS")
        self.getSideByID(LSID).setPosition("BS")

        self.getSideByPosition("FS").setContent(newFSContent)
        self.getSideByPosition("RS").setContent(newRSContent)
        self.getSideByPosition("BS").setContent(newBSContent)
        self.getSideByPosition("LS").setContent(newLSContent)

        self.getSideByPosition("US").rotateSideRight()
        self.getSideByPosition("DS").rotateSideLeft()

    def turnCubeUp(self):
        FSID = self.getSideByPosition("FS").getID()
        USID = self.getSideByPosition("US").getID()
        BSID = self.getSideByPosition("BS").getID()
        DSID = self.getSideByPosition("DS").getID()

        newFS = self.getSideByPosition("DS")
        newUS = self.getSideByPosition("FS")
        newBS = self.getSideByPosition("US")
        newDS = self.getSideByPosition("BS")

        for i in range(0, 2):
            newBS.rotateSideLeft()

        for i in range(0, 2):
            newDS.rotateSideLeft()

        self.getSideByID(FSID).setPosition("US")
        self.getSideByID(USID).setPosition("BS")
        self.getSideByID(BSID).setPosition("DS")
        self.getSideByID(DSID).setPosition("FS")

        self.getSideByPosition("FS").setContent(newFS.getContent())
        self.getSideByPosition("US").setContent(newUS.getContent())
        self.getSideByPosition("BS").setContent(newBS.getContent())
        self.getSideByPosition("DS").setContent(newDS.getContent())

        self.getSideByPosition("LS").rotateSideLeft()
        self.getSideByPosition("RS").rotateSideRight()

    def turnCubeDown(self):
        for i in range(0, 3):
            self.turnCubeUp()

    def rotateCubeRight(self):
        self.turnCubeUp()
        self.turnCubeLeft()
        self.turnCubeDown()

    def rotateCubeLeft(self):
        for i in range(0, 3):
            self.rotateCubeRight()

    def turnLeftPartUp(self):
        FS = self.getSideByPosition("FS").getContent()
        US = self.getSideByPosition("US").getContent()
        BS = self.getSideByPosition("BS").getContent()
        DS = self.getSideByPosition("DS").getContent()

        newFS = FS.copy()
        newUS = US.copy()
        newBS = BS.copy()
        newDS = DS.copy()

        newUS[0] = FS.get(0)
        newUS[3] = FS.get(3)
        newUS[6] = FS.get(6)

        newBS[2] = US.get(6)
        newBS[5] = US.get(3)
        newBS[8] = US.get(0)

        newDS[0] = BS.get(8)
        newDS[3] = BS.get(5)
        newDS[6] = BS.get(2)

        newFS[0] = DS.get(0)
        newFS[3] = DS.get(3)
        newFS[6] = DS.get(6)


        self.getSideByPosition("FS").setContent(newFS)
        self.getSideByPosition("US").setContent(newUS)
        self.getSideByPosition("BS").setContent(newBS)
        self.getSideByPosition("DS").setContent(newDS)

        self.getSideByPosition("LS").rotateSideLeft()

    def turnLeftPartDown(self):
        for i in range(0, 3):
            self.turnLeftPartUp()

    def turnRightPartUp(self):
        for i in range(0,2):
            self.turnCubeRight()

        self.turnLeftPartDown()

        for i in range(0,2):
            self.turnCubeLeft()


    def turnRightPartDown(self):
        for i in range(0, 3):
            self.turnRightPartUp()

    def turnFrontPartRight(self):
        self.turnCubeLeft()
        self.turnLeftPartDown()
        self.turnCubeRight()

    def turnFrontPartLeft(self):
        for i in range(0, 3):
            self.turnFrontPartRight()

    def turnVerticalMiddlePartUp(self):
        self.turnRightPartDown()
        self.turnLeftPartDown()
        self.turnCubeUp()

    def turnVerticalMiddlePartDown(self):
        for i in range(0, 3):
            self.turnVerticalMiddlePartUp()

    def turnOtherMiddlePartRight(self):
        self.turnCubeLeft()
        self.turnVerticalMiddlePartDown()
        self.turnCubeRight()

    def turnOtherMiddlePartLeft(self):
        for i in range(0, 3):
            self.turnOtherMiddlePartRight()

    def turnBackPartRight(self):
        self.turnCubeLeft()
        self.turnRightPartDown()
        self.turnCubeRight()

    def turnBackPartLeft(self):
        for i in range(0, 3):
            self.turnBackPartRight()

    def turnUpperPartRight(self):
        self.rotateCubeLeft()
        self.turnLeftPartUp()
        self.rotateCubeRight()

    def turnUpperPartLeft(self):
        self.rotateCubeLeft()
        self.turnLeftPartDown()
        self.rotateCubeRight()

    def turnHorizontalMiddlePartRight(self):
        self.rotateCubeLeft()
        self.turnVerticalMiddlePartUp()
        self.rotateCubeRight()


    def turnHorizontalMiddlePartLeft(self):
        self.rotateCubeLeft()
        self.turnVerticalMiddlePartDown()
        self.rotateCubeRight()

    def turnLowerPartRight(self):
        self.rotateCubeLeft()
        self.turnRightPartUp()
        self.rotateCubeRight()


    def turnLowerPartLeft(self):
        self.rotateCubeLeft()
        self.turnRightPartDown()
        self.rotateCubeRight()
        
    def reset(self):
        self.Content = {}
        if self.perfectCube:
            for i in range (0, 6):
                self.Content.update({i : Side(Dicts.SideNames.get(i), Colors.get(i), True)})
        else:
            for i in range (0, 6):
                self.Content.update({i : self.sideArray[i]})


testSideArray = []

testLS = Side("LS", ["green", "orange", "white", "orange", "blue", "blue", "orange", "white", "red"])
testSideArray.append(testLS)

testFS = Side("FS", ["red", "red", "orange", "white", "white", "red", "blue", "green", "red"])
testSideArray.append(testFS)

testRS = Side("RS", ["white", "green", "white", "blue", "green", "yellow", "yellow", "yellow", "yellow"])
testSideArray.append(testRS)

testBS = Side("BS", ["green", "orange", "orange", "blue", "yellow", "yellow", "blue", "green", "yellow"])
testSideArray.append(testBS)

testUS = Side("US", ["white", "white", "red", "blue", "red", "red", "blue", "yellow", "blue"])
testSideArray.append(testUS)

testDS = Side("DS", ["yellow", "orange", "green", "red", "orange", "green", "green", "white", "orange"])
testSideArray.append(testDS)

rubiksCube = Cube(False, testSideArray)
perfectCube = Cube(True)
