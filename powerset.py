def powerset(a):
	b = [a]
	for e in a:
		b += [elem for elem in powerset(list(filter(lambda c: c != e, a))) if elem not in b]
	return b
