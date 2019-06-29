def mod(n, p):
    #works for n in Z
    return int(n) if 0 < n <= abs(p) else mod(n + ((-1)**(n >= p))*p, p)

def base(n, b):
    return '' if n == 0 else base((n - mod(n, b))/b, b) + str(mod(n, b))

#def choose (n, k, b):
#    return 1 if k == 0 else mod(mod(n+1-k, b)*mod(mod(k, b)**(b-2), b)*choose(n, k-1, b), b)

b = 2

def choose (n, k):
    return 1 if k == 0 else mod((n+1-k)*choose(n, k-1)*(mod(k**(b-2), b) if mod(k, b) != n else 1/b), b)

def disp(n):
	s = ''
	for i in range(n+1):
		s += str(choose(n, i)) + ' '
	print(s)

def coeffs(n, m):
    for i in range(n+1):
        print(base(i, m), choose(n, i, m))
        
