
import pygame as pg
import numpy as np
from random import randint

SCREEN_SIZE = (800, 600)
target_number = 3


BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()


class Ball():
    def __init__(self, coord, vel, rad=15, color=None):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self, t_step=1., g=2.):
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
               self.is_alive = False

    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad

                self.flip_vel(n[i], 0.8, 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i], 0.8, 0.9)

    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()

class Table():
    pass

class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], 
                 min_pow=20, max_pow=50):
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False
        self.shots = 0

    def draw(self, screen):
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 5)

    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
        
    def move(self):
        if self.active and self.power < self.max_pow:
            self.power += 1

    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])


class Target():
    
    def __init__(self):
        self.r = randint(50, 100)
        self.x = randint(400, 800 - self.r)
        self.y = randint(self.r, 600 - self.r)
        self.vx = 0 #randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = (randint(30, 255), randint(30, 255), randint(30, 255)  ) 
        self.is_alive = True
        
        
    def draw(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
       
    def border_hit(self):
        
        #if self.x < self.r or self.x > width - self.r :
         #   self.vx = - self.vx 
            
        if self.y < self.r or self.y > 600 - self.r:
            self.vy = -self.vy                    
    
            
    def move(self):
        #self.x += self.vx
        self.y += self.vy
        self.border_hit()
    

        
targets = [ Target() for i in range(target_number)   ]


class Manager():
    def __init__(self):
        self.gun = Gun()
        self.table = Table()
        self.balls = []
        self.score = 0
        
        
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.draw(screen)
        self.check_alive()
        self.check_alive_target()
        self.hit()
        
        
        return done

    def draw(self, screen):
        screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(screen)
        for target in targets:
            target.draw()    
        self.gun.draw(screen)

    def move(self):
        for ball in self.balls:
            ball.move()
        for target in targets:
            target.move()
        self.gun.move()
            
    def check_alive_target(self):
        dead_targets = []
       
        for i, target in enumerate(targets):
            if not target.is_alive:
                dead_targets.append(i)
        
        for i in reversed(dead_targets):
            targets.pop(i)

    def hit(self):
        for ball in self.balls:
                for target in targets:
                    if (ball.coord[0] - target.x)**2 + (ball.coord[1] - target.y)**2 < (ball.rad + target.r)**2:
                        target.is_alive = False
                        ball.is_alive = False
                        self.score += 1

                        
    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.is_alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)

            
    
        
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 5
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 5
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)

        return done
   

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Khiryanov")
clock = pg.time.Clock()


    

mgr = Manager()

done = False

while not done:
    clock.tick(15)
    
    done = mgr.process(pg.event.get(), screen)
    
    
                    
    pg.display.flip()

