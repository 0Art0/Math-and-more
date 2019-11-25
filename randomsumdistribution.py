import random
import matplotlib.pyplot as plt
import numpy
from math import e
from scipy.optimize import curve_fit

def generate(n, N=100000, f=3):
    D = [sum([random.random() for j in range(n)]) for i in range(N)]
    L = [0 for k in range(n*10**f)]

    for d in D:
        L[int(d*10**f)] += 1

    for l in range(n*10**f):
        L[l] /= N

    def bell(x, a):
        return a*e**(-6/n*(x-n/2)**2)

    popt, pconv = curve_fit(bell, numpy.arange(0, n, 10**(-f)), L)

    print(popt)
    
    plt.scatter([k/(10**f) for k in range(n*10**f)], L, s=0.01)
    plt.plot(numpy.arange(0, n, 10**(-f)), [bell(x, *popt) for x in numpy.arange(0, n, 10**(-f))])
    plt.show()
