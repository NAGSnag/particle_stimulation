import pygame
import math
import random


w,h=1400,780
win=pygame.display.set_mode((w,h))
fps=120

particles=[]
class particle:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.xv=0
        self.yv=0
        self.color=color
    def draw(self):
        # self.x+=self.xv
        # self.y+=self.yv
        if self.x<0 or self.x>1400:self.xv*=-1
        if self.y<0 or self.y>800:self.yv*=-1
        pygame.draw.rect(win,self.color,pygame.Rect(self.x,self.y,7,7),border_radius=2)

def create(num,color):
    g=[]
    for i in range(num):
        p=particle(random.randint(0,1400),random.randint(0,800),color)
        g.append(p)
        particles.append(p)
    return g

def rule(g1, g2, g):
    for i in range(len(g1)):
        fx,fy=0,0
        for j in range(len(g2)):
            a=g1[i]
            b=g2[j]
            dx=a.x-b.x
            dy=a.y-b.y
            d = (dx * dx + dy * dy) ** 0.5
            if(d > 0 and d < 80):
                F = g / d
                fx += F * dx
                fy += F * dy
        a.xv=(a.xv+fx)*0.5
        a.yv=(a.yv+fy)*0.5
        a.x+=a.xv
        a.y+=a.yv

def main():
    run=True
    clock=pygame.time.Clock()
    yellow = create(150, "orange")
    red=create(150,'red')
    green=create(150,'purple')
    white=create(60,'white')
 



    while run:
        win.fill((0, 0, 0))
        clock.tick(fps)
        pygame.display.set_caption(f"life_simulation{round(clock.get_fps())}")
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            key=pygame.key.get_pressed()
            if key==pygame.K_ESCAPE:
                run=False
        # rule(red,red,-0.2)
        # rule(red,yellow,-0.1)
        # rule(yellow,red,0.01)
        # rule(yellow,green,-0.1)
        # rule(yellow,yellow,-0.2)
        # rule(green,yellow,-0.4)
        # rule(green,red,0.5)
        # rule(white,red,-0.3)
        # rule(red,white,0.35)
        # rule(white,yellow,0.3)
        # rule(white,green,-0.2)
        # rule(white,white,0.1)
        # rule(green,white,0.9)
        # rule(green,green,-0.3)\
        rule(red,red,-0.2)
        rule(red,yellow,-0.1)
        rule(yellow,green,-0.1)
        rule(yellow,red,-0.001)
        rule(green,yellow,-0.3)
        rule(green,red,-0.5)
        rule(white,red,-0.6)
        rule(red,white,0.35)
        rule(white,yellow,0.9)
        rule(white,green,-0.2)
        rule(green,white,0.9)
        rule(white,white,-0.001)
        rule(green,green,-0.3)

        # rule(green,green, -0.32)
        # rule(green,red, -0.17)
        # rule(green,yellow, 0.34)
        # rule(red,red, -0.1)
        # rule(red,green,-0.34)
        # rule(yellow,yellow,0.15)
        # rule(yellow,green,-0.2)

        #######################################################
        for i in range(len(particles)):particles[i].draw()
        pygame.display.update()
    pygame.quit()


if __name__=="__main__":
    main()