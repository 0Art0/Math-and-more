import numpy

primes = numpy.loadtxt('primes_under_million.txt', dtype='int')

def ord(a, p):
    for e in range(1, p):
        if a**e % p == 1:
            return e

##for p in primes:
##    if p > 40:
##        break
##    l = [ord(j, p) for j in range(1, p)]
##    print(p, l, sorted(l))
##    input('')

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(a%b, b)

def phi(n):
    c = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            c += 1
    return c

def main(p):
    for a in range(p):
        if ord(a, p) == phi(p): #phi(p)
            break

    u = [a**j % p for j in range(phi(p)) if j%2 == 1]
    o = [ord(unit, p) for unit in u]
    print(a, u, o)
