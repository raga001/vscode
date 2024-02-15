from turtle import *
speed(0)
def polygon(side,size,color):
    fillcolor(color)
    begin_fill()
    for _ in range(side):
        fd(100)
        lt(360/side)
    end_fill()
    
for i in range(6):
    polygon(8,100,'red')
    polygon(6,50,'green')
    lt(60)

hideturtle()
mainloop()
    