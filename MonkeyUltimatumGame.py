import random
from numpy import mean, std, array
import matplotlib.pyplot as plt

d = 100
mutation_rate = 0.05

class Monkey:
    def __init__(self, m = 1.0*d, g = -1, t = -1):
        self.money = m
        self.give =  g if g >= 0 else random.random()*d         #amount of money that the monkey decides to give    
        self.take =  t if t >= 0 else random.random()*d         #mininum amount of money that the monkey will accept

    def __str__(self):
        return '(%g, %g, %g)' %(self.money, self.give, self.take)

def permute(n):
    N, P = list(range(n)), []

    for j in range(n):
        k = random.choice(N)

        P.append(k)
        N.remove(k)

    return P

#Exchange money
def exchange(M):
    R = permute(len(M))
    
    for i, monkey in enumerate(M):
        koti = M[R[i]]

##        if monkey == koti:
##            continue

        if monkey.give > koti.take:
            monkey.money -= monkey.give
            koti.money += monkey.give
        else:
            monkey.money = 0

#Monkeys of the next generation
def gen(M):
    F = []

    correct = lambda x: x % d if (x//d % 2) == 0 else d - (x%d)
    mutate = lambda x: x + random.random()*mutation_rate*d*((-1)**(random.random() > 0.5))

    while len(F) < len(M):
        koti = random.choice(M)

        if 2*d*random.random() < koti.money:
            F.append( Monkey(1.0*d, correct(mutate(koti.give)), correct(mutate(koti.take)) ))

    return F

#Rank monkeys according to success
##for i in range(len(M)):
##    pos = i
##
##    for j in range(i, len(M)):
##        if M[j].money > M[pos].money:
##            pos = j
##
##    M[i], M[pos] = M[pos], M[i]


def main(n, runs, sx=-1, sy=-1):
    M = [Monkey(1, sx, sy) for i in range(n)]

    V = []

    plt.axis((0, d, 0, d))
    plt.xlabel('Give')
    plt.ylabel('Take')

    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlim=(0, d), ylim=(0, d))
    ax.set_xlabel('Give')
    ax.set_ylabel('Take')
    pop, = ax.plot([], [], 'ro', color=(0, 0, 0))
    popmean, = ax.plot([], [], 'r*')

    pop.set_markersize(100/n)
    
    for i in range(runs):
        G, T = [], []

        for monkey in M:
            G.append(monkey.give)
            T.append(monkey.take)
        
        v = [mean(G), std(G), mean(T), std(T)]
        
        #plt.plot(v[0], v[2], 'bo')
        #plt.annotate(str(i), (v[0], v[2]))
        #plt.scatter(G, T, s=0.5*(v[1]+v[3]), c=[(0, i/runs, 0) for k in range(len(M))])
        #plt.clf()

        pop.set_xdata(G)
        pop.set_ydata(T)
        pop.set_color((0, i/runs, 0))

        popmean.set_xdata(v[0])
        popmean.set_ydata(v[2])
        popmean.set_color((0.5, 0.5, i/runs))
        popmean.set_markersize(25/d*(v[1] + v[3]))

        fig.canvas.draw()
        fig.canvas.flush_events()
        
        V.append(v)
            
        exchange(M)
        M = gen(M)
##        if (i > runs // 2) and i%(runs//100) == 0:
##            bandar = Monkey()
##            bandar.take = random.random()
##            print(bandar.take)  
##            M[-1] = bandar

    print('Done')

    #plt.scatter(V[:, 0], V[:, 2])

    #plt.show()

    print(V[-1])

    V = array(V)
    
    gif = plt.figure()
    m_ax = gif.add_subplot(111)
    m_ax.set(xlim=(0, d), ylim=(0, d))
    m_ax.scatter(V[:, 0], V[:, 2])

##    if input('') == 'showdata':
##        return V
