from fraction import *

class mass:
    def __init__(self, m, v, pos):
        self.mass = m
        self.v = v
        self.pos = pos
    
m = mass(1, 0, 1)
M = mass(100**1, -1, 10)
#w = mass(Fraction(1, 0), 0, 0)

count = 0

while((m.v > M.v) or m.v < 0):
    if count % 2:
        m.pos = 0
        M.pos += M.v/m.v*m.pos*-1
        m.v *= -1
    else:
        m.pos = M.pos = (M.v*m.pos - m.v*M.pos)/(M.v - m.v)
        v = M.v - m.v
        M.v = (m.mass*2*m.v + (M.mass-m.mass)*M.v)/(m.mass+M.mass)
        m.v = v + M.v

    count += 1

print(count)

a = 100**2

for n in range(int((1.5*a)**0.5), a):
    s = t = 2*n + 1
    for  k in range(1, n):
        t *= (((2*n + 2)/(2*k + 1) - 1) * (1 - n/k))/a
        s += t
    if s <= 0:
        print(2*n + ((n-1)%2))
        break
