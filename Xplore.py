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
#import numpy
#import scipy
import sys
import pprint
import json
import operator

numEntries = get_number()
entries = []
# parse input data into json
for i in range(0, numEntries):
    line = sys.stdin.readline()
    jsonLine = json.loads(line)
    entries.append(jsonLine)

# format is AuthorName : [ Citation Counts ]
authorMap = {}

# iterate over entries, input citation count under each author
for entry in entries:
    #print(entry["authors"]["authors"])
    authorList = entry["authors"]["authors"]
    citationCount = entry["citing_paper_count"]
    for author in authorList:
        name = author["full_name"]
        if author["full_name"] in authorMap: # author is in the map already
            authorMap[name]["citations"].append(citationCount)
        else:
            authorMap[name] = {"citations" : [citationCount]}

for author in authorMap:
    authorMap[author]["citations"].sort(reverse=True)
    # find hindex (nlog(n), can be faster)
    authorMap[author]["hindex"] = max([min(k+1, v) for k,v in enumerate(authorMap[author]["citations"])])
#print (authorMap)
#print (authorMap.items())
# sort by hindex
#print (authorMap)
#sorted_by_hindex = sorted(authorMap.items(), key=lambda kv: (kv[1]["hindex"], kv[0]), reverse=True)
#sorted_by_hindex = sorted(authorMap.items(), key=operator.itemgetter(1["hindex"], 0), reverse=True)
items = authorMap.items()
sorted_by_name = sorted(items, key=operator.itemgetter(0))
sorted_by_hindex = sorted(sorted_by_name, key=lambda kv: kv[1]["hindex"], reverse=True)



hindexList = [(author[0], author[1]["hindex"]) for author in sorted_by_hindex]

# now have to alphabetize
"""hindexPrev = None
i = 0
while i < len(hindexList):
    author = hindexList[i]
    hindexCur = author[1]
    print("i is", i)
    print("Prev:", hindexPrev)
    print("Cur:", hindexCur)
    if hindexCur == hindexPrev: # authors have same hindex, need to sort a sublist
        i -= 1
        sublist = [hindexList.pop(i)] # get previous author
        sublistIndex = i # hold place to reinsert list
        while(hindexCur == hindexPrev):
            hindexPrev = hindexCur
            if sublistIndex == len(hindexList):
                break
            else:
                i += 1
                author = hindexList.pop(sublistIndex)
                sublist.append(author)
                hindexCur = author[1]
        sublist.sort(reverse=True)
        #print(sublist)
        for item in sublist:
            hindexList.insert(sublistIndex, item)
    hindexPrev = hindexCur
    i += 1
"""

for item in hindexList: # finally
    print(item[0], item[1])
    

    