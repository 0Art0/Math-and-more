from math import inf

def gcd(a, b):
	return a if a == b else \
                round(float(a+b), 8) if (round(float(a), 8) == 0 or round(float(b), 8) == 0) else gcd(a%b, b%a)

class Fraction:

    def __init__(self, num=0, den=1):
        self.numerator = float(num)
        self.denominator = float(den)
        self.simplify()
        if self.denominator < 0:
            self.numerator *= -1; self.denominator *= -1

    def simplify(self):
        d = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = round(self.numerator/d); self.denominator = round(self.denominator/d);

    def __str__(self):
        return '%d/%d' %(self.numerator, self.denominator)

    def __add__(self, f):
        if type(f) is int: f = Fraction(f)
        return Fraction(self.numerator*f.denominator + f.numerator*self.denominator, self.denominator*f.denominator)

    def __mul__(self, f):
        if type(f) is int or type(f) is float: f = Fraction(f)
        return Fraction(self.numerator*f.numerator, self.denominator*f.denominator)

    def __sub__(self, f):
        if type(f) is int: f = Fraction(f)
        return self + f*-1

    def __truediv__(self, f):
        if type(f) is int: f = Fraction(f)
        return self*Fraction(f.denominator, f.numerator)

    def __lt__(self, f):
        return (self - f).numerator < 0

    def __le__(self, f):
        return (self - f).numerator <= 0

    def __eq__(self, f):
        return (self - f).numerator == 0

    def __gt__(self, f):
        return (self - f).numerator > 0

    def __ge__(self, f):
        return (self - f).numerator >= 0

    def __ne__(self, f):
        return (self - f).numerator != 0

    def __abs__(self):
        return self*-1 if self < Fraction() else self

    def __float__(self):
        return self.numerator/self.denominator if self.denominator != 0 else inf
