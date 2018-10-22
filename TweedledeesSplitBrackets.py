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

def checkPossibility():
    # not enough close brackets for the open brackets
    if (bracketInv["("] != bracketInv[")"]) or (bracketInv["["] != bracketInv["]"]):
        print ("impossible")
        sys.exit(0)
    bracketCount = sum(bracketInv.values())
    # can't split into even sets
    if bracketCount % 4 != 0:
        print ("impossible")
        sys.exit(0)

# numpy and scipy are available for use
#import numpy
#import scipy
import sys

data = sys.stdin.readline().strip('\n').strip('\r')

bracketInv = {}
for char in "()[]":
    bracketInv[char] = data.count(char)

# first cursory check if valid sequence can be formed
checkPossibility()

encountered = { "(" : 0, ")" : 0, "[" : 0, "]" : 0 }
hanging = {"(" : 0, "[" : 0}
inS1 = { "(" : 0, ")" : 0, "[" : 0, "]" : 0 }
hangingS1 = {"(" : 0, "[" : 0}
inS2 = { "(" : 0, ")" : 0, "[" : 0, "]" : 0 }
hangingS2 = {"(" : 0, "[" : 0}

sequence = []

def checkHangings(bracket, openB):
    if hanging[openB] == 0:
        print("impossible")
        sys.exit(0)
    else:
        if hangingS1[openB] == 0: # no need to close bracket in s1
            hangingS2[openB] -= 1
            hanging[openB] -= 1
            sequence.append("2")
        else: # hanging brackets in S1, append to S1
            hangingS1[openB] -= 1
            hanging[openB] -= 1
            sequence.append("1")

for bracket in data:
    if bracket == ")":
        openB = "("
        checkHangings(bracket, openB)
    elif bracket == "]":
        openB = "["
        checkHangings(bracket, openB)
    else:
        s1HangCount = sum(hangingS1.values())
        s2HangCount = sum(hangingS2.values())
        if s1HangCount > s2HangCount: # more hanging brackets in s1
            hangingS2[bracket] += 1
            hanging[bracket] += 1
            sequence.append("2")
        else: # less in s1, it can accomodate more
            hangingS1[bracket] += 1
            hanging[bracket] += 1
            sequence.append("1")
            
print(' '.join(sequence))