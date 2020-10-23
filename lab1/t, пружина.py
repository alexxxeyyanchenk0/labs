import turtle as tr

def hring(r):
    for i in range(0,180,5):
        tr.forward(2*3.14*r/72)
        tr.left(5)

tr.left(90)    
for j in range(0,20,1):
    hring(20)
    hring(50)
