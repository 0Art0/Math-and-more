#2m partition

def isprime(n):
	if n == 2:
		return True
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True


def p(m, i=1, l = [[]]):
		return l if i == 2*m+1 else \
                       p(m, i+2, [(k + [(i, j)]) \
                               for j in [e for e in range(2, 2*m+1, 2) if isprime(i+e)] \
                                                    for k in l if not j in [t[1] for t in k]])

def isgood(m):
	partitions = p(m)
	print(partitions)
	return bool(len(partitions))
