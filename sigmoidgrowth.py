import matplotlib.pyplot as plt

r = 2.5
K = 10

P = [1]
T = [0]
V = [1]

for t in range(1, 101):
    N = P[-1]
    V.append(N)
    
    N_ = N + r*N*(1-N/K)
    P.append(N_)
    
    T.append(N_)
    
    V.append(N_)
    T.append(N_)
    

plt.figure()
plt.subplot(211)
plt.plot(P)
plt.plot(P, 'ro')


plt.subplot(212)
plt.plot([N * (1 + r - r*N/K) for N in V])
plt.plot([N * (1 + r - r*N/K) for N in V], 'k*')
plt.plot(T, V, 'g^')

plt.show()
