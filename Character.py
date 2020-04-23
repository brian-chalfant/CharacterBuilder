
from pathlib import Path

from CharacterClass import *
from Race import *
from backgrounds import Background
from build_sheet import build_sheet
from equipment import *
from looks import looks
from modifiers import ability_modifiers, splashscreen
from write_backgrounds import read_background_names

home = str(Path.home())

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
    
    # the user picked Halfling, clear the screen and display genasi sub-races, query for selection
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
    character_name = 'Default Name'  # Default
    user_level = 1   # Default
    valid = False
    while valid is not True:
        character_name = str(input("Please Enter your character's name :"))
        if valid_name(character_name):
            valid = True
        else:
            print("Invalid Name")
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
    # Passive Perception
    if newcharacter.character_class.perception_skill:
        passive_perc = 10 + proficiency(newcharacter.level) + \
                       ability_modifiers(newcharacter.race.get_wisdom() +
                                         newcharacter.character_class.get_wisdom_addition())
    else:
        passive_perc = 10 + ability_modifiers(newcharacter.race.get_wisdom() +
                                              newcharacter.character_class.get_wisdom_addition())
    # HP_MAX
    hpmax = newcharacter.character_class.hit_die + \
        (ability_modifiers(newcharacter.race.get_constitution() +
                           newcharacter.character_class.get_constitution_addition())) + \
        (diceroll(newcharacter.level, newcharacter.character_class.hit_die))
    # SAVING THROWS
    throws = saving_throws(newcharacter.character_class.saves)
    # PROFICIENCIES
    proficiencies = list(['ARMOR:'])
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

    newcharacter.equipment = starting_equipment(newcharacter.character_class.name, newcharacter.background.name,
                                                proficiencies)

    # Skill Transform
    def skill_transform(skill):
        if skill is False:
            skill = " "
        else:
            skill = "X"
        return skill

    newcharacter.character_class.athletics_skill = skill_transform(newcharacter.character_class.athletics_skill)
    newcharacter.character_class.acrobatics_skill = skill_transform(newcharacter.character_class.acrobatics_skill)
    newcharacter.character_class.sleight_of_hand_skill = \
        skill_transform(newcharacter.character_class.sleight_of_hand_skill)
    newcharacter.character_class.stealth_skill = skill_transform(newcharacter.character_class.stealth_skill)
    newcharacter.character_class.arcana_skill = skill_transform(newcharacter.character_class.arcana_skill)
    newcharacter.character_class.history_skill = skill_transform(newcharacter.character_class.history_skill)
    newcharacter.character_class.investigation_skill = skill_transform(newcharacter.character_class.investigation_skill)
    newcharacter.character_class.nature_skill = skill_transform(newcharacter.character_class.nature_skill)
    newcharacter.character_class.religion_skill = skill_transform(newcharacter.character_class.religion_skill)
    newcharacter.character_class.animal_handling_skill = \
        skill_transform(newcharacter.character_class.animal_handling_skill)
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
            weps = dict()
            weps['name'] = i
            weps['cost'] = simple_melee_weapons().get(i).get('Cost')
            weps['damage'] = simple_melee_weapons().get(i).get('Damage')
            weps['weight'] = simple_melee_weapons().get(i).get('Weight')
            weps['properties'] = simple_melee_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
        elif simple_ranged_weapons().get(i):
            weps = dict()
            weps['name'] = i
            weps['cost'] = simple_ranged_weapons().get(i).get('Cost')
            weps['damage'] = simple_ranged_weapons().get(i).get('Damage')
            weps['weight'] = simple_ranged_weapons().get(i).get('Weight')
            weps['properties'] = simple_ranged_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
        elif martial_melee_weapons().get(i):
            weps = dict()
            weps['name'] = i
            weps['cost'] = martial_melee_weapons().get(i).get('Cost')
            weps['damage'] = martial_melee_weapons().get(i).get('Damage')
            weps['weight'] = martial_melee_weapons().get(i).get('Weight')
            weps['properties'] = martial_melee_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
        elif martial_ranged_weapons().get(i):
            weps = dict()
            weps['name'] = i
            weps['cost'] = martial_ranged_weapons().get(i).get('Cost')
            weps['damage'] = martial_ranged_weapons().get(i).get('Damage')
            weps['weight'] = martial_ranged_weapons().get(i).get('Weight')
            weps['properties'] = martial_ranged_weapons().get(i).get('Properties')
            if in_sheath(i, newcharacter.weapons):
                pass
            else:
                newcharacter.weapons.append(weps)
        count += 1

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
            "wisdom_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                     newcharacter.character_class.get_wisdom_addition())),
            "dexterity_mod": "%+d" % (ability_modifiers(newcharacter.race.get_dexterity() +
                                                        newcharacter.character_class.get_dexterity_addition())),
            "constitution_mod": "%+d" % (ability_modifiers(newcharacter.race.get_constitution() +
                                                           newcharacter.character_class.get_constitution_addition())),
            "charisma_mod": "%+d" % (ability_modifiers(newcharacter.race.get_charisma() +
                                                       newcharacter.character_class.get_charisma_addition())),
            "intelligence_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                           newcharacter.character_class.get_intelligence_addition())),
            "athletics_skill": newcharacter.character_class.athletics_skill,
            "athletics_mod": "%+d" % (ability_modifiers(newcharacter.race.get_strength() +
                                                        newcharacter.character_class.get_strength_addition())),
            "acrobatics_skill": newcharacter.character_class.acrobatics_skill,
            "acrobatics_mod": "%+d" % (ability_modifiers(newcharacter.race.get_dexterity() +
                                                         newcharacter.character_class.get_dexterity_addition())),
            "sleight_of_hand_skill": newcharacter.character_class.sleight_of_hand_skill,
            "sleight_of_hand_mod": "%+d" % (ability_modifiers(newcharacter.race.get_dexterity() +
                                                              newcharacter.character_class.get_dexterity_addition())),
            "stealth_skill": newcharacter.character_class.stealth_skill,
            "stealth_mod": "%+d" % (ability_modifiers(newcharacter.race.get_dexterity() +
                                                      newcharacter.character_class.get_dexterity_addition())),
            "arcana_skill": newcharacter.character_class.arcana_skill,
            "arcana_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                     newcharacter.character_class.get_intelligence_addition())),
            "history_skill": newcharacter.character_class.history_skill,
            "history_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                      newcharacter.character_class.get_intelligence_addition())),
            "investigation_skill": newcharacter.character_class.investigation_skill,
            "investigation_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                            newcharacter.character_class.get_intelligence_addition())),
            "nature_skill": newcharacter.character_class.nature_skill,
            "nature_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                     newcharacter.character_class.get_intelligence_addition())),
            "religion_skill": newcharacter.character_class.religion_skill,
            "religion_mod": "%+d" % (ability_modifiers(newcharacter.race.get_intelligence() +
                                                       newcharacter.character_class.get_intelligence_addition())),
            "animal_handling_skill": newcharacter.character_class.animal_handling_skill,
            "animal_handling_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                              newcharacter.character_class.get_wisdom_addition())),
            "insight_skill": newcharacter.character_class.insight_skill,
            "insight_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                      newcharacter.character_class.get_wisdom_addition())),
            "medicine_skill": newcharacter.character_class.medicine_skill,
            "medicine_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                       newcharacter.character_class.get_wisdom_addition())),
            "perception_skill": newcharacter.character_class.perception_skill,
            "perception_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                         newcharacter.character_class.get_wisdom_addition())),
            "survival_skill": newcharacter.character_class.survival_skill,
            "survival_mod": "%+d" % (ability_modifiers(newcharacter.race.get_wisdom() +
                                                       newcharacter.character_class.get_wisdom_addition())),
            "deception_skill": newcharacter.character_class.deception_skill,
            "deception_mod": "%+d" % (ability_modifiers(newcharacter.race.get_charisma() +
                                                        newcharacter.character_class.get_charisma_addition())),
            "intimidation_skill": newcharacter.character_class.intimidation_skill,
            "intimidation_mod": "%+d" % (ability_modifiers(newcharacter.race.get_charisma() +
                                                           newcharacter.character_class.get_charisma_addition())),
            "performance_skill": newcharacter.character_class.performance_skill,
            "performance_mod": "%+d" % (ability_modifiers(newcharacter.race.get_charisma() +
                                                          newcharacter.character_class.get_charisma_addition())),
            "persuasion_skill": newcharacter.character_class.persuasion_skill,
            "persuasion_mod": "%+d" % (ability_modifiers(newcharacter.race.get_charisma() +
                                                         newcharacter.character_class.get_charisma_addition())),
            "passive_perception": passive_perc,
            "abilities": newcharacter.character_class.abilities + newcharacter.race.abilities,
            "languages": newcharacter.race.language + newcharacter.character_class.language,
            "spells": newcharacter.character_class.spells + newcharacter.race.cantrip,
            'armor_pro': newcharacter.character_class.armorpro,
            'weapon_pro': newcharacter.character_class.weaponpro + newcharacter.race.weaponpro,
            'proficiencies': proficiencies,
            'wealth': newcharacter.character_class.wealth,
            'equipment': newcharacter.equipment

        }
        count = 0
        for _ in newcharacter.weapons:
            character_data['wep'+str(count) + '_name'] = str(newcharacter.weapons[count].get('name'))
            character_data['wep' + str(count) + '_damage'] = str(
                newcharacter.weapons[count].get('damage') + damage_rolls_selector(
                    newcharacter.weapons[count].get('properties'),
                    "%+d" % (ability_modifiers(newcharacter.race.get_dexterity() +
                                               newcharacter.character_class.get_dexterity_addition())),
                    "% +d" % (ability_modifiers(newcharacter.race.get_strength() +
                                                newcharacter.character_class.get_strength_addition()))))
            character_data['wep' + str(count) + '_hit'] = "+" + str(
                ((ability_modifiers(newcharacter.race.get_strength() +
                                                              newcharacter.character_class.get_strength_addition())) +
                                                            proficiency(newcharacter.level)))
            character_data['wep'+str(count) + '_weight'] = str(newcharacter.weapons[count].get('weight'))
            character_data['wep'+str(count) + '_properties'] = str(newcharacter.weapons[count].get('properties'))
            count += 1

        # Class Specific Entries
        if newcharacter.character_class.name == 'Warlock':
            character_data['Eldritch Invocation Spells'] = newcharacter.character_class.invocations
        if newcharacter.character_class.name == 'Fighter':
            character_data['maneuver'] = newcharacter.character_class.maneuver
        if newcharacter.character_class.name == 'Monk':
            character_data['elemental_discipline'] = newcharacter.character_class.elemental_discipline

    # Print out Character Data for Debugging
    #     for key, value in character_data.items():
    #         print(key.capitalize(), ":", value)

    build_sheet(character_data)


def another():
    print("Generate Another Character?: ")
    a = input('Y/N: ')
    if a.lower() == ('y' or 'yes'):
        return True
    else:
        return False


if __name__ == '__main__':
    done = False
    while done is False:
        generate_character()
        print("Your Character Sheet is located in the 'characters' directory")
        x = another()
        if x is True:
            done = False
        else:
            done = True


