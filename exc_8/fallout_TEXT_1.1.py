from random import randint


def replay():
    while True:
        cmd = input("Try again? (Yes or No) ")
        cmd.lower()
        if cmd == "yes":
            start()
            break
        elif cmd == "no":
            break
        else:
            print("I can't understand that!")


def combat(attacker, defender, max_hp):
    if attacker["Health"] > 0 and defender["Health"] > 0:
        cmd = input("What do you want to do? (Melee, Shoot, Dodge, Block or Heal) ")
        cmd.lower()
        if cmd == "melee":
            melee(attacker, defender, max_hp)
        elif cmd == "shoot":
            shoot(attacker, defender, max_hp)
        elif cmd == "dodge":
            dodge(attacker, defender, max_hp)
        elif cmd == "block":
            block(attacker, defender, max_hp)
        elif cmd == "heal":
            heal(attacker, defender, max_hp)
        else:
            print("I couldn't understand your craps!")
            combat(attacker, defender, max_hp)
    elif attacker["Health"] <= 0 or defender["Health"] <= 0:
        if attacker["Health"] > 0:
            print(attacker["Name"], "win!")
        else:
            print(attacker["Name"], "sucks dick!")


def melee(attacker, defender, max_hp):
    attacker_melee = attacker["Melee Damage"] - defender["Armor"]
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    if attacker["Speed"] == defender["Speed"]:
        print("Both of you attacked at the same time.")
        if attacker_melee > 0:
            defender["Health"] -= attacker_melee
        else:
            defender["Health"] -= abs(attacker_melee)

        if defender_melee > defender_long_range:
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    elif attacker["Speed"] > defender["Speed"]:
        print(attacker["Name"], "attacked", defender["Name"])
        if attacker_melee > 0:
            defender["Health"] -= attacker_melee
        else:
            defender["Health"] -= abs(attacker_melee)

        if defender["Health"] > 0:
            if defender_melee > defender_long_range:
                print(defender["Name"], "attacked", attacker["Name"])
                if defender_melee > 0:
                    attacker["Health"] -= defender_melee
                else:
                    attacker["Health"] -= abs(defender_melee)
            else:
                print(defender["Name"], "shot", attacker["Name"])
                if defender_long_range > 0:
                    attacker["Health"] -= defender_long_range
                else:
                    attacker["Health"] -= abs(defender_long_range)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    elif attacker["Speed"] < defender["Speed"]:
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)

        if attacker["Health"] > 0:
            print(attacker["Name"], "attacked", defender["Name"])
            if attacker_melee > 0:
                defender["Health"] -= attacker_melee
            else:
                defender["Health"] -= abs(attacker_melee)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    combat(attacker, defender, max_hp)


def shoot(attacker, defender, max_hp):
    attacker_long_range = attacker["Long range Damage"] - defender["Armor"]
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    hit_chance = randint(1, 100)
    if hit_chance & 2 == 0:
        print(attacker["Name"], "shot", defender["Name"])
        if attacker_long_range > 0:
            defender["Health"] -= attacker_long_range
        else:
            defender["Health"] -= abs(attacker_long_range)
    else:
        print(attacker["Name"], "missed the shot!")

    if defender["Health"] > 0:
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
    print(attacker["Name"], "has", attacker["Health"], "HP left!")
    print(defender["Name"], "has", defender["Health"], "HP left!")
    combat(attacker, defender, max_hp)


