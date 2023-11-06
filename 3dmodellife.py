from vpython import *
import random

w, h, z = 1500,750, 500
scene = canvas(width=w, height=h)

particles = []

class Particle:
    def __init__(self, x, y,z, color):
        # self.x,self.y,self.z=x,y,z
        # self.sphere = sphere(pos=vector(self.x,self.y,self.z), radius=7, color=color)
        # self.vel = vector(0, 0, 0)
        self.x, self.y, self.z = x, y, z
        self.sphere = sphere(pos=vector(self.x, self.y, self.z), radius=10, color=color)
        self.vel = vector(0,0,0)

def create(num, color):
    g = []
    for i in range(num):
        p = Particle(random.uniform(0,600), random.uniform(0,650),random.uniform(0,600), color)
        g.append(p)
        particles.append(p)
    return g

def rule(g1, g2, g):
    for i in range(len(g1)):
        fx, fy, fz = 0, 0, 0
        for j in range(len(g2)):
            a = g1[i]
            b = g2[j]
            dx = a.x - b.x
            dy = a.y - b.y
            dz = a.z - b.z
            d = sqrt(dx**2 + dy**2 + dz**2)

            if (d > 0 and d <300):
                F = g / d
                fx += F * dx
                fy += F * dy
                fz += F * dz
            a.vel.x = (a.vel.x + fx) * 0.5
            a.vel.y = (a.vel.y + fy) * 0.5
            a.vel.z = (a.vel.z + fz) * 0.5
            a.x += a.vel.x
            a.y += a.vel.y
            a.z += a.vel.z
            a.sphere.pos.x = a.x
            a.sphere.pos.y = a.y
            a.sphere.pos.z = a.z    

    if a.sphere.pos.x > 0:
       # a.sphere.pos.x =10
        a.vel.x = -a.vel.x
    elif a.sphere.pos.x < 600:
       # a.sphere.pos.x=580
        a.vel.x = -a.vel.x
    if a.sphere.pos.y > 0:
       # a.sphere.pos.y=10
        a.vel.y = -a.vel.y
    elif a.sphere.pos.y<600:
       # a.sphere.pos.y=580
        a.vel.y = -a.vel.y
    if a.sphere.pos.z > 0 :
       # a.sphere.pos.z=10
        a.vel.z = -a.vel.z
    elif a.sphere.pos.z<600 :
        #a.sphere.pos.z=580
        a.vel.z = -a.vel.z
      

def main():
    
    yellow=create(100,color.orange)
    red=create(100,color.red)
    green=create(200,color.purple)
   # white=create(50,color=color.white)

    while True:
        rate(30)
        rule(green,green, -0.32)
        rule(green,red, -0.17)
        rule(green,yellow, 0.34)
        rule(red,red, -0.1)
        rule(red,green,-0.34)
        rule(yellow,yellow,0.15)
        rule(yellow,green,-0.2)

        # rule(red,red,-0.2)
        # rule(red,yellow,-0.1)
        # rule(yellow,red,0.01)
        # rule(yellow,green,-0.1)
        # rule(yellow,yellow,-0.2)
        # rule(green,yellow,-0.4)
        # rule(green,red,0.5)
        # rule(white,red,-0.9)
        # rule(white,yellow,-0.9)
        # rule(white,green,-0.9)
        
        # rule(red,red,-0.2)
        # rule(red,yellow,-0.1)
        # rule(yellow,green,-0.1)
        # rule(yellow,red,-0.001)
        # rule(green,yellow,-0.3)
        # rule(green,red,0.5)
        # rule(white,red,-0.6)
        # rule(red,white,0.35)
        # rule(white,yellow,0.9)
        # rule(white,green,-0.2)
        # rule(green,white,0.9)
        # rule(white,white,-0.001)
        # rule(green,green,-0.3)

if __name__ == "__main__":
    main()
