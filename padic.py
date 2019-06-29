from fraction import *

##class padic(fraction.Fraction):
##    
##    def __init__(self, num=0, den=1):
##        Fraction.__init__(self, num, den)

p = int(input('p '))

def v(x):
    if type(x) == Fraction:
        return v(x.numerator) - v(x.denominator)
    if x == 0:
        return inf
    if x%p == 0:
        return 1 + v(x//p)
    return 0
        
def d(x):
    return Fraction(1, p**v(x))

    
