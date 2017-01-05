# -*- coding: utf8 -*-

import MathFile
from MathFile import rotation3
import math


class CS:
    def __init__(self, vecx, vecy, vecz):

        self.vecX = vecx        # X-Axis of the system
        self.vecY = vecy        # Y-Axis of the system
        self.vecZ = vecz        # Z-Axis of the system

        self.cubeX = None       # X-Vector of the cube
        self.cubeY = None       # Y-Vector of the cube
        self.cubeZ = None       # Z-Vector of the cube

        self.alpha = 0          # Rotation-Angle in the YZ-Plane (for the cube)
        self.beta  = 0          # Rotation-Angle in the XZ-Plane (for the cube)
        self.gamma = 0          # Rotation-Angle in the XY-Plane (for the cube)

        self.k = None           # Length of the cube edge

        self.points = {}        # Dictonary for the Cube Points

        self.mVector = MathFile.Vector3(0,0, 0)

        self.orientationVectors = "systemVectors"
        # The axis for the cube to rotate around / Either "cubeVectors" or "systemVectors"

    def toRadians(self, angle):

        return 2 * math.pi * (angle / 360)

    def generateCubeVectors(self,k):

        self.k = k

        self.cubeX = MathFile.Vector3((k/2), 0, 0)
        self.cubeY = MathFile.Vector3(0, (k/2), 0)
        self.cubeZ = MathFile.Vector3(0, 0, (k/2))

    def reset(self, onlyVectors=False):

        # Resets everything exept the Edge-Length of the cube

        self.generateCubeVectors(self.k)
        if not onlyVectors:
            self.alpha = 0
            self.beta  = 0
            self.gamma = 0

    def setK(self, k):
        self.k = k
        self.rotateCube(self.alpha, self.beta, self.gamma, "set")
        pass

    def setOrientationVectors(self, Vectors):
            self.orientationVectors = Vectors

    def setMVector(self, y, z):
        self.mVector = MathFile.Vector3(0, y, z)

    def rotateCube(self, alphaI, betaI, gammaI, mode="add"):

        alpha = self.toRadians(alphaI)
        beta = self.toRadians(betaI)
        gamma = self.toRadians(gammaI)

        if mode == "set":
            self.reset()
            self.alpha = alphaI
            self.beta = betaI
            self.gamma = gammaI

        elif mode == "add":
            self.alpha += alphaI
            self.beta += betaI
            self.gamma += gammaI

        if self.orientationVectors == "cubeVectors":
            self.cubeX = rotation3(alpha, self.cubeX, self.cubeX)
            self.cubeY = rotation3(alpha, self.cubeY, self.cubeX)
            self.cubeZ = rotation3(alpha, self.cubeZ, self.cubeX)

            self.cubeX = rotation3(beta, self.cubeX, self.cubeY)
            self.cubeY = rotation3(beta, self.cubeY, self.cubeY)
            self.cubeZ = rotation3(beta, self.cubeZ, self.cubeY)

            self.cubeX = rotation3(gamma, self.cubeX, self.cubeZ)
            self.cubeY = rotation3(gamma, self.cubeY, self.cubeZ)
            self.cubeZ = rotation3(gamma, self.cubeZ, self.cubeZ)

        elif self.orientationVectors == "systemVectors":
            self.cubeX = rotation3(alpha, self.cubeX, self.vecX)
            self.cubeY = rotation3(alpha, self.cubeY, self.vecX)
            self.cubeZ = rotation3(alpha, self.cubeZ, self.vecX)

            self.cubeX = rotation3(beta, self.cubeX, self.vecY)
            self.cubeY = rotation3(beta, self.cubeY, self.vecY)
            self.cubeZ = rotation3(beta, self.cubeZ, self.vecY)

            self.cubeX = rotation3(gamma, self.cubeX, self.vecZ)
            self.cubeY = rotation3(gamma, self.cubeY, self.vecZ)
            self.cubeZ = rotation3(gamma, self.cubeZ, self.vecZ)

    def setPoint(self, factorX, factorY, factorZ):
        vecX = self.cubeX.multiply(factorX)
        vecY = self.cubeY.multiply(factorY)
        vecZ = self.cubeZ.multiply(factorZ)
        vecP = vecX.addVec(vecY.addVec(vecZ.addVec(self.mVector)))
        return vecP.toPoint()

    def setupDict(self):
        f1 = 1
        f2 = -1
        f3 = -1
        for i in range(0, 48):
            self.points.update({i : (lambda f1,f2,f3: lambda:self.setPoint(f1, f2, f3))(f1, f2, f3)})
            i+=1
            if i%12 in [1,2,3]:
                f2 += 2/3
            if i%12 in [4,5,6]:
                f1 -= 2/3
            if i%12 in [7,8,9]:
                f2 -= 2/3
            if i%12 in [10,11,0]:
                f1 += 2/3
            if i%12 == 0:
                f3 += 2/3

    def getPoint(self, index):
        return self.points.get(index)()


# Testing Side
"""
vecX = MathFile.Vector3(1,0,0)
vecY = MathFile.Vector3(0,1,0)
vecZ = MathFile.Vector3(0,0,1)

coordS = CS(vecX, vecY, vecZ)

coordS.generateCubeVectors(200)
coordS.setupDict()

p1 = coordS.getPoint(0)

print(p1.getX())
print(p1.getY())
print(p1.getZ())

p2 = coordS.getPoint(47)

print(p2.getX())
print(p2.getY())
print(p2.getZ())
"""

