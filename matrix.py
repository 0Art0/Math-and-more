import numpy

#matrix = numpy.loadtxt('matrix.txt')

def minor(m, i, j):
    m_ = numpy.append(m[:i, :], m[i+1:, :], axis=0)
    return(numpy.append(m_[:, :j], m_[:, j+1:], axis=1))

def determinant(m):
    return sum([((-1)**j)*m[0][j]*determinant(minor(m, 0, j)) for j in range(len(m[0]))]) if m.size != 0 else 1
 
def multiply(A, B):  
    return numpy.array([[sum(A[i, :] * B[:, j]) for j in range(B.shape[1])] for i in range(A.shape[0])]) \
           if A.shape[1] == B.shape[0] else print("Matrices not compatible for multiplication.")     

def inverse(m):
    inv = numpy.array(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            inv[j, i] = ((-1)**(i+j))*determinant(minor(m, i, j))
    return inv/determinant(m)
