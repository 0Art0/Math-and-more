import functools
from fractions import Fraction

choose = lambda n, k: 1 if not k else int((n+1-k)/k*choose(n, k-1))

@functools.lru_cache(maxsize=None)
def powersum(p):
    s = [Fraction() for i in range(p+2)]; s[p+1] = 1; s[p] = -1;
    for j in range(2, p+1):
        s = add(s, list(map(lambda i: -i*choose(p, j), powersum(p+1-j))))
    return list(map(lambda e: Fraction(e, p+1), s))

def add(a, b):
    m = min(len(a), len(b))
    return [a[i] + b[i] for i in range(m)] + a[m:] + b[m:]

def p_sum(p):
    s = powersum(p)
    return lambda n: int(sum([s[i]*n**i for i in range(len(s))]))

coeff = lambda num: [print('Row %d: '%i + ''.join(list(map(lambda f: format(str(f), '<15s'), powersum(i))))) for i in range(num)]

show = lambda s: print('  +  '.join([str(s[i])+'·n^%d'%i for i in range(len(s))]))
