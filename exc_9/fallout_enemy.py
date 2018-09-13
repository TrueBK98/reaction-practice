from random import randint
from fallout_stats import *
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
betrayal_max_hp = betrayal["Health"]

wolf = {
    "Name": "Wolf",
    "Lvl": 1,
    "Health": randint(90, 120),
    "Armor": 1,
    "Melee Damage": 8,
    "Long range Damage": 0,
    "Speed": 5,
    "Luck": 2,
}
wolf_full_hp = wolf["Health"]

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
zombie_full_hp = zombie["Health"]

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
thieve_full_hp = thieve["Health"]
