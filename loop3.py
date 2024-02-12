from turtle import *
speed('slow')
pencolor('yellow')
bgcolor('black')

for i in range(5):
    fd(100)
    for i in range(5):
        fd(75)
        lt(360/65)
    lt(360/5)
    dot(10)
hideturtle()
mainloop()
