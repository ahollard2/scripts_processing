from random import choice, randint
sheepList=[]
grassList=[]
wolfList=[]
patchSize = 10
WHITE  = color(255)
BROWN  = color(102, 51,0)
RED    = color(255,0,0)
GREEN  = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
color = [WHITE ,RED ,YELLOW, PURPLE]
class Wolf():
    def __init__(self,x,y,sz):
        self.x=x
        self.y=y
        self.sz=sz
        self.energy=10000
        
    def update(self):
        move = 10
        self.energy-=1
        if self.energy<=0:
            wolfList.remove(self)
        self.x+= random(-move,+move)
        self.y+= random(-move,+move)
        if self.x > width:
            self.x -= width
        if self.y > height:
            self.y -= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
            
        fill(0)
        ellipse(self.x,self.y,self.sz,self.sz)
        
class Sheep():
    def __init__(self,x,y,col):
        self.x=x
        self.y=y
        self.sz=10
        self.energy = 20
        self.col=col
        self.age=200
    
    def update(self):
        #self.sz=self.energy//2
        
        self.age-=1
        if self.age==0:
            sheepList.remove(self)
            
        move = 10
        
        #if self.col==PURPLE:
         #   move=15
            
        self.energy-=1
        
        if self.energy<=0 and self in sheepList:
            sheepList.remove(self)
        self.x+= random(-move,+move)
        self.y+= random(-move,+move)
        
        if self.x > width:
            self.x -= width
        if self.y > height:
            self.y -= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        
        grass=grassList[int(self.x//patchSize * rows_of_grass + self.y//patchSize)]   
        if not grass.eaten:
            #if self.col==RED:
             #   self.energy+=grass.energy//2
            self.energy+=grass.energy
            grass.eaten = True
        
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz) 
        
        if self.energy>=50:
            self.energy-=30
            #if self.col==YELLOW:
               # for i in range(randint(0,4)):
               #     sheepList.append(Sheep(self.x,self.y,self.col))
            
            sheepList.append(Sheep(self.x,self.y,self.col))

class Grass():
    def __init__(self,x,y,sz):
        self.x=x
        self.y=y
        self.energy=5
        self.eaten=False
        self.sz=sz
    
    def update(self):
        if self.eaten:
            if random(100)<0.5:
                self.eaten=False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)
        
        
            
    
def setup():
    global patchSize, rows_of_grass
    rows_of_grass=height//patchSize
    size(600,600)
    noStroke()
    for i in range(20):
        sheepList.append(Sheep(random(width),random(height),choice(color)))
    for x in range(0, width, patchSize):
        for y in range(0, height, patchSize):
            grassList.append(Grass(x,y,patchSize))
    for i in range(2):
        wolfList.append(Wolf(600,600,20))
            
            
     
def draw():
    background(255)
    for grass in grassList:
        grass.update()
    for sheep in sheepList:
        sheep.update()
    for wolf in wolfList:
        wolf.update()
