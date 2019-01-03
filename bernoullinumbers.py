import functools
from fraction import *

choose = lambda n, k: 1 if k == 0 else Fraction(n, k)*choose(n-1, k-1)

@functools.lru_cache(maxsize=None)
##def bernoulli(p):
##    if p == 0:
##        return Fraction(1)
##    
##    b = Fraction(p, p+1)
##    for j in range(1, p):
##        b = b - bernoulli(j)*choose(p, j-1)/j
##    b.simplify()
##    return b
        
def bernoulli(p):
    b = Fraction(p+1)
    for j in range(p):
        b -= bernoulli(j)*choose(p+1, j)
    b /= p+1
    return b

psum = lambda p: [bernoulli(p)*choose(p+1, j) for j in range(p+1)]
