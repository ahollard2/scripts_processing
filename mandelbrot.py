from math import sqrt, degrees,atan2, sin, cos,radians


xmin=-2
xmax=2


ymin = -2
ymax = 2


rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl= width / rangex
    yscl= -height / rangey
    
def draw():
    translate(width/2,height/2)
    for x in arange(xmin,xmax,.01):
        for y in arange(ymin,ymax,.01):
            z=[x,y]
            col=mandelbrot(z,100)
            if col == 100:
                fill(0)
            else:
                fill(255-15*col,255,255)
            rect(x*xscl,y*yscl,1,1)

    

def mandelbrot(z,num):
    count=0
    z1=z
    while count <= num:
        
        if magnitude(z1) > 2.0:
        
            return count
       
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    
    return num

def arange(start,stop,step):
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output


def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
 

def theta(z):
    
    return degrees(atan2(z[1],z[0]))

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
