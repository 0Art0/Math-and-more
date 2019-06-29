import random
import turtle
import math

def run(n):
    #l = []
    paths = [[j for j in range(n) if j != i] for i in range(n)]

    epath = [0]

    for k in range(int(n*(n-1)/2)):
        pt = epath[-1]
        #l.append(len(paths[pt]))

        if len(paths[pt]):
            nxt = random.choice(paths[pt])
            epath.append(nxt)
        else:
            break

        paths[pt].remove(nxt)
        paths[nxt].remove(pt)

    #print(sorted(l))
    return epath

#
def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
#

def draw(path, n, d = 100):
    turtle.up(); turtle.goto(d, 0); turtle.down()
    poldist = 0
    for pt in path:
        poldist += dist((turtle.xcor(), turtle.ycor()), (d*math.cos(pt*2*math.pi/n), d*math.sin(pt*2*math.pi/n)))
        turtle.goto(d*math.cos(pt*2*math.pi/n), d*math.sin(pt*2*math.pi/n))

    print(poldist)
    print(d*n/math.tan(math.pi/(2*n)))
    
def main(n):
    
    path = run(n)

    while len(path) <= n*(n-1)/2:
        path = run(n)

    print(path)
    
    turtle.reset()
    draw(path, n, 200)
        





