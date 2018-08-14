from turtle import *

shape("arrow")
speed(0)
#Triangle
for h in range(3):
    color("blue")
    forward(100)
    left(120)
#Pentagon
for k in range(5):
    color("blue")
    forward(100)
    left(72)
#Square
for j in range(4):
    color("red")
    forward(100)
    left(90)
#Hexagon
for i in range(6):
    color("red")
    forward(100)
    left(60)
hideturtle()

mainloop()