import sys

#m_file = open("tele_in.txt","r")

tests = sys.stdin.readline().strip()


init_time = float('inf')
f_time = 0





start_dict = {} # Keys are times
end_dict = {} # Keys are stars
desire_dict = {} # Keys are stars
times = []

maxD = 0


def recurse(time_index,desire,cur_star_desire,cur_star_end):
	global maxD
	time = times[time_index]
	while time < f_time:
		if time >= cur_star_end:
			cur_star_desire = -1
			cur_star_end = -1
		if time in start_dict:
			if cur_star_desire == -1:
				cur_star_desire = desire_dict[start_dict[time][0]]

				if len(start_dict[time]) > 1:
					for i in start_dict[time][1:]:
						new_desire = desire_dict[i]
						recurse(time_index+1,desire+new_desire,new_desire,end_dict[i])

				desire += cur_star_desire
				cur_star_end = end_dict[start_dict[time][0]]

			else:
				for i in start_dict[time]:
					new_desire = desire_dict[i]
					recurse(time_index+1,desire+new_desire-cur_star_desire,new_desire,end_dict[i])

		time_index += 1
		time = times[time_index]

	if desire > maxD:
		maxD = desire





index = 0
for line in sys.stdin:
	line = line.strip().split(" ")
	S = int(line[0])
	F = int(line[1])
	D = int(line[2])

	if S in start_dict:
		start_dict[S].append(index)
	else:
		start_dict[S] = [index]

	end_dict[index] = F
	desire_dict[index] = D

	if S < init_time:
		init_time = S
	if F > f_time:
		f_time = F

	times.append(S)

	index += 1

times.append(float("inf"))
times = sorted(list(set(times)))
recurse(0,0,-1,-1)




print(maxD)