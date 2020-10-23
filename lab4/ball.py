import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

score = 0
width = 1920
length = 1080
black = (0,0,0)
number_of_balls =  20
number_of_flowers = 10

frames = 0

FPS = 60
screen = pygame.display.set_mode((width, length))

class Ball:
    

    
    def __init__(self, width, length):
        self.r = randint(50, 100)
        self.x = randint(self.r, width - self.r)
        self.y = randint(self.r, length - self.r)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = (randint(30, 255), randint(30, 255), randint(30, 255)  ) 
        self.random_factor = 1
        
        
    def draw(self):   
        circle(screen, self.color, (self.x, self.y), self.r)
        
       
    def border_hit(self):
        
        if self.x < self.r or self.x > width - self.r :
            self.vx = - self.vx * self.random_factor
            
        if self.y < self.r or self.y > length - self.r:
            self.vy = -self.vy * self.random_factor
            
            
    def collide(self, other):
        if ((self.x - other.x)**2 + (self.y - other.y)**2) < (self.r + other.r):
            self.vx = - self.vx
            self.vy = - self.vy
            other.vx = - other.vx
            other.vy = - other.vy
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.random_factor = int(randint(100, 150)/100)
        self.border_hit()


    def delete(self):
        self.r = 0

class Flower:
    

    
    def __init__(self, width, length):
        self.r = randint(20, 100)
        self.x = randint(self.r, width - self.r)
        self.y = randint(self.r, length - self.r)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = (randint(30, 255), randint(30, 255), randint(30, 255)  ) 
        self.random_factor = 1
        self.r  = int(self.r/2)
        
        
    def draw(self):   
        circle(screen, self.color, (self.x + self.r, self.y), self.r)
        circle(screen, self.color, (self.x - self.r, self.y), self.r)
        circle(screen, self.color, (self.x, self.y + self.r), self.r)
        circle(screen, self.color, (self.x, self.y - self.r), self.r)
        circle(screen, (255-self.color[0], 255 - self.color[1], 255 - self.color[2]), (self.x, self.y ), self.r)
        
       
    def border_hit(self):
        
        if self.x < 2*self.r or self.x > width - 2*self.r :
            self.vx = - self.vx
            
        if self.y < 2*self.r or self.y > length - 2*self.r:
            self.vy = -self.vy  
            
            
    
   
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        self.border_hit()


      
        

balls = [ Ball(width, length) for i in range(number_of_balls)   ]
flowers = [ Flower(width, length) for i in range(number_of_flowers)   ]

pygame.display.update()
clock = pygame.time.Clock()
finished = False


 
while not finished:
    clock.tick(FPS)
    
    frames += 1
    for i in range(number_of_balls):        
        for j in range(i+1, number_of_balls):
            balls[i].collide(balls[j])        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            
        for i in range(number_of_balls):        
            for j in range(i+1, number_of_balls):
                balls[i].collide(balls[j])
            
    for b in balls:    
        b.draw()
        b.move()

    for f in flowers:
        f.draw()
        f.move()

    #for i in range(3,number_of_flowers):
      #  j =     
       #
       #
      # flowers[j].r = 0
        
            

     
    
    
    
    for b in balls:    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ((b.x - event.pos[0])**2 + (b.y - event.pos[1])**2) < b.r**2:
            balls.pop()
            score += 1
        
    
            
        
   
    
    pygame.display.update()
    screen.fill(black)
    
if finished  == True:
    print(score)
        

pygame.quit()            
        
        
