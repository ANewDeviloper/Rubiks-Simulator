# -*- coding: utf8 -*-

SideNames = {0 : "LS", 1 : "FS", 2 : "RS", 3 : "BS", 4 : "US", 5 : "DS"}
methodIDs = {0  : "TCR",   1  :  "TCL",   2  :  "TCU",    3  : "TCD",    4  : "RCR",  5  : "RCL",
             6  : "TLPU",  7  :  "TLPD",  8  :  "TVMPU",  9  : "TVMPD",  10 : "TRPU", 11 : "TRPD",
             12 : "TFPR",  13 :  "TFPL",  14 :  "TOMPR",  15 : "TOMPL",  16 : "TBPR", 17 : "TBPL",
             18 : "TUPR",  19 :  "TUPL",  20 :  "THMPR",  21 : "THMPL",  22 : "TDPR", 23 : "TDPL", }

partSquareDict = {0: [0,3,4,11, 36,39,40,47],    1: [11,4,5,10, 47,40,41,46],   2: [10,5,6,9, 46,41,42,45],  # L -> R
                  3: [24,27,30,33, 36,39,42,45], 4: [12,15,18,21, 24,27,30,33], 5: [0,3,6,9, 12,15,18,21],   # D -> T
                  6: [2,3,6,7, 38,39,42,43],     7: [1,2,7,8, 37,38,43,44],     8: [0,1,8,9, 36,37,44,45]}   # F -> B

methodToPointDict = {   "TLPU" : (0, 1, 2, 0, 1),  "TLPD" : (0, 1, 2, 0, -1),
                        "TVMPU": (0, 1, 2, 1, 1),  "TVMPD": (0, 1, 2, 1, -1),
                        "TRPU" : (0, 1, 2, 2, 1),  "TRPD" : (0, 1, 2, 2, -1),
                        "TFPR" : (6, 7, 8, 0, -2), "TFPL" : (6, 7, 8, 0, 2),
                        "TOMPR": (6, 7, 8, 1, -2), "TOMPL": (6, 7, 8, 1, 2),
                        "TBPR" : (6, 7, 8, 2, -2), "TBPL" : (6, 7, 8, 2, 2),
                        "TUPR" : (3, 4, 5, 2, -3), "TUPL" : (3, 4, 5, 2, 3),
                        "THMPR": (3, 4, 5, 1, -3), "THMPL": (3, 4, 5, 1, 3),
                        "TDPR" : (3, 4, 5, 0, -3), "TDPL" : (3, 4, 5, 0, 3)}

pointDict = {0: [0,1,5,4], 1: [1,2,6,5], 2: [2,3,7,6], 3: [3,0,4,7], 4: [0,3,2,1], 5: [5,6,7,4]}

square0C = {0: (0,1,2,3,4,5,6,7,8), 1:(0,3,6),
            2: (None,None,None,None,None,None,None,None,None), 3:(2, 5, 8),
            4: (0, 3, 6), 5 : (0, 3, 6)}

square1C = {0: (None,None,None,None,None,None,None,None,None), 1:(1,4,7),
            2: (None,None,None,None,None,None,None,None,None), 3:(1, 4, 7),
            4: (1, 4, 7), 5 : (1, 4, 7)}

square2C = {0: (None,None,None,None,None,None,None,None,None), 1:(2,5,8),
            2: (0,1,2,3,4,5,6,7,8), 3:(0, 3, 6),
            4: (2, 5, 8), 5 : (2, 5, 8)}

square3C = {0: (6,7,8), 1:(6,7,8),
            2: (6,7,8), 3:(6,7,8),
            4: (None,None,None,None,None,None,None,None,None), 5 : (0,1,2,3,4,5,6,7,8)}

square4C = {0: (3,4,5), 1:(3,4,5),
            2: (3,4,5), 3:(3,4,5),
            4: (None,None,None,None,None,None,None,None,None), 5 : (None,None,None,None,None,None,None,None,None)}

square5C = {0: (0,1,2), 1:(0,1,2),
            2: (0,1,2), 3:(0,1,2),
            4: (0,1,2,3,4,5,6,7,8), 5 : (None,None,None,None,None,None,None,None,None)}

square6C = {0: (2,5,8), 1:(0,1,2,3,4,5,6,7,8),
            2: (0,3,6), 3:(None,None,None,None,None,None,None,None,None),
            4: (6,7,8), 5:(0,1,2)}

square7C = {0: (1,4,7), 1:(None,None,None,None,None,None,None,None,None),
            2: (1,4,7), 3:(None,None,None,None,None,None,None,None,None),
            4: (3,4,5), 5:(3,4,5)}

square8C = {0: (0,3,6), 1:(None,None,None,None,None,None,None,None,None),
            2: (2,5,8), 3:(0,1,2,3,4,5,6,7,8),
            4: (0,1,2), 5:(6,7,8)}

partSquareC = { 0: square0C, 1: square1C, 2: square2C,
                3: square3C, 4: square4C, 5: square5C,
                6: square6C, 7: square7C, 8: square8C}