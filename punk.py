import pygame
from pygame.draw import *
import math 
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

skin_color = (255,223,196)

punk_pos1 = (400,300)


def draw_head(head_size, head_location, eye_color):
    
    circle(screen,skin_color, head_location,int(head_size))
    
    
    circle(screen,eye_color,(int(head_location[0] + head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/5))
    circle(screen,eye_color,(int(head_location[0] - head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/5))
    circle(screen,(150,75,0),(int(head_location[0] + head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/5),int(head_size/100))
    circle(screen,(150,75,0),(int(head_location[0] - head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/5),int(head_size/100))
    circle(screen,(0,0,0),(int(head_location[0] + head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/15))
    circle(screen,(0,0,0),(int(head_location[0] - head_size/3),
                             int(head_location[1] - head_size/10)),int(head_size/15))
    
    polygon(screen,(150,75,0),(
            ((int(head_location[0] + head_size/15), head_location[1])),
            ((int(head_location[0] - head_size/15), head_location[1])),
            ((head_location[0], int(head_location[1] + 1.73*head_size/15)))))

    polygon(screen,(255,0,0),(
            ((int(head_location[0] + head_size/3), int(head_location[1]+head_size/3))),
            ((int(head_location[0] - head_size/3), int(head_location[1]+head_size/3))),
            ((head_location[0], int(head_location[1] + head_size/2)))))
    
    

def hands(punk_pos):
    line(screen, skin_color,(int(punk_pos[0]),700),(int(punk_pos[0]) + 220,100),20)
    line(screen, skin_color,(int(punk_pos[0]),700),(int(punk_pos[0]) - 220,100),20)
    

def shoulder ( shoulder_pos, shoulder_size, alpha0, dress_color ):
    r = shoulder_size
    coordinates = []
    alpha = alpha0
    
    while alpha < 2*3.14 + alpha0:
        coordinates.append((( shoulder_pos[0]-r*math.cos( alpha ) ),( shoulder_pos[1] + r*math.sin( alpha ) )))
        alpha += 2*3.14/5
        
    polygon(screen, dress_color,( coordinates ))
    polygon(screen,(0,0,0),( coordinates ),1)
    
    
# def hair(hair_size, punk_pos, hair_color, head_size):
#    rh = hair_size
#    r = head_size
#    alpha0 = 0
#    
#    coordinates = []
#    beta = 0.5
#    alpha = alpha0

#    while beta < 2*(3.14-0.5):
        
#        while alpha < 2*3.14 + alpha0:
#            coordinates.append((int(punk_pos[0] - r*math.cos(beta)-rh*math.cos( alpha ))),int(punk_pos[1] - r*math.sin(beta) + rh*math.sin( alpha )))
#            alpha += 2*3.14/3 
#            polygon(screen, hair_color,( coordinates ))
#            coordinates = []
#            alpha0 += 3.14/10
            
 #       beta += 0.5 
        
def draw_punk(eye_color, dress_color, x_coordinate):
    punk_pos = (x_coordinate,300)             
    hands(punk_pos)    

    circle(screen, dress_color,(int(punk_pos[0]),500),150)
    polygon(screen,(0,0,0),((int(punk_pos[0]) - 250,500),
                            (int(punk_pos[0]) + 250,500),
                            (int(punk_pos[0]) + 250,1000),
                            (int(punk_pos[0]) - 250,1000)))
    
    
    
    shoulder((punk_pos[0] + 110,380), 40, -0.2, dress_color)
    shoulder((punk_pos[0] - 110,380), 40, -0.2, dress_color)
    draw_head(100,punk_pos, eye_color)
#    hair(10,punk_pos,(23,150,90),100)


draw_punk((0,0,255),(255,0,0),300)
draw_punk((0,0,255),(105,140,170),800)


    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

