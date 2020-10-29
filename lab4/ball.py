import pygame
import math
from pygame.draw import *
from random import randint


with open('best_score.txt', 'r') as bs:
    best_score = bs.readlines()
    best_score = str(best_score)
    best_score = best_score[2:len(best_score)-2]
    best_score = int(best_score)
    bs.close()
    
with open('best_player.txt', 'r') as bp:
    best_player = bp.readlines()
    best_player = str(best_player)
    best_player = best_player[2:len(best_player)-2]    
    bp.close()
    
print(best_score)
print(best_player)

player = input()                      
pygame.init()

time = 100
size = 10
number_of_balls =  100
number_of_flowers = 100

frames = 0
score = 0
FPS = 60
black = (0,0,0)
width = 160*size
length = 90* size
total_time = 0

screen = pygame.display.set_mode((width, length))

def text() :
    f1 = pygame.font.Font(None, 15*size )
    text1 = f1.render('victory', 1, (180, 0, 0))
    screen.blit(text1, (int(width/2 - 25*size), int(length/2 - 15*size)))
        
    f2 = pygame.font.Font(None, 15*size )
    text2 = f2.render('Your score is:' , 1, (0, 0, 180))
    screen.blit(text2, (int(width/2 - 45*size), int(length/2 )))
    
    f3 = pygame.font.Font(None, 15*size )
    text3 = f3.render( str(score) , 1, (0, 180, 0))
    screen.blit(text3, (int(width/2 + 27*size) , int(length/2)))

    f4 = pygame.font.Font(None, 10*size )
    text4 = f4.render( 'your time is:'  , 1, (180, 180, 180))
    screen.blit(text4, (int(width/2 - 45*size ) , int(length/2 + 15*size)))

    f5 = pygame.font.Font(None, 10*size )
    text5 = f5.render( str(total_time) , 1, (180, 180, 180))
    screen.blit(text5, (int(width/2 - 2*size) , int(length/2 + 15*size)))
    
    f6 = pygame.font.Font(None, 10*size )
    text6 = f6.render( 'best score is: ' + best_player + '(' + str(best_score) + ')', 1, (200, 0, 170))
    screen.blit(text6, (int(width/2 - 45*size) , int(length/2 + 23*size)))

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
            self.vx = - self.vx 
            
        if self.y < self.r or self.y > length - self.r:
            self.vy = -self.vy                    
    
            
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
        
    def special_move(self):
        self.vx = - self.vx
        self.vy = - self.vy

balls = [ Ball(width, length) for i in range(number_of_balls)   ]
flowers = [ Flower(width, length) for i in range(number_of_flowers)   ]

pygame.display.update()
clock = pygame.time.Clock()
finished = False


 
while not finished:
    clock.tick(FPS)
             
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
                    
    for b in balls:    
        b.draw()
        b.move()

    for f in flowers:
        f.draw()
        f.move()
        if randint(0, 50) == 5:
            f.special_move()

    
    for j, b in enumerate(balls):    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ((b.x - event.pos[0])**2 + (b.y - event.pos[1])**2) < b.r**2:
            balls.pop(j)
            score += 1

    for j, f in enumerate(flowers):    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and( (f.x +f.r - event.pos[0])**2 + (f.y - event.pos[1])**2 < f.r**2 or (f.x -f.r - event.pos[0])**2 + (f.y - event.pos[1])**2 < f.r**2 or (f.x - event.pos[0])**2 + (f.y + f.r - event.pos[1])**2 < f.r**2 or (f.x - event.pos[0])**2 + (f.y - f.r- event.pos[1])**2 < f.r**2 ):
            flowers.pop(j)
            score += 2
   
    
    pygame.display.update()
    screen.fill(black)


    if frames < time*FPS and not(not balls and not flowers):
        frames += 1
    if  frames >= time*FPS or (not balls and not flowers) :  
        balls = []
        flowers = []
        total_time = round(frames/FPS, 2)
        if score >= best_score:
            best_score = score
            best_player = player

            with open('best_player.txt', 'w') as bp:
                bp.write(best_player)
                bp.close()
            with open('best_score.txt', 'w') as bs:
                bs.write(str(best_score))
                bs.close()
        text()
       
        
    
if finished  == True:
    print(score)
        

pygame.quit()            
        
        
