import matplotlib.pyplot as plt
import random
import numpy as np

def init(n, p):
    popln = [str(int(random.random() < p)) + str(int(random.random() < p)) for i in range(n)]
    return popln

def repr(a, b):
    return random.choice(list(a)) + random.choice(list(b))

def run(popln, fitness):
    prog = []
    
    while(len(prog) < len(popln)):
        ind = repr(random.choice(popln), random.choice(popln))

        if random.random() < fitness[ind]:
            prog.append(ind)

    return prog

def decompose(popln):
    homr, hetr, homd = 0, 0, 0

    for ind in popln:
        if ind == '00':
            homr += 1
        elif ind == '10' or ind == '01':
            hetr += 1
        elif ind == '11':
            homd += 1

    return homr/len(popln), hetr/len(popln), homd/len(popln)

def main(n = 10000, runs = 50, p=0.5, fitness = {'00':1, '01': 1, '10': 1, '11': 1}):
    popln = init(n, p)
    
    plt.ion()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set(xlim=(-0.15, 1.15), ylim=(0, 1))
    ax.set_xlabel('Genotype [0, 0.5, 1]'); ax.set_ylabel('Frequency'); ax.set_title('Hardy-Weinberg Equilibrium')
    pop, = ax.plot([], [], 'ro')
    popmean, = ax.plot([], [], )
    popdata = []

    for r in range(runs):
        states = [0, 0.5, 1]
        compost = decompose(popln)
        print('Run', r, ': ', compost, 0.5*compost[1] + compost[2])

        mean = sum([states[i] * compost[i] for i in range(3)])

        popdata.append(np.array(compost))
        
        pop.set_xdata (states)
        pop.set_ydata(compost)

        popmean.set_xdata([mean]*6)
        popmean.set_ydata([i/5 for i in range(6)])

        ax.bar(states, compost, width=0.25, color='blue', alpha=0.01)
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        popln = run(popln, fitness)
    
    plt.close(fig)

    gif = plt.figure()
    ax = gif.add_subplot(111)
    
    ax.plot(popdata, linestyle='dashed')
    gif.canvas.draw()
    
main(p=0.5, runs = 30, fitness = {'00':0, '01': 1, '10': 1, '11': 1})
