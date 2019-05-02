import turtle

turtle.hideturtle()
turtle.speed(100000000)
turtle.delay(0); turtle.tracer(0, 0);

N = int(input("Number of rows: "))
p = int(input("mod "))

rt3 = 3**0.5
a = 1850/(rt3*3*N) #the side length of the individual hexagons


#this function draws the hexagons
def drawhex(x, y, r):
    turtle.up(); turtle.goto(x, y+a);
    turtle.setheading(30); turtle.rt(60);
    turtle.down()

    #this decides the fill colour based on the remainder mod p
    turtle.fillcolor((r/p)%1, ((r+1)/p)%1, ((r+2)/p)%1)
    turtle.begin_fill()
    
    for i in range(6):
        turtle.rt(60)
        turtle.forward(a)
    turtle.end_fill()
    
    ##turtle.up(); turtle.goto(x-a/2, y); turtle.down()
    ##turtle.write(str(number), False, align="left", font=('Times New Roman', int(a/2), 'normal'))


pts = [(0, 300)] #the list of points where hexagons are to be drawn
see = []

for i in range(N):
    sea = [] #"memory" of the previous row
    s = [(pts[0][0]-rt3*a/2, pts[0][1]-3*a/2)] #related to pts

    for j, pt in enumerate(pts):
        C = 1 if (j == 0 or j == i) else (see[j-1] + see[j]) % p #the binomial coefficient
        #Alternative definition: C = C*(i-j)/(j+1)
        drawhex(pt[0], pt[1], C)

        sea.append(C)
        s.append((pt[0]+rt3*a/2, pt[1]-3*a/2))

    see = list(sea); pts = list(s)