def block(attacker, defender, max_hp):
    attacker_long_range = attacker["Long range Damage"] - defender["Armor"]
    attacker_melee = attacker["Melee Damage"] - defender["Armor"]
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    block_chance = randint(1, 100)
    if block_chance & 2 == 0:
        print(defender["Name"] + "'s attack has been blocked!")
        if attacker_melee > attacker_long_range:
            print(attacker["Name"], "paid back", defender["Name"])
            if attacker_melee > 0:
                defender["Health"] -= attacker_melee
            else:
                defender["Health"] -= abs(attacker_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            if attacker_long_range > 0:
                defender["Health"] -= attacker_long_range
            else:
                defender["Health"] -= abs(attacker_long_range)
        print(defender["Name"], "has", defender["Health"], "HP left!")
    else:
        print(attacker["Name"], " can't block shit!")
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
    combat(attacker, defender, max_hp)


def dodge(attacker, defender, max_hp):
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    dodge_chance = randint(1, 100)
    if dodge_chance & 2 == 0:
        print(attacker["Name"], "successfully dodged an attack.")
        attacker["Health"] += 20
        if attacker["Health"] > max_hp:
            attacker["Health"] = max_hp
    else:
        print(attacker["Name"], "is sucks at dodging!")
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
    print(attacker["Name"], "has", attacker["Health"], "HP left!")
    combat(attacker, defender, max_hp)


def heal(attacker, defender, max_hp):
    if attacker["Med"] > 0:
        print("You healed yourself")
        attacker["Health"] = max_hp
        attacker["Med"] -= 1
        print(attacker["Name"], "has", attacker["Health"], "HP left.")
    else:
        print("There aren't any medkit left.")
    combat(attacker, defender, max_hp)


def enter():
    enter = input(">>>")


def start():
    global player, player_full_hp, betrayal, companions, zombie, wolf, thieve
    companions = 0
    destination = 0
    player = {
        "Name": "Unknown",
        "Lvl": 1,
        "Health": 1,
        "Armor": 1,
        "Melee Damage": 1,
        "Long range Damage": 0,
        "Speed": 1,
        "Luck": 1,
        "Med": 0,
    }
    betrayal = {
        "Name": "Betrayal",
        "Lvl": 1,
        "Health": randint(50, 100 - player["Luck"]),
        "Armor": randint(1, 3),
        "Melee Damage": randint(6, 13),
        "Long range Damage": 0,
        "Speed": randint(1, 5),
        "Luck": 3
    }
    wolf = {
        "Name": "Wolf",
        "Lvl": 1,
        "Health": randint(90, 120),
        "Armor": 1,
        "Melee Damage": 8,
        "Long range Damage":0,
        "Speed": 5,
        "Luck": 2,
    }
    zombie = {
        "Name": "Zombie",
        "Lvl": 1,
        "Health": randint(50, 200),
        "Armor": 1,
        "Melee Damage": 15,
        "Long range Damage": 0,
        "Speed": randint(3, 6),
        "Luck": 5,
    }
    thieve = {
        "Name": "Thieve",
        "Lvl": 1,
        "Health": randint(50, 100 - player["Luck"]),
        "Armor": randint(1, 3),
        "Melee Damage": randint(6, 13),
        "Long range Damage": randint(10, 20),
        "Speed": randint(1, 5),
        "Luck": 3
    }

    print("-The time is here! It's time to go out there and take back America!")
    enter()
    print("The voice resounding through out the Vault, Vault 88.")
    enter()
    print("-We might never see each other again, but we're still a family, and I'm proud to be "
          "your Observer.")
    enter()
    print('A well-dressed man called "Observer" giving speech to a crowd in the middle of the Vault.')
    enter()
    print("-Things got tough after the nuke landed in Washington DC, but the world is rebuilding and so we will.")
    enter()
    print("-The time we lived here was precious but it's time to leave it behind and take your own path!")
    enter()
    print("Right when the speech ended, the Vault door open.")
    print("The sunlight of the summer, the green trees of a rebuilding world and a aftermath of the nuclear war"
          " are in front of their eyes.")
    enter()
    name = input("What is your character name? ")
    while name == "":
        name = input("What is your character name? ")
    player["Name"] = name
    player["Health"] = randint(70, 200)
    player["Armor"] = randint(1, 4)
    player["Melee Damage"] = randint(9, 15)
    player["Speed"] = randint(1, 5)
    player["Luck"] = randint(1, 10)
    player_full_hp = player["Health"]

    while True:
        cmd = input("Do you want to check your stats?\n"
                    "(Yes or No) ")
        cmd.lower()
        if cmd == "yes":
            print("Your Name:", player["Name"])
            print("Your Level:", player["Lvl"])
            print("Your Health:", player["Health"])
            print("Your Armor:", player["Armor"])
            print("Your Melee Damage:", player["Melee Damage"])
            print("Your Long range Damage:", player["Long range Damage"])
            print("Your Speed:", player["Speed"])
            print("Your Luck:", player["Luck"])
            break
        elif cmd == "no":
            break
        else:
            print("I can't understand your answer!")
    print("After wandering outside for a while, you find a map.")
    while True:
        cmd = input("Do you want to pick it up? (Yes or No) ")
        cmd.lower()
        if cmd == "yes":
            print("There're 2 cities marked in the map.\n"
                  "Wastie in the west.\n"
                  "Havani in the east.")
            while True:
                destin = input("Where do you want go? (Wastie or Havani) ")
                destin.lower()
                if destin == "wastie":
                    destination = 1
                    print("You're going to Wastie in the west.")
                    break
                elif destin == "havani":
                    destination = 2
                    print("You're going to Havani in the east.")
                    break
                else:
                    print("I can't understand your answer!")
            break
        elif cmd == "no":
            print("You keep wandering around.")
            break
        else:
            print("I can't understand your command!")
    enter()
    if destination == 0:
        print("You found a lonely dog in near an abandoned gas station.")
        while True:
            cmd = input("Do you want her to travel with you? (Yes or No) ")
            cmd.lower()
            if cmd == "yes":
                player["Melee Damage"] += 8
                player["Speed"] += 2
                player["Long range Damage"] -= 2
                print("You take the dog with you.")
                print("Your Long range Attack:", player["Long range Damage"])
                print("Your Melee Attack:", player["Melee Damage"])
                print("Your Speed:", player["Speed"])
                break
            elif cmd == "no":
                print("The dog drop you a [Colt 1911] and want to travel with you.")
                player["Long range Damage"] += 20
                print("Your Long range Damage:", player["Long range Damage"])
                while True:
                    cmd = input("Do you want her to travel with you? (Yes or No) ")
                    cmd.lower()
                    if cmd == "yes":
                        player["Long range Damage"] -= 2
                        player["Melee Damage"] += 8
                        player["Speed"] += 2
                        print("You take the dog with you.")
                        print("Your Long range Attack:", player["Long range Damage"])
                        print("Your Melee Attack:", player["Melee Damage"])
                        print("Your Speed:", player["Speed"])
                        break
                    elif cmd == "no":
                        print("You ignored the dog.")
                        break
                    else:
                        print("I can't understand your answer!")
                break
            else:
                print("I can't understand your answer!")
    elif destination == 1:
        print("After travel about 100 meters away from the Vault, someone ask you to group up with him.")
        enter()
        while True:
            cmd = input("Do you want to group up with him? (Yes or No) ")
            cmd.lower()
            if cmd == "yes":
                print("You decided to group up with him.")
                enter()
                player_full_hp += randint(70, 120)
                player["Health"] = player_full_hp
                player["Armor"] += 1
                player["Melee Damage"] += randint(1, 3)
                player["Speed"] *= 2
                player["Luck"] += 2
                print("Your Health:", player["Health"])
                print("Your Armor:", player["Armor"])
                print("Your Melee Damage:", player["Melee Damage"])
                print("Your Speed:", player["Speed"])
                print("Your Luck:", player["Luck"])
                companions = 1
                break
            elif cmd == "no":
                if player["Luck"] <= 5:
                    print("-Then die!!! He screamed at you.")
                    enter()
                    for key, value in betrayal.items():
                        print(key + ":", value)
                    enter()
                    combat(player, betrayal, player_full_hp)
                    break
                else:
                    print("He gave you an [Rusty Axe] to defend yourself against whatever out there.")
                    player["Melee Damage"] += 8
                    enter()
                    print("You keep on traveling to Wastie.")
                    break
            else:
                print("I can't understand your command!")
    elif destination == 2:
        if player["Luck"] > 3:
            print("Fortunately, you found a chest along the way to Havani.")
            while True:
                cmd = input("Do you want to open it? (Open or Ignore) ")
                cmd.lower()
                if cmd == "open":
                    chest_chance = randint(1, 100)
                    if chest_chance % 2 == 0:
                        print("You received a [Plasma Rifle].")
                        player["Long range Damage"] += 30
                        print("Your Long range Damage:", player["Long range Damage"])
                    else:
                        print("It's a trap! You got hit by poison dart.")
                        player["Health"] -= 20
                        player["Speed"] -= 1
                        print("Your Health:", player["Health"])
                        print("Your Speed:", player["Speed"])
                    break
                elif cmd == "ignore":
                    print("You lost the chance to get a [Plasma Rifle].")
                    break
                else:
                    print("I can't understand your command!")
        else:
            print("You've going for 2 hours in the waste land. You finally see someone in the distant. He seem to be fighting"
                  " with a wolf")
            while True:
                cmd = input("What do you want to do? (Help, Ignore or Wait) ")
                cmd.lower()
                if cmd == "help":
                    print("-Why don't you just die! The man shout at the wolf.")
                    enter()
                    print("The wolf don't seem to care and immediately bite the man left leg.")
                    enter()
                    print("Running faster than an athletic, you kick the dog away.")
                    enter()
                    print("Are you alright? I'm", player["Name"])
                    enter()
                    print("Thank you so much. Let's beat this son of a bitch together!")
                    enter()
                    for key, value in wolf.items():
                        print(key + ":", value)
                    enter()
                    combat(player, wolf, player_full_hp)
                    break
                elif cmd == "ignore":
                    print("-I'm so sorry but I have things to deal with too. You said that to yourself.")
                    enter()
                    print("You keep on traveling to Havani.")
                    break
                elif cmd == "wait":
                    print("You've 15 minutes for the wolf to kills that man. You looted a [Combat Knife] from the man's body")
                    player["Melee Damage"] += 4
                    print("Your Melee Damage:", player["Melee Damage"])
                    break
                else:
                    print("I can't understand your command!")
    if player["Lvl"] > 1:
        enter()
        print("You have leveled up!")
        player_full_hp += 50
        player["Health"] = player_full_hp
        player["Speed"] += 2
        print("Player Health:", player["Health"])
        print("Player Speed:", player["Speed"])
    else:
        pass
    if player["Health"] > 0:
        enter()
        print("You realized there's a [Medkit] in your pocket.")
        enter()
        if player["Health"] < player_full_hp:
            while True:
                cmd = input("What do you want to do? (Use or Save) ")
                cmd.lower()
                if cmd == "use":
                    player["Health"] = player_full_hp
                    print("You're fully healed.")
                    print("Your Health:", player["Health"])
                    break
                elif cmd == "save":
                    print("You save it for later.")
                    player["Med"] = 1
                    break
                else:
                    print("I can't understand your command!")
        elif player["Health"] == player_full_hp:
            print("You save it for later.")
            player["Med"] = 1
    if player["Health"] > 0:
        enter()
        if destination == 0:
            print("It's currently noon, the weather is hot as fuck.")
            enter()
            print("You take a rest in an abandoned building.")
            enter()
            building_loot = ["M4A4", "Colt Python", "Remington Spartan 310"]
            print("After looking around building a bit, you found a", "[" + building_loot[randint(0, 2)] + "]")
            player["Long range Damage"] += 23
        elif destination == 1:
            if companions == 1:
                print("We're about 500 meters away from Wastie. Let's rest here,", player["Name"] + ".")
                enter()
                print("-Yeah.")
                enter()
                print("You and your companion take a rest for the time being.")
                enter()
                print("Your companion are making equipment out of remains of enemies you faced along the way. ")
                enter()
                print("You received a [Leather Helmet], a [Leather Armor] and a [Pair of Claws]")
                enter()
                player["Armor"] += 5
                player["Melee Damage"] += 3
                print("Your Armor:", player["Armor"])
                print("Your Melee Damage:", player["Melee Damage"])
            else:
                print("While continue travel to Wastie city, you encountered a Zombie.")
                enter()
                while True:
                    cmd = input("What do you want to do? (Fight or Run) ")
                    cmd.lower()
                    if cmd == "fight":
                        for key, value in zombie.items():
                            print(key + ":", value)
                        enter()
                        combat(player, zombie, player_full_hp)
                        break
                    elif cmd == "run":
                        if player["Speed"] > zombie["Speed"]:
                            print("You ran away from the zombie.")
                        else:
                            print("The zombie is too fast to escape!")
                            enter()
                            for key, value in zombie.items():
                                print(key + ":", value)
                            enter()
                            combat(player, zombie, player_full_hp)
                            break
                    else:
                        print("I can't understand your command!")
        elif destination == 2:
            encounter_list = ["Wolf", "Thieve", "Zombie"]
            encounter = encounter_list[randint(0, 2)]
            print("Only about 100 meters away from Havani, you encountered a", encounter)
            enter()
            print("You're too tired to run away, so you must fight.")
            enter()
            if encounter == "Wolf":
                for key, value in wolf.items():
                    print(key + ":", value)
                enter()
                combat(player, wolf, player_full_hp)
            elif encounter == "Thieve":
                for key, value in thieve.items():
                    print(key + ":", value)
                enter()
                combat(player, thieve, player_full_hp)
            elif encounter == "Zombie":
                for key, value in zombie.items():
                    print(key + ":", value)
                enter()
                combat(player, thieve, player_full_hp)
    if player["Health"] > 0:
        print("To be continue>")
    else:
        replay()


begin = input("Press Enter to start.")
start()
