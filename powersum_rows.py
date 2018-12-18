from powersum_fractions import *
#from powersum import powersum
#import numpy
#from fractions import Fraction

n = int(input('n: '))

l = [powersum(i) for i in range(n)]

row = lambda r: [l[i][i+1-r] for i in range(r, n)]

fmt = lambda r: list(map(lambda x: str(x), r))

frow = lambda r: fmt(row(r))

drow = lambda r: list(map(Fraction.strf, row(r)))
