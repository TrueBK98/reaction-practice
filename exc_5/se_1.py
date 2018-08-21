shop_list = ["T-Shirt", "Sweater"]
while True:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if command == "C" or command == "c":
        Create = input("Enter new item: ")
        shop_list.append(Create)
    elif command == "R" or command == "e":
        pass
    elif command == "U" or command == "u":
        Update = int(input("Update position? "))
        new_item = input("New item? ")
        shop_list[Update] = new_item
    elif command == "D" or command == "d":
        Delete = int(input("Delete position? "))
        del shop_list[Delete]
    print("Our items:", shop_list)