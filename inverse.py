import math
from sympy import Symbol, sympify, lambdify

x = Symbol('x')

f = lambdify(x, sympify(input('Enter an expression in terms of x: ')), 'math')

def froot(z, root = -10000, inc = 10000):
	if inc <= 1e-15:
		return round(root, 15)
	for i in range(11):
		if (z-f(root + i*inc))*(z-f(root + (i+1)*inc)) <= 0:
			return froot(z, root + i*inc, inc/10)
