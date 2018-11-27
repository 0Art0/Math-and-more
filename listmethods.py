def addlists(l1, l2):
    lmin = min(len(l1), len(l2))
    return [l1[i]+l2[i] for i in range(lmin)] + l1[lmin:] + l2[lmin:]

def multscal(l, k):
    return [k*a for a in l]

def multlists(l1, l2):
    lmin = min(len(l1), len(l2))
    return [l1[i]*l2[i] for i in range(lmin)] + l1[lmin:] + l2[lmin:]

def zerolist(n):
    return [0 for i in range(n)]

def tidyup(l, n):
    return [round(a, n) for a in l]

def remelem(a, e):
    b = list(a)
    b.remove(e)
    return b

    


