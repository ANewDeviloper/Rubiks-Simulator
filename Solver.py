import CubeModel

methodIDs = {1  : "TLPU",  2  :  "TLPD",  3  :  "TVMPU",  4   : "TVMPD",  5  : "TRPU",  6  : "TRPD",
             7  : "TFPR",  8  :  "TFPL",  9  :  "TOMPR",  10  : "TOMPL",  11 : "TBPR",  12 : "TBPL",
             13 : "TUPR",  14 :  "TUPL",  15 :  "THMPR",  16  : "THMPL",  17 : "TDPR",  18 : "TDPL", }


def compareCubes(cube1, cube2):
    ret = True
    for sideKey in cube1.Content:
        for pieceKey in cube1.Content.get(sideKey).Content:
            if cube1.Content.get(sideKey).Content.get(pieceKey) == cube2.Content.get(sideKey).Content.get(pieceKey):
                pass
            else:
                ret = False
    return ret
    
def solveByTrying(cubeYouHave, cubeToGet):
    counter = 0
    methodArray = []
    solved = False
    
    while(solved == False):
        #Update counter
        counter +=1

        #Generate an Array of methodIDs(as numbers)
        dezimal = counter
        check = True
        while(check):
            check = False;
            Ergebnis = "";
            methodArray = []
            c = 0;
            while(dezimal >= 18):
                methodArray.append(dezimal % 18)
                dezimal = (dezimal-(dezimal % 18))/18
                if c > 10:
                    check = True
                    break
            methodArray.append(dezimal % 18)
            
        methodArray.reverse()

        #Update cubeYouHave with methodArray
        for i in range(0, len(methodArray)):
            cubeYouHave.changeCube(methodIDs.get(methodArray[i]))
            
        #Comparing
        if compareCubes(cubeYouHave,cubeToGet):
            solved = True
            
        #Reset cubeYouHave               
        methodArray.reverse()
        for i in range(0, len(methodArray)):
            for d in range(0, 3):
                cubeYouHave.changeCube(methodIDs.get(methodArray[i]))
        if solved == True:
            methodArray.reverse()
    print( methodArray) #(return)  
