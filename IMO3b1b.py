import random
import turtle

d = 250

turtle.hideturtle(); turtle.speed(100000000); turtle.delay(0); turtle.tracer(0, 0);

pts = [(random.choice([-1, 1])*random.random()*d, random.choice([-1, 1])*random.random()*d) for i in range(50)]

#Draw square
turtle.up(); turtle.goto(d, d); turtle.down(); turtle.pensize(4)
for i in range(4):
    turtle.right(90)
    turtle.forward(2*d)
turtle.pensize(1)

for pt in pts:
    turtle.up()
    turtle.goto(pt)
    turtle.down()
    turtle.circle(2)
