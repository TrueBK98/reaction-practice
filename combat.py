from random import randint
from inventory import *


def combat(player, enemy):
    while True:
        if player["HP"] > 0 and enemy["HP"] > 0:
            print("Bạn sẽ:\n"
                  "1. Đánh\n"
                  "2. Dùng đồ")
            choice = input(">>>")
            if choice == "1":
                move(player, enemy)
            elif choice == "2":
                if len(items) > 0:
                    use_item(player)
                else:
                    print("Bạn không còn đồ để dùng")
            else:
                print("Đánh lại đê!")
        else:
            if player["HP"] <= 0:
                print("Bạn thua")
                break
            else:
                print("Bạn thắng")
                new_item()
                break


def move(player, enemy):
    normal_dmg = player["STR"] - enemy["DEF"]
    kamekameha = (player["STR"] * 3) - enemy["DEF"]
    dmg_take = enemy["STR"] - player["DEF"]
    while True:
        player_speed = randint(1, player["AGI"])
        enemy_speed = randint(1, enemy["AGI"])
        print("Bạn sẽ:\n"
              "1. Đánh thường\n"
              "2. Cường hóa\n"
              "3. Kamehameka")
        choice = input(">>>")
        if choice == "1":
            print("Bạn đánh con sói\n"
                  "Nó không hiệu quả cho lắm")
            enemy["HP"] -= normal_dmg
            if enemy["HP"] > 0:
                print("Con sói cắn bạn\n"
                      "Nó không hiệu quả cho lắm")
                player["HP"] -= dmg_take
            print("HP của bạn:", player["HP"])
            print("HP đối phương", enemy["HP"])
            break
        elif choice == "2":
            print("Bạn cường hóa bản thân")
            player["STR"] += 2
            if enemy["HP"] > 0:
                print("Con sói cắn bạn\n"
                      "Nó không hiệu quả cho lắm")
                player["HP"] -= dmg_take
            print("HP của bạn:", player["HP"])
            print("STR của bạn", player["STR"])
            print("HP đối phương", enemy["HP"])
            break
        elif choice == "3":
            if player_speed >= enemy_speed:
                print("Bạn thổi bay đối phương!")
                enemy["HP"] -= kamekameha
            else:
                print("Bạn bắn trượt!")

            if enemy["HP"] > 0:
                print("Con sói cắn bạn\n"
                      "Nó không hiệu quả cho lắm")
                player["HP"] -= dmg_take
            print("HP của bạn:", player["HP"])
            print("HP đối phương", enemy["HP"])
            break
        else:
            print("Đánh lại đê!")