from turtle import *

turtle_list = []

for i in range(5):
    t = Turtle()
    turtle_list.append(t)

hideturtle()

n = len(turtle_list)
print("I have", n, "turtles")

turtle_position = int(input("Turtle position? "))
turtle_color = input("Turtle color? ")
turtle_shape = input("Turtle shape? ")
turtle_list[turtle_position - 1].color(turtle_color)
turtle_list[turtle_position - 1].shape(turtle_shape)

command = input("What is your command (fd, bd, lt, rt) ")
command.lower()
command_list = command.split(" ")


for c in command_list:
    if "fd" in c:
        if len(c) > 2:
            c_split = c.split("_")
            turtle_list[turtle_position - 1].forward(int(c_split[1]))
        else:
            step_forward = float(input("How many pixel: "))
            turtle_list[turtle_position - 1].forward(step_forward)
    elif "bd" in c:
        if len(c) > 2:
            c_split = c.split("_")
            turtle_list[turtle_position - 1].backward(int(c_split[1]))
        else:
            step_backward = float(input("How many pixel: "))
            turtle_list[turtle_position - 1].backward(step_backward)
    elif "lt" in c:
        if len(c) > 2:
            c_split = c.split("_")
            turtle_list[turtle_position - 1].left(int(c_split[1]))
        else:
            left_angle = float(input("Angle to turn: "))
            turtle_list[turtle_position - 1].left(left_angle)
    elif "rt" in c:
        if len(c) > 2:
            c_split = c.split("_")
            turtle_list[turtle_position - 1].right(int(c_split[1]))
        else:
            right_angle = float(input("Angle to turn: "))
            turtle_list[turtle_position - 1].right(right_angle)
    else:
        pass


mainloop()