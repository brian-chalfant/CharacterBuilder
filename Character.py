from Race import *
from CharacterClass import *
import os
# clear screen method


def clear():
    os.system('cls')


# list of races to display to the user
list_races = {
    1: "Aarokocra",
    2: "Dragonborn",
    3: "Dwarf",
    4: "Elf",
    5: "Genasi",
    6: "Gnome",
    7: "Goliath",
    8: "Half-Elf",
    9: "Half-Orc",
    10: "Halfling",
    11: "Human",
    12: "Tiefling"
}
# dwarf sub-races
dwarf_races = {
    1: "Hill Dwarf",
    2: "Mountain Dwarf"
}
# elf sub-races
elf_races = {
    1: "High Elf",
    2: "Wood Elf",
    3: "Eladrin",
    4: "Drow Elf"
}
# genasi sub-races
genasi_races = {
    1: "Air Genasi",
    2: "Earth Genasi",
    3: "Fire Genasi",
    4: "Water Genasi"
}
# halfling sub-races
halfling_races = {
    1: "Lightfoot Halfling",
    2: "Stout Halfling"
}

_race = Race()
# ----- MAIN PROGRAM -----------------
print("Welcome to Character Creator.")
# Enter Character's Name
character_name = str(input("Please Enter your character's name :"))
user_level = int(input("What level is your character? (1-20): "))
# List the main races available for the user and query for selection
print("Please Choose a Race.")
for key, value in list_races.items():
    print(key, value)
user_race = int(input("Enter a number:"))

# the user picked Dwarf, clear the screen and display Dwarf sub-races, query for selection
if user_race == 3:
    clear()
    print("Please Choose a Race.")
    for key, value in dwarf_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = HillDwarf()
    else:
        _race = MountainDwarf()

# the user picked Elf, clear the screen and display elf sub-races, query for selection
elif user_race == 4:
    clear()
    print("Please Choose a Race.")
    for key, value in elf_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = HighElf()
    elif user_race == 2:
        _race = WoodElf()
    elif user_race == 3:
        _race = Eladrin()
    else:
        _race = DrowElf()

# the user picked Genasi, clear the screen and display genasi sub-races, query for selection
elif user_race == 5:
    clear()
    print("Please Choose a Race.")
    for key, value in genasi_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = AirGenasi()
    elif user_race == 2:
        _race = EarthGenasi()
    elif user_race == 3:
        _race = FireGenasi()
    else:
        _race = WaterGenasi()

# the user picked Halfling, clear teh screen and display genasi sub-races, query for selection
elif user_race == 10:
    clear()
    print("Please Choose a Race.")
    for key, value in halfling_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = LightfootHalfling()
    else:
        _race = StoutHalfling()

# the user pick a main race that does not have sub-races.  assign appropriate race to the _race variable.
else:
    if user_race == 1:
        _race = Aarakocra()
    elif user_race == 2:
        _race = Dragonborn()
    elif user_race == 6:
        _race = Gnome()
    elif user_race == 7:
        _race = Goliath()
    elif user_race == 8:
        _race = HalfElf()
    elif user_race == 9:
        _race = HalfOrc()
    elif user_race == 11:
        _race = Human()
    elif user_race == 12:
        _race = Tiefling()
# This shouldn't happen.  if it does tell the user that there was a problem.
    else:
        print("Error, Please Try Again")


# -------------BEGIN CLASS SELECTION --------------------
clear()
print("What Class is", character_name + "?")

classes_list = {
    1: "Barbarian",
    2: "Bard",
    3: "Cleric",
    4: "Druid",
    5: "Fighter",
    6: "Monk",
    7: "Paladin",
    8: "Ranger",
    9: "Rogue",
    10: "Sorcerer",
    11: "Warlock",
    12: "Wizard"
}

for key, value in classes_list.items():
    print(key, value)
_class = int(input("Enter a number: "))
if _class == 1:
    _class = Barbarian()
elif _class == 2:
    _class = Bard()
elif _class == 3:
    _class = Cleric()
elif _class == 4:
    _class = Druid()
elif _class == 5:
    _class = Fighter()
elif _class == 6:
    _class = Monk()
elif _class == 7:
    _class = Paladin()
elif _class == 8:
    _class = Ranger()
elif _class == 9:
    _class = Rogue()
elif _class == 10:
    _class = Sorcerer()
elif _class == 11:
    _class = Warlock()
elif _class == 12:
    _class = Wizard()

user_race = _race
user_class = _class

character_data = {

    "name": character_name,
    "race": user_race.name,
    "level": user_level,
    "class": user_class.name,
    "strength": user_race.get_strength(),
    "wisdom": user_race.get_wisdom(),
    "dexterity": user_race.get_dexterity(),
    "constitution": user_race.get_constitution(),
    "charisma": user_race.get_charisma(),
    "intelligence": user_race.get_intelligence(),



}

print(character_data)
