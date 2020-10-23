import turtle as tr
import math
tr.shape('turtle')
tr.speed(10)
A = 30
N = 3
def mnogo(x):
    for i in range(x):
        tr.forward(A)
        tr.left(360 / x)
while N <= 13:
    R = A / (2 * math.sin(math.pi/N))
    tr.left(90 + 180/N)
    mnogo(N)
    tr.right(90 + 180/N)
    tr.penup()
    tr.forward(10)
    tr.pendown()
    A = 2 * (R + 10) * math.sin(math.pi/(N+1))
    N += 1
    
