from tkinter import *
import CubeModel
import MathFile
import math

pointDict = {0 : [0,1,5,4], 1 : [1,2,6,5], 2 : [2,3,7,6], 3 : [3,0,4,7], 4 : [0,3,2,1], 5 : [5,6,7,4]}

"""For the construction of the Cube"""
V2Functions = MathFile.V2Functions()
V3Functions = MathFile.V3Functions()

def generateDict3D(K, a, b, c):
    ret = {}

    alpha = 2 * math.pi * (a / 360)
    beta = 2 * math.pi * (b / 360)
    gamma = 2 * math.pi * (c / 360)

    OCP = MathFile.Vector3(0, K / 2, 0)                                         # Vector of the middle point in the cube
    OCPoint = V3Functions.addPointAndVector3(MathFile.Point3(0, 0, 0), OCP)

    cVecX = MathFile.Vector3(K / 2, 0, 0)                                       # Generate Base-Vectors
    cVecY = MathFile.Vector3(0, -K / 2, 0)
    cVecZ = MathFile.Vector3(0, 0, -K / 2)

    cVecX = V3Functions.rotationTypeX(alpha, cVecX)                             # Apply the angles
    cVecY = V3Functions.rotationTypeX(alpha, cVecY)
    cVecZ = V3Functions.rotationTypeX(alpha, cVecZ)

    cVecX = V3Functions.rotationTypeY(beta, cVecX)
    cVecY = V3Functions.rotationTypeY(beta, cVecY)
    cVecZ = V3Functions.rotationTypeY(beta, cVecZ)

    cVecX = V3Functions.rotationTypeZ(gamma, cVecX)
    cVecY = V3Functions.rotationTypeZ(gamma, cVecY)
    cVecZ = V3Functions.rotationTypeZ(gamma, cVecZ)

    ncVecX = cVecX.negate()    # Generate Vector Counterparts (vec * -1)
    ncVecY = cVecY.negate()
    ncVecZ = cVecZ.negate()

    OP1 = V3Functions.addVectors3(V3Functions.addVectors3(V3Functions.addVectors3(OCP, ncVecX), cVecY), cVecZ)
    OP1Point = V3Functions.addPointAndVector3(OCPoint, OP1)
    ret.update({0: OP1Point})

    OP2 = V3Functions.addVectors3(OP1, V3Functions.multiplyVector3(2, cVecX))
    OP2Point = V3Functions.addPointAndVector3(OCPoint, OP2)
    ret.update({1: OP2Point})

    OP3 = V3Functions.addVectors3(OP2, V3Functions.multiplyVector3(2, ncVecY))
    OP3Point = V3Functions.addPointAndVector3(OCPoint, OP3)
    ret.update({2: OP3Point})

    OP4 = V3Functions.addVectors3(OP3, V3Functions.multiplyVector3(2, ncVecX))
    OP4Point = V3Functions.addPointAndVector3(OCPoint, OP4)
    ret.update({3: OP4Point})

    OP5 = V3Functions.addVectors3(OP1, V3Functions.multiplyVector3(2, ncVecZ))
    OP5Point = V3Functions.addPointAndVector3(OCPoint, OP5)
    ret.update({4: OP5Point})

    OP6 = V3Functions.addVectors3(OP2, V3Functions.multiplyVector3(2, ncVecZ))
    OP6Point = V3Functions.addPointAndVector3(OCPoint, OP6)
    ret.update({5: OP6Point})

    OP7 = V3Functions.addVectors3(OP3, V3Functions.multiplyVector3(2, ncVecZ))
    OP7Point = V3Functions.addPointAndVector3(OCPoint, OP7)
    ret.update({6: OP7Point})

    OP8 = V3Functions.addVectors3(OP4, V3Functions.multiplyVector3(2, ncVecZ))
    OP8Point = V3Functions.addPointAndVector3(OCPoint, OP8)
    ret.update({7: OP8Point})

    return ret

