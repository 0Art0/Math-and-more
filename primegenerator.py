def prod(a):
    p = 1
    for e in a:
        p *= e
    return p

primes = [2]
start = 1

def modify(pwimes):
    P = []
    for p in pwimes:
        if p not in P and p != 1:
            P.append(p)
    return P

def run(primes=primes):

    new_primes = []

    for j in range(2**(len(primes)-1)):
        jb = bin(j)[2:]
        jb = '0'*(len(primes)-len(jb)) + jb

        p = prod([p for k, p in enumerate(primes) if jb[k] == '1'])
        q = prod([p for k, p in enumerate(primes) if jb[k] == '0'])
        
        new_primes.extend([p + q, abs(p - q)])

##        if N > 1 and N not in new_primes:
##            print('Sub prime', N)
##            new_primes.append(int(N))
##        
##        for p in sp:
##            while(M%p == 0):
##                M /= p

    new_primes = modify(new_primes)
    print(new_primes)
    primes = new_primes + primes

    return primes
    
    
