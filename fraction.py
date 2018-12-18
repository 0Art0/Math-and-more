def gcd(c, d):
	a, b = abs(c), abs(d)
	return a if abs(a) == abs(b) else gcd(a%b, b%a) if (a!=0 and b!=0) else a+b

class Fraction:

    def __init__(self, num=0, den=1):
        self.numerator = num
        self.denominator = den

    def simplify(self):
        d = gcd(self.numerator, self.denominator)
        self.numerator //= d; self.denominator //= d;

    def __str__(self):
        return '%d/%d' %(self.numerator, self.denominator)

    def __add__(self, f):
        sd, fd = self.denominator, f.denominator
        d = gcd(sd, fd)
        return Fraction(self.numerator*(fd//d) + f.numerator*(sd//d), (sd*fd)//d)

    def __mul__(self, f):
        return Fraction(self.numerator*f.numerator, self.denominator*f.denominator)

    def __sub__(self, f):
        return self + Fraction(-1)*f

    def __truediv__(self, f):
        return self*Fraction(f.denominator, f.numerator)
