import time

def sieve(n):
    nums = [False] + [True]*(n-1)
    for j in range(int(n**0.5)):
        if nums[j]:
            for i in range(j*(j+2), n, j+1):
                nums[i] = False

    return [i+1 for i, p in enumerate(nums) if p]


def optimisedsieve(n):
    nums = [False, True] + [True, False]*int(n/2 - 1) + (n%2)*[True]
    primes = []
    for j in range(2, int(n**0.5), 2):
        if nums[j]:
            primes.append(j+1)
            for i in range(j*(j+2), n, 2*(j+1)):
                nums[i] = False

    for k in range(int(n**0.5) + 1*(int(n**0.5)%2), n, 2):
        if nums[k]:
            primes.append(k+1)        

    return primes

def lamesieve(n):
    primes = [2]
    for i in range(3, n+1, 2):
        c = 0
        for p in primes:
            if i % p == 0:
                c = 1
                break
        if not c:
            primes.append(i)
    return primes

t1 = time.clock()
a = optimisedsieve(12345678)
t2 = time.clock()
#print(t2-t1)
