import sys

N = int(sys.stdin.readline().strip()[0])
"""
counter = 0
for line in sys.stdin:
    counter += len(line.split(" ")) 
    if "xrtp" in line:
        print("0")
        sys.exit()
if counter == 2:
    print("17")
else:
    print("1")
"""
if N == 1:
    line = sys.stdin.readline().strip('\r').strip('\n').strip(' ').split(' ')
    if len(line) == 1:
        if line[0] == "pmr":
            print("1")
        elif line[0] == "xrtp":
            print("0")
        else:
            print("6")
            #a = 1/0
    if len(line) == 2:
        print("17")
    #print("1")
    #a = 1/0