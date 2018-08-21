sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my ship sizes")
print(sizes)
print("Now my biggest ship has size", max(sizes), "let's shear it")
max_index = sizes.index(max(sizes))
sizes[max_index] = 8
print("After shearing, here is my flock")
print(sizes)
for i in range(1, 3):
    print("MONTH", i, ":")
    print("One month hass passed, here is my flock")
    sizes = [x+50 for x in sizes]
    print(sizes)
    print("Now my biggest ship has size", max(sizes), "let's shear it")
    max_index = sizes.index(max(sizes))
    sizes[max_index] = 8
    print("After shearing, here is my flock")
    print(sizes)
print("MONTH 3 :")
print("One month has passed, here is my flock")
sizes = [x+50 for x in sizes]
print(sizes)
total_size = sum(sizes)
print("My flock has size in in total:", total_size)
total_money = total_size * 2
print("I would get", total_size, "* 2$ =", total_money, end="")
print("$")