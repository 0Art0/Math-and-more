import turtle
turtle.hideturtle(); turtle.speed(100000000); turtle.delay(0); turtle.tracer(0, 0);

c = 1

def grid(n=10):
    return [[(c*t, x) for t in range(-n, n+1)] for x in range(-n, n+1)]

def plot(grid, color='black', scale=25):
    turtle.color(color); turtle.fillcolor(color)
    for i in range(len(grid)):
        for pt in grid[i]:
            turtle.up(); turtle.goto(pt[1]*scale, pt[0]*scale); turtle.down(); turtle.circle(scale/10);
            
        turtle.up(); turtle.goto(grid[i][0][1]*scale, grid[i][0][0]*scale); turtle.down(); turtle.goto(grid[i][-1][1]*scale, grid[i][-1][0]*scale);
        turtle.up(); turtle.goto(grid[0][i][1]*scale, grid[0][i][0]*scale); turtle.down(); turtle.goto(grid[-1][i][1]*scale, grid[-1][i][0]*scale);
        
def transform(grid, v):
    gamma = 1/(1-(v/c)**2)**0.5
    return [[(gamma*(pt[0] - v/(c*c)*pt[1]), gamma*(pt[1] - v*pt[0])) for pt in row] for row in grid]

def v(v, l = 11):
    return [[(t, t*(v)) for t in range(l)]]

axes = [[(-1000, 0), (1000, 0)], [(0, 1000), (0, -1000)]]; light = v(c); bg = grid()
plot(axes, 'black'); plot(bg, 'green')
