import turtle as tr
import numpy as np

tr.shape('turtle')



ay = - 10
Vx = 20
Vy = 20
dt = 1
x = y = 0


n = 0

while n<1:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    tr.goto(x,y)
    
    if y == 0:
        Vy = -Vy
    else:
        Vy = Vy
  
