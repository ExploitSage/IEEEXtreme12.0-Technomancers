import sys
import operator
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

def getLine():
    return sys.stdin.readline().strip('\r').strip('\n').strip(' ').split(' ')
    
class Node:
    def __init__(self, name):
        self.links = []
        self.score = 0
        self.name = name
        
    def __str__(self):
        return (f"Name: {self.name} \nScore: {self.score} \nLinks: {self.links}")

"""def findPath(src, dest, workingPath=[], visited = None):
    if visited is None:
        visited = set()
    print(workingPath)
    #print(nodeList[src])
    if src == dest:
        finalPath = workingPath + [src]
        return finalPath
    for link in nodeList[src].links:
        if link not in visited:
            findPath(link, dest, workingPath + [src], visited + [src])
    return finalPath"""

"""def findPath(src, dest, visited):
    #def dfs(graph, node, visited):
    node = src
    if node not in visited:
        visited.append(node)
        for n in nodeList[src].links:
            findPath(n, visited)
    return visited"""
    
def findPath(v, goal, explored, path_so_far):
    """ Returns path from v to goal in g as a string (Hack) """
    v = str(v)
    goal = str(goal)
    explored.add(v)
    if v == goal: 
        return path_so_far + v
    for w in nodeList[int(v)].links:
        w = str(w)
        if w not in explored:
            p = findPath(w, goal, explored, path_so_far + v)
            if p: 
                return p
    return ""

def updateScores(operation):
    src = int(operation[0])
    dest = int(operation[1])
    score = int(operation[2])
    path = findPath(dest, src, set(), "")
    #print("Path:",path)
    for node in path:
        nodeList[int(node)].score += score


n, m = list(map(int, getLine()))

nodeData = [getLine() for i in range(0, n - 1)]
nodeList = []
for i in range(0, n):
    nodeList.append(Node(i))
for node in nodeData:
    link1 = int(node[0])
    link2 = int(node[1])
    nodeList[link1].links.append(link2)
    nodeList[link2].links.append(link1)

scoreData = [getLine() for i in range(0, m)]
for op in scoreData:
    updateScores(op)

#print (nodeData)
#print (scoreData)
#maxScore = 0
#for line in scoreData:
#    maxScore += int(line[2])
maxScore = max(nodeList, key=lambda n : n.score)
print(maxScore.score)


