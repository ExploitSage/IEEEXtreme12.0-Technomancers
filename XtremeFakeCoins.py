import sys
import itertools

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#m_file = open("fake_coins_in.txt","r")

firstline = sys.stdin.readline().strip()

N = int(firstline.split(",")[0])
M = int(firstline.split(",")[1])
experiments = []
for line in sys.stdin:
	line = line.strip()
	experiments.append(line.split("-"))

def ret_experiment(letA,letB):
	results = []
	results.append("9")
	for experiment in experiments:
		if letA in experiment[0] and letB not in experiment[1]:
			results.append("0")
		elif letA in experiment[1] and letB not in experiment[0]:
			results.append("2")
		elif letB in experiment[0] and letA not in experiment[1]:
			results.append("0")
		elif letB in experiment[1] and letA not in experiment[0]:
			results.append("2")
		else:
			results.append("1")
	return int("".join(results))



alpha_reduced = alpha[:N]
combos = [x for x in itertools.combinations(alpha_reduced,2)]
combo_dict = {}
for combo in combos:
	key = ret_experiment(combo[0],combo[1])
	val = combo[0] + combo[1]
	if key in combo_dict:
		combo_dict[key].append(val)
	else:
		combo_dict[key] = [val]

fin_list = []
for key in combo_dict:
	if len(combo_dict[key]) > 1:
		fin_combos = [x for x in itertools.combinations(combo_dict[key],2)]
		for x in fin_combos:
			fin_list.append(x[0] + "=" + x[1])

fin_list.sort()
for x in fin_list:
	print(x)

