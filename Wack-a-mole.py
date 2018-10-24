import pygame
import random

#intializing
pygame.init()
width, height = 480, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()
xvalue, yvalue = 0, 0
xvalues = []
yvalues = []
moles = []

class mole():
    def __init__(self):
        self.rect = pygame.Rect(random.choice(xvalues), random.choice(yvalues), pygame.Surface.get_width(screen)/10, pygame.Surface.get_width(screen)/10)
        moles.append(self)

    def __call__(self):
        return

class hammer():
    def __init__(self):
        pygame.mouse.set_visible(False)
        self.rect = pygame.Rect(100,100, pygame.Surface.get_width(screen)/10, pygame.Surface.get_width(screen)/10)
        self.rect.center = pygame.mouse.get_pos()
        #pygame.draw.rect(screen, (0,0,255), self.rect)
    def __call__(self):
        return

def Field():
    global xvalue, yvalue
    for x in range(3):
        for y in range(3):
            xvalue = 0.25*(x+1)*pygame.Surface.get_width(screen) - (pygame.Surface.get_width(screen)/20)
            yvalue = 0.25*(y+1)*pygame.Surface.get_height(screen) - (pygame.Surface.get_height(screen)/20)
            xvalues.append(xvalue)
            yvalues.append(yvalue)
            rect = pygame.Rect(xvalue, yvalue, pygame.Surface.get_width(screen)/10, pygame.Surface.get_height(screen)/10)
            pygame.draw.rect(screen, (255,255,255), rect)

while True:
    clock = pygame.time.Clock()
    #setup:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    #create the field:
    Field()
    for i in range(10):
        i = mole()


    #moles
    for mole in moles:
        pygame.draw.rect(screen, (255,0,0), mole.rect)
        if mole.rect.colliderect(hammer().rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            moles.pop(moles.index(mole))

    pygame.draw.rect(screen, (0,0,255), hammer().rect)

    print(moles)
    xvalues = []
    yvalues = []
    pygame.display.flip()
    screen.fill(0)
