def derivative(p): 
	return [i*p[i] for i in range(1, len(p))] or [0]

f = lambda p, x: sum([p[i]*(x**i) for i in range(len(p))])

def extrema(p): 
	return [] if len(p) <= 2 else zeros(derivative(p), extrema(derivative(p)))           

def zeros(p, m, l1=-1e2, l2=1e2):
    m = [l1] + sorted(m) + [l2]; roots = []

    def root(p, a, b):
        if f(p, a)*f(p, b) <= 0:
            r = (a+b)/2
            if (abs(f(p, r)) < 1e-5):  
                roots.append(r); return;	        
            root(p, a, r); root(p, r, b);

    for i in range(0, len(m)-1):
        root(p, m[i], m[i+1])

    return roots

def main():
        p = eval(input('p: '))
        z = zeros(p, extrema(p));
        print([float(format(zero, '.5f')) for zero in z])
