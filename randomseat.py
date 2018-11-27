import random

def run(t):
        c = 0; n = 100
        for j in range(t):
                seats = [0 for i in range(n)];
                seats[random.randint(0, n-1)] = 1;
                for i in range(1, n):
                        if seats[i] == 0:
                                seats[i] = 1;
                                if i == n-1:
                                        c += 1;
                        else:
                                s = random.randint(1, n-sum(seats))
                                uc = 0
                                for k in range(n):
                                        if seats[k] == 0:
                                                uc += 1
                                        if uc == s:
                                                seats[k] = 1;
                                                break

        return (c/t)


