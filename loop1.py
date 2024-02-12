from turtle import *
speed('fast')
pencolor('red')
pensize(5)

for i in range(8):
    fd(100)
    rt(45)
    write(f'n={i}', font=("bold",16,))

hideturtle()
mainloop()