import turtle as tr

tr.shape('turtle')
tr.width(5)

opened = open(r"index.txt", "r")
text = opened.read(7)



index1 = str(text)

index = []
for p in range(0,len(index1), 1) :
    index.append(index1[p])

print(index)




a = 50


b = a*2**(0.5)
  
digit = [
     [ [a,90] , [2*a,90] , [a,90] , [2*a,90] ] ,         
     [ [0,90] , [2*a,135] , [b,135] ] ,                  
     [ [a,180] , [a,-135] , [b,45] , [a,90] , [a , 180] ] ,
     [ [a/10000,45] , [b,135] , [a,-135] , [b,135] , [a, 180] ] ,
     [ [0,90] , [2*a,180] , [a,-90] , [a,-90], [a,-90] ]  ,
     [ [a,90] , [a,90] , [a,-90] , [a,-90] , [a,0] ] ,
     [ [a,90] , [a,90] , [a,-90] , [a,180], [2*a,180], [2*a,-90] , [a,0] ] ,
     [ [a/10000,90] , [a,-45] , [b,135] , [a,180] ] ,
     [ [a,90] , [2*a,90] , [a,90] , [2*a,180] , [a,-90] , [a,0] ] ,
     [ [a,90] , [2*a,90] , [a,90] , [a,90] , [a,0] ]

]

for j in range(0,len(index),1):
    n = int(index[j])

    for i in range(len(digit[n])):
        if digit[n][0][0] == 0:
                tr.penup()
                tr.forward(a)
                tr.pendown()
                tr.left(digit[n][0][1])
                digit[n][0][0] = 1
        else  :  
                tr.forward(digit[n][i][0])
                tr.left(digit[n][i][1])
                
    digit[1][0][0] = 0
    digit[4][0][0] = 0
    tr.penup()        
    tr.goto((j + 1)*(a + a/2),0)
    tr.pendown()
    
   
    
tr.hideturtle()
