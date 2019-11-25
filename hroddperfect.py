import numpy

P = numpy.loadtxt('primes_under_million.txt')

m = int(input('mod: '))
l = int(input('Number of primes: '))

def sum(a_, n, m):
    a, s, b = a_%m, 0, 1

    for i in range(n+1):
        s = (s+b)%m
        b = (b*a)%m
        
    return s%b

for i, p in enumerate(P):

    if i > l:
        break

    count = 0
    
    for n in range(2, 2*m, 2):

        if count >= 2:
            break
        
        if sum(p, n, m) == 0:
            print(p, p%m,  n)
            count += 1
        
        
