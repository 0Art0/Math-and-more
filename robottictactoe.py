import numpy as np
import random

k = 2**0.5
I = k*np.ones((3, 3))

c = lambda a: sum(a) % 3 == 0

check = lambda A: c(A[0]) or c(A[1]) or c(A[2]) or c(A[:, 0]) or c(A[:, 1]) or c(A[:, 2]) or c(np.diagonal(A)) or c(np.diagonal(np.fliplr(A)))

def walk():
    B = I.copy()

    for j in range(9):
        L = np.reshape(B, (1, 9))[0]
        m = random.choice([i for i in range(9) if L[i] == k])
        B[m//3, m%3] = (1, 2)[j%2]
        if check(B):
            return j+1

    return 9

def run(N):
    return sum([walk() for i in range(N)])/N

