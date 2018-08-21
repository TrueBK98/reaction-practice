from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")
speed(0)

for c in colors:
    color(c)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
hideturtle()


mainloop()