import matplotlib.pyplot as plt
from fraction import Fraction
from math import log

def run(N):
    s = Fraction()

    v = []
    f = []
    w = []
    u = []
    
    l = 0

    for n in range(1, N+1):
        s = s + Fraction(1, n)
        v.append(float(s))
        w.append(log(n))
        u.append(float(s) - log(n))

        if float(s)//1 > l:
            f.append(n)
            l = float(s) // 1


    print(f)

    print(u[-3:])

    plt.scatter([i for i in range(1, N+1)], v, s=0.5)
    plt.scatter([i for i in range(1, N+1)], w ,s=0.5)
    plt.scatter([i for i in range(1, N+1)], u ,s=0.75)
    plt.plot(f, [0 for i in range(len(f))], 'b*')
    plt.show()
