from random import random as r
from math import pi, e
import time
import turtle

v, B = r(), [r()]
turtle.speed(10000); turtle.delay(0);

def gaussian(x=r()):
    return e**(-2*pi*x**2)

def select(v, b):
    return 0 if gaussian(v - b) > r() else 1 #try 1 - gaussian(v-b) < r()
    #return 0 if abs(v-b) < 0.1 else 1

def variation():
    x = r()
    return x**2 if gaussian(x) > r() else variation()

def correct(var):
    return var if 0<=var<=1 else (-var if var < 0 else 2-var); print(var)

print(v), print(B);

def duplicate(B):
    A = []
    for b in B:
        if select(v, b):
            A.extend([correct(b+variation()), correct(b+variation())])
    return A

for i in range(10):
    for b in B:
        turtle.up(); turtle.goto(b*100, 0); turtle.down(); turtle.circle(3)
    B = duplicate(B)
    print(B)
    time.sleep(1)
    turtle.clear()