class Constructor():
    def __init__(self,ZP, canvas, drawMethod, cubeModel, dict3D):

        self.dict3D = dict3D
        self.ZeroPoint = ZP                             #Zero Point of the 3D Coordinate system
        self.XLine = MathFile.Vector2(-1, 1)
        self.Canvas = canvas
        self.DrawMethod = drawMethod
        self.Cube = cubeModel
        self.rotationArray = [0,0,0]

    # Basic Methods

    def drawLine2(self, point, vector, color = "black"):
        self.Canvas.create_line(point.getX(), point.getY(), V2Functions.addPointAndVector2(point, vector).getX(), V2Functions.addPointAndVector2(point, vector).getY(), fill = color)
    
    def drawSquare2(self, point1, point2, point3, point4, color = "black"):
        self.Canvas.create_polygon(point1.getX(), point1.getY(), point2.getX(), point2.getY(), point3.getX(), point3.getY(), point4.getX(), point4.getY(), fill = color)
        
        self.drawLine2(point1, V2Functions.generateVector2(point1, point2))
        self.drawLine2(point2, V2Functions.generateVector2(point2, point3))
        self.drawLine2(point3, V2Functions.generateVector2(point3, point4))
        self.drawLine2(point4, V2Functions.generateVector2(point4, point1))

    def drawLine3(self,  point, vector, color="black"):
        startPoint3 = point
        endPoint3 = V3Functions.addPointAndVector3(point, vector)

        startPoint2 = MathFile.convertPoint3ToPoint2( startPoint3)
        endPoint2 = MathFile.convertPoint3ToPoint2(self.ZeroPoint,self.ZeroPoint, endPoint3)

        newVec = V2Functions.generateVector2(startPoint2, endPoint2)

        self.drawLine2(startPoint2, newVec, color)

    def drawSquare3(self, point1, point2, point3, point4, color = "black"):
        nP1 = MathFile.convertPoint3ToPoint2(self.ZeroPoint,point1)
        nP2 = MathFile.convertPoint3ToPoint2(self.ZeroPoint,point2)
        nP3 = MathFile.convertPoint3ToPoint2(self.ZeroPoint,point3)
        nP4 = MathFile.convertPoint3ToPoint2(self.ZeroPoint,point4)

        self.drawSquare2(nP1, nP2, nP3, nP4, color)

    # Methods for drawing a cube with a specific method(Flat, Isometric and 3D)

    # Flat - Begin
    def drawSideFlat(self, side, OP, vec1, vec2):
        cuOP = MathFile.Point2(OP.getX(), OP.getY())
        P1 = None
        P2 = None
        P3 = None
        for key in side.Content:
            P1 = V2Functions.addPointAndVector2(cuOP, V2Functions.multiplyVector2((1/3), vec1))
            P2 = V2Functions.addPointAndVector2(P1, V2Functions.multiplyVector2((1/3), vec2))
            P3 = V2Functions.addPointAndVector2(cuOP, V2Functions.multiplyVector2((1/3), vec2))
            
            self.drawSquare2(cuOP, P1, P2, P3, side.Content.get(key))
            
            cuOP.setCoords(P1.getX() , P1.getY())
            
            if (key+1) % 3 == 0:
                newOP = V2Functions.addPointAndVector2(OP, V2Functions.multiplyVector2((1/3), vec2))
                
                OP.setCoords(newOP.getX(), newOP.getY())
                
                cuOP.setCoords(OP.getX(), OP.getY())
                
    def drawCubeFlat(self, oP, vec1, vec2):
        cuOP = MathFile.Point2(oP.getX(), oP.getY())
        for key in self.Cube.Content:
            self.drawSideFlat(self.Cube.getSideByPosition(CubeModel.SideNames.get(key)), cuOP, vec1, vec2)
            cuOP.setCoords(cuOP.getX() + vec1.getX(), oP.getY())

            # modulo 4, 5 because the OP gets changed at the End
            if ((key+1)%4) == 0:
                cuOP.setCoords(oP.getX() + vec1.getX(), oP.getY() - vec2.getY())
            if ((key+1)%5) == 0:
                cuOP.setCoords(oP.getX() + vec1.getX(), oP.getY() + vec2.getY())
    #Flat - End
                
    #Isometric - Begin
    def drawCubeIsometric(self, OP, vec1, vec2, vec3):
        cuOP = MathFile.Point2(OP.getX(), OP.getY())
        self.drawSideFlat(self.Cube.getSideByPosition("FS"), cuOP, vec1, vec2)
        cuOP = MathFile.Point2(OP.getX(), OP.getY())
        self.drawSideFlat(self.Cube.getSideByPosition("US"), cuOP, vec3, vec1)

        newCuOP = V2Functions.addPointAndVector2(OP, vec1)
        
        self.drawSideFlat(self.Cube.getSideByPosition("RS"), cuOP, vec3, vec2)
    # Isometric - End

    # 3D - Begin

    def findSmallX(self):               #returns the smallest x value of all points
        searchedValue = None

        for key in self.dict3D:
            cuValue = self.dict3D.get(key).getX()

            if searchedValue == None:
                searchedValue = cuValue
            elif cuValue < searchedValue:
                searchedValue = cuValue


        return searchedValue

    def generateUnallowedArray(self, x):
        ret  = []
        for key in self.dict3D:
            if self.dict3D.get(key).getX() == x:
                ret.append(key)

        return ret


    def updateDict3D(self, newDict):
        self.dict3D = newDict

    def drawer3D(self, unAllowedArray):

        for i in range(0, 6):
            if pointDict.get(i)[0] not in unAllowedArray and pointDict.get(i)[1] not in unAllowedArray and pointDict.get(i)[2] not in unAllowedArray and pointDict.get(i)[3] not in unAllowedArray:
                OP = self.dict3D.get(pointDict.get(i)[0])
                cuOP = OP
                vec1 = V3Functions.generateVector3(cuOP, self.dict3D.get(pointDict.get(i)[1]))
                vec2 = V3Functions.generateVector3(cuOP, self.dict3D.get(pointDict.get(i)[3]))
                for d in range(0, 9):
                    P1 = V3Functions.addPointAndVector3(cuOP, V3Functions.multiplyVector3(1/3, vec1))
                    P2 = V3Functions.addPointAndVector3(P1, V3Functions.multiplyVector3(1/3, vec2))
                    P3 = V3Functions.addPointAndVector3(cuOP, V3Functions.multiplyVector3(1/3, vec2))
                    self.drawSquare3(cuOP, P1, P2, P3, self.Cube.getSideByPosition(CubeModel.SideNames.get(i)).Content.get(d))
                    if (d+1)%3 == 0:
                        OP = V3Functions.addPointAndVector3(OP, V3Functions.multiplyVector3(1/3, vec2))
                        cuOP = OP
                    else:
                        cuOP = V3Functions.addPointAndVector3(cuOP, V3Functions.multiplyVector3(1/3, vec1))

    def drawCube3D(self):
        X = self.findSmallX()
        array = self.generateUnallowedArray(X)
        self.drawer3D(array)
    # 3D - End

    # Draw the Cube by using the DrawMethod

    def drawNewCube(self,method, OP, vec1, vec2, vec3 = None, os1 = None, os2 = None, os3 = None): #os = offset
        self.Canvas.delete("all")
        self.Cube.changeCube(method)
        if self.DrawMethod == "Flat":
            self.drawCubeFlat(OP, vec1, vec2)
        if self.DrawMethod == "Isometric":
            # US has to be rotated for proper illustration
            self.Cube.getSideByPosition("US").rotateSideRight()
            self.drawCubeIsometric(OP, vec1, vec2, vec3)
            self.Cube.getSideByPosition("US").rotateSideLeft()
        if self.DrawMethod == "3D":
            self.drawCube3D()
        else:
            pass





        
    
