from Race import *
from CharacterClass import *
import os
from modifiers import ability_modifiers
from pathlib import Path
import json

print('   __          ________ _      _____ ____  __  __ ______                            ')
print('   \ \        / /  ____| |    / ____/ __ \|  \/  |  ____|                           ')
print('    \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__                              ')
print('     \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|                             ')
print('      \  /\  /  | |____| |___| |___| |__| | |  | | |____                            ')
print('    ___\/__\/___|______|______\_____\____/|_|__|_|______| _____                     ')
print('   |__   __/ __ \  |__   __| |  | |  ____| |  __ \  ___  |  __ \                    ')
print('      | | | |  | |    | |  | |__| | |__    | |  | |( _ ) | |  | |                   ')
print('      | | | |  | |    | |  |  __  |  __|   | |  | |/ _ \/\ |  | |                   ')
print('      | | | |__| |    | |  | |  | | |____  | |__| | (_>  < |__| |                   ')
print('     _|_|_ \____/     |_|  |_|__|_|______| |_____/_\___/\/_____/ _____              ')
print('    / ____| |  | |   /\   |  __ \     /\   / ____|__   __|  ____|  __ \             ')
print('   | |    | |__| |  /  \  | |__) |   /  \ | |       | |  | |__  | |__) |            ')
print('   | |    |  __  | / /\ \ |  _  /   / /\ \| |       | |  |  __| |  _  /             ')
print('   | |____| |  | |/ ____ \| | \ \  / ____ \ |____   | |  | |____| | \ \             ')
print('    \_____|_|  |_/_/__ _\_\_| _\_\/_/____\_\_____|  |_|  |______|_|  \_\            ')
print('   |  _ \| |  | |_   _| |    |  __ \|  ____|  __ \                                  ')
print('   | |_) | |  | | | | | |    | |  | | |__  | |__) |                                 ')
print('   |  _ <| |  | | | | | |    | |  | |  __| |  _  /                                  ')
print('   | |_) | |__| |_| |_| |____| |__| | |____| | \ \                                  ')
print('   |____/ \____/|_____|______|_____/|______|_|  \_\___ ______ ______ ________     __')
print('   |  _ \         / ____| |  | |   /\   | |    |  ____|  ____|  ____|___  /\ \   / /')
print('   | |_) |_   _  | |    | |__| |  /  \  | |    | |__  | |__  | |__     / /  \ \_/ / ')
print('   |  _ <| | | | | |    |  __  | / /\ \ | |    |  __| |  __| |  __|   / /    \   /  ')
print('   | |_) | |_| | | |____| |  | |/ ____ \| |____| |    | |____| |____ / /__    | |   ')
print('   |____/ \__, |  \_____|_|  |_/_/    \_\______|_|    |______|______/_____|   |_|   ')
print('           __/ | ')


home = str(Path.home())
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
# gnome sub-races
gnome_races = {
    1: "Rock Gnome",
    2: "Deep Gnome"
    }

# halfling sub-races
halfling_races = {
    1: "Lightfoot Halfling",
    2: "Stout Halfling"
}

_race = Race()
# ----- MAIN PROGRAM -----------------
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
        _race = HillDwarf(user_level)
    else:
        _race = MountainDwarf(user_level)

# the user picked Elf, clear the screen and display elf sub-races, query for selection
elif user_race == 4:
    clear()
    print("Please Choose a Race.")
    for key, value in elf_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = HighElf(user_level)
    elif user_race == 2:
        _race = WoodElf(user_level)
    elif user_race == 3:
        _race = Eladrin(user_level)
    else:
        _race = DrowElf(user_level)

# the user picked Genasi, clear the screen and display genasi sub-races, query for selection
elif user_race == 5:
    clear()
    print("Please Choose a Race.")
    for key, value in genasi_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = AirGenasi(user_level)
    elif user_race == 2:
        _race = EarthGenasi(user_level)
    elif user_race == 3:
        _race = FireGenasi(user_level)
    else:
        _race = WaterGenasi(user_level)

elif user_race == 6:
    clear()
    print("Please Choose a Race.")
    for key, value in gnome_races.items():
        print(key, value)
    user_race = (int(input("Enter a number")))
    if user_race == 1:
        _race = RockGnome(user_level)
    elif user_race == 2:
        _race = DeepGnome(user_level)


