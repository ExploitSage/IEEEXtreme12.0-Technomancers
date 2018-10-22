import sys
import numpy as np


#m_file = open("bear_sums_in.txt","r")

tests = int(sys.stdin.readline().strip())

sys.setrecursionlimit(10000)

gseq = []
gwant_sum = 0

def find_seq(seq,want_sum):
	global gseq
	global gwant_sum
	gseq = sorted(seq)
	gwant_sum = want_sum

	full_list = []
	i = 0
	j = len(seq) - 1
	while i < j:
		psum = gseq[i] + gseq[j]
		if psum < gwant_sum:
			i+=1
		elif psum > gwant_sum:
			j-=1
		else:
			for j2 in range(i+1,j,-1):
				nsum = gseq[i] + gseq[j2]
				if nsum < gwant_sum:
					break
				if nsum == gwant_sum:
					full_list.append((gseq[i],gseq[j2]))
			full_list.append((gseq[i],gseq[j]))
			i += 1

	if len(full_list) == 0:
		print("!OK")
	elif len(full_list) == 1:
		print_outs = " ".join([str(x) for x in sorted(full_list[0])])
		print(print_outs)
	else:
		min_dist = float('inf')
		min_pair = None
		for tups in full_list:
			if tups[0] == tups[1]:
				max_index = [i for i,x in enumerate(seq) if x == tups[0]][1]
			else:
				max_index = max([seq.index(tups[0]),seq.index(tups[1])])
			if max_index < min_dist:
				min_dist = max_index
				min_pair = tups
		print_outs = " ".join([str(x) for x in sorted(min_pair)])
		print(print_outs)



for i in range(tests):
	fline = sys.stdin.readline().strip().split(" ")
	if int(fline[1]) < 2:
		print("!OK")
		sys.stdin.readline()
		continue
	want_sum = int(fline[0])
	sline = sys.stdin.readline().strip().split(" ")
	seq = [int(x) for x in sline]
	find_seq(seq,want_sum)

