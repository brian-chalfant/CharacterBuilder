
def ability_modifiers(ability_score):
    modifiers = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5,
        21: 5,
        22: 6,
        23: 6,
        24: 7,
        25: 7,
        26: 8,
        27: 8,
        28: 9,
        29: 9,
        30: 10

    }
    if 1 <= ability_score <= 30:
        return modifiers.get(ability_score)


def exp(level):
    exp_points = {
        1: 0,
        2: 300,
        3: 900,
        4: 2700,
        5: 6500,
        6: 14000,
        7: 23000,
        8: 34000,
        9: 48000,
        10: 64000,
        11: 85000,
        12: 100000,
        13: 120000,
        14: 140000,
        15: 165000,
        16: 195000,
        17: 225000,
        18: 265000,
        19: 305000,
        20: 355000
    }
    return exp_points.get(level)


def proficiency(level):
    pro_bonus = {
        1: 2,
        2: 2,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 4,
        10: 4,
        11: 4,
        12: 4,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 6,
        18: 6,
        19: 6,
        20: 6
    }
    return pro_bonus.get(level)


def primary_abilities():

    primary_abilities_list = {
        1: "Strength",
        2: "Dexterity",
        3: "Constitution",
        4: "Intelligence",
        5: "Wisdom",
        6: "Charisma"
        }
    return primary_abilities_list


def levelup_ability_increase():
    strength_addition = 0
    dexterity_addition = 0
    constitution_addition = 0
    intelligence_addition = 0
    wisdom_addition = 0
    charisma_addition = 0
    print("You may increase one ability score by 2, or two ability scores by 1, which do you prefer \n"
          "1: One ability score by 2 \n"
          "2: Two ability scores by 1")
    a = int(input(": "))
    if a == 1:
        print(primary_abilities())
        b = int(input("Enter a number: "))
        if b == 1:
            strength_addition = 2
        if b == 2:
            dexterity_addition = 2
        if b == 3:
            constitution_addition = 2
        if b == 4:
            intelligence_addition = 2
        if b == 5:
            wisdom_addition = 2
        if b == 6:
            charisma_addition = 2
    elif a == 2:
        print(primary_abilities())  # Enter code to keep the user from entering the same number twice
        b = int(input("Enter the first number: "))
        c = int(input("Enter the second number: "))
        if (b == 1) or (c == 1):
            strength_addition = 1
        if (b == 2) or (c == 2):
            dexterity_addition = 1
        if (b == 3) or (c == 3):
            constitution_addition = 1
        if (b == 4) or (c == 4):
            intelligence_addition = 1
        if (b == 5) or (c == 5):
            wisdom_addition = 1
        if (b == 6) or (c == 6):
            charisma_addition = 1
    else:
        print("error")
    ability_dict = {
        1: strength_addition,
        2: dexterity_addition,
        3: constitution_addition,
        4: intelligence_addition,
        5: wisdom_addition,
        6: charisma_addition
        }
    return ability_dict


def draconic_lines():
    lines = {
        1: 'Black: Acid',
        2: 'Blue: Lightning',
        3: 'Brass: Fire',
        4: 'Bronze: Copper',
        5: 'Copper: Acid',
        6: 'Gold: Fire',
        7: 'Green: Poison',
        8: 'Red: Fire',
        9: 'Silver: Cold',
        10: 'White: Cold'
        }
    return lines


def metamagic():
    meta = {
        1: 'Careful Spell (Protect some creatures from spells full force)',
        2: 'Distant Spell (Double Range)',
        3: 'Empowered Spell (Damage Re-roll)',
        4: 'Extended Spell (Double Duration)',
        5: 'Heightened Spell (Saving Throw Disadvantage)',
        6: 'Quickened Spell (Bonus Action)',
        7: 'Subtle Spell (Remove Somatic or Verbal Components)',
        8: 'Twinned Spell (Target Two Creatures)',
    }
    return meta


def metamagic_names():
    meta = {
        1: 'Careful Spell',
        2: 'Distant Spell',
        3: 'Empowered Spell',
        4: 'Extended Spell',
        5: 'Heightened Spell',
        6: 'Quickened Spell',
        7: 'Subtle Spell',
        8: 'Twinned Spell',
    }
    return meta

def barbarian_skill_list():
    skill_list = {  # List options for Skill Proficiency
        1: "Animal Handling",
        2: "Athletics",
        3: "Intimidation",
        4: "Nature",
        5: "Perception",
        6: "Survival"
        }
    return skill_list


