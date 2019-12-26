import numpy as np


def run(N=7, show=False):
    G = lambda n: np.array([[1]*j + [-1]*(j != n) + [0]*(n-j-1) for j in range(1, n+1)])

    A = np.concatenate((np.eye(N), G(N)), axis=1)

    def row_operate(M, a, i, j):
        M[i] += a*M[j]

    if show: print('Original\n', A)

    for j in range(N):
        for i in range(j+1, N):
            row_operate(A, -1, i, j)

    if show: print('Upper triangular\n', A)

    for i in range(1, N):
        for j in range(1, i+1):
            row_operate(A, (0.5)**j, i-j, i)

    if show: print('Diagonal\n', A)

    for i in range(1, N):
        row_operate(A, -0.5, i, i)

    if show: print('Identity\n', A)

    if show: print('Final\n', A[:, tuple(range(N, 2*N))])

    J = A[:, tuple(range(N))]

    if show: print('Inverse\n',  J)

    if show: print('Product\n', np.matmul(J, G(N)))

    return J
