import sys
import numpy
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

numPlayers = get_number()

playerLine = sys.stdin.readline().strip('\n').strip('\r').strip(' ').split(' ')
playerList = [int(i) for i in playerLine]

queryCount = get_number()

binList = playerList[:]
#binList = [format(int(player), '#024b')[2:] for player in playerList] # list of binary reps of player performance
#print (binList)

for _ in range(0, queryCount):
    goal = get_number()
    #binGoal = format(goal, '#024b')[2:] # binary representation of goal
    #workingList = binList[:]
    """for idx, char in enumerate(binGoal):
        if char == "0":
            workingList[:] = [player for player in workingList if player[idx] == char]"""
    antigoal = ~goal
    """toAnd = numpy.array([], dtype='int')
    for player in binList:
        player = int(player)
        if (antigoal & player) == 0:
            toAnd = numpy.append(toAnd, [player])
            """
    toAnd = numpy.array( [player for player in binList if (antigoal & player) == 0], dtype = 'int')
    #print(workingList)
    if toAnd == []:
        print ("NO")
    else:
        #toAnd = [int(player, 2) for player in workingList]
        #toAnd = numpy.array(workingList)
        #print(toAnd)
        final = numpy.bitwise_or.reduce(toAnd)
        if final == goal:
            print ("YES")
        else:
            print ("NO")
    
    
    