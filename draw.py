import stdio
import stddraw
from plot import *

# Read x and y scales from standard input, and configure standard
# draw accordingly. Then read points from standard input until
# end-of-file, and plot them on standard draw.

stddraw.setCanvasSize(800,800)

def draw_map(f):
    stdio.setFile(f)
    x0 = stdio.readFloat()
    y0 = stdio.readFloat()
    x1 = stdio.readFloat()
    y1 = stdio.readFloat()

    stddraw.setXscale(x0, x1)
    stddraw.setYscale(y0, y1)

    # Read and plot the points.
    stddraw.setPenRadius(0.0)
    while not stdio.isEmpty():
        n = stdio.readInt()
        previous = [0.0,0.0]
        for i in range(n):
            x = stdio.readFloat()
            y = stdio.readFloat()
            if i!=0:
                stddraw.line(previous[0],previous[1],x,y)
            previous = [x,y]

def scale_value(x,min,max):
    a,b = 0.005,0.045
    return (b-a)*(x-min)/(max-min)+a

def show_cases(day):
    data = map_data(day)
    mini = 1000000
    maxi = 1
    stddraw.setPenColor(stddraw.RED)
    for d in data:
        mini = min(mini,d[0])
        maxi = max(maxi,d[0])
    for d in data:
        v = scale_value(d[0],mini,maxi)
        stddraw.setPenRadius(max(v,0))
        stddraw.point(d[2],d[1])

def show_map():
    stddraw.show(1000.0)

draw_map("usa_map.txt")
show_cases("12")
show_map()