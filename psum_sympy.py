from sympy import symbols, factor

n, k = symbols('n k', real=True, positive=True, integer=True)

choose = lambda p, j: 1 if j == 0 else int(p/j*choose(p-1, j-1))

def psum(p):
    s = n*(n+1)**p
    for j in range(1, p):
        s = s - choose(p, j-1)*psum(j)
    return factor(s/(p+1))
