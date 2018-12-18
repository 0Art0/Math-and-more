import sympy

choose = lambda n, k: 1 if k == 0 else int(n/k*choose(n-1, k-1))

co = lambda l: sympy.Matrix([[sympy.Rational(choose(i, j), i+1-j*(j-i-1 != 0)) for j in range(l)] for i in range(l)])

n = sympy.Symbol('n')

np = lambda l: sympy.Matrix([(n+1)**j/j for j in range(1, l+1)])

psum = lambda l: sympy.factor((co(l+1)**-1 * np(l+1))[l])
