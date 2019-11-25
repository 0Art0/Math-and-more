def permute(a):
    return [([a[i]] + p) for i in range(len(a)) for p in permute(a[:i] + a[i+1:])] if a else [[]]

def pos(n):
    
    b = [0]*(n-1)
    
    pos = [b]
    
    def succ(b):
        return [1] + b[1:] if b[0] == 0 else [0] + succ(b[1:])
    
    for i in range(int(2**(n-1)-1)):
        b = succ(b)
        pos.append(b)
           
    return pos

def main(n):
    
    def run(c, p_, n):
        i = c.index(0)
        p = p_[:i] + [1] + p_[i:]
        
        o = []
        
        for i in range(n):
            h = c[i] + p[i]
            
            if h not in o:
                o.append(h)
            
            else:
                h = c[i] + (p[i] + 1)%2
                
                if h not in o and c[i] != 0:
                    o.append(h)
                    p[i] = (p[i] + 1)%2
                else:
                    return p[:i+1]
        
        return p            
                    
    fav = 0
    N = 0
                
    for c in permute(list(range(n))):
        space = []
        
        for p in pos(n):
            r = run(c, p, n)
            if r not in space:
                space.append(r)
        
        fav += 1
        N += len(space)
    
    return (fav, N)

def psum(n):
    sum = 0
    for i in range(1, n+1):
        f = main(i)
        sum += f[0]/f[1]
    return sum
