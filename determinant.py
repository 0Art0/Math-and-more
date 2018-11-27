import numpy

matrix = numpy.loadtxt('matrix.txt')
print(matrix)
def determinant(m):
    return sum([((-1)**i)*m[0][i]*determinant(minor(m, i)) for i in range(len(m[0]))]) if m.any() else 1

def minor(m, i):
    m_ = m[1:, :]
    return(numpy.append(m_[:, :i], m_[:, i+1:], axis=1))
    
print(determinant(matrix))