def cleric_skill_list():
    skill_list = {
        1: "History",
        2: "Insight",
        3: "Medicine",
        4: "Persuasion",
        5: "Religion"
    }
    return skill_list


def sorcerer_skill_list():
    skill_list = {
        1: 'Arcana',
        2: 'Deception',
        3: 'Insight',
        4: 'Intimidation',
        5: 'Persuasion',
        6: 'Religion'
        }
    return skill_list


def druid_skill_list():

    skill_list = {
        1: 'Arcana',
        2: 'Animal Handling',
        3: 'Insight',
        4: 'Medicine',
        5: 'Nature',
        6: 'Perception',
        7: 'Religion',
        8: 'Survival',
    }
    return skill_list


def fighter_skill_list():
    skill_list = {  # List options for Skill Proficiency
        1: "Acrobatics",
        2: "Animal Handling",
        3: "Athletics",
        4: "History",
        5: "Insight",
        6: "Intimidation",
        8: "Perception",
        9: "Survival"
        }
    return skill_list


def warlock_skill_list():
    skill_list = {  # List options for Skill Proficiency
        1: "History",
        2: "Intimidation",
        3: "Investigation",
        4: "Nature",
        5: "Religion",
        }
    return skill_list


def fighter_fighting_style():
    style_list = {
        1: "Archery ( +2 Bonus to Ranged Attacks)",
        2: "Defense ( +1 Bonus to AC)",
        3: "Dueling ( +2 Bonus to Damage)",
        4: "Great Weapon Fighting (Re-roll 1's and 2's)",
        5: "Protection ( Invoke Disadvantage on Attacks on players near you)",
        6: "Two-Weapon Fighting ( Add Ability Modifier to Damage for Second Weapon)",
        }
    return style_list


def ranger_fighting_style():
    style_list = {
        1: "Archery ( +2 Bonus to Ranged Attacks)",
        2: "Defense ( +1 Bonus to AC)",
        3: "Dueling ( +2 Bonus to Damage)",
        6: "Two-Weapon Fighting ( Add Ability Modifier to Damage for Second Weapon)",
        }
    return style_list


def full_skill_list():

    skill_list = {
        1: 'Athletics',
        2: 'Acrobatics',
        3: 'Sleight of Hand',
        4: 'Stealth',
        5: 'Arcana',
        6: 'History',
        7: 'Investigation',
        8: 'Nature',
        9: 'Religion',
        10: 'Animal Handling',
        11: 'Insight',
        12: 'Medicine',
        13: 'Perception',
        14: 'Survival',
        15: 'Deception',
        16: 'Intimidation',
        17: 'Performance',
        18: 'Persuasion'
        }
    return skill_list


def ranger_skill_list():
    skills = {
        1: 'Animal Handling',
        2: 'Athletics',
        3: 'Insight',
        4: 'Investigation',
        5: 'Nature',
        6: 'Perception',
        7: 'Stealth',
        8: 'Survival'
    }
    return skills


def rogue_skill_list():
    skills = {
        1: 'Acrobatics',
        2: 'Athletics',
        3: 'Deception',
        4: 'Insight',
        5: 'Intimidation',
        6: 'Investigation',
        7: 'Perception',
        8: 'Performance',
        9: 'Persuasion',
        10: 'Sleight of Hand',
        11: 'Stealth'
    }
    return skills


def divine_domains():

    domains = {
        1: "Knowledge Domain",
        2: "Life Domain",
        3: "Light Domain",
        4: "Nature Domain",
        5: "Tempest Domain",
        6: "Trickery Domain",
        7: "War Domain"
        }
    return domains


def druidic_lands():
    druidic_lands = {
        1: "Arctic",
        2: "Coast",
        3: "Desert",
        4: "Forest",
        5: "Grassland",
        6: "Mountain",
        7: "Swamp",
        8: "Underdark"
    }
    return druidic_lands

