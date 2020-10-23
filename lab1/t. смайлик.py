
import turtle as tr
import numpy as np

tr.speed(500)
tr.shape()

def ring(r):
    tr.penup()
    tr.forward(r)
    tr.pendown()
    tr.left(90)
    for i in range(0,360,5):
        tr.forward(2*3.14*r/72)
        tr.left(5)
    tr.right(90)
    tr.penup()
    tr.backward(r)
    tr.pendown()


def hring(r):
    tr.penup()
    tr.forward(r)
    tr.pendown()
    tr.left(90)
    for i in range(0,180,5):
        tr.forward(2*3.14*r/72)
        tr.left(5)
    tr.right(90)
    tr.penup()
    tr.backward(r)
    tr.pendown()
        


tr.color('yellow')
tr.begin_fill()
ring(200)
tr.end_fill()
tr.left(90)
tr.penup()

tr.forward(100)
tr.left(90)
tr.forward(70)
tr.left(180)
tr.color('blue')
tr.pendown()
tr.begin_fill()
ring(40)
tr.end_fill()
tr.penup()

tr.forward(140)
tr.color('blue')
tr.pendown()
tr.begin_fill()
ring(40
     )
tr.end_fill()

tr.penup()
tr.goto(0,0)
tr.color('black')
tr.pendown()
tr.left(90)
tr.width(20)
tr.forward(50)
tr.backward(50)
tr.left(90)
tr.color('red')
hring(80)

tr.penup()
tr.goto(0,0)
tr.pendown()

tr.color('black')
tr.width(5)

ring(200)
tr.left(90)
tr.penup()

tr.forward(100)
tr.left(90)
tr.forward(70)
tr.left(180)

tr.pendown()

ring(40)

tr.penup()

tr.forward(140)
tr.pendown()
ring(40)
tr.hideturtle()

        
         

         
         

