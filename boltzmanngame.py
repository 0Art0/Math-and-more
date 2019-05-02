#Boltzmann Game
import random

n = int(input('n: '))
p = [1]*n
for i in range(10):
    for j in range(n):
        a, b = random.randint(0, n-1), random.randint(0, n-1)
        win = round(random.random())
        if win and p[b] > 0:
           p[a] += 1
           p[b] -= 1
        if not win and p[a] > 0:
           p[b] += 1
           p[a] -= 1 

    print(sorted(p))   
