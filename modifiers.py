
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
