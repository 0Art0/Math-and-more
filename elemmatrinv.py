import numpy
import matrix

M = numpy.loadtxt('matrix.txt', delimiter=' ') #input matrix
N = [] #list of row operations for inverse

from powerset import powerset

#class defining elementary row operations
class E:
    def __init__(self, a, i, j):
        self.alpha = a
        self.i = i
        self.j = j

    def real(self): #returns e in matrix form
        Z = numpy.zeros(M.shape)
        Z[self.i, self.j] = self.alpha
        return Z

    def __mul__(self, e): #multiplying two e's
        return E(int(self.j == e.i) * self.alpha * e.alpha, self.i, e.j)

    def __eq__(self, e):
        return (self.alpha == e.alpha and self.i == e.i and self.j == e.j)

    def __str__(self): #printing an e
        return str((self.alpha, self.i, self.j))


#swapping two rows
def swap(i, j):
    return numpy.array([E(-2, j, j), E(1, i, j), E(-1, j, i), E(1, i, j)])


#sorts for non-zero pivots
def sort(A, S = []):

    if A.size == 0:
        return S

    if A[0, 0] != 0:
        return sort(A[1:, 1:], S)

    B = numpy.zeros(A.shape)

    os = len(M) - len(A) #offset
    
    for i in range(len(A)-1):
        B[i] = numpy.array(A[(i+1)])
        S += list(swap(os+i, os+i+1))
        
    B[-1] = numpy.array(A[0])
    
    return sort(B, S) + S



#Finally sorting M

N = sort(M)

for e in N[::-1]:
    M += numpy.matmul(e.real(), M)

print('Sorted Matrix\n', M)


#Gaussian elimination for inverse
def eliminate(A):
    O = []

    for row in range(len(A)):
        O = [E(1/A[row, row] - 1, row, row)] + O
        A[row] = A[row]/A[row, row]

        for rho in range(len(A)):
            if row == rho:
                continue
            
            O = [E(A[rho, row], rho, row)] + O
            A[rho] += -A[rho, row]*A[row]

    return O


#Perform row elimination
F = eliminate(numpy.array(M))
N = F + N

I = numpy.eye(len(M))

for e in F[::-1]:
    I = I  + numpy.matmul(e.real(), I)

print('Inverse\n', matrix.inverse(M))

print('Inversee\n', I)

print('Product\n', matrix.multiply(M, I))
