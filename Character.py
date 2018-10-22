from Race import *
from CharacterClass import *
import os
from modifiers import ability_modifiers, clearscreen, splashscreen
from pathlib import Path
import json
home = str(Path.home())


os.system('color F4')
splashscreen()
begin = (input("Press <ENTER> to Begin."))
clearscreen()
_race = Race()
# ----- MAIN PROGRAM -----------------
# Enter Character's Name
character_name = str(input(BColors.UNDERLINE + "Please Enter your character's name :"))
clearscreen()
valid = False
user_level = 0
while valid is not True:
    user_level = validate_choice(20, message="What level is {} (1-20): ".format(character_name))
    if 1 < user_level <= 20:
        valid = True
    else:
        valid = False
# List the main races available for the user and query for selection
print("What RACE is {}".format(character_name))
for key, value in list_races().items():
    print(key, value)
user_race = validate_choice(len(list_races().items()))


# the user picked Dwarf, clear the screen and display Dwarf sub-races, query for selection
if user_race == 3:
    clearscreen()
    print("Please Choose a Subrace.")
    for key, value in dwarf_races().items():
        print(key, value)
    user_race = validate_choice(len(dwarf_races().items()))
    if user_race == 1:
        _race = HillDwarf()
    else:
        _race = MountainDwarf()

# the user picked Elf, clear the screen and display elf sub-races, query for selection
elif user_race == 4:
    clearscreen()
    print("Please Choose a Subrace.")
    for key, value in elf_races().items():
        print(key, value)
    user_race = validate_choice(len(elf_races().items()))
    if user_race == 1:
        _race = HighElf()
    elif user_race == 2:
        _race = WoodElf()
    elif user_race == 3:
        _race = Eladrin()
    else:
        _race = DrowElf(user_level)

# the user picked Genasi, clear the screen and display genasi sub-races, query for selection
elif user_race == 5:
    clearscreen()
    print("Please Choose a Subrace.")
    for key, value in genasi_races().items():
        print(key, value)
    user_race = validate_choice(len(genasi_races().items()))
    if user_race == 1:
        _race = AirGenasi()
    elif user_race == 2:
        _race = EarthGenasi()
    elif user_race == 3:
        _race = FireGenasi()
    else:
        _race = WaterGenasi()

elif user_race == 6:
    clearscreen()
    print("Please Choose a Subrace.")
    for key, value in gnome_races().items():
        print(key, value)
    user_race = validate_choice(len(gnome_races().items()))
    if user_race == 1:
        _race = RockGnome()
    elif user_race == 2:
        _race = DeepGnome()


# the user picked Halfling, clear teh screen and display genasi sub-races, query for selection
elif user_race == 10:
    clearscreen()
    print("Please Choose a Subrace.")
    for key, value in halfling_races().items():
        print(key, value)
    user_race = validate_choice(len(halfling_races().items()))
    if user_race == 1:
        _race = LightfootHalfling()
    else:
        _race = StoutHalfling()

# the user pick a main race that does not have sub-races.  assign appropriate race to the _race variable.
else:
    if user_race == 1:
        _race = Aarakocra()
    elif user_race == 2:
        _race = Dragonborn(character_name)
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

# -------------BEGIN CLASS SELECTION --------------------
clearscreen()
print("What CLASS is {}?".format(character_name))

for key, value in classes_list().items():
    print(key, value)
_class = validate_choice(len(classes_list().items()))
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
        "classpath": user_class.classpath,
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
        character_data['Eldritch Invocation Spells'] = user_class.invocations

#     for key, value in character_data.items():
#         outputfile.write('%s:%s\n' % (key, value))
    for key, value in character_data.items():
        print(key.capitalize(), ":", value)

with open('data.json', 'w') as outfile:
    json.dump(character_data, outfile)