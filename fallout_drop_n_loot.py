from random import randint
from fallout_inventory import *

betrayal_drop = [medkit, dirty_shoes, rusty_axe]
wolf_drop = [dirty_shoes, medkit, leather_helmet]
zombie_drop = [leather_armor, combat_knife, colt_1911, dirty_shoes, m4a4, medkit]
thieve_drop = [colt_1911, rusty_axe, medkit]


def drop(player_invent, enemy):
    loot_chance = randint(1, 20)
    if enemy["Name"] == "Betrayal":
        if loot_chance > len(betrayal_drop):
            pass
        else:
            print("Enemy dropped a", betrayal_drop[loot_chance - 1])
            player_invent = loot(player_invent, betrayal_drop[loot_chance - 1])

    elif enemy["Name"] == "Wolf":
        if loot_chance > len(wolf_drop):
            pass
        else:
            print("Enemy dropped a", wolf_drop[loot_chance - 1])
            player_invent = loot(player_invent, wolf_drop[loot_chance - 1])

    elif enemy["Name"] == "Zombie":
        if loot_chance > len(zombie_drop):
            pass
        else:
            print("Enemy dropped a", zombie_drop[loot_chance - 1])
            player_invent = loot(player_invent, zombie_drop[loot_chance - 1])

    elif enemy["Name"] == "Thieve":
        if loot_chance > len(thieve_drop):
            pass
        else:
            print("Enemy dropped a", thieve_drop[loot_chance - 1])
            player_invent = loot(player_invent, thieve_drop[loot_chance - 1])
    return player_invent


def loot(player_invent, item):
    cmd = input("Do you want to pick it up? (Yes or No) ")
    cmd.lower()
    if cmd == "yes":
        if len(player_invent) > 9:
            print("Your inventory are full!")
        else:
            print(item, "is added to your inventory.")
            player_invent.append(item)
    elif cmd == "no":
        pass
    else:
        print("I can't understand your shit!")
        loot(player_invent, item)
    return player_invent
