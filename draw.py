import stdio
import stddraw
from plot import *

# Read x and y scales from standard input, and configure standard
# draw accordingly. Then read points from standard input until
# end-of-file, and plot them on standard draw.

stddraw.setCanvasSize(500*2.32,500)
x0,y0,x1,y1 = 0,0,0,0
def draw_map(f):
    stdio.setFile(f)
    global x0,y0,x1,y1
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
    a,b = 0.3,1.2
    return (b-a)*(x-min)/(max-min)+a

def draw_scale(mini,maxi):
    delta = (maxi-mini)/4
    for i in range(4):
        v = scale_value(delta*(i+1),mini,maxi)
        stddraw.circle(x0+4+4*i,y0+5,max(v,0))
        stddraw.text(x0+4+4*i,y0+3,str(delta*(i+1)))

def show_cases(day):
    data = map_data(day)
    mini = 1000000
    maxi = 1
    stddraw.setPenColor(stddraw.RED)
    for d in data:
        mini = min(mini,d[0])
        maxi = max(maxi,d[0])
    
    draw_scale(mini,maxi)
    for d in data:
        v = scale_value(d[0],mini,maxi)
        #stddraw.setPenRadius(max(v,0))
        stddraw.circle(d[2],d[1],max(v,0))


def show_map():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(16)
    stddraw.text(x0+10,y0+1.4,"Relative Covid Cases per State") 
    stddraw.show()

draw_map("usa_map.txt")
show_cases("01-22-2022")
show_map()