import random
import matplotlib.pyplot as plt
from math import exp, factorial

def run(p, q):    
    freq = [0]*(q+1)
    
    buffer = [[0]*j for j in range(q)]
    
    for i in range(10000):
        out = int(random.random() < p/q)
        
        for i, bf in enumerate(buffer):
            if len(bf) == q:
                freq[sum(bf)] += 1
                buffer[i] = []
                
            buffer[i] = buffer[i] + [out]
            
    poisson = lambda k, m: (exp(-m)*(m**k))/factorial(k)    
        
    plt.plot([fq/sum(freq) for fq in freq], 'bo')
    plt.plot([fq/sum(freq) for fq in freq], 'g--')
    plt.plot([poisson(k, p) for k in range(q+1)])
    plt.show()    