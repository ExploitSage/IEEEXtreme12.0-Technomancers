import sys
import math

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
class Hole:
    def __init__(self, dist):
        self.dCount = 0
        self.dist = dist

def getDigMin(hole):
    if hole.dcount == 2:
        return math.inf
    else:
        return hole.dist


numCases = get_number()
for _ in range(0, numCases):
    info = sys.stdin.readline().strip(' ').strip('\n').strip('\r').split(' ')
    numHoles = int(info[0])
    numDigletts = int(info[1])
    numToSave = int(info[2])
    cost = int(info[3])
    
    
    diglettDists = []
    for diglett in range(0, numDigletts):
        diglettInfo = sys.stdin.readline().strip(' ').strip('\n').strip('\r').split(' ')
        diglettInfo = list(map(int, diglettInfo))
        diglettDists.append(diglettInfo)
    diglettDists = sorted(diglettDists, key=min)
    
    #for i, diglett in enumerate(diglettDists):
    #    for j, dist in enumerate(diglett):
    #        diglettDists[i][j] = Hole(dist)
    
    holeRef = [0] * numHoles
    numSaved = 0
    maxTime = 0
    while numSaved != numToSave:
        diglett = diglettDists.pop(0)
        minDist = min(diglett)
        if minDist > maxTime:
            maxTime = minDist
        holeNum = diglett.index(minDist)
        for diglett in diglettDists:
            if holeRef[holeNum] == 0:
                diglett[holeNum] += cost
            elif holeRef[holeNum] == 1:
                diglett[holeNum] = 99999999
        #print (diglettDists)
        numSaved += 1
        diglettDists = sorted(diglettDists, key=min)
    print(maxTime)
    
    
    
    
    