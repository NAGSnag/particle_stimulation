import ptext
import pygame
import math

pygame.init()

# window loop
width, height = 1500, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("planet stimulation")
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (188, 39, 50)
grey = (80, 78, 81)
brown=(64, 68, 54)
font = pygame.font.SysFont("comicsanc",20)

# class button():
#     def __init__(self,surface):
#         self.surface=surface
#     def drawButton(self,posx,posy,btnw,btnh,color,radius,shadow=0,scolor='grey'):
#         if shadow:
#             pygame.draw.rect(self.surface,scolor,(posx+shadow,posy+shadow,btnw,btnh),border_radius=radius)
#         self.btn=pygame.draw.rect(self.surface,scolor,(posx+shadow,posy+shadow,btnw,btnh),border_radius=radius)
#         return self.btn
#     def textButton(self,btntext,tcolor,font,size,shadow=(0,0),scolor='grey'):
#         ptext.draw(btntext,center=self.btn.center,color=tcolor,sysfontname=font,fontsize=size,shadow=shadow,scolor=scolor)

class planet:
    AU = 149.6e6 * 1000  # number-actual distence 1000 for convt to meters
    G = 6.67428e-11  # gravitational constant
    SCALE = 140 / AU  # stumulation game scale   1AU = 1000 pixel
    TIMESTEP = 3600 * 24   # for visualising 1day in stimuation per sec

    def __init__(self, x, y, radius, color, mass):
        self.days = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distence_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        self.days+=1

        x = self.x * self.SCALE + width / 2
        y = self.y * self.SCALE + height / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + width / 2
                y = y * self.SCALE + height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 1)

        pygame.draw.circle(win, self.color, (x , y), self.radius)


        if not self.sun:
            days = 0
            distence_text = font.render(f"{round(self.distence_to_sun / 1000)}km", 1, white)

            days_text = font.render(f"{self.days}days", 1, white)

            win.blit(distence_text, (x - distence_text.get_width() / 2, y - distence_text.get_height() / 2))
            win.blit(days_text, (x,y))




    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distence_x = other_x - self.x
        distence_y = other_y - self.y
        distence = math.sqrt(distence_x ** 2 + distence_y ** 2)#pythogrus--✓x2+y2

        if other.sun:
            self.distence_to_sun = distence

        force = self.G * self.mass * other.mass / distence ** 2
        theta = math.atan2(distence_y, distence_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        # velocity
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        # f=m/a
        # a=f/m
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

    # def up(self,planets):
    #     for d in planets:
    #         d.SCALE+=10


def main():
    run = True
    clock = pygame.time.Clock()  # to get speed of computer

    sun = planet(0, 0, 30, yellow, 1.9891 * 10 ** 30)
    sun.sun = True

    # sun2=planet(6.6 * planet.AU,0, 30, yellow, 0.9891 * 10 ** 30)
    # sun2.sun=True


    earth = planet(-1 * planet.AU, 0, 16, blue, 5.97219 * 10 **24)  # -1 for distence from left 1 for distence at right       5.97219 * 10 ** 24
    earth.y_vel = 29.783 * 1000

    mars = planet(-1.524 * planet.AU, 0, 12, red, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = planet(0.387 * planet.AU, 0, 8, grey, 3.285 * 10 ** 23)#23
    mercury.y_vel = -47.4 * 1000

    venus = planet(0.723 * planet.AU, 0, 14, white, 4.867 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    jupiter = planet(5.2 * planet.AU, 0, 20, brown, 1.898 * 10**27)
    jupiter.y_vel=-13.1*1000


    planets = [sun, earth, mars, mercury, venus, jupiter,]
    #mClick=False
    while run:
        clock.tick(60)  # to run stimulation in 60fps
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # mpos=pygame.mouse.get_pos()
            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     if pygame.mouse.get_pressed()[0]:
            #         mClick=True
            #     if pygame.mouse==pygame.mouse.get_pressed()[0]:
            #         mClick=False

        for p in planets:
            p.update_position(planets)
            p.draw(win)

        # scaleup=button(win)
        # btnup=scaleup.drawButton(1200,750,70,30,blue,20,5)
        # scaleup.textButton('scale+','white','Arial',30)
        #
        # scaledown=button(win)
        # btndown=scaledown.drawButton(1300,750,70,30,blue,20,5)
        # scaledown.textButton('scale-' ,'white','Arial',30)
        #
        # if mClick and btnup.collidepoint(mpos):
        #     for v in planets:
        #         v.up(planets)

        pygame.display.update()
    pygame.quit()


main()
