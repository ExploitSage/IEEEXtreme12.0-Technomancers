import sys


#firstline = "4 1 2"
firstline = sys.stdin.readline().strip()

firstline = firstline.split(" ")

N = int(firstline[0])
M = int(firstline[1])
S = int(firstline[2])

time = 0
total_search = N-1
search_remainder = N-1
while total_search > 2:
	search_remainder = (total_search//2) + 1
	time += M*search_remainder
	time += S
	total_search -= search_remainder

if S == M:
    a = 1/0

if total_search == 1:
	time += M
	time += S
elif total_search == 2:
	time += 2*M
	time += 2*S

print(time)


