player_stats = {
    "Name": "BlackKnight_98",
    "Class": "Spellblade",
    "Lvl": 1,
    "Damage": 8,
    "Armor": 0.1,
    "Heath": 60,
    "Magicka": 100,
    "Stamina": 100,
}
opt_loop = 1
while opt_loop == 1:
    command = input("Your command? (stats, start) ")
    command.lower()
    if command == "stats":
        print("Your name:", player_stats["Name"])
        print("Your class: ", player_stats["Class"])
        print("Your level: ", player_stats["Lvl"])
        print("Your Heath Points: ", player_stats["Heath"])
        print("Your Magicka: ", player_stats["Magicka"])
        print("Your Stamina: ", player_stats["Stamina"])
    elif command == "start":
        opt_loop = 0
        print("You're currently at the castle gate")
        print("There are 2 ways to go:")
        print("1. Return to the castle")
        print("2. Go to the Forest of Javania")
        opt_loop1 = 1
        while opt_loop1 == 1:
            option = int(input("Your choice? "))
            if option == 1:
                print("You have a destiny to fulfill!")
            elif option == 2:
                opt_loop1 = 0
                print("You traveled to the Forest of Javania")
                print("There is a Heath Potion you can pick up")
                print("1. Ignore")
                print("2. Pick it up")
                opt_loop = 1
                while opt_loop == 1:
                    option = int(input("Your choice? "))
                    player_stats["Heath"] = 100
                    if option == 1:
                        opt_loop = 0
                        print("The Heath Potion disappeared")
                    elif option == 2:
                        opt_loop = 0
                        print("You picked it up and healed yourself")
                        print("Heath:", player_stats["Heath"])
                    else:
                        print("I can't understand your command!")
                print("You encountered a Small Wolf")
                print("1. Escape")
                print("2. Hide")
                print("3. Fight")
                option = int(input("Your choice? "))
                if option == 1:
                    print("You run back to the castle")
                elif option == 2:
                    print("You hidden away from the Small Wolf")
                elif option == 3:
                    wolf_small = {
                        "Name": "Small Wolf",
                        "Lvl": 1,
                        "Damage": 8,
                        "Heath": 30,
                        "Magicka": 0,
                        "Stamina": 120,
                    }
                    print("Name:", wolf_small["Name"])
                    print("Level: ", wolf_small["Lvl"])
                    print("Damage", wolf_small["Damage"])
                    print("Heath Points: ", wolf_small["Heath"])
                    print("Magicka: ", wolf_small["Magicka"])
                    print("Stamina: ", wolf_small["Stamina"])
                    print("You go first")
                    combat_seq = 1
                    while combat_seq == 1:
                        if wolf_small["Heath"] > 0:
                            print("1. Physical Attack")
                            print("2. Magical Attack")
                            print("3. Block")
                            option = int(input("Your choice? "))
                            wolf_small_damage = wolf_small["Damage"] - (wolf_small["Damage"] * player_stats["Armor"])
                            fire_ball_dmg = player_stats["Damage"] + 8
                            if option == 1:
                                print("You attacked the Small Wolf with One-Handed Iron Sword and dealt", player_stats["Damage"],
                                      "damage")
                                wolf_small["Heath"] = wolf_small["Heath"] - player_stats["Damage"]
                                print("You received", wolf_small_damage, "damage")
                                player_stats["Heath"] -= wolf_small_damage
                                print("Your Heath:", player_stats["Heath"])
                                print("Small Wolf:", wolf_small["Heath"])
                            elif option == 2 and player_stats["Magicka"] > 0:
                                player_stats["Magicka"] -= 25
                                print("You attacked the Small Wolf with Fire Ball and dealt", player_stats["Damage"], "damage")
                                wolf_small["Heath"] = wolf_small["Heath"] - player_stats["Damage"]
                                print("You received", wolf_small_damage, "damage")
                                player_stats["Heath"] -= wolf_small_damage
                                print("Your Heath:", player_stats["Heath"])
                                print("Your Magicka:", player_stats["Magicka"])
                                print("Small Wolf:", wolf_small["Heath"])
                            elif option == 2 and player_stats["Magicka"] == 0:
                                print("You're out of Magicka!")
                                print("You received", wolf_small_damage, "damage")
                                player_stats["Heath"] -= wolf_small_damage
                                print("Your Heath:", player_stats["Heath"])
                                print("Small Wolf:", wolf_small["Heath"])
                            elif option == 3:
                                print("You blocked an attack from Small Wolf")
                                print("Your Heath:", player_stats["Heath"])
                                print("Small Wolf:", wolf_small["Heath"])
                        elif wolf_small["Heath"] < 0:
                            combat_seq = 0
                            print("You won!")
                else:
                    print("I can't understand your command!")
            else:
                print("I can't understand your command!")
    else:
        print("please, re-enter your choice")