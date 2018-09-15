    return item_name


def generate_item():
    name = generate_item_names()
    item = {
        "NAME": name,
        "AGI": 0,
        "HP": 0,
        "DEF": 0,
        "STR": 0,
    }
    if "bánh bao" in name:
        item["HP"] += 5
    elif "cơm" in name:
        item["HP"] += 8
        item["STR"] += 2
        item["AGI"] += -1
    elif "mỳ" in name:
        item["HP"] += 10
        item["STR"] += 3
        item["AGI"] += -2

    if "hấp" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                if v > 0:
                    item[k] += 2
    elif "chiên" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                if v > 0:
                    item[k] += 3
    elif "luộc" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                if v > 0:
                    item[k] += 4

    if "rẻ" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                item[k] *= 1.5
    elif "thường" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                item[k] *= 2
    elif "đắt" in name:
        for k, v in item.items():
            if k == "NAME":
                pass
            else:
                item[k] *= 2.5
    return item


#
#
def show_item(game_item):
    print("* " * 15)

    for key, value in game_item.items():
        print("*", key, ":", value)

    print("* " * 15)

#
#
# steel_gauntlet = {
#     "NAME": "STEEL GAUNLET",
#     "HP": 10,
#     "AGI": 5,
#     "LUCK": 1,
# }
#
# bronze_shield = {
#     "NAME": "BRONZE SHIElD",
#     "HP": 5,
#     "AGI": 1,
# }
#
# golden_stick = {
#     "NAME": "GOLDEN STICK",
#     "AGI": 15,
#     "HP": 20,
#     "STR": 100,
# }
#
# inventory = [steel_gaunlet, bronze_shield, golden_stick]
# for item in inventory:
#     show_item(item)


def show_items():
    print("Your inventory:")
    for i in items:
        print(str(items.index(i) + 1) + ".", i["NAME"])
