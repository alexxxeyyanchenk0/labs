import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(300)   

def star(n):
    if n % 2 == 1:
        for i in range(0,n,1):
            tr.forward(100)
            tr.left(180-180/n)
    
star(5)
tr.penup()
tr.goto(200,0)
tr.pendown()
star(11)
