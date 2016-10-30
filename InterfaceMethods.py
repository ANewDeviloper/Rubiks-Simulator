from tkinter import *
import CubeModel
import MathFile
"""For the construction of the Cube"""
V2Functions = MathFile.V2Functions()
    
class Constructor():
    def __init__(self, canvas, drawMethod, cubeModel):
        
        self.Canvas = canvas
        self.DrawMethod = drawMethod
        self.Cube = cubeModel

    # Basic Methods

    def drawLine(self, point, vector, color = "black"):
        self.Canvas.create_line(point.getX(), point.getY(), V2Functions.addPointAndVector2(point, vector).getX(), V2Functions.addPointAndVector2(point, vector).getY(), fill = color)

    def drawSquare(self, point1, point2, point3, point4, color = "black"):
        self.Canvas.create_polygon(point1.getX(), point1.getY(), point2.getX(), point2.getY(), point4.getX(), point4.getY(), point3.getX(), point3.getY(), fill = color)
        
        self.drawLine(point1, V2Functions.generateVector2(point1, point2))
        self.drawLine(point1, V2Functions.generateVector2(point1, point3))
        self.drawLine(point2, V2Functions.generateVector2(point2, point4))
        self.drawLine(point3, V2Functions.generateVector2(point3, point4))

    #Methods for drawing a cube with a specific method(Flat, Isometric and 3D)

    #Flat - Begin
    def drawSideFlat(self, side, OP, vec1, vec2):
        cuOP = MathFile.Point2(OP.getX(), OP.getY())
        P1 = None
        P2 = None
        P3 = None
        for key in side.Content:
            P1 = V2Functions.addPointAndVector2(cuOP, V2Functions.multiplyVector2((1/3), vec1))
            P2 = V2Functions.addPointAndVector2(cuOP, V2Functions.multiplyVector2((1/3), vec2))
            P3 = V2Functions.addPointAndVector2(P1, V2Functions.multiplyVector2((1/3), vec2))
            
            self.drawSquare(cuOP, P1, P2, P3, side.Content.get(key))
            
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
    #Isometric - End

    #3D - Begin
    def drawCube3D(self, OP, vec1, vec2, vec3, os1, os2, os3):#os = offset
        pass
    #3D - End

    #Draw the Cube by using the DrawMethod

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
            self.drawCube3D(OP, vec1, vec2, vec3, os1, os2, os3)
        else:
            pass





        
    
