from fallout_enemy import *
from fallout_combat import *
from fallout_stats import *
from fallout_drop_n_loot import *
from fallout_inventory import *
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


def enter():
    enter = input(">>>")


def start():
    inventory = []
    companions = 0
    destination = 0
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
                inventory.append(colt_1911)
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
                    combat(player, betrayal, player_full_hp, betrayal_max_hp, inventory)
                    if player["Health"] > 0:
                        inventory = drop(inventory, betrayal)
                    break
                else:
                    print("He gave you an [Rusty Axe] to defend yourself against whatever out there.")
                    inventory.append(rusty_axe)
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
                        inventory.append(plasma_rifle)
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
                    combat(player, wolf, player_full_hp, wolf_full_hp, inventory)
                    if player["Health"] > 0:
                        inventory = drop(inventory, wolf)
                    break
                elif cmd == "ignore":
                    print("-I'm so sorry but I have things to deal with too. You said that to yourself.")
                    enter()
                    print("You keep on traveling to Havani.")
                    break
                elif cmd == "wait":
                    print("You've 15 minutes for the wolf to kills that man. You looted a [Combat Knife] from the man's body")
                    inventory.append(combat_knife)
                    player["Melee Damage"] += 8
                    break
                else:
                    print("I can't understand your command!")
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
                    inventory.append(medkit)
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
            if inventory <= 9:
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
                if inventory <= 6:
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
                        combat(player, zombie, player_full_hp, zombie_full_hp, inventory)
                        if player["Health"] > 0:
                            inventory = drop(inventory, zombie)
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
                            combat(player, zombie, player_full_hp, zombie_full_hp, inventory)
                            if player["Health"] > 0:
                                inventory = drop(inventory, zombie)
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
                combat(player, wolf, player_full_hp, wolf_full_hp, inventory)
                if player["Health"] > 0:
                    inventory = drop(inventory, wolf)
            elif encounter == "Thieve":
                for key, value in thieve.items():
                    print(key + ":", value)
                enter()
                combat(player, thieve, player_full_hp, thieve, inventory)
                if player["Health"] > 0:
                    inventory = drop(inventory, thieve)
            elif encounter == "Zombie":
                for key, value in zombie.items():
                    print(key + ":", value)
                enter()
                combat(player, zombie, player_full_hp, zombie_full_hp, inventory)
                if player["Health"] > 0:
                    inventory = drop(inventory, zombie)
    if player["Health"] > 0:
        print("To be continue>")
    else:
        replay()


begin = input("Press Enter to start.")
start()
