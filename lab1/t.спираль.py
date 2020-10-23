
import turtle

turtle.shape('turtle')
turtle.speed(8000)
k = 0.001
dphi = 1
for phi in range(0,10800,1):
    turtle.forward(dphi*k*( 1 + phi*phi )**0.5)   
    turtle.left(dphi)
