from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

shape("arrow")
speed(0)
angle = 0
times = 3
for c in colors:
    angle = angle + 180
    color(c)
    for i in range(times):
        forward(100)
        left(180 - (angle / times))
    times = times + 1
hideturtle()




mainloop()