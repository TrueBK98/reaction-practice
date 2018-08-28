from random import randint


def enter():
    enter = input(">>>")


med = 0
companions = 0
destination = 0
player = {
    "Name": "Unknown",
    "Lvl": 1,
    "Heath": 1,
    "Armor": 1,
    "Melee Damage": 1,
    "Long range Damage": 0,
    "Speed": 1,
    "Luck": 1
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
player["Heath"] = randint(70, 200)
player["Armor"] = randint(1, 4)
player["Melee Damage"] = randint(9, 15)
player["Speed"] = randint(1, 5)
player["Luck"] = randint(1, 10)
player_full_hp = player["Heath"]
opt_loop = 1
while opt_loop == 1:
    cmd = input("Do you want to check your stats?\n"
                "(Yes or No) ")
    if cmd == "Yes":
        print("Your Name:", player["Name"])
        print("Your Level:", player["Lvl"])
        print("Your Health:", player["Heath"])
        print("Your Armor:", player["Armor"])
        print("Your Melee Damage:", player["Melee Damage"])
        print("Your Long range Damage:", player["Long range Damage"])
        print("Your Speed:", player["Speed"])
        print("Your Luck:", player["Luck"])
        opt_loop = 0
    elif cmd == "No":
        pass
        opt_loop = 0
    else:
        print("I can't understand your answer!")
print("After wandering outside for a while, you find a map.")
opt_loop = 1
while opt_loop == 1:
    cmd = input("Do you want to pick it up? (Yes or No) ")
    if cmd == "Yes":
        print("There're 2 cities marked in the map.\n"
              "Wastie in the west.\n"
              "Havani in the east.")
        while opt_loop == 1:
            destin = input("Where do you want go? (Wastie or Havani) ")
            if destin == "Wastie":
                destination = 1
                print("You're going to Wastie in the west.")
                opt_loop = 0
            elif destin == "Havani":
                destination = 2
                print("You're going to Havani in the east.")
                opt_loop = 0
            else:
                print("I can't understand your answer!")
    if cmd == "No":
        print("You keep wandering around.")
        opt_loop = 0
    else:
        pass
enter()
if destination == 0:
    print("You found a lonely dog in near an abandoned gas station.")
    opt_loop = 1
    while opt_loop == 1:
        cmd = input("Do you want her to travel with you? (Yes or No) ")

        if cmd == "Yes":
            opt_loop = 0
            player["Melee Damage"] += 8
            player["Speed"] += 2
            player["Long range Damage"] -= 2
            print("You take the dog with you.")
            print("Your Long range Attack:", player["Long range Damage"])
            print("Your Melee Attack:", player["Melee Damage"])
            print("Your Speed:", player["Speed"])
        elif cmd == "No":
            print("The dog drop you a [Colt 1911] and want to travel with you.")
            player["Long range Damage"] += 20
            print("Your Long range Damage:", player["Long range Damage"])
            while opt_loop == 1:
                cmd = input("Do you want her to travel with you? (Yes or No) ")
                if cmd == "Yes":
                    opt_loop = 0
                    player["Long range Damage"] -= 2
                    player["Melee Damage"] += 8
                    player["Speed"] += 2
                    print("You take the dog with you.")
                    print("Your Long range Attack:", player["Long range Damage"])
                    print("Your Melee Attack:", player["Melee Damage"])
                    print("Your Speed:", player["Speed"])
                elif cmd == "No":
                    opt_loop = 0
                    print("You ignored the dog.")
                else:
                    print("I can't understand your answer!")
        else:
            pass
elif destination == 1:
    print("After travel about 100 meters away from the Vault, someone ask you to group up with him")
    enter()
    opt_loop = 1
    while opt_loop == 1:
        cmd = input("Do you want to group up with him? (Yes or No) ")
        if cmd == "Yes":
            opt_loop = 0
            print("You decided to group up with him.")
            enter()
            player_full_hp += randint(70, 120)
            player["Heath"] = player_full_hp
            player["Armor"] += 1
            player["Melee Damage"] += randint(1, 3)
            player["Speed"] *= 2
            player["Luck"] += 2
            print("Your Health:", player["Heath"])
            print("Your Armor:", player["Armor"])
            print("Your Melee Damage:", player["Melee Damage"])
            print("Your Speed:", player["Speed"])
            print("Your Luck:", player["Luck"])
            companions = 1
        elif cmd == "No":
            betrayal = {
                "Name": "Louis P. Connors",
                "Lvl": 1,
                "Heath": randint(50, 100 - player["Luck"]),
                "Armor": randint(1, 3),
                "Melee Damage": randint(6, 13),
                "Long range Damage": 0,
                "Speed": randint(1, 5),
                "Luck": 3
            }
            if player["Luck"] <= 5:
                opt_loop = 0
                print("-Then die!!! He screamed at you.")
                enter()
                print("Enemy Name:", betrayal["Name"])
                print("Enemy Level:", betrayal["Lvl"])
                print("Enemy Health:", betrayal["Heath"])
                print("Enemy Armor:", betrayal["Armor"])
                print("Enemy Melee Damage:", betrayal["Melee Damage"])
                print("Enemy Long range Damage:", betrayal["Long range Damage"])
                print("Enemy Speed:", betrayal["Speed"])
                print("Enemy Luck:", betrayal["Luck"])
                combat_seq = 1
                while combat_seq == 1:
                    player_dmg = player["Melee Damage"] - betrayal["Armor"]
                    betrayal_dmg = betrayal["Melee Damage"] - player["Armor"]
                    if player["Heath"] > 0 and betrayal["Heath"] > 0:
                        cmd = input("What do you want to do? (Melee Attack, Dodge or Block) ")
                        if cmd == "melee attack" or cmd == "Melee Attack":
                            if player["Speed"] == betrayal["Speed"]:
                                print("Both of you punched each other at the same time.")
                                player["Heath"] -= betrayal_dmg
                                betrayal["Heath"] -= player_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", betrayal["Heath"])
                            elif player["Speed"] > betrayal["Speed"]:
                                print("You punched him in the face!")
                                betrayal["Heath"] -= player_dmg
                                if betrayal["Heath"] > 0:
                                    print("Enemy kicked you in the ass!")
                                    player["Heath"] -= betrayal_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", betrayal["Heath"])
                            elif player["Speed"] < betrayal["Speed"]:
                                print("Enemy kicked you in the ass!")
                                player["Heath"] -= betrayal_dmg
                                if player["Heath"] > 0:
                                    print("You punched him in the face!")
                                    betrayal["Heath"] -= player_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", betrayal["Heath"])
                        elif cmd == "dodge" or cmd == "Dodge":
                            dodge_chance = randint(1, 100)
                            if dodge_chance % 2 == 0:
                                print("You successfully dodged attack.")
                                player["Heath"] += 20
                                print("Your Health:", player["Heath"])
                            if dodge_chance % 2 == 1:
                                print("You failed at dodging incoming attack.")
                                player["Heath"] -= betrayal_dmg
                                print("Your Health:", player["Heath"])
                        elif cmd == "block" or cmd == "Block":
                            block_chance = randint(1, 100)
                            if block_chance % 2 == 0:
                                print("You successfully blocked and paid back the enemy.")
                                betrayal["Heath"] -= player_dmg
                                print("Enemy Heath:", betrayal["Heath"])
                            if block_chance % 2 == 1:
                                print("You can't block shit!")
                                player["Heath"] -= betrayal_dmg
                                print("Your Health:", player["Heath"])
                        else:
                             print("I can't understand your command!")
                    elif player["Heath"] < 1:
                        print("You die!")
                        combat_seq = 0
                    elif betrayal["Heath"] < 1:
                        print("You've defeated the enemy!")
                        combat_seq = 0
                        player["Lvl"] = randint(1, 2)
                        print("You received a [Vault Suit].")
                        player["Armor"] += betrayal["Armor"]
            else:
                opt_loop = 0
                print("He gave you an [Rusty Axe] to defend yourself against whatever out there.")
                player["Melee Damage"] += 8
                enter()
                print("You keep on traveling to Wastie.")
        else:
            print("I can't understand your command!")
elif destination == 2:
    if player["Luck"] > 3:
        print("Fortunately, you found a chest along the way to Havani.")
        opt_loop = 1
        while opt_loop == 1:
            cmd = input("Do you want to open it? (Open or Ignore) ")
            if cmd == "Open":
                opt_loop = 0
                chest_chance = randint(1, 10)
                if chest_chance <= 5:
                    print("You received a [Plasma Rifle].")
                    player["Long range Damage"] += 30
                    print("Your Long range Damage:", player["Long range Damage"])
                elif chest_chance > 5:
                    print("It's a trap! You got hit by poison dart.")
                    player["Heath"] -= 20
                    player["Speed"] -= 1
                    print("Your Heath:", player["Heath"])
                    print("Your Speed:", player["Speed"])
            elif cmd == "Ignore":
                opt_loop = 0
                print("You lost the chance to get a [Plasma Rifle].")
            else:
                print("I can't understand your command!")
    else:
        print("You've going for 2 hours in the waste land. You finally see someone in the distant. He seem to be fighting"
              " with a wolf")
        wolf = {
            "Name": "Wolf",
            "Lvl": 1,
            "Heath": randint(90, 120),
            "Armor": 1,
            "Melee Damage": 8,
            "Speed": 5,
            "Luck": 2,
        }
        opt_loop = 1
        while opt_loop == 1:
            cmd = input("What do you want to do? (Help, Ignore or Wait) ")
            if cmd == "Help":
                opt_loop = 0
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
                print("Enemy Name:", wolf["Name"])
                print("Enemy Level:", wolf["Lvl"])
                print("Enemy Health:", wolf["Heath"])
                print("Enemy Armor:", wolf["Armor"])
                print("Enemy Melee Damage:", wolf["Melee Damage"])
                print("Enemy Speed:", wolf["Speed"])
                print("Enemy Luck:", wolf["Luck"])
                combat_seq = 1
                while combat_seq == 1:
                    player_dmg = player["Melee Damage"] - wolf["Armor"]
                    wolf_dmg = wolf["Melee Damage"] - player["Armor"]
                    if player["Heath"] > 0 and wolf["Heath"] > 0:
                        cmd = input("What do you want to do? (Melee Attack, Dodge or Block) ")
                        if cmd == "melee attack" or cmd == "Melee Attack":
                            if player["Speed"] == wolf["Speed"]:
                                print("Both of you bited each other at the same time.")
                                player["Heath"] -= wolf_dmg
                                wolf["Heath"] -= player_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", wolf["Heath"])
                            elif player["Speed"] > wolf["Speed"]:
                                print("You bitch slapped the wolf!")
                                wolf["Heath"] -= player_dmg
                                if wolf["Heath"] > 0:
                                    print("Enemy bite you in the nuts!")
                                    player["Heath"] -= wolf_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", wolf["Heath"])
                            elif player["Speed"] < wolf["Speed"]:
                                print("Enemy bite you in the nuts!")
                                player["Heath"] -= wolf_dmg
                                if player["Heath"] > 0:
                                    print("You bitch slapped the wolf!")
                                    wolf["Heath"] -= player_dmg
                                print("Your Health:", player["Heath"])
                                print("Enemy Heath:", wolf["Heath"])
                        elif cmd == "dodge" or cmd == "Dodge":
                            dodge_chance = randint(1, 100)
                            if dodge_chance % 2 == 0:
                                print("You successfully dodged attack.")
                                player["Heath"] += 20
                                print("Your Health:", player["Heath"])
                            if dodge_chance % 2 == 1:
                                print("You failed at dodging incoming attack.")
                                player["Heath"] -= wolf_dmg
                                print("Your Health:", player["Heath"])
                        elif cmd == "block" or cmd == "Block":
                            block_chance = randint(1, 100)
                            if block_chance % 2 == 0:
                                print("You successfully blocked and paid back the enemy.")
                                wolf["Heath"] -= player_dmg
                                print("Enemy Heath:", wolf["Heath"])
                            if block_chance % 2 == 1:
                                print("You can't block shit!")
                                player["Heath"] -= wolf_dmg
                                print("Your Health:", player["Heath"])
                        else:
                            print("I can't understand your command!")
                    elif player["Heath"] < 1:
                        print("You die!")
                        combat_seq = 0
                    elif wolf["Heath"] < 1:
                        print("You've defeated the enemy!")
                        enter()
                        combat_seq = 0
                        print("Here, take this with you! The man gave you a [Combat Knife]")
                        player["Melee Damage"] += 4
                        print("Your Melee Damage:", player["Melee Damage"])
                        player["Lvl"] = randint(1, 2)
            elif cmd == "Ignore":
                opt_loop = 0
                print("-I'm so sorry but I have things to deal with too. You said that to yourself.")
                enter()
                print("You keep on traveling to Havani.")
            elif cmd == "Wait":
                opt_loop = 0
                print("You've 15 minutes for the wolf to kills that man. You looted a [Combat Knife] from the man's body")
                player["Melee Damage"] += 4
                print("Your Melee Damage:", player["Melee Damage"])
            else:
                print("I can't understand your command!")
if player["Lvl"] > 1:
    enter()
    print("You have leveled up!")
    player_full_hp += 50
    player["Heath"] = player_full_hp
    player["Speed"] += 2
    print("Player Heath:", player["Heath"])
    print("Player Speed:", player["Speed"])
else:
    pass
if player["Heath"] > 0:
    enter()
    print("You realized there's a [Medkit] in your pocket.")
    enter()
    if player["Heath"] < player_full_hp:
        opt_loop = 1
        while opt_loop == 1:
            cmd = input("What do you want to do? (Use or Save) ")
            if cmd == "Use":
                opt_loop = 0
                player["Heath"] = player_full_hp
                print("You're fully healed.")
                print("Your Heath:", player["Heath"])
            elif cmd == "Save":
                opt_loop = 0
                print("You save it for later.")
                med = 1
            else:
                print("I can't understand your command!")
    elif player["Heath"] == player_full_hp:
        print("You save it for later.")
        med = 1
if player["Heath"] > 0:
    enter()
    if destination == 0:
        print("It's currently noon, the weather is hot as fuck.")
        enter()
        print("You take a rest in an abandoned building.")
        enter()
        building_loot = ["M4A4", "Colt Python", "Remington Spartan 310"]
        print("After looking around building a bit, you found a", building_loot[randint(0, 2)])
        player["Long range Damage"] += 23
    elif destination == 1:
        if companions == 1:
            print("We're about 500 meters away from Wastie. Let's rest here,", player["Name"])
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
            zombie = {
                "Name": "Zombie",
                "Lvl": player["Lvl"],
                "Heath": player["Heath"],
                "Armor": 1,
                "Melee Damage": 15,
                "Speed": randint(3, 6),
                "Luck": 5,
            }
            opt_loop = 1
            while opt_loop == 1:
                cmd = input("What do you want to do? (Fight or Run) ")
                if cmd == "Fight":
                    opt_loop = 0
                    print("Enemy Name:", zombie["Name"])
                    print("Enemy Level:", zombie["Lvl"])
                    print("Enemy Health:", zombie["Heath"])
                    print("Enemy Armor:", zombie["Armor"])
                    print("Enemy Melee Damage:", zombie["Melee Damage"])
                    print("Enemy Speed:", zombie["Speed"])
                    print("Enemy Luck:", zombie["Luck"])
                    combat_seq = 1
                    while combat_seq == 1:
                        player_dmg = player["Melee Damage"] - zombie["Armor"]
                        zombie_dmg = zombie["Melee Damage"] - player["Armor"]
                        player_long_dmg = player["Long range Damage"] - zombie["Armor"]
                        if player["Heath"] > 0 and zombie["Heath"] > 0:
                            cmd = input("What do you want to do? (Long range Attack, Melee Attack, Dodge, Block or Heal) ")
                            if cmd == "melee attack" or cmd == "Melee Attack":
                                if player["Speed"] == zombie["Speed"]:
                                    print("Both of you bited each other at the same time.")
                                    player["Heath"] -= zombie_dmg
                                    zombie["Heath"] -= player_dmg
                                    print("Your Health:", player["Heath"])
                                    print("Enemy Heath:", zombie["Heath"])
                                elif player["Speed"] > zombie["Speed"]:
                                    print("You attacked the zombie!")
                                    zombie["Heath"] -= player_dmg
                                    if zombie["Heath"] > 0:
                                        print("Enemy bite you in the nuts!")
                                        player["Heath"] -= zombie_dmg
                                    print("Your Health:", player["Heath"])
                                    print("Enemy Heath:", zombie["Heath"])
                                elif player["Speed"] < zombie["Speed"]:
                                    print("Enemy bite you in the nuts!")
                                    player["Heath"] -= zombie_dmg
                                    if player["Heath"] > 0:
                                        print("You attacked the zombie!")
                                        zombie["Heath"] -= player_dmg
                                    print("Your Health:", player["Heath"])
                                    print("Enemy Heath:",zombie["Heath"])
                            elif cmd == "dodge" or cmd == "Dodge":
                                dodge_chance = randint(1, 100)
                                if dodge_chance % 2 == 0:
                                    print("You successfully dodged attack.")
                                    player["Heath"] += 20
                                    print("Your Health:", player["Heath"])
                                if dodge_chance % 2 == 1:
                                    print("You failed at dodging incoming attack.")
                                    player["Heath"] -= zombie_dmg
                                    print("Your Health:", player["Heath"])
                            elif cmd == "block" or cmd == "Block":
                                block_chance = randint(1, 100)
                                if block_chance % 2 == 0:
                                    print("You successfully blocked and paid back the enemy.")
                                    zombie["Heath"] -= player_dmg
                                    print("Enemy Heath:", zombie["Heath"])
                                if block_chance % 2 == 1:
                                    print("You can't block shit!")
                                    player["Heath"] -= zombie_dmg
                                    print("Your Health:", player["Heath"])
                            elif cmd == "Long range Attack" or cmd == "long range attack":
                                hit_chance = randint(1, 100)
                                if hit_chance > 50:
                                    print("You shot the zombie chest.")
                                    zombie["Heath"] -= player_long_dmg
                                    if zombie["Heath"] > 0:
                                        print("Enemy bite you in the nuts!")
                                        player["Heath"] -= zombie_dmg
                                    print("Your Health:", player["Heath"])
                                    print("Enemy Heath:", zombie["Heath"])
                                elif hit_chance <= 50:
                                    print("You missed the shot.")
                                    if zombie["Heath"] > 0:
                                        print("Enemy bite you in the nuts!")
                                        player["Heath"] -= zombie_dmg
                                    print("Your Health:", player["Heath"])
                            elif cmd == "heal" or cmd == "Heal":
                                if player["Heath"] < player_full_hp:
                                    if med == 1:
                                        player["Heath"] = player_full_hp
                                        print("Your Health:", player["Heath"])
                                        med -= 1
                                    elif med == 0:
                                        print("You don't have any [Medkit] left")
                                elif player["Heath"] == player_full_hp:
                                    print("Your heath are full!")
                            else:
                                print("I can't understand your command!")
                        elif player["Heath"] < 1:
                            print("You die!")
                            combat_seq = 0
                        elif zombie["Heath"] < 1:
                            print("You've defeated the enemy!")
                            enter()
                            combat_seq = 0
                            player["Lvl"] += randint(0, 1)
                elif cmd == "Run":
                    opt_loop = 0
                    if player["Speed"] > zombie["Speed"]:
                        print("You ran away from the zombie.")
                    else:
                        print("The zombie is too fast to escape!")
                        enter()
                        print("Enemy Name:", zombie["Name"])
                        print("Enemy Level:", zombie["Lvl"])
                        print("Enemy Health:", zombie["Heath"])
                        print("Enemy Armor:", zombie["Armor"])
                        print("Enemy Melee Damage:", zombie["Melee Damage"])
                        print("Enemy Speed:", zombie["Speed"])
                        print("Enemy Luck:", zombie["Luck"])
                        combat_seq = 1
                        while combat_seq == 1:
                            player_dmg = player["Melee Damage"] - zombie["Armor"]
                            zombie_dmg = zombie["Melee Damage"] - player["Armor"]
                            player_long_dmg = player["Long range Damage"] - zombie["Armor"]
                            if player["Heath"] > 0 and zombie["Heath"] > 0:
                                cmd = input("What do you want to do? (Long range Attack, Melee Attack, Dodge, Block or Heal) ")
                                if cmd == "melee attack" or cmd == "Melee Attack":
                                    if player["Speed"] == zombie["Speed"]:
                                        print("Both of you bited each other at the same time.")
                                        player["Heath"] -= zombie_dmg
                                        zombie["Heath"] -= player_dmg
                                        print("Your Health:", player["Heath"])
                                        print("Enemy Heath:", zombie["Heath"])
                                    elif player["Speed"] > zombie["Speed"]:
                                        print("You attacked the zombie!")
                                        zombie["Heath"] -= player_dmg
                                        if zombie["Heath"] > 0:
                                            print("Enemy bite you in the nuts!")
                                            player["Heath"] -= zombie_dmg
                                        print("Your Health:", player["Heath"])
                                        print("Enemy Heath:", zombie["Heath"])
                                    elif player["Speed"] < zombie["Speed"]:
                                        print("Enemy bite you in the nuts!")
                                        player["Heath"] -= zombie_dmg
                                        if player["Heath"] > 0:
                                            print("You attacked the zombie!")
                                            zombie["Heath"] -= player_dmg
                                        print("Your Health:", player["Heath"])
                                        print("Enemy Heath:", zombie["Heath"])
                                elif cmd == "dodge" or cmd == "Dodge":
                                    dodge_chance = randint(1, 100)
                                    if dodge_chance % 2 == 0:
                                        print("You successfully dodged attack.")
                                        player["Heath"] += 20
                                        print("Your Health:", player["Heath"])
                                    if dodge_chance % 2 == 1:
                                        print("You failed at dodging incoming attack.")
                                        player["Heath"] -= zombie_dmg
                                        print("Your Health:", player["Heath"])
                                elif cmd == "block" or cmd == "Block":
                                    block_chance = randint(1, 100)
                                    if block_chance % 2 == 0:
                                        print("You successfully blocked and paid back the enemy.")
                                        zombie["Heath"] -= player_dmg
                                        print("Enemy Heath:", zombie["Heath"])
                                    if block_chance % 2 == 1:
                                        print("You can't block shit!")
                                        player["Heath"] -= zombie_dmg
                                        print("Your Health:", player["Heath"])
                                elif cmd == "Long range Attack" or cmd == "long range attack":
                                    hit_chance = randint(1, 100)
                                    if hit_chance > 50:
                                        print("You shot the zombie chest.")
                                        zombie["Heath"] -= player_long_dmg
                                        if zombie["Heath"] > 0:
                                            print("Enemy bite you in the nuts!")
                                            player["Heath"] -= zombie_dmg
                                        print("Your Health:", player["Heath"])
                                        print("Enemy Heath:", zombie["Heath"])
                                    elif hit_chance <= 50:
                                        print("You missed the shot.")
                                        if zombie["Heath"] > 0:
                                            print("Enemy bite you in the nuts!")
                                            player["Heath"] -= zombie_dmg
                                        print("Your Health:", player["Heath"])
                                    elif cmd == "heal" or cmd == "Heal":
                                        if player["Heath"] < player_full_hp:
                                            if med == 1:
                                                player["Heath"] = player_full_hp
                                                print("Your Health:", player["Heath"])
                                                med -= 1
                                            elif med == 0:
                                                print("You don't have any [Medkit] left")
                                        elif player["Heath"] == player_full_hp:
                                            print("Your heath are full!")
                                else:
                                    print("I can't understand your command!")
                            elif player["Heath"] < 1:
                                print("You die!")
                                combat_seq = 0
                            elif zombie["Heath"] < 1:
                                print("You've defeated the enemy!")
                                enter()
                                combat_seq = 0
                                player["Lvl"] += randint(0, 1)
                else:
                    print("I can't understand your command!")
    elif destination == 2:
        encounter_list = ["Wolf", "Thieve", "Zombie"]
        encounter = encounter_list[randint(0, 2)]
        betrayal = {
            "Name": "Louis P. Connors",
            "Lvl": 1,
            "Heath": randint(50, 100 - player["Luck"]),
            "Armor": randint(1, 3),
            "Melee Damage": randint(6, 13),
            "Long range Damage": 0,
            "Speed": randint(1, 5),
            "Luck": 3
        }
        wolf = {
            "Name": "Wolf",
            "Lvl": 1,
            "Heath": randint(90, 120),
            "Armor": 1,
            "Melee Damage": 8,
            "Speed": 5,
            "Luck": 2,
        }
        zombie = {
            "Name": "Zombie",
            "Lvl": player["Lvl"],
            "Heath": player["Heath"],
            "Armor": 1,
            "Melee Damage": 15,
            "Speed": randint(3, 6),
            "Luck": 5,
        }
        print("Only about 100 meters away from Havani, you encountered a", encounter)
        enter()
        print("You're too tired to run away, so you must fight.")
        if encounter == "Wolf":
            combat_seq = 1
            while combat_seq == 1:
                player_dmg = player["Melee Damage"] - wolf["Armor"]
                wolf_dmg = wolf["Melee Damage"] - player["Armor"]
                player_long_dmg = player["Long range Damage"] - wolf["Armor"]
                if player["Heath"] > 0 and wolf["Heath"] > 0:
                    cmd = input("What do you want to do? (Long range Attack, Melee Attack, Dodge, Block or Heal) ")
                    if cmd == "melee attack" or cmd == "Melee Attack":
                        if player["Speed"] == wolf["Speed"]:
                            print("Both of you bited each other at the same time.")
                            player["Heath"] -= wolf_dmg
                            wolf["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", wolf["Heath"])
                        elif player["Speed"] > wolf["Speed"]:
                            print("You bitch slapped the wolf!")
                            wolf["Heath"] -= player_dmg
                            if wolf["Heath"] > 0:
                                print("Enemy bite you in the nuts!")
                                player["Heath"] -= wolf_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", wolf["Heath"])
                        elif player["Speed"] < wolf["Speed"]:
                            print("Enemy bite you in the nuts!")
                            player["Heath"] -= wolf_dmg
                            if player["Heath"] > 0:
                                print("You bitch slapped the wolf!")
                                wolf["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", wolf["Heath"])
                    elif cmd == "dodge" or cmd == "Dodge":
                        dodge_chance = randint(1, 100)
                        if dodge_chance % 2 == 0:
                            print("You successfully dodged attack.")
                            player["Heath"] += 20
                            print("Your Health:", player["Heath"])
                        if dodge_chance % 2 == 1:
                            print("You failed at dodging incoming attack.")
                            player["Heath"] -= wolf_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "block" or cmd == "Block":
                        block_chance = randint(1, 100)
                        if block_chance % 2 == 0:
                            print("You successfully blocked and paid back the enemy.")
                            wolf["Heath"] -= player_dmg
                            print("Enemy Heath:", wolf["Heath"])
                        if block_chance % 2 == 1:
                            print("You can't block shit!")
                            player["Heath"] -= wolf_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "Long range Attack" or cmd == "long range attack":
                        hit_chance = randint(1, 100)
                        if hit_chance > 50:
                            print("You shot the the wolfy ass!.")
                            wolf["Heath"] -= player_long_dmg
                            if wolf["Heath"] > 0:
                                print("Enemy bite you in the nuts!")
                                player["Heath"] -= wolf_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", wolf["Heath"])
                        elif hit_chance <= 50:
                            print("You missed the shot.")
                            print("Enemy bite you in the nuts!")
                            player["Heath"] -= wolf_dmg
                            print("Your Health:", player["Heath"])
                        elif cmd == "heal" or cmd == "Heal":
                            if player["Heath"] < player_full_hp:
                                if med == 1:
                                    player["Heath"] = player_full_hp
                                    print("Your Health:", player["Heath"])
                                    med -= 1
                                elif med == 0:
                                    print("You don't have any [Medkit] left")
                            elif player["Heath"] == player_full_hp:
                                print("Your heath are full!")
                    else:
                        print("I can't understand your command!")
                elif player["Heath"] < 1:
                    print("You die!")
                    combat_seq = 0
                elif wolf["Heath"] < 1:
                    print("You've defeated the enemy!")
                    combat_seq = 0
        elif encounter == "Thieve":
            combat_seq = 1
            while combat_seq == 1:
                player_dmg = player["Melee Damage"] - betrayal["Armor"]
                betrayal_dmg = betrayal["Melee Damage"] - player["Armor"]
                player_long_dmg = player["Long range Damage"] - betrayal["Armor"]
                if player["Heath"] > 0 and betrayal["Heath"] > 0:
                    cmd = input("What do you want to do? (Long range Attack, Melee Attack, Dodge, Block or Heal) ")
                    if cmd == "melee attack" or cmd == "Melee Attack":
                        if player["Speed"] == betrayal["Speed"]:
                            print("Both of you punched each other at the same time.")
                            player["Heath"] -= betrayal_dmg
                            betrayal["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", betrayal["Heath"])
                        elif player["Speed"] > betrayal["Speed"]:
                            print("You punched him in the face!")
                            betrayal["Heath"] -= player_dmg
                            if betrayal["Heath"] > 0:
                                print("Enemy kicked you in the ass!")
                                player["Heath"] -= betrayal_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", betrayal["Heath"])
                        elif player["Speed"] < betrayal["Speed"]:
                            print("Enemy kicked you in the ass!")
                            player["Heath"] -= betrayal_dmg
                            if player["Heath"] > 0:
                                print("You punched him in the face!")
                                betrayal["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", betrayal["Heath"])
                    elif cmd == "dodge" or cmd == "Dodge":
                        dodge_chance = randint(1, 100)
                        if dodge_chance % 2 == 0:
                            print("You successfully dodged attack.")
                            player["Heath"] += 20
                            print("Your Health:", player["Heath"])
                        if dodge_chance % 2 == 1:
                            print("You failed at dodging incoming attack.")
                            player["Heath"] -= betrayal_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "block" or cmd == "Block":
                        block_chance = randint(1, 100)
                        if block_chance % 2 == 0:
                            print("You successfully blocked and paid back the enemy.")
                            betrayal["Heath"] -= player_dmg
                            print("Enemy Heath:", betrayal["Heath"])
                        if block_chance % 2 == 1:
                            print("You can't block shit!")
                            player["Heath"] -= betrayal_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "Long range Attack" or cmd == "long range attack":
                        hit_chance = randint(1, 100)
                        if hit_chance > 50:
                            print("You shot the enemy dick.")
                            betrayal["Heath"] -= player_long_dmg
                            if betrayal["Heath"] > 0:
                                print("Enemy kicked you in the ass!")
                                player["Heath"] -= betrayal_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", betrayal["Heath"])
                        elif hit_chance <= 50:
                            print("You missed the shot.")
                            print("Enemy kicked you in the ass!")
                            player["Heath"] -= betrayal_dmg
                            print("Your Health:", player["Heath"])
                        elif cmd == "heal" or cmd == "Heal":
                            if player["Heath"] < player_full_hp:
                                if med == 1:
                                    player["Heath"] = player_full_hp
                                    print("Your Health:", player["Heath"])
                                    med -= 1
                                elif med == 0:
                                    print("You don't have any [Medkit] left")
                            elif player["Heath"] == player_full_hp:
                                print("Your heath are full!")
                    else:
                        print("I can't understand your command!")
                elif player["Heath"] < 1:
                    print("You die!")
                    combat_seq = 0
                elif betrayal["Heath"] < 1:
                    print("You've defeated the enemy!")
                    combat_seq = 0
        elif encounter == "Zombie":
            combat_seq = 1
            while combat_seq == 1:
                player_dmg = player["Melee Damage"] - zombie["Armor"]
                zombie_dmg = zombie["Melee Damage"] - player["Armor"]
                player_long_dmg = player["Long range Damage"] - zombie["Armor"]
                if player["Heath"] > 0 and zombie["Heath"] > 0:
                    cmd = input("What do you want to do? (Long range Attack, Melee Attack, Dodge, Block or Heal) ")
                    if cmd == "melee attack" or cmd == "Melee Attack":
                        if player["Speed"] == zombie["Speed"]:
                            print("Both of you bited each other at the same time.")
                            player["Heath"] -= zombie_dmg
                            zombie["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", zombie["Heath"])
                        elif player["Speed"] > zombie["Speed"]:
                            print("You attacked the zombie!")
                            zombie["Heath"] -= player_dmg
                            if zombie["Heath"] > 0:
                                print("Enemy bite you in the nuts!")
                                player["Heath"] -= zombie_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", zombie["Heath"])
                        elif player["Speed"] < zombie["Speed"]:
                            print("Enemy bite you in the nuts!")
                            player["Heath"] -= zombie_dmg
                            if player["Heath"] > 0:
                                print("You attacked the zombie!")
                                zombie["Heath"] -= player_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", zombie["Heath"])
                    elif cmd == "dodge" or cmd == "Dodge":
                        dodge_chance = randint(1, 100)
                        if dodge_chance % 2 == 0:
                            print("You successfully dodged attack.")
                            player["Heath"] += 20
                            print("Your Health:", player["Heath"])
                        if dodge_chance % 2 == 1:
                            print("You failed at dodging incoming attack.")
                            player["Heath"] -= zombie_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "block" or cmd == "Block":
                        block_chance = randint(1, 100)
                        if block_chance % 2 == 0:
                            print("You successfully blocked and paid back the enemy.")
                            zombie["Heath"] -= player_dmg
                            print("Enemy Heath:", zombie["Heath"])
                        if block_chance % 2 == 1:
                            print("You can't block shit!")
                            player["Heath"] -= zombie_dmg
                            print("Your Health:", player["Heath"])
                    elif cmd == "Long range Attack" or cmd == "long range attack":
                        hit_chance = randint(1, 100)
                        if hit_chance > 50:
                            print("You shot the zombie chest.")
                            zombie["Heath"] -= player_long_dmg
                            if zombie["Heath"] > 0:
                                print("Enemy bite you in the nuts!")
                                player["Heath"] -= zombie_dmg
                            print("Your Health:", player["Heath"])
                            print("Enemy Heath:", zombie["Heath"])
                        elif hit_chance <= 50:
                            print("You missed the shot.")
                            print("Enemy bite you in the nuts!")
                            player["Heath"] -= zombie_dmg
                            print("Your Health:", player["Heath"])
                        elif cmd == "heal" or cmd == "Heal":
                            if player["Heath"] < player_full_hp:
                                if med == 1:
                                    player["Heath"] = player_full_hp
                                    print("Your Health:", player["Heath"])
                                    med -= 1
                                elif med == 0:
                                    print("You don't have any [Medkit] left")
                            elif player["Heath"] == player_full_hp:
                                print("Your heath are full!")
                    else:
                        print("I can't understand your command!")
                elif player["Heath"] < 1:
                    print("You die!")
                    combat_seq = 0
                elif zombie["Heath"] < 1:
                    print("You've defeated the enemy!")
                    combat_seq = 0
if player["Heath"] > 0:
    print("To be continue>")
