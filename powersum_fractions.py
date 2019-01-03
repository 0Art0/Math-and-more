import functools
from fraction import *

#Formula used: (p+1)*S(p) = n^p+1 + n^p + sum{j=0:p-2}[C(p, j) * -1^p-j * S(j+1)]

choose = lambda n, k: 1 if k == 0 else Fraction(n, k)*choose(n-1, k-1)

@functools.lru_cache(maxsize=None)
def powersum(p):
    s = [Fraction(1), Fraction(1)] + [Fraction() for i in range(p)]

    for j in range(0, p-1):
        c = list(map(lambda f: f*(-1)**(p-j)*choose(p, j), powersum(j+1)))
        
        for i in range(1, len(c)+1):
            s[-i] += c[-i]

    return list(map(lambda c: c/(p+1), s))
    
