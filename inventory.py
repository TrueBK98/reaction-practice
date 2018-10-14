items = []
medkit = {
    "NAME": "Hộp cứu thương",
    "HP": 20,
}


def show_items():
    print("Đồ của bạn:")
    for i in items:
        print(str(items.index(i) + 1) + ".", i["NAME"])


def use_item(player):
    show_items()
    while True:
        item_position = int(input("Bạn muốn dùng: "))
        item = items[item_position - 1]
        if item_position <= len(items):
            for k, v in item.items():
                if k == "NAME":
                    pass
                else:
                    player[k] += item[k]
                    if player["HP"] > 100:
                        player["HP"] = 100
                    print(k, "của bạn:", player[k])
            items.remove(item)
            break
        else:
            print("Đánh lại đê!")


def new_item():
    print("Con sói rơi ra", medkit["NAME"])
    while True:
        print("Bạn sẽ:\n"
              "1. Nhặt lên\n"
              "2. Vứt đi")
        choice = input(">>>")
        if choice == "1":
            items.append(medkit)
            show_items()
            break
        elif choice == "2":
            print("Bạn vứt nó đi")
            break
        else:
            print("Đánh lại đê!")