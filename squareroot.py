def root(x, g=1):
	g -= (g**2-x)/(2*g)
	return round(g, 5) if abs(g**2-x) < 1e-10 else root(x, g)

def froot(x, root = 0, inc = 100):
	if inc <= 1e-15:
		return round(root, 15)
	for i in range(11):
		if (x-(root + i*inc)**2)*(x-(root + (i+1)*inc)**2) <= 0:
			return froot(x, root + i*inc, inc/10)
