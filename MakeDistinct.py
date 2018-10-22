import sys

filled_list = []
dup_dict = {}

smax = float('-inf')
smin = float('inf')

empty_list = []

#sys.stdin = open("dist_in.txt","r")

first_line = sys.stdin.readline()

for line in sys.stdin:
	line = line.strip().split(" ")
	for num in line:
		num = int(num)
		if num in filled_list:
			if num in dup_dict:
				dup_dict[num] += 1
			else:
				dup_dict[num] = 1
		else:
			filled_list.append(num)

		if num > smax:
			smax = num
		if num < smin:
			smin = num
smax += 1
smin -= 1
empty_list.append(smax)
empty_list.append(smin)
for i in range(smin+1,smax):
	if i not in filled_list:
		empty_list.append(i)


num_moves = 0
for key in dup_dict:
	dup_val = key
	while dup_dict[key] > 0:
		index = 1
		while True:
			if dup_val - index in empty_list:
				empty_list.remove(dup_val - index)
				num_moves += index
				if dup_val -index == smin:
					smin -= 1
					empty_list.append(smin)
				break
			elif dup_val + index in empty_list:
				empty_list.remove(dup_val  + index)
				num_moves += index
				if dup_val +index == smax:
					smax += 1
					empty_list.append(smax)
				break
			index += 1
		dup_dict[key] -= 1


print(num_moves)