import random
from numpy import mean, std, array
import matplotlib.pyplot as plt

d = 1

class Monkey:
    def __init__(self, m = 100*d, g = -1, t = -1):
        self.money = m
        self.give =  g if g >= 0 else int(random.random()*d*100)   
        self.take =  t if t >= 0 else int(random.random()*d*100)
        
def exchange(M): #possible bug: call by reference
    
    for i, monkey in enumerate(M):
        koti = M[(i+1)%len(M)]

        if monkey.give > koti.take:
            monkey.money -= monkey.give
            koti.money += monkey.give
        else:
            monkey.money = 0

def gen(M):
    F = []

    mutate = lambda x: (x + random.choice([-1, 1])*int(random.random()*5)*d)%(d*100)

    while len(F) < len(M):
        koti = random.choice(M)

        if int(200*d*random.random()) < koti.money:
            F.append( Monkey(100*d, mutate(koti.give), mutate(koti.take)) )

    return F

def main(n, runs, sx=-1, sy=-1):
    M = [Monkey(100, sx, sy) for i in range(n)]

    V = []
    
    for i in range(runs):
        G, T = [], []

        for monkey in M:
            G.append(monkey.give)
            T.append(monkey.take)
        
        v = (mean(G), std(G), mean(T), std(T))
        
        plt.plot(v[0], v[2], 'ro', color = (0, i/runs, 0))
        plt.annotate(str(i), (v[0], v[2]))

        V.append(v)
            
        exchange(M)
        M = gen(M)
    print('Done')

    
    plt.axis((0, 100*d, 0, 100*d))
    plt.xlabel('Give')
    plt.ylabel('Take')

    print(V[-1])
    
    if input('') == 'showdata':
        return V
