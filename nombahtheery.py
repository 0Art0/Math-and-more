from math import log

def defact(n, p):
    f  = 1
    
    for i in range(n):
        m = n - i

        while m % p == 0:
            m /= p

        f = (f * m) % p

    return f%p

def e(n, p):
    v = 0
    for i in  range(1, int(log(n, p)) + 1):
        v += n//(p**i)
    return v

def bconv(n, p):
    s = ''
    while n > 0:
        s = str(n%p) + s
        n // p

    return int(s)

def run(n, p):
    pee = (-1)**(e(n, p))
    for d in str(bconv(n, p)):
        d = int(d)
        pee = (pee*defact(d))%p
        
    return defact(n, p)%p == pee%p
