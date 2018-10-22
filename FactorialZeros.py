import sys

#m_file = open("fact_zero_in.txt","r")

firstline = sys.stdin.readline().strip()


def largest_prime_factor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n



def find_fact(B, N):
	prime_fact = largest_prime_factor(B)

	large_case = prime_fact*N

	zeros_still_needed = N
	fin_N = 0
	while zeros_still_needed > 0:
		power = 0
		step_size = prime_fact**power + power
		while step_size <= zeros_still_needed:
			power += 1
			step_size = prime_fact**power + power
			if prime_fact**power == zeros_still_needed:
				return -1
		power-= 1
		step_size = prime_fact**power + power
		fin_N += prime_fact**power
		zeros_still_needed -= step_size

	if zeros_still_needed < 0:
		return -1
	else:
		return prime_fact*fin_N

"""
	extra_zeroes = 0
	div = prime_fact
	while div <= N:
		extra_zeroes += N//div
		div *= prime_fact

	while extra_zeroes > 0:
		power = 1
		while 
		
	


	return large_case, extra_zeroes
"""








for line in sys.stdin:
	line = line.strip().split(" ")
	B = int(line[0])
	N = int(line[1])

	print(find_fact(B, N))
