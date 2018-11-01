import json
import os
from pathlib import Path
from backgrounds import Background
from CharacterClass import *
from Race import *
from modifiers import ability_modifiers, clearscreen, splashscreen
from write_backgrounds import read_background_names, read_backgrounds

home = str(Path.home())


os.system('color F4')
splashscreen()
begin = (input("Press <ENTER> to Begin."))
clearscreen()


class Character:
    def __init__(self, Name, Level, Race, CharacterClass, Background):
        self.name = Name
        self.level = Level
        self.race = Race
        self.character_class = CharacterClass
        self.background = Background
        self.equipment = []
        self.sex = ''

# ----- MAIN PROGRAM -----------------
# Enter Character's Name

# ______
# | ___ \
# | |_/ /__ _  ___ ___
# |    // _` |/ __/ _ \
# | |\ \ (_| | (_|  __/
# \_| \_\__,_|\___\___|

# List the main races available for the user and query for selection


def race_selection(character_name, user_level):
    _race = Race()
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

    return _race

#  _____ _
# /  __ \ |
# | /  \/ | __ _ ___ ___
# | |   | |/ _` / __/ __|
# | \__/\ | (_| \__ \__ \
#  \____/_|\__,_|___/___/


def class_selection(character_name, user_level):
    clearscreen()
    print("What CLASS is {}?".format(character_name))
    
    for key, value in classes_list().items():
        print(key, value)
    _class = validate_choice(len(classes_list().items()))
    if _class == 1:
        _class = Barbarian(user_level, character_name)
    elif _class == 2:
        _class = Bard(user_level, character_name)
    elif _class == 3:
        _class = Cleric(user_level, character_name)
    elif _class == 4:
        _class = Druid(user_level, character_name)
    elif _class == 5:
        _class = Fighter(user_level, character_name)
    elif _class == 6:
        _class = Monk(user_level, character_name)
    elif _class == 7:
        _class = Paladin(user_level, character_name)
    elif _class == 8:
        _class = Ranger(user_level, character_name)
    elif _class == 9:
        _class = Rogue(user_level, character_name)
    elif _class == 10:
        _class = Sorcerer(user_level, character_name)
    elif _class == 11:
        _class = Warlock(user_level, character_name)
    elif _class == 12:
        _class = Wizard(user_level, character_name)
    return _class


# ______            _                                   _
# | ___ \          | |                                 | |
# | |_/ / __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |
# | ___ \/ _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |
# | |_/ / (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |
# \____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|
#                        __/ |
#                       |___/

def background_selection():
    for key, value in read_background_names().items():
        print(key, value)
    back_choice = validate_choice(len(read_background_names().items()), message='Choose a Background')
    print(read_background_names().get(back_choice))
    _background = Background(read_background_names().get(back_choice))
    return _background


def generate_character():
    valid = False
    while valid is not True:
        character_name = str(input(BColors.UNDERLINE + "Please Enter your character's name :"))
        if character_name.isalpha():
            valid = True
        else:
            print(BColors.FAIL + "Invalid Name")
            print(BColors.ENDC)
    clearscreen()
    valid = False
    while valid is not True:
        user_level = validate_choice(20, message="What level is {} (1-20): ".format(character_name))
        if 1 <= user_level <= 20:
            valid = True
        else:
            valid = False

    newcharacter = Character(character_name, user_level, race_selection(character_name, user_level),
                             class_selection(character_name, user_level), background_selection())
    print(newcharacter.race.name)
    
    with open(home + '\\desktop\\output.txt', 'w') as outputfile:
        character_data = {

            "name": newcharacter.name,
            "race": newcharacter.race.name,
            "level": newcharacter.level,
            "xp": exp(newcharacter.level),
            "class": newcharacter.character_class.name,
            "classpath": newcharacter.character_class.classpath,
            "speed": newcharacter.race.speed + newcharacter.character_class.get_speed_addition(),
            "strength": newcharacter.race.get_strength() +
            newcharacter.character_class.get_strength_addition(),
            "wisdom": newcharacter.race.get_wisdom() +
            newcharacter.character_class.get_wisdom_addition(),
            "dexterity": newcharacter.race.get_dexterity() +
            newcharacter.character_class.get_dexterity_addition(),
            "constitution": newcharacter.race.get_constitution() +
            newcharacter.character_class.get_constitution_addition(),
            "charisma": newcharacter.race.get_charisma() +
            newcharacter.character_class.get_charisma_addition(),
            "intelligence": newcharacter.race.get_intelligence() +
            newcharacter.character_class.get_intelligence_addition(),
            "strength_mod": ability_modifiers(newcharacter.race.get_strength() +
                                              newcharacter.character_class.get_strength_addition()),
            "wisdom_mod": ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition()),
            "dexterity_mod": ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition()),
            "constitution_mod": ability_modifiers(newcharacter.race.get_constitution() +
                                                  newcharacter.character_class.get_constitution_addition()),
            "charisma_mod": ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition()),
            "intelligence_mod": ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition()),
            "athletics_skill": newcharacter.character_class.athletics_skill,
            "acrobatics_skill": newcharacter.character_class.acrobatics_skill,
            "sleight_of_hand_skill": newcharacter.character_class.sleight_of_hand_skill,
            "stealth_skill": newcharacter.character_class.stealth_skill,
            "arcana_skill": newcharacter.character_class.arcana_skill,
            "history_skill": newcharacter.character_class.history_skill,
            "investigation_skill": newcharacter.character_class.investigation_skill,
            "nature_skill": newcharacter.character_class.nature_skill,
            "religion_skill": newcharacter.character_class.religion_skill,
            "animal_handling_skill": newcharacter.character_class.animal_handling_skill,
            "insight_skill": newcharacter.character_class.insight_skill,
            "medicine_skill": newcharacter.character_class.medicine_skill,
            "perception_skill": newcharacter.character_class.perception_skill,
            "survival_skill": newcharacter.character_class.survival_skill,
            "deception_skill": newcharacter.character_class.deception_skill,
            "intimidation_skill": newcharacter.character_class.intimidation_skill,
            "performance_skill": newcharacter.character_class.performance_skill,
            "persuasion_skill": newcharacter.character_class.persuasion_skill,
            "abilities": newcharacter.character_class.abilities + newcharacter.race.abilities,
            "languages": newcharacter.race.language + newcharacter.character_class.language,
            "spells": newcharacter.character_class.spells + newcharacter.race.cantrip,
            'armor_pro': newcharacter.character_class.armorpro,
            'weapon_pro': newcharacter.character_class.weaponpro

        }
        # Class Specific Entries
        print(newcharacter.character_class.name)
        if newcharacter.character_class.name == 'Warlock':
            character_data['Eldritch Invocation Spells'] = newcharacter.character_class.invocations

    #     for key, value in character_data.items():
    #         outputfile.write('%s:%s\n' % (key, value))
        for key, value in character_data.items():
            print(key.capitalize(), ":", value)

    with open(home + '..\data.json', 'w') as outfile:
        json.dump(character_data, outfile)


if __name__ == '__main__':
    generate_character()
