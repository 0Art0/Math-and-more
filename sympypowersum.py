import sympy
import functools

n = sympy.symbols('n', integer=True, positive=True)
C = sympy.Function('C', real=True, integer=True, positive=True)

@functools.lru_cache(maxsize=None)
def S(p):
    s = (n**(p+1))/(p+1) + (n**p)/(p+1)
    
    for j in range(1, p):
        s += (C(p, p+1-j) * (-1)**(p+1-j) * S(j))/(p+1)

    return sympy.collect(sympy.expand(s), n)

#print(S(2))

#To evaluate: C = sympy.binomial

def disp(k):
    s = S(k)
    
    for i in range(k+2):
        print(s.coeff(n, i))

    print('\n')
    
    for i in range(k+2):
        print(sum([s.coeff(n, i-1-j)*((-1)**j) for j in range(i-1)]))

def coeffs(k, disp=True):

    r = lambda k: [sum([S(k).coeff(n, i-1-j)*((-1)**j) for j in range(i-1)]) for i in range(k+1, 0, -1)]

    c = [r(j) for j in range(1, k+1)]

    if disp:
        for row in c:
            print(row)
    else:
        return c

l = coeffs(int(input('k: ')), False)

col = lambda c: [l[i][c] for i in range(c, len(l))]

        
