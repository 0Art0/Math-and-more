p = eval(input('p: '))

def diff(a):
    return [a[i+1]-a[i] for i in range(len(a)-1)]

def deg(a):
    b = diff(list(a))
    n = 0
    while(sum([e != 0 for e in b]) != 0):
        b = diff(b)
        n += 1
    return n-1*bool(n)

def polconstruct(pol):
    pfit = [0 for i in range(deg(p)+1)]
    g = lambda n: sum()
    

