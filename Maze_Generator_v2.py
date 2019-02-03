import pygame as pg
import random
from pygame import gfxdraw

WIDTH,HEIGHT=1200,800

pg.init()
screen=pg.display.set_mode((WIDTH,HEIGHT))

clock=pg.time.Clock()
running=True

def controlls():
    running=True

    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

        if event.type==pg.KEYDOWN:
           if event.key==pg.K_ESCAPE:
               running=False

    return running

arr=[]

x,y=50,50
xoffset,yoffset=WIDTH/200,HEIGHT/200#increase ofset for smooth edges

for i in range(y):
    for i2 in range(x):
        arr.append((random.randint(WIDTH/x*(i2)+xoffset,WIDTH/x*(i2+1)-xoffset),random.randint(HEIGHT/y*(i)+yoffset,HEIGHT/y*(i+1)-yoffset)))


grid=pg.Surface((WIDTH,HEIGHT))
size=x*y

color=(0,50,50)



for i in range(size):
    if i%x is not x-1:
        pg.draw.line(grid,color,arr[i],arr[i+1])
    if i<size-x:
        pg.draw.line(grid,color,arr[i],arr[i+x])
#        if i%x!=0:
#            pg.draw.line(grid,color,arr[i],arr[i+x-1])
            

grid.set_colorkey((0,0,0))
#grid.convert()


path=pg.Surface((WIDTH,HEIGHT))
color=(200,200,0)

possible_ways=[]

for i in range(1,y):
    for i2 in range(1,x):
        possible_ways.append((i2*WIDTH/x,i*HEIGHT/y))

path.set_colorkey((0,0,0))
#path.convert()


px,py=x-1,y-1
size=px*py



used=[]
a=0
furthest=a

for i in range(int(size*1.2)):
    
    b=random.randint(0,3)

    loop=True
    used.append(a)

    while  loop:
        if  (a+px in used or a>size-px-1) and (a-px in used or a-px<0) and (a+1 in used or a%px+1>px-1) and (a-1 in used or a%px-1<0):
                a=used[random.randint(0,len(used)-1)]
                loop=True
                

        if b==0 and a+px in used:
                b=random.randint(1,3)
                loop=True
        elif b==1 and a-px in used:
                while b==1:
                    b=random.randint(0,3)
                loop=True
        elif b==2 and a+1 in used:
                while b==2:
                    b=random.randint(0,3)
                loop=True
        elif b==3 and a-1 in used:
                b=random.randint(0,2)
                loop=True

        else:
             loop=False


    if a<size-px and b==0:#down
       pg.draw.line(path,color,possible_ways[a],possible_ways[a+px])
       pg.draw.line(grid,(10,10,10),arr[a+x+a//px],arr[a+x+1+a//px])
       a+=px

    elif a>px and b==1:#up
       pg.draw.line(path,color,possible_ways[a],possible_ways[a-px])
       pg.draw.line(grid,(10,10,10),arr[a+a//px],arr[a+a//px+1])
       a-=px

    elif a%px is not px-1 and b==2:#right        
       pg.draw.line(path,color,possible_ways[a],possible_ways[a+1])
       pg.draw.line(grid,(10,10,10),arr[a+1+a//px],arr[a+x+1+a//px])
       a+=1

    elif a%px is not 0 and b==3:#left
       pg.draw.line(path,color,possible_ways[a],possible_ways[a-1])
       pg.draw.line(grid,(10,10,10),arr[a+a//px],arr[a+x+a//px])
       a-=1


    if a>furthest:
        furthest=a


pg.draw.circle(grid,(0,200,0),(int((used[0]%px+1)*WIDTH/x),int((used[0]//px+1)*HEIGHT/y)),3)
#pg.draw.circle(grid,(200,0,0),(int((used[len(used)-1]+1)%px*WIDTH/x),int((used[len(used)-1]//px+1)*HEIGHT/y)),3)
pg.draw.circle(grid,(200,0,0),(int((furthest%px+1)*WIDTH/x),int((furthest//px+1)*HEIGHT/y)),3)

grid.convert()
path.convert()


while running:
    running=controlls()
    screen.fill((10,10,10))

    screen.blit(grid,(0,0))

    key=pg.key.get_pressed()

    if key[pg.K_SPACE]:
        screen.blit(path,(0,0))    

    pg.display.flip()



