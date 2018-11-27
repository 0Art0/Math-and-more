import time

permute = lambda a: [[e] + p for e in a for p in \
                               permute(list(filter(lambda n: n != e, a)))] if a else [a]

def diag(a):
	for i in range(len(a)-1):
		for j in range(i+1, len(a)):
			if abs(a[i]-a[j]) == j - i:
				return True
			    
def solutions(a):
    c = 0
    for l in a:
        if not diag(l):
            c += 1
    return c

def run():
    n = int(input('n: '))
    #start = time.clock()
    s = (solutions(permute(list(range(n)))))
    #stop = time.clock()
    #duration = stop-start
    print(s) #duration

run()
