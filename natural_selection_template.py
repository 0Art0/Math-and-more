from random import random as r
from math import pi, e
import time

v, B = r(), [r()]

def gaussian(x=r()):
    return e**(-2*pi*x**2)

def select(v, b):
    return 0 if gaussian(v - b) > r() else 1 #try 1 - gaussian(v-b) < r()

def variation(x=r()):
    return x if gaussian(x) > r() else variation(x)

def correct(var):
    return var if 0<=var<=1 else (-var if var < 0 else 2-var if var > 1)

print(v), print(B);
for i in range(5):
    for b in B:
        B.remove(b)
        if select(v, b):
                B.extend([correct(b+variation()), correct(b+variation())])
        print(B)
    time.sleep(1)
