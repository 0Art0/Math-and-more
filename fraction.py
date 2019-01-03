def gcd(c, d):
	a, b = abs(c), abs(d)
	return (-1)**(c < 0 and d < 0)*a if a == b else \
                round(c+d, 8) if (round(c, 8) == 0 or round(d, 8) == 0) else ((-1)**(c < 0 and d < 0)*gcd(a%b, b%a))

class Fraction:

    def __init__(self, num=0, den=1):
        self.numerator = num
        self.denominator = den
        self.simplify()

    def simplify(self):
        d = gcd(self.numerator, self.denominator)
        self.numerator = round(self.numerator/d); self.denominator = round(self.denominator/d);

    def __str__(self):
        return '%d/%d' %(self.numerator, self.denominator)

    def __add__(self, f):
        if type(f) is int: f = Fraction(f)
        return Fraction(self.numerator*f.denominator + f.numerator*self.denominator, self.denominator*f.denominator)

    def __mul__(self, f):
        if type(f) is int: f = Fraction(f)
        return Fraction(self.numerator*f.numerator, self.denominator*f.denominator)

    def __sub__(self, f):
        if type(f) is int: f = Fraction(f)
        return self + f*-1

    def __truediv__(self, f):
        if type(f) is int: f = Fraction(f)
        return self*Fraction(f.denominator, f.numerator)

    def clone(self):
        return Fraction(self.numerator, self.denominator)
