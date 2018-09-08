player = {
    "NAME": "ASS",
    "HP": 100,
    "ATK": 8,
    "DEF": 0,
}

orc = {
    "NAME": "PIGLET",
    "HP": 20,
    "ATK": 8,
    "DEF": 0,
}


def combat(attacker, defender):
    if attacker["HP"] > 0 and defender["HP"] > 0:
        print(attacker["NAME"], "is hitting", defender["NAME"] + "'s nuts!")
        damage = attacker["ATK"] - defender["DEF"]
        if damage > 0:
            defender["HP"] -= damage
            print(defender["NAME"], "lost", damage, "HP")
            print(defender["HP"])
        else:
            defender["HP"] -= abs(damage)
        combat(defender, attacker)
    elif attacker["HP"] <= 0 or defender["HP"] <= 0:
        if defender["HP"] <= 0:
            print(attacker["NAME"], "win!")
        elif attacker["HP"] <= 0:
            print(defender["NAME"], "win!")


combat(player, orc)