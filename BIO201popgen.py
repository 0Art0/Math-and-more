# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:24:01 2019

@author: 91886
"""
T = 200

import numpy as np
import matplotlib.pyplot as plt

L = np.matrix('[0, 2, 1, 1]; [0.5, 0, 0, 0]; [0, 0.2, 0, 0]; [0, 0, 0.1, 0]')

N = np.matrix('[200; 0; 0; 0]')
print(N)

#plt.bar(np.matrix('[1;2;3;4]'), N)

size = [200]
R2, R3, R4 = [0], [0], [0]

for i in range(T):
    N = L*N
    size.append(sum(N)[0, 0])
    R2.append(N[1, 0]/N[0, 0])
    R3.append(N[2, 0]/N[1, 0])
    R4.append(N[3, 0]/N[2, 0])
    
   
print(N)

plt.plot(list(range(T+1)), size, 'g-')
plt.yscale('log')
plt.show()
plt.clear()

##plt.plot(list(range(T+1)), R2)
##plt.plot(list(range(T+1)), R3)
##plt.plot(list(range(T+1)), R4)
##plt.show()
