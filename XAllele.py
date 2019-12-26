import matplotlib.pyplot as plt
import random
import numpy as np

def init(n, p_m, p_f):
    males = [str(int(random.random() < p_m)) + '2' for i in range(n)]
    females = [str(int(random.random() < p_f)) + str(int(random.random() < p_f)) for i in range(n)]
    return males, females

def repr(a, b):
    return random.choice(list(a)) + random.choice(list(b))

def run(males, females, fitness):
    prog_males, prog_females = [], []
    
    while(len(prog_males) < len(males) or len(prog_females) < len(females)):
        ind = repr(random.choice(males), random.choice(females))

        #if random.random() < fitness[ind]:
        if '2' in ind:
            prog_males.append(ind)
        else:
            prog_females.append(ind)

    return prog_males, prog_females

def decompose(males, females):
    p_males, p_females = 0, 0

    for male in males:
        p_males += sum([a == '1' for a in male])

    for female in females:
        p_females += sum([a == '1' for a in female])
    
    return p_males/(2*len(males)), p_females/(2*len(females))

def main(n = 10000, runs = 50, p_m=0.4, p_f=0.8, fitness = {'00':1, '01': 1, '10': 1, '11': 1}):
    males, females = init(n, p_m, p_f)
    
    plt.ion()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set(xlim=(-0.15, 1.15), ylim=(0, 1))
    ax.set_xlabel('M/F'); ax.set_ylabel('Frequency of Allele'); ax.set_title('Hardy-Weinberg Equilibrium')
    pop, = ax.plot([], [], 'ro')
    popmean, = ax.plot([], [])
    popdata = []

    for r in range(runs):
        states = [0, 1]
        compost = decompose(males, females)
        print('Run', r, ': ', compost)

        popdata.append(np.array(compost))
        
        pop.set_xdata (states)
        pop.set_ydata(compost)

        popmean.set_ydata([0.25*p_m + 0.5*p_f]*6)
        popmean.set_xdata([i/5 for i in range(6)])

        ax.bar(states, compost, width=0.25, color='blue', alpha=0.01)
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        males, females = run(males, females, fitness)
    
    plt.close(fig)

    gif = plt.figure()
    ax = gif.add_subplot(111)
    
    ax.plot(popdata, linestyle='dashed')
    gif.canvas.draw()
    
main(n = 100, runs = 1000, p_m = 0.4, p_f = 0.8)
