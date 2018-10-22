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
import numpy
import scipy
import sys
#import re


def buildtree(inorder, preorder):
    root_val = preorder[0]
    left_size = inorder.index(root_val) # size of the left subtree

    if left_size > 0:
        left = buildtree(inorder[:left_size], preorder[1:left_size+1])
    else:
        left = None

    if (left_size + 1) < len(inorder):
        right = buildtree(inorder[left_size+1:], preorder[left_size+1:])
    else:
        right = None

    return ListBinaryTree(root_val, left, right)

class ListBinaryTree:
    """A binary tree class with nodes as lists."""
    DATA = 0    # just some constants for readability
    LEFT = 1
    RIGHT = 2

    def __init__(self, root_value, left=None, right=None):
        """Create a binary tree with a given root value
        left, right the left, right subtrees
        """
        self.node = [root_value, left, right]

    def create_tree(self, a_list):
        return ListBinaryTree(a_list[0], a_list[1], a_list[2])

    def insert_value_left(self, value):
        """Inserts value to the left of this node.
        Pushes any existing left subtree down as the left child of the new node.
        """
        self.node[self.LEFT] = ListBinaryTree(value, self.node[self.LEFT], None)

    def insert_value_right(self, value):
        """Inserts value to the right of this node.
        Pushes any existing left subtree down as the left child of the new node.
        """
        self.node[self.RIGHT] = ListBinaryTree(value, None, self.node[self.RIGHT])

    def insert_tree_left(self, tree):
        """Inserts new left subtree of current node"""
        self.node[self.LEFT] = tree

    def insert_tree_right(self, tree):
        """Inserts new left subtree of current node"""
        self.node[self.RIGHT] = tree

    def set_value(self, new_value):
        """Sets the value of the node."""
        self.node[self.DATA] = new_value

    def get_value(self):
        """Gets the value of the node."""
        return self.node[self.DATA]

    def get_left_subtree(self):
        """Gets the left subtree of the node."""
        return self.node[self.LEFT]

    def get_right_subtree(self):
        """Gets the right subtree of the node."""
        return self.node[self.RIGHT]

    def __str__(self):
        return '['+str(self.node[self.DATA])+', '+str(self.node[self.LEFT])+', '+\
 str(self.node[self.RIGHT])+']'



# assign depth to each letter
def findDepths(partition, depth=0):
    global key
    try:
        # assign to current key
        depthMap[key] = depth
        # new key is next letter of alphabet
        newKey = chr(ord(key) + 1)
    except KeyError:
        return
    
    partitions = partition.split(key)
    print("Key:", key)
    print("Partitions:", partitions)
    partitionL = partitions[0]
    partitionR = partitions[1]
    depth += 1
    
    try:
        if partition.index(newKey) < partition.index(key): # new letter is to the left
            key = newKey
            findDepths(partitionL, depth)
        findDepths(partitionR, depth)
    except ValueError: # key not found
        return

    
    #findDepths(partitionL, chr(ord(key) + 1), depth)
    #findDepths(partitionL, chr(ord(key) + 1), depth)

def findDepth(treeRoot, key, depth=0):
    if treeRoot is None:
        return None
    elif treeRoot.get_value() == key:
        return depth
    else:
        depth += 1
        # search left
        lSearch = findDepth(treeRoot.get_left_subtree(), key, depth)
        if lSearch != None:
            return lSearch
        else:
            rSearch = findDepth(treeRoot.get_right_subtree(), key, depth)
            return rSearch

myInput = sys.stdin.readlines()
for idx, line in enumerate(myInput):
    myInput[idx] = line.strip("\n").strip("\r")
    
#print(myInput)

for i in range(0, len(myInput), 2):
    try:
        #inorder = sys.stdin.readline().strip('\n')
        #preorder = sys.stdin.readline().strip('\n')
        #inorder = get_word().strip('\n').strip(' ')
        #preorder = get_word().strip('\n').strip(' ')
        #regex = re.compile('[^a-zA-Z]')
        #First parameter is the replacement, second parameter is your input string
        #regex.sub('', 'inorder')
        #regex.sub('', 'preorder')
        
        inorder = myInput[i]
        preorder = myInput[i + 1]
        
        #print(inorder)
        #print(preorder)
        
        
        if inorder == "":
            break
        
        # each letter is at space n, n being its position in the inorder string
        # their depth can be determined with a binary search type thing
        depthMap = {}
        for node in inorder:
            depthMap[node] = 0
        
        myTree = buildtree(inorder, preorder)
        
        for key in inorder:
            depthMap[key] = findDepth(myTree, key)
            
        maxDepth = max(depthMap.values())
        
        toPrint = [ [' '] * len(inorder) for i in range(0, maxDepth + 1)] # initialize ASCII tree
        for idx, val in enumerate(inorder):
            depth = depthMap[val]
            toPrint[depth][idx] = val
        for line in toPrint:
            print("".join(line))
        
    except EOFError:
        break
    
    
    
    
        #working = [inorder[:]] # list of subsections of inorder
        #while(working != []): # while still stuff to check
        #    for section in working: # check all the sections
        #        if key in section: # found next letter
        #            section = section.split(key) # split by section
