from turtle import *
speed('fastest')
s= 0
while s < 250:
    fd(50 + s)
    lt(60)
    dot(10)
    write(s)
    s += 5
hideturtle()
mainloop()
