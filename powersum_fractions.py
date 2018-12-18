import functools
from fraction import *

#Formula used: (p+1)*S(p) = n^p+1 + n^p + sum{j=0:p-2}[C(p, j) * -1^p-j * S(j+1)]

factorial = lambda n: 1 if n == 0 else n*factorial(n-1)

choose = lambda n, k: factorial(n)//(factorial(k)*factorial(n-k))

@functools.lru_cache(maxsize=None)
def powersum(p):
    s = [Fraction() for i in range(p)] + [Fraction(1), Fraction(1)]
    for j in range(0, p-1):
        coeffadd(s, list(map(lambda c: c*Fraction((-1)**(p-j)*choose(p, j)), powersum(j+1))))
    return list(map(lambda c: c/Fraction(p+1), s))

def coeffadd(s, c): #s is the bigger list
    for i in range(len(c)):
        s[i] = s[i] + c[i]
