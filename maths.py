factorial = lambda n: 0**n or n*factorial(n-1)

choose = lambda n, k: 0**n or (n+1-k)/k*choose(n, k-1)//1

absolute = lambda n: (n*n)**0.5

signum = lambda n: absolute(n)/n