def circle_spells(land_type, level):
    if land_type == "Arctic":
        switcher = {
            3: ["Hold Person", "Spike Growth"],
            5: ["Sleet Storm", "Slow"],
            7: ["Freedom of Movement", "Ice Storm"],
            9: ["Commune with Nature", "Cone of Cold"]
        }
        return switcher.get(level)
    if land_type == "Coast":
        switcher = {
            3: ["Mirror Image", "Misty Step"],
            5: ["Water Breathing", "Water Walk"],
            7: ["Control Water", "Freedom of Movement"],
            9: ["Conjure Elemental", "Scrying"]
        }
        return switcher.get(level)
    if land_type == "Desert":
        switcher = {
            3: ["Blur", "Silence"],
            5: ["Create Food and Water", "Protection from Energy"],
            7: ["Blight", "Hallucinatory Terrain"],
            9: ["Insect Plague", "Wall of Stone"]
        }
        return switcher.get(level)
    if land_type == "Forest":
        switcher = {
            3: ["Barkskin", "Spider Climb"],
            5: ["Call Lightning", "Plant Growth"],
            7: ["Freedom of Movement", "Divination"],
            9: ["Commune with Nature", "Tree Stride"]
        }
        return switcher.get(level)
    if land_type == "Grassland":
        switcher = {
            3: ["Invisibility", "Pass without Trace"],
            5: ["Daylight", "Haste"],
            7: ["Divination", "Freedom of Movement"],
            9: ["Dream", "Insect Plague"]
        }
        return switcher.get(level)
    if land_type == "Mountain":
        switcher = {
            3: ["Spider Climb", "Spike Growth"],
            5: ["Lighting Bolt", "Meld into Stone"],
            7: ["Stone Shape", "Stone Skin"],
            9: ["Passwall", "Wall of Stone"]
        }
        return switcher.get(level)
    if land_type == "Swamp":
        switcher = {
            3: ["Darkness", "Melf\'s Acid Arrow"],
            5: ["Water Walk", "Stinking Cloud"],
            7: ["Freedom of Movement", "Locate Creature"],
            9: ["Insect Plague", "Scrying"]
        }
        return switcher.get(level)
    if land_type == "Underdark":
        switcher = {
            3: ["Spider Climb", "Web"],
            5: ["Gaseous Form", "Stinking Cloud"],
            7: ["Greater Invisibility", "Stone Shape"],
            9: ["Cloudkill", "Insect Plague"]
        }
        return switcher.get(level)


def enemy_types():
    _enemy_types = {
        1: 'Aberrations',
        2: 'Beasts',
        3: 'Celestials',
        4: 'Constructs',
        5: 'Dragons',
        6: 'Elementals',
        7: 'Fey',
        8: 'Fiends',
        9: 'Giants',
        10: 'Monstrosities',
        11: 'Oozes',
        12: 'Plants',
        13: 'Undead'
        }
    return _enemy_types

def enemy_languages():
    lang = {
        'Celestials': 'Celestial',
        'Dragons': 'Draconic',
        'Elementals': 'Primoridal',
        'Fey': 'Sylvan',
        'Giants': 'Giant',
        }
    return lang


def race_languages():
    lang = {
        'Aarakocra': 'Auran',
        'Dragonborn': 'Draconic',
        'Dwarf': 'Dwarven',
        'Elf': 'Elvish',
        'Genasi': 'Primordial',
        'Gnome': 'Gnomish',
        'Goliath': 'Giant',
        'Half-Elf': 'Elvish',
        'Half-Orc': 'Orc',
        'Halfling': 'Halfling',
        'Human': 'Common',
        'Tiefling': 'Infernal'
    }
    return lang

def list_races():
    races = {
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
    return races


def favored_enemy():
    print("FAVORED ENEMY Selection")
    print("Will you pick: \n 1: one enemy type \n 2: two races")
    selection = int(input(":"))
    rtn = []
    if selection == 1:
        for key, value in enemy_types().items():
            print(key, ": ", value)
        x = int(input("Choose One(1) enemy type"))
        fav_enemy = enemy_types().get(x)
        if fav_enemy in enemy_languages().keys():
            rtn.append([fav_enemy, enemy_languages().get(fav_enemy)])
        else:
            rtn.append([fav_enemy, None])
    if selection == 2:
        for key, value in list_races().items():
            print(key, ": ", value)
        x = int(input("Choose the first Race"))
        y = int(input("Choose the second Race"))
        race1 = list_races().get(x)
        race2 = list_races().get(y)
        if race1 in race_languages().keys():
            rtn.append([race1, race_languages().get(race1)])
        else:
            rtn.append(None)
        if race2 in race_languages().keys():
            rtn.append([race2, race_languages().get(race2)])
        else:
            rtn.append(None)
    return rtn