# the user picked Halfling, clear teh screen and display genasi sub-races, query for selection
elif user_race == 10:
    clear()
    print("Please Choose a Race.")
    for key, value in halfling_races.items():
        print(key, value)
    user_race = (int(input("Enter a number:")))
    if user_race == 1:
        _race = LightfootHalfling(user_level)
    else:
        _race = StoutHalfling(user_level)

# the user pick a main race that does not have sub-races.  assign appropriate race to the _race variable.
else:
    if user_race == 1:
        _race = Aarakocra(user_level)
    elif user_race == 2:
        _race = Dragonborn(user_level)
    elif user_race == 7:
        _race = Goliath(user_level)
    elif user_race == 8:
        _race = HalfElf(user_level)
    elif user_race == 9:
        _race = HalfOrc(user_level)
    elif user_race == 11:
        _race = Human(user_level)
    elif user_race == 12:
        _race = Tiefling(user_level)
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
    _class = Barbarian(user_level)
elif _class == 2:
    _class = Bard(user_level)
elif _class == 3:
    _class = Cleric(user_level)
elif _class == 4:
    _class = Druid(user_level)
elif _class == 5:
    _class = Fighter(user_level)
elif _class == 6:
    _class = Monk(user_level)
elif _class == 7:
    _class = Paladin(user_level)
elif _class == 8:
    _class = Ranger(user_level)
elif _class == 9:
    _class = Rogue(user_level)
elif _class == 10:
    _class = Sorcerer(user_level)
elif _class == 11:
    _class = Warlock(user_level)
elif _class == 12:
    _class = Wizard(user_level)

user_race = _race
user_class = _class
with open(home + '\\desktop\\output.txt', 'w') as outputfile:
    character_data = {

        "name": character_name,
        "race": user_race.name,
        "level": user_level,
        "class": user_class.name,
        "speed": user_race.speed + user_class.get_speed_addition(),
        "strength": user_race.get_strength() + user_class.get_strength_addition(),
        "wisdom": user_race.get_wisdom() + user_class.get_wisdom_addition(),
        "dexterity": user_race.get_dexterity() + user_class.get_dexterity_addition(),
        "constitution": user_race.get_constitution() + user_class.get_constitution_addition(),
        "charisma": user_race.get_charisma() + user_class.get_charisma_addition(),
        "intelligence": user_race.get_intelligence() + user_class.get_intelligence_addition(),
        "strength_mod": ability_modifiers(user_race.get_strength() + user_class.get_strength_addition()),
        "wisdom_mod": ability_modifiers(user_race.get_wisdom() + user_class.get_wisdom_addition()),
        "dexterity_mod": ability_modifiers(user_race.get_dexterity() + user_class.get_dexterity_addition()),
        "constitution_mod": ability_modifiers(user_race.get_constitution() + user_class.get_constitution_addition()),
        "charisma_mod": ability_modifiers(user_race.get_charisma() + user_class.get_charisma_addition()),
        "intelligence_mod": ability_modifiers(user_race.get_intelligence() + user_class.get_intelligence_addition()),
        "athletics_skill": user_class.athletics_skill,
        "acrobatics_skill": user_class.acrobatics_skill,
        "sleight_of_hand_skill": user_class.sleight_of_hand_skill,
        "stealth_skill": user_class.stealth_skill,
        "arcana_skill": user_class.arcana_skill,
        "history_skill": user_class.history_skill,
        "investigation_skill": user_class.investigation_skill,
        "nature_skill": user_class.nature_skill,
        "religion_skill": user_class.religion_skill,
        "animal_handling_skill": user_class.animal_handling_skill,
        "insight_skill": user_class.insight_skill,
        "medicine_skill": user_class.medicine_skill,
        "perception_skill": user_class.perception_skill,
        "survival_skill": user_class.survival_skill,
        "deception_skill": user_class.deception_skill,
        "intimidation_skill": user_class.intimidation_skill,
        "performance_skill": user_class.performance_skill,
        "persuasion_skill": user_class.persuasion_skill,
        "abilities": user_class.abilities + user_race.abilities,
        "languages": user_race.language + user_class.language,
        "spells": user_class.spells + user_race.cantrip
    }
    # Class Specific Entries
    print(user_class.name)
    if user_class.name == 'Warlock':
        character_data['evocation'] = user_class.evocations

#     for key, value in character_data.items():
#         outputfile.write('%s:%s\n' % (key, value))
    for key, value in character_data.items():
        print(key.capitalize(), ":", value)

with open('data.json','w') as outfile:
    json.dump(character_data, outfile)