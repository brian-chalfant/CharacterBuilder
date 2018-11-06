import json
import os
from pathlib import Path
from backgrounds import Background
from CharacterClass import *
from Race import *
from build_sheet import build_sheet
from looks import looks
from modifiers import ability_modifiers, clearscreen, splashscreen
from write_backgrounds import read_background_names, read_backgrounds
from equipment import *

home = str(Path.home())


os.system('color F4')
splashscreen()
begin = (input("Press <ENTER> to Begin."))
clearscreen()


class Character:
    def __init__(self, name, level, race, characterclass, background):
        self.name = name
        self.level = level
        self.race = race
        self.character_class = characterclass
        self.background = background
        self.equipment = []
        self.weapons = []
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

    _race = looks(_race)

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
    print(newcharacter.character_class.name)
    # Passive Perception
    if newcharacter.character_class.perception_skill:
        passive_perc = 10 + proficiency(newcharacter.level) + ability_modifiers(newcharacter.race.get_wisdom() +
                            newcharacter.character_class.get_wisdom_addition())
    else:
        passive_perc = 10 + ability_modifiers(newcharacter.race.get_wisdom() +
                            newcharacter.character_class.get_wisdom_addition())
    # HP_MAX
    hpmax = newcharacter.character_class.hit_die + (ability_modifiers(newcharacter.race.get_constitution() + newcharacter.character_class.get_constitution_addition())) + (diceroll(newcharacter.level, newcharacter.character_class.hit_die))
    # SAVING THROWS
    throws = saving_throws(newcharacter.character_class.saves)
    # PROFICIENCIES
    proficiencies = []
    proficiencies.append('ARMOR:')
    for i in newcharacter.character_class.armorpro:
        proficiencies.append(("-" + i))
    proficiencies.append('WEAPONS:')
    for i in newcharacter.character_class.weaponpro:
        proficiencies.append(("-" + i))
    for i in newcharacter.race.weaponpro:
        proficiencies.append(("-" + i))
    proficiencies.append('TOOLS:')
    for i in newcharacter.character_class.toolpro:
        proficiencies.append(("-" + i))
    proficiencies.append('LANGUAGES:')
    for i in newcharacter.character_class.language:
        proficiencies.append(("-" + i))
    for i in newcharacter.race.language:
        proficiencies.append(("-" + i))
    if len(proficiencies) < 23:
        hm = 23 - len(proficiencies)
        for i in range(hm):
            proficiencies.append('')
    print(proficiencies)

    newcharacter.equipment = starting_equipment(newcharacter.character_class.name, newcharacter.background.name,
                                                proficiencies)

    #Skill Transform
    def skill_transform(skill):
        if skill is False:
            skill = " "
        else:
            skill = "X"
        return skill

    newcharacter.character_class.athletics_skill = skill_transform(newcharacter.character_class.athletics_skill)
    newcharacter.character_class.acrobatics_skill = skill_transform(newcharacter.character_class.acrobatics_skill)
    newcharacter.character_class.sleight_of_hand_skill = skill_transform(newcharacter.character_class.sleight_of_hand_skill)
    newcharacter.character_class.stealth_skill = skill_transform(newcharacter.character_class.stealth_skill)
    newcharacter.character_class.arcana_skill = skill_transform(newcharacter.character_class.arcana_skill)
    newcharacter.character_class.history_skill = skill_transform(newcharacter.character_class.history_skill)
    newcharacter.character_class.investigation_skill = skill_transform(newcharacter.character_class.investigation_skill)
    newcharacter.character_class.nature_skill = skill_transform(newcharacter.character_class.nature_skill)
    newcharacter.character_class.religion_skill = skill_transform(newcharacter.character_class.religion_skill)
    newcharacter.character_class.animal_handling_skill = skill_transform(newcharacter.character_class.animal_handling_skill)
    newcharacter.character_class.insight_skill = skill_transform(newcharacter.character_class.insight_skill)
    newcharacter.character_class.medicine_skill = skill_transform(newcharacter.character_class.medicine_skill)
    newcharacter.character_class.perception_skill = skill_transform(newcharacter.character_class.perception_skill)
    newcharacter.character_class.survival_skill = skill_transform(newcharacter.character_class.survival_skill)
    newcharacter.character_class.deception_skill = skill_transform(newcharacter.character_class.deception_skill)
    newcharacter.character_class.intimidation_skill = skill_transform(newcharacter.character_class.intimidation_skill)
    newcharacter.character_class.performance_skill = skill_transform(newcharacter.character_class.performance_skill)
    newcharacter.character_class.persuasion_skill = skill_transform(newcharacter.character_class.persuasion_skill)

    # WEAPONIZE

    count = 0
    for i in newcharacter.equipment:
        if simple_melee_weapons().get(i):
            weps = {}
            weps['name'] = i
            weps['cost'] = simple_melee_weapons().get(i).get('Cost')
            weps['damage'] = simple_melee_weapons().get(i).get('Damage')
            weps['weight'] = simple_melee_weapons().get(i).get('Weight')
            weps['properties'] = simple_melee_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
                print('newcharacter.weapons:')
                print(newcharacter.weapons)
                print(weps)
                print('<1weps')
        elif simple_ranged_weapons().get(i):
            weps = {}
            weps['name'] = i
            weps['cost'] = simple_ranged_weapons().get(i).get('Cost')
            weps['damage'] = simple_ranged_weapons().get(i).get('Damage')
            weps['weight'] = simple_ranged_weapons().get(i).get('Weight')
            weps['properties'] = simple_ranged_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
                print('newcharacter.weapons:')
                print(newcharacter.weapons)
                print(weps)
                print('<2weps')
        elif martial_melee_weapons().get(i):
            weps = {}
            weps['name'] = i
            weps['cost'] = martial_melee_weapons().get(i).get('Cost')
            weps['damage'] = martial_melee_weapons().get(i).get('Damage')
            weps['weight'] = martial_melee_weapons().get(i).get('Weight')
            weps['properties'] = martial_melee_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
                print('newcharacter.weapons:')
                print(newcharacter.weapons)
                print(weps)
                print('<3weps')
        elif martial_ranged_weapons().get(i):
            weps = {}
            weps['name'] = i
            weps['cost'] = martial_ranged_weapons().get(i).get('Cost')
            weps['damage'] = martial_ranged_weapons().get(i).get('Damage')
            weps['weight'] = martial_ranged_weapons().get(i).get('Weight')
            weps['properties'] = martial_ranged_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
                print('newcharacter.weapons:')
                print(newcharacter.weapons)
                print(weps)
                print('<4weps')
        count += 1
    with open(home + '\\desktop\\output.txt', 'w') as outputfile:
        character_data = {

            "name": newcharacter.name,
            "race": newcharacter.race.name,
            'age': newcharacter.race.age,
            'height': newcharacter.race.height,
            'weight': newcharacter.race.weight,
            'skin': newcharacter.race.skin,
            'hair': newcharacter.race.hair,
            'eyes': newcharacter.race.eyes,
            "level": newcharacter.level,
            "xp": exp(newcharacter.level),
            "klass": newcharacter.character_class.name,
            "background": newcharacter.background.name,
            'pers_trait1': "-" + newcharacter.background.personalitytraits[0],
            'pers_trait2': "-" + newcharacter.background.personalitytraits[1],
            'ideals': "-" + newcharacter.background.ideals[0],
            'bonds': "-" + newcharacter.background.bonds[0],
            'flaws': "-" + newcharacter.background.flaws[0],
            'alignment': newcharacter.background.alignment,
            "classpath": newcharacter.character_class.classpath,
            'ac': (ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition()) + 10),
            'initiative': ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition()),
            'starting_gp': str(newcharacter.character_class.wealth),
            "speed": newcharacter.race.speed + newcharacter.character_class.get_speed_addition(),
            'probonus': proficiency(newcharacter.level),
            "hp_maximum": hpmax,
            "hp_modifier": "+" + str(ability_modifiers(newcharacter.race.get_constitution() +
                                                  newcharacter.character_class.get_constitution_addition())),
            "hit_dice": "1d" + str(newcharacter.character_class.hit_die),
            "strength": newcharacter.race.get_strength() +
            newcharacter.character_class.get_strength_addition(),
            'str_save': throws.get('Strength'),
            "wisdom": newcharacter.race.get_wisdom() +
            newcharacter.character_class.get_wisdom_addition(),
            'wis_save': throws.get('Wisdom'),
            "dexterity": newcharacter.race.get_dexterity() +
            newcharacter.character_class.get_dexterity_addition(),
            'dex_save': throws.get('Dexterity'),
            "constitution": newcharacter.race.get_constitution() +
            newcharacter.character_class.get_constitution_addition(),
            'con_save': throws.get('Constitution'),
            "charisma": newcharacter.race.get_charisma() +
            newcharacter.character_class.get_charisma_addition(),
            'char_save': throws.get('Charisma'),
            "intelligence": newcharacter.race.get_intelligence() +
            newcharacter.character_class.get_intelligence_addition(),
            'int_save': throws.get('Intelligence'),
            "strength_mod": "%+d" % (ability_modifiers(newcharacter.race.get_strength() +
                                              newcharacter.character_class.get_strength_addition())),
            "wisdom_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "dexterity_mod": "%+d" %(ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition())),
            "constitution_mod": "%+d" %(ability_modifiers(newcharacter.race.get_constitution() +
                                                  newcharacter.character_class.get_constitution_addition())),
            "charisma_mod": "%+d" %(ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition())),
            "intelligence_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "athletics_skill": newcharacter.character_class.athletics_skill,
            "athletics_mod": "%+d" %(ability_modifiers(newcharacter.race.get_strength() +
                                              newcharacter.character_class.get_strength_addition())),
            "acrobatics_skill": newcharacter.character_class.acrobatics_skill,
            "acrobatics_mod": "%+d" %(ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition())),
            "sleight_of_hand_skill": newcharacter.character_class.sleight_of_hand_skill,
            "sleight_of_hand_mod": "%+d" %(ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition())),
            "stealth_skill": newcharacter.character_class.stealth_skill,
            "stealth_mod": "%+d" %(ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition())),
            "arcana_skill": newcharacter.character_class.arcana_skill,
            "arcana_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "history_skill": newcharacter.character_class.history_skill,
            "history_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "investigation_skill": newcharacter.character_class.investigation_skill,
            "investigation_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "nature_skill": newcharacter.character_class.nature_skill,
            "nature_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "religion_skill": newcharacter.character_class.religion_skill,
            "religion_mod": "%+d" %(ability_modifiers(newcharacter.race.get_intelligence() +
                                                  newcharacter.character_class.get_intelligence_addition())),
            "animal_handling_skill": newcharacter.character_class.animal_handling_skill,
            "animal_handling_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "insight_skill": newcharacter.character_class.insight_skill,
            "insight_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "medicine_skill": newcharacter.character_class.medicine_skill,
            "medicine_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "perception_skill": newcharacter.character_class.perception_skill,
            "perception_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "survival_skill": newcharacter.character_class.survival_skill,
            "survival_mod": "%+d" %(ability_modifiers(newcharacter.race.get_wisdom() +
                                            newcharacter.character_class.get_wisdom_addition())),
            "deception_skill": newcharacter.character_class.deception_skill,
            "deception_mod": "%+d" %(ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition())),
            "intimidation_skill": newcharacter.character_class.intimidation_skill,
            "intimidation_mod": "%+d" %(ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition())),
            "performance_skill": newcharacter.character_class.performance_skill,
            "performance_mod": "%+d" %(ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition())),
            "persuasion_skill": newcharacter.character_class.persuasion_skill,
            "persuasion_mod": "%+d" %(ability_modifiers(newcharacter.race.get_charisma() +
                                              newcharacter.character_class.get_charisma_addition())),
            "passive_perception": passive_perc,
            "abilities": newcharacter.character_class.abilities + newcharacter.race.abilities,
            "languages": newcharacter.race.language + newcharacter.character_class.language,
            "spells": newcharacter.character_class.spells + newcharacter.race.cantrip,
            'armor_pro': newcharacter.character_class.armorpro,
            'weapon_pro': newcharacter.character_class.weaponpro + newcharacter.race.weaponpro,
            'proficiencies': proficiencies,
            'wealth': newcharacter.character_class.wealth,

        }
        count = 0
        for i in newcharacter.weapons:
            print(newcharacter.weapons[count].get('name'))
            character_data['wep'+str(count) + '_name'] = str(newcharacter.weapons[count].get('name'))
            character_data['wep'+str(count) + '_damage'] = str(newcharacter.weapons[count].get('damage'))
            character_data['wep'+str(count) + '_hit'] = str(((ability_modifiers(newcharacter.race.get_strength() +
                                              newcharacter.character_class.get_strength_addition())) +
                                                        proficiency(newcharacter.level)))
            character_data['wep'+str(count) + '_weight'] = str(newcharacter.weapons[count].get('weight'))
            character_data['wep'+str(count) + '_properties'] = str(newcharacter.weapons[count].get('properties'))
            count += 1
        # 'prim_weap_name': 'Greataxe',
        #              'prim_weap_hit': '+5',
        #              'prim_weap_dmg': '1d12+3 Slashing',
        #              'prim_weap_properties': 'Martial, Heavy, Two-Handed',
        #              'prim_weap_weight': '3lbs',


        # build_sheet({'name': 'Salem',x
        #              'race': 'Half-Elf',x
        #              'klass': 'Wizard',x
        #              'background': 'Acolyte',x
        #              'alignment': 'Chaotic Neutral',x
        #              'level': '3',x
        #              'xp': '17000',x
        #              'ac': '12',x
        #              'initiative': '+1',x
        #              'speed': '25',x
        #              'probonus': '+3',x
        #              'passive_perception': '12',x
        #              'hp_maximum': '24',x
        #              'hp_modifier': '+4',x
        #              'hit_dice': '1d10',x
        #              'strength': 9,x
        #              'strength_mod': '+2',x
        #              'str_save': ' ',x
        #              'dexterity': 15,x
        #              'dexterity_mod': '+3',x
        #              'dex_save': ' ',x
        #              'constitution': 11,x
        #              'constitution_mod': '+1',x
        #              'con_save': ' ',x
        #              'intelligence': 11,x
        #              'intelligence_mod': '-1',x
        #              'int_save': 'X',x
        #              'wisdom': 10,x
        #              'wisdom_mod': '+2',x
        #              'wis_save': ' ',x
        #              'charisma': 12,x
        #              'charisma_mod': '+4',x
        #              'cha_save': 'X',
        #              'proficiencies': ['ARMOR:', '-Light Armor', '-Medium Armor', '-Shields', 'WEAPONS:',
        #                                '-Simple Weapons', '-Martial Weapons',
        #                                '-Crossbows', '-Daggers', 'TOOLS:', 'Artisan Tools', 'LANGUAGE:', '-Abyssal',
        #                                '-Orcish', '', '', '', '', '', '', '', ],x
        #              'acrobatics_skill': 'X',x
        #              'acrobatics_mod': '+3',x
        #              'animal_handling_skill': ' ',x
        #              'animal_handling_mod': '+2',x
        #              'arcana_skill': 'X',x
        #              'arcana_mod': '+3',x
        #              'athletics_skill': 'X',x
        #              'athletics_mod': '+3',x
        #              'deception_skill': ' ',x
        #              'deception_mod': '+3',x
        #              'history_skill': ' ',x
        #              'history_mod': '+3',x
        #              'insight_skill': 'X',x
        #              'insight_mod': '+3',x
        #              'intimidation_skill': 'X',x
        #              'intimidation_mod': '+3',x
        #              'investigation_skill': ' ',x
        #              'investigation_mod': '+1',x
        #              'medicine_skill': ' ',x
        #              'medicine_mod': '+1',x
        #              'nature_skill': ' ',x
        #              'nature_mod': '+1',x
        #              'perception_skill': ' ',x
        #              'perception_mod': '+1',x
        #              'performance_skill': 'X',x
        #              'performance_mod': '+4',x
        #              'persuasion_skill': ' ',x
        #              'persuasion_mod': '+2',x
        #              'religion_skill': ' ',x
        #              'religion_mod': '+2',x
        #              'sleight_of_hand_skill': ' ',x
        #              'sleight_of_hand_mod': '+2',x
        #              'stealth_skill': ' ',x
        #              'stealth_mod': '+2',x
        #              'survival_skill': ' ',x
        #              'survival_mod': '+2',x
        #              'currency_cp': 20,
        #              'currency_sp': 20,
        #              'currency_ep': 20,
        #              'currency_gp': 20,
        #              'currency_pp': 20,
        #              'prim_weap_name': 'Greataxe',
        #              'prim_weap_hit': '+5',
        #              'prim_weap_dmg': '1d12+3 Slashing',
        #              'prim_weap_properties': 'Martial, Heavy, Two-Handed',
        #              'prim_weap_weight': '3lbs',
        #              'second_weap_name': 'Handaxe',
        #              'second_weap_hit': '+5',
        #              'second_weap_dmg': '1d6+3 Slashing',
        #              'second_weap_properties': 'Light, Thrown, Range (20/60)',
        #              'second_weap_weight': '2lbs',
        #              'third_weap_name': 'Javelin',
        #              'third_weap_hit': '+5',
        #              'third_weap_dmg': '1d6+3 Piercing',
        #              'third_weap_properties': 'Thrown, Range (30/120)',
        #              'third_weap_weight': '8lbs',
        #              'fourth_weap_name': 'Unarmed Strike',
        #              'fourth_weap_hit': '+5',
        #              'fourth_weap_dmg': '4 Bludgeoning',
        #              'fourth_weap_properties': '',
        #              'fourth_weap_weight': '',
        #              'abilities': ['COMBAT WILD SHAPE', 'CIRCLE FORMS', 'PRIMAL STRIKE', 'WILD SHAPE (CR 1 OR BELOW)',
        #                            'ELEMENTAL WILD SHAPE', 'THOUSAND FORMS', 'TIMELESS BODY', 'BEAST SPELLS',
        #                            'DAMAGE RESISTANCE'],
        #              'spells': ['Acid Splash', 'Blade Ward', 'Chill Touch', 'Dancing Lights', 'Alarm', 'Burning Hands',
        #                         'Charm Person', 'Chromatic Orb', 'Alter Self', 'Arcane Lock', 'Blindness/Deafness',
        #                         'Animate Dead', 'Bestow Curse', 'Blink', 'Arcane Eye']
        #              })
        # Class Specific Entries
        print(newcharacter.character_class.name)
        if newcharacter.character_class.name == 'Warlock':
            character_data['Eldritch Invocation Spells'] = newcharacter.character_class.invocations

    #     for key, value in character_data.items():
    #         outputfile.write('%s:%s\n' % (key, value))
        for key, value in character_data.items():
            print(key.capitalize(), ":", value)

    with open('characters\\data.json', 'w') as outfile:
        json.dump(character_data, outfile)

    build_sheet(character_data)


if __name__ == '__main__':
    generate_character()
