import time

def sieve(n):
    nums = [True for i in range(n)]; nums[0] = False;
    primes = []
    for j in range(int(n**0.5)):
        if nums[j]:
            primes.append(j+1)
            for i in range(j*(j+2), n, j+1):
                nums[i] = False

    return primes


def optimisedsieve(n):
    nums = [False, True] + [True, False]*int(n/2 - 1) + (n%2)*[True]
    primes = []
    for j in range(2, int(n**0.5), 2):
        if nums[j]:
            primes.append(j+1)
            for i in range(j*(j+2), n, 2*(j+1)):
                nums[i] = False

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
a = optimisedsieve(123456789)
t2 = time.clock()
print(t2-t1)