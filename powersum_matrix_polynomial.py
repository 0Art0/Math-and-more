from matrix import *

n = int(input('n: '))

def psum(n):
    a = numpy.array([[i**j for j in range(n+2)[::-1]] for i in range(1, n+3)])
    b = numpy.array([sum([i**n for i in range(1, j+1)]) for j in range(1, n+3)])[:, None]
    return multiply(inverse(a), b)[:, 0]

print(psum(n))
