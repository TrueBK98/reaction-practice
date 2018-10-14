from random import randint
from inventory import *


def calculate_crit(attacker):
    has_crit = False
    dice = randint(0, 10)
    chance = attacker["LUCK"] + attacker["AGI"]
    if chance > dice:
        has_crit = True

    return has_crit


def combat_round(attacker, defender):
    print(attacker["NAME"], "đang tấn công", defender["NAME"])
    has_crit = calculate_crit(attacker)

    if has_crit:
        print("Đòn chí mạng")
        damage = attacker["STR"] * 2 - defender["DEF"]
    else:
        damage = attacker["STR"] - defender["DEF"]

    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "mất", damage, "HP")
        print(defender["NAME"], "còn", defender["HP"], "HP")
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "mất", abs(damage), "HP")
        print(attacker["NAME"], "còn", attacker["HP"], "HP")


def combat_full(player, opponent):
    while True:
        combat_round(player, opponent)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break

        combat_round(opponent, player)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break

        print("Bạn muốn:")
        print("1. Đánh tiếp")
        print("2. Chạy")
        print("3. Dùng đồ")
        print("4. Tự động đánh")
        option = input(">>> ")
        if option == "1":
            print("Nhào zô")
        elif option == "2":
            dice = randint(0, 100)
            if player["LUCK"] > dice:
                print("Bạn đã chạy thoát")
                break
            else:
                print("Chạy trốn không thành công, bạn quay trở lại cuộc chiến")
        elif option == "3":
            use_item(player)
            for k, v in player.items():
                print(k + ":", v)
        elif option == "4":
            print("Bài tập về nhà, hihi")
        else:
            print("Bị ngu à?!")
    if player["HP"] <= 0:
        print("Lost")
    else:
        print(opponent["NAME"], "died")
        item_after_cmbt()