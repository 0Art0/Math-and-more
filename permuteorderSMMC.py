def permute(a):
    return [([a[i]] + p) for i in range(len(a)) for p in permute(a[:i] + a[i+1:])] if a else [[]]

def asc(p):
    o = 0
    for i, e in enumerate(p):
        if e != 0 and i > p.index(e-1): #indexing
            o += 1
    return o

def inc(p):
    c = 0
    for i in range(len(p)-1):
        if p[i] < p[i+1]:
            c += 1
    return c

def partition(L):
    S = []
    j = 0
    for i, e in enumerate(L):
        if i > 0 and (L[i-1] != e):
            S.append(L[j:i])
            j = i
    S.append(L[j:])
    return S

def sort(sigma):
    return [sigma.index(i) for i in range(len(sigma))]

def main(n):
    #P = partition(sorted([asc(p) for p in permute(list(range(n+1)))]))
    #print(P)
    #print([len(p) for p in P])
    S = permute(list(range(1, n+1)))
    E = []
    for p in S:
        if inc(p) != asc(p):
            E.append(p)
    return E

def A(n):
    if n == 0:
        return [1]
    A_ = A(n-1)
    d = [(i+1)*A_[i+1] for i in range(len(A_)-1)] + [0] if n > 1 else [0, 0]
    return [([0]+d)[i] - ([0, 0] + d[:-1])[i] + (A_+[0])[i] + (n-1)*([0]+list(A_))[i] for i in range(len(A_)+1)]

            

