import math
import pygame
black =(0,0,0)

class Pendulum:
    def __init__(self, pivot_x=0, pivot_y=0, m=1, l=200, a=math.pi/2, g=1, color="red"):
        self.pivot =(pivot_x, pivot_y)
        self.m = m
        self.l = l
        self.a = a
        self.g = g
        self.clr =color

        self.x = 200
        self.y = 40
        self.av =0
        self.trajectory=[]

    def step(self):
        acc=(-self.g/self.l)*math.sin(self.a)
        self.av += acc
        self.av *=0.99

        self.a += self.av
        self.x = self.pivot[0]+self.l*math.sin(self.a)
        self.y=self.pivot[1]+self.l* math.cos(self.a)
        
    def draw(self, surface):
        pygame.draw.line(surface, black, self.pivot,(self.x, self.y))
        pygame.draw.circle(surface, self.clr, (self.x, self.y), 15)



def init_surface(size, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    surface = pygame.display.set_mode(size)
    clock= pygame.time.Clock()
    return surface, clock


def run():
    width, height = 1440, 950
    fps = 60
    surface, clock = init_surface((width, height), 'Pendulum Test')
    bg = pygame.image.load("images/background.png")

    pendulum = Pendulum(width//2, height//2)

    stop =False
    while not stop:
        clock.tick(fps)
        surface.blit(bg, (0, 0))
        for event in pygame.event.get():
            stop = event.type == pygame.QUIT
        pendulum.step()
        pendulum.draw(surface)
        pygame.display.flip()
    pygame.quit()

run()