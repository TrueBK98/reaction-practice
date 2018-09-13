from random import randint
from fallout_inventory import *


def critical_calc(target):
    has_crit = False
    crit_chance = randint(0, 100)
    if target["Luck"] > crit_chance:
        has_crit = True
    return has_crit


def combat(attacker, defender, max_hp, defender_hp, player_invent):
    if attacker["Health"] > 0 and defender["Health"] > 0:
        cmd = input("What do you want to do? (Melee, Shoot, Dodge, Block or Heal) ")
        cmd.lower()
        if cmd == "melee":
            melee(attacker, defender, max_hp, defender_hp, player_invent)
        elif cmd == "shoot":
            shoot(attacker, defender, max_hp, defender_hp, player_invent)
        elif cmd == "dodge":
            dodge(attacker, defender, max_hp, defender_hp, player_invent)
        elif cmd == "block":
            block(attacker, defender, max_hp, defender_hp, player_invent)
        elif cmd == "heal":
            heal(attacker, defender, max_hp, defender_hp, player_invent)
        else:
            print("I couldn't understand your craps!")
            combat(attacker, defender, max_hp, defender_hp, player_invent)
    elif attacker["Health"] <= 0 or defender["Health"] <= 0:
        if attacker["Health"] > 0:
            print(attacker["Name"], "win!")
        else:
            print(attacker["Name"], "sucks dick!")
    defender["HP"] = defender_hp


def melee(attacker, defender, max_hp, defender_hp, player_invent):
    attacker_melee = attacker["Melee Damage"] - defender["Armor"]
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    if attacker["Speed"] == defender["Speed"]:
        print("Both of you attacked at the same time.")
        critical = critical_calc(attacker)
        if critical:
            print("Critical hit!")
            defender["Health"] -= attacker_melee * 1.5
        else:
            pass

        if attacker_melee > 0:
            defender["Health"] -= attacker_melee
        else:
            defender["Health"] -= abs(attacker_melee)

        if defender_melee > defender_long_range:
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_melee * 1.5
            else:
                pass
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_long_range * 1.5
            else:
                pass

            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    elif attacker["Speed"] > defender["Speed"]:
        print(attacker["Name"], "attacked", defender["Name"])
        critical = critical_calc(attacker)
        if critical:
            print("Critical hit!")
            defender["Health"] -= attacker_melee * 1.5
        else:
            pass

        if attacker_melee > 0:
            defender["Health"] -= attacker_melee
        else:
            defender["Health"] -= abs(attacker_melee)

        if defender["Health"] > 0:
            if defender_melee > defender_long_range:
                print(defender["Name"], "attacked", attacker["Name"])
                critical = critical_calc(defender)
                if critical:
                    print("Critical hit!")
                    attacker["Health"] -= defender_melee * 1.5
                else:
                    pass
                if defender_melee > 0:
                    attacker["Health"] -= defender_melee
                else:
                    attacker["Health"] -= abs(defender_melee)
            else:
                print(defender["Name"], "shot", attacker["Name"])
                critical = critical_calc(defender)
                if critical:
                    print("Critical hit!")
                    attacker["Health"] -= defender_long_range * 1.5
                else:
                    pass
                if defender_long_range > 0:
                    attacker["Health"] -= defender_long_range
                else:
                    attacker["Health"] -= abs(defender_long_range)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    elif attacker["Speed"] < defender["Speed"]:
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_melee * 1.5
            else:
                pass
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_long_range * 1.5
            else:
                pass
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_long_range * 1.5
            else:
                pass
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)

        if attacker["Health"] > 0:
            print(attacker["Name"], "attacked", defender["Name"])
            critical = critical_calc(attacker)
            if critical:
                print("Critical hit!")
                defender["Health"] -= attacker_melee * 1.5
            else:
                pass
            if attacker_melee > 0:
                defender["Health"] -= attacker_melee
            else:
                defender["Health"] -= abs(attacker_melee)
        print(attacker["Name"], "has", attacker["Health"], "HP left!")
        print(defender["Name"], "has", defender["Health"], "HP left!")
    combat(attacker, defender, max_hp, defender_hp, player_invent)


def shoot(attacker, defender, max_hp, defender_hp, player_invent):
    attacker_long_range = attacker["Long range Damage"] - defender["Armor"]
    defender_melee = defender["Melee Damage"] - attacker["Armor"]
    defender_long_range = defender["Long range Damage"] - attacker["Armor"]
    hit_chance = randint(1, 100)
    if hit_chance & 2 == 0:
        print(attacker["Name"], "shot", defender["Name"])
        critical = critical_calc(attacker)
        if critical:
            print("Critical hit!")
            defender["Health"] -= attacker_long_range * 1.5
        else:
            pass
        if attacker_long_range > 0:
            defender["Health"] -= attacker_long_range
        else:
            defender["Health"] -= abs(attacker_long_range)
    else:
        print(attacker["Name"], "missed the shot!")

    if defender["Health"] > 0:
        if defender_melee > defender_long_range:
            print(defender["Name"], "attacked", attacker["Name"])
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_melee * 1.5
            else:
                pass
            if defender_melee > 0:
                attacker["Health"] -= defender_melee
            else:
                attacker["Health"] -= abs(defender_melee)
        else:
            print(defender["Name"], "shot", attacker["Name"])
            critical = critical_calc(defender)
            if critical:
                print("Critical hit!")
                attacker["Health"] -= defender_long_range * 1.5
            else:
                pass
            if defender_long_range > 0:
                attacker["Health"] -= defender_long_range
            else:
                attacker["Health"] -= abs(defender_long_range)
    print(attacker["Name"], "has", attacker["Health"], "HP left!")
    print(defender["Name"], "has", defender["Health"], "HP left!")
    combat(attacker, defender, max_hp, defender_hp, player_invent)


def block(attacker, defender, max_hp, defender_hp, player_invent):
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
            print(attacker["Name"], "shot", defender["Name"])
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
    combat(attacker, defender, max_hp, defender_hp, player_invent)


def dodge(attacker, defender, max_hp, defender_hp, player_invent):
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
    combat(attacker, defender, max_hp, defender_hp, player_invent)


def heal(attacker, defender, max_hp, defender_hp, player_invent):
    if medkit in player_invent:
        print("You healed yourself")
        attacker["Health"] = max_hp
        player_invent.remove(medkit)
        print(attacker["Name"], "has", attacker["Health"], "HP left.")
    else:
        print("There aren't any medkit left.")
    combat(attacker, defender, max_hp, defender_hp, player_invent)
