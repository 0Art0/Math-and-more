class HammingSpace:            
    def __init__(self, A, n):
        self.alphabet = A
        self.dimension = n
        self.space = self.createSpace()

    def createSpace(self, S=[[]]):
        if len(S[0]) == self.dimension:
            return S
        
        T = []
        for v in S:
            for a in self.alphabet:
                T.append(v + [a])
        
        return self.createSpace(T)
    
    def HammingDistance(self, v, w):
        return sum([v[i] != w[i] for i in range(self.dimension)])
    
    def Ball(self, c, r):
        ball = []
        
        for v in self.space:
            if self.HammingDistance(v, c) <= r:
                ball.append(v)
        
        return ball

import random
    
def findPacking(n, approach = 0):
    P = HammingSpace([0, 1], n)
    S = list(P.space); random.shuffle(S)
    
    N = []
    
    bound = (2**n/(n+1))//1
    
    #Approach 0: Minimize the total distance from all balls
    dist = lambda w: sum([P.HammingDistance(w, p) for p in N])
    while(len(S)):
        mv, md = S[0], P.dimension**len(N)
        for v in S:
            if dist(v) < md:
                mv, md = v, dist(v)

    #Approach 1: Choose a random point that is adjacent to atleast one sphere
##    while(True):
##        f = False
##        mv = []
##        for v in S:
##            if len(N) == 0 or sum([P.HammingDistance(p, v) == 3 for p in N]):
##                f = True; mv = v; break
##
##        if not f:
##            break
        #mv = random.choice(S) #Approach 2: Randomly selecting vectors
        N.append(mv)

        for vec in P.Ball(mv, 2):
            if vec in S:
                S.remove(vec)
                
    return N, len(N), bound
