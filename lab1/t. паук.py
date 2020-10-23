import turtle


    
turtle.shape('turtle')
turtle.pendown()
n = 12
i = 1
while i <= n:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(360/n)
    i = i + 1
    

turtle.hideturtle()
