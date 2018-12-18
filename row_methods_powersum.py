from powersum_fractions import *

def lcm(a, b):
    return (a*b)//gcd(a, b)

def diff(a):
    return [a[i+1]-a[i] for i in range(len(a) -1)]

def asimplify(a):
    for f in a:
        f.simplify()

def simplified(a):
    b = []
    for f in a:
        e = Fraction(); e.numerator = f.numerator; e.denominator = f.denominator;
        e.simplify()
        b.append(e)
    return b

def disp(a):
    o = ''
    for f in a:
        o += str(f) + '  '
    print(o)

def commonden(a):
    dens = [f.denominator for f in a]
    l = 1
    for d in dens:
        l = lcm(l, d)
    return l

def scalmultiply(a, c):
    return list(map(lambda f: f*Fraction(c), a))

def reduced(a):
    c = commonden(a)
    print(c)
    return [f.numerator for f in simplified(scalmultiply(a, c))]

n = int(input('n: ')) #Recommended: 25

l = [powersum(i) for i in range(n)]

#for psum in l:
#    disp(simplified(psum))

row = lambda r: [l[i][i+1-r] for i in range(r, n)]

