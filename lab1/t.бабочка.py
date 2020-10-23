import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(100)


def   f(r):
        a = 2 * 3.14 * r /360
        for i in range(0,360,5):
            tr.forward(a)
            tr.left(5)

        for i in range(0,360,5):
            tr.forward(a)
            tr.right(5)


tr.left(90)            
r = 100
for i in range(0,7,1):
    f(r)
    r = r + 50
    
            
