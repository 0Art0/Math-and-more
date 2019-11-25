import random
import numpy as np
import matplotlib.pyplot as plt
#Fairneesss versus Reason in the Ultimatum Game
d = 100

class givers:
    def __init__(self, g = -1):
        self.give =  g if g >= 0 else random.random()*d #INT
        self.fitness = d/2

class takers:
    def __init__(self, t = -1):
        self.take =  t if t >= 0 else random.random()*d #INT
        self.fitness = d/2
        
def exchange(G, T):
    n = len(G)
    DG, DT = np.zeros((n, n)), np.zeros((n, n)) #Data from the fitness exchanges

    #perform exchanges
    for g, giver in enumerate(G):
        for t, taker in enumerate(T):
            DG[g, t], DT[g, t] = (d-giver.give, giver.give) if giver.give > taker.take else (0, 0)

    #Re-evaluate fitness
    for g, giver in enumerate(G):
        giver.fitness = np.mean(DG[g, :])

    for t, taker in enumerate(T):
        taker.fitness = np.mean(DT[:, t])

def gen(G, T):
    FG, FT = [], []
    n = len(G)

    mutation_rate = 0.02

    from math import e
    
    correct = lambda x: x % d if (x//d % 2) == 0 else d - (x%d)
    #correct = lambda x: x if (0 <= x < d) else (0 if x < 0 else d)
    mutate = lambda x: x + random.choice([-1, 1])*(random.random()*mutation_rate*d) #INT
    #rescale = lambda x, k=(1+5**0.5)/d: (e**(k*x) - 1)/(e**(k*d) - 1)*d
    rescale = lambda x: x

    while len(FG) < n or len(FT) < n:
        for k in range(n):
            if d*random.random() < rescale(G[k].fitness):
                FG.append( givers(correct(mutate(G[k].give))) )

            if d*random.random() < rescale(T[k].fitness):
                FT.append( takers(correct(mutate(T[k].take))) )

    return FG[:n], FT[:n]

def main(n, runs, gee=-1, tee=-1):
    G, T = [givers(gee) for i in range(n)], [takers(tee) for i in range(n)]

    file = open('ultimatum_means.txt', 'w')

    plt.axis((0, d, 0, d))
    plt.xlabel('Give')
    plt.ylabel('Take')
    
    plt.ion()

    fig = plt.figure()

    gax = fig.add_subplot(311)
    tax = fig.add_subplot(313)


    gax.set_title('Givers')
    gax.set_xlabel('Give value')
    tax.set_title('Takers')
    tax.set_xlabel('Take value')

    gax.set(xlim=(0, d), ylim=(-0.1, 0.1))
    tax.set(xlim=(0, d), ylim=(-0.1, 0.1))
    

    gpop, = gax.plot([], [], 'ro')
    tpop, = tax.plot([], [], 'ro')

    gmean, = gax.plot(d/2, 0, 'b*')
    tmean, = tax.plot(d/2, 0, 'g*')

    gpop.set_ydata( list(np.zeros((1, len(G)))[0]) )
    gpop.set_markersize( 100/len(G) )
    tpop.set_ydata( list(np.zeros((1, len(T)))[0]) )
    tpop.set_markersize( 100/len(T) )
    
    for i in range(runs):
        Gdata = [giver.give for giver in G]
        
        gpop.set_xdata( Gdata )
        #gpop.set_ydata( list(np.zeros((1, len(Gdata)))[0]) )
        gpop.set_color((0, i/runs, 0))

        gmean.set_xdata( np.mean(Gdata) )
        gmean.set_markersize( np.std(Gdata) )

        Tdata = [taker.take for taker in T]
        tpop.set_xdata( Tdata )
        #tpop.set_ydata( list(np.zeros((1, len(Tdata)))[0]) )
        tpop.set_color((0, 0, i/runs))

        tmean.set_xdata( np.mean(Tdata) )
        tmean.set_markersize( np.std(Tdata) )

        file.write(str(np.mean(Gdata)) + ', ' + str(np.mean(Tdata)) + '\n' )

        fig.canvas.draw()
        fig.canvas.flush_events()

        exchange(G, T)
        G, T = gen(G, T)

    file.close()
    data = np.loadtxt('ultimatum_means.txt', dtype='float', delimiter=',')

    gif = plt.figure()
    ax = gif.add_subplot(111)
    ax.set_title('Mean values of "give" and "take" over time')
    ax.set_xlabel('Timesteps')
    ax.set_ylabel('Value')
    ax.plot(data)
    ax.show()
