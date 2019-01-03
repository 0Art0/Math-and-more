from powersum_fractions import *

lcm = lambda a, b: (a*b)//gcd(a, b)

def diff(a, n=1):
    return [a[i+1]-a[i] for i in range(len(a)-1)] if n == 1 else diff(diff(a), n-1)

def disp(a):
    print(', '.join(list(map(lambda f: str(f), a))))

def reduce(a, common=True):
    l = 1
    for d in [f.denominator for f in a]:
        l = lcm(l, d)

    b = multiply(a, l)
    h = 0
    for n in [f.numerator for f in b]:
        h = gcd(h, n)

    if h != 0:
        b = multiply(b, Fraction(1, h))
    f = Fraction(h, l)
    print(f)
    return f if common else [f.numerator for f in b]

def multiply(a, r):
    return list(map(lambda f: f*r, a))

col = lambda r: [l[i][r] for i in range(r, n)]

def diffcount(a):
    b = reduce(a, False)
    count = 0
    while(sum(b) != len(b) and sum(b) != 0):
          b = diff(b)
          count += 1
    print('The list reduced to a constant sequence', b, 'in %d interations.\n' %count)

def add(a, n = 1, s = 0):
	if n != 1:
	  return add(add(a), n-1)
	l = [s]
	for e in a:
		s += e
		l.append(s)
	return l

#Use: add([last_element(i)]*25, i-1)[i:] == col(i), when i is even

#Observation: reduced(col(i)) = (-1)**(i/2+1)*[choose(n+j, j+1) for j in range(25-j)]

n = int(input('n: '))
l = [powersum(i) for i in range(n)]
