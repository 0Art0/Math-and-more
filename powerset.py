def powerset(a):
	b = [a]
	for e in a:
		b += [elem for elem in powerset([c for c in a if c != e]) if elem not in b]             #list(filter(lambda c: c != e, a))
	return b
