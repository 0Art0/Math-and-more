import random

n = int(input('n: '))

d = [0]*(n+1)
d[1] = n

print(d)
for k in range(20):
    for j in range(int(n/2)):
        if j % 3 == 0:
            continue
        av = [i for i, d_ in enumerate(d) if d_ != 0]

        a = random.choice(av)
        if d[a] == 1: av.remove(a)
        b = random.choice(av)

        if a != 0 and b != 0:
            d[a] -= 1; d[a-1] += 1
            d[b] -= 1; d[b+1] += 1

    print(d)
    



