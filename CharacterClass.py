from DiceRoll import diceroll
from modifiers import levelup_ability_increase


class CharacterClass:
    def __init__(self):
        self.athletics_skill = False
        self.acrobatics_skill = False
        self.sleight_of_hand_skill = False
        self.stealth_skill = False
        self.arcana_skill = False
        self.history_skill = False
        self.investigation_skill = False
        self.nature_skill = False
        self.religion_skill = False
        self.animal_handling_skill = False
        self.insight_skill = False
        self.medicine_skill = False
        self.perception_skill = False
        self.survival_skill = False
        self.deception_skill = False
        self.intimidation_skill = False
        self.performance_skill = False
        self.persuasion_skill = False
        self.strength_addition = 0
        self.dexterity_addition = 0
        self.constitution_addition = 0
        self.intelligence_addition = 0
        self.wisdom_addition = 0
        self.charisma_addition = 0
        self.armor = 'None'
        self.speed_addition = 0
        self.abilities = []

    def get_athletics(self):
        return self.athletics_skill

    def get_acrobatics(self):
        return self.acrobatics_skill

    def get_sleight_of_hand(self):
        return self.sleight_of_hand_skill

    def get_stealth(self):
        return self.stealth_skill

    def get_arcana(self):
        return self.arcana_skill

    def get_history(self):
        return self.history_skill

    def get_investigation(self):
        return self.investigation_skill

    def get_nature(self):
        return self.nature_skill

    def get_religion(self):
        return self.religion_skill

    def get_animal_handling(self):
        return self.animal_handling_skill

    def get_insight(self):
        return self.insight_skill

    def get_medicine(self):
        return self.medicine_skill

    def get_perception(self):
        return self.perception_skill

    def get_survival(self):
        return self.survival_skill

    def get_deception(self):
        return self.deception_skill

    def get_intimidation(self):
        return self.intimidation_skill

    def get_performance(self):
        return self.performance_skill

    def get_persuasion(self):
        return self.persuasion_skill

    def get_abilities(self):
        return self.abilities

    def get_strength_addition(self):
        return self.strength_addition

    def get_dexterity_addition(self):
        return self.dexterity_addition

    def get_constitution_addition(self):
        return self.constitution_addition

    def get_intelligence_addition(self):
        return self.intelligence_addition

    def get_wisdom_addition(self):
        return self.wisdom_addition

    def get_charisma_addition(self):
        return self.wisdom_addition

    def get_speed_addition(self):
        return self.speed_addition


class Barbarian(CharacterClass):
    def __init__(self, level):
        super(Barbarian, self).__init__()
        self.name = 'Barbarian'
        self.hit_die = diceroll(1, 12)
        self.primary_ability = "Strength"
        self.saves = ["Strength", "Constitution"]
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]
        self.toolpro = []
        skill_list = {
            1: "Animal Handling",
            2: "Athletics",
            3: "Intimidation",
            4: "Nature",
            5: "Perception",
            6: "Survival"
        }
        print("pick two(2) skills from this list")
        for key, value in skill_list.items():
            print(key, value)
        s = input("Enter one number:")
        s = int(s)
        r = input("Enter the second number:")
        r = int(r)
        if (s == 1) or (r == 1):
            self.animal_handling_skill = True

        if (s == 2) or (r == 2):
            self.athletics_skill = True

        if (s == 3) or (r == 3):
            self.intimidation_skill = True

        if (s == 4) or (r == 4):
            self.nature_skill = True

        if (s == 5) or (r == 5):
            self.perception_skill = True

        if (s == 6) or (r == 6):
            self.survival_skill = True

        self.abilities = ["RAGE", "UNARMORED DEFENSE"]
        if level >= 2:
            self.abilities.append("RECKLESS ATTACK")
            self.abilities.append("DANGER SENSE")
        if level >= 3:
            print("you must now choose your primal path, you have the following options: \n"
                  "1: Path of the Berzerker ('FRENZY', 'MINDLESS RAGE', 'INTIMIDATING PRESENCE') \n"
                  "2: Path of the Totem Warrior ('TOTEM SPIRIT', 'ASPECT OF THE BEAST', 'SPIRIT WALKER')")
            a = int(input("Choose your Path: "))
            if a == 1:
                self.classpath = "Berzerker"
                self.abilities.append("FRENZY")
            else:
                self.classpath = "Totem"
                self.abilities.append("SPIRIT SEEKER")
        if level >= 4:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)

            # print("You may increase one ability score by 2, or two ability scores by 1, which do you prefer \n"
            #       "1: One ability score by 2 \n"
            #       "2: Two ability scores by 1")
            # a = input(": ")
            # if a == 1:
            #     print(primary_abilities())
            #     b = input("Enter a number: ")
            #     if b == 1:
            #         self.strength_addition += 2
            #     if b == 2:
            #         self.dexterity_addition += 2
            #     if b == 3:
            #         self.constitution_addition += 2
            #     if b == 4:
            #         self.intelligence_addition += 2
            #     if b == 5:
            #         self.wisdom_addition += 2
            #     if b == 6:
            #         self.charisma_addition += 2
            #     else:
            #         print("ERROR")
            # elif a == 2:
            #     print(primary_abilities()) # Enter code to keep the user from entering the same number twice
            #     b = int(input("Enter the first number: "))
            #     c = int(input("Enter the second number: "))
            #
            #     if (b == 1) or (c == 1):
            #         self.strength_addition += 1
            #     if (b == 2) or (c == 2):
            #         self.dexterity_addition += 1
            #     if (b == 3) or (c == 3):
            #         self.constitution_addition += 1
            #     if (b == 4) or (c == 4):
            #         self.intelligence_addition += 1
            #     if (b == 5) or (c == 5):
            #         self.wisdom_addition += 1
            #     if (b == 6) or (c == 6):
            #         self.charisma_addition += 1
            #     else:
            #         print("ERROR")
            # else:
            #     print("error")
        if level >= 5:
            self.abilities.append("EXTRA ATTACK")
            if self.armor != 'Heavy':
                self.speed_addition += 10
            else:
                pass
        if level >= 6:
            if self.classpath == "Berzerker":
                self.abilities.append("MINDLESS RAGE")
            else:
                self.abilities.append("ASPECT OF THE BEAST")
        if level >= 7:
            self.abilities.append("FERAL INSTINCT")
        if level >= 8:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 9:
            self.abilities.append("BRUTAL CRITICAL")
        if level >= 10:
            if self.classpath == "Berzerker" :
                self.abilities.append("INTIMIDATING PRESENCE")
            else:
                self.abilities.append("SPIRIT WALKER")
        if level >= 11:
            self.abilities.append("RELENTLESS RAGE")
        if level >= 12:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 16:
            if self.classpath == "Totem":
                self.abilities.append("TOTEMIC ATTUNEMENT")
        if level >= 15:
            self.abilities.append("PERSISTANT RAGE")
        if level >= 16:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 18:
            self.abilities.append("INDOMITABLE MIGHT")
        if level >= 19:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level == 20:
            self.strength_addition += 4
            self.constitution_addition += 4

    def get_classpath(self):
        return self.classpath


class Bard(CharacterClass):
    def __init__(self, level):
        super(Bard, self).__init__()
        self.name = 'Bard'


class Cleric(CharacterClass):
    def __init__(self, level):
        super(Cleric, self).__init__()
        self.name = 'Cleric'


class Druid(CharacterClass):
    def __init__(self, level):
        super(Druid, self).__init__()
        self.name = 'Druid'


class Fighter(CharacterClass):
    def __init__(self, level):
        super(Fighter, self).__init__()
        self.name = 'Fighter'


class Monk(CharacterClass):
    def __init__(self, level):
        super(Monk, self).__init__()
        self.name = 'Monk'


class Paladin(CharacterClass):
    def __init__(self, level):
        super(Paladin, self).__init__()
        self.name = 'Paladin'


class Ranger(CharacterClass):
    def __init__(self, level):
        super(Ranger, self).__init__()
        self.name = 'Ranger'


class Rogue(CharacterClass):
    def __init__(self, level):
        super(Rogue, self).__init__()
        self.name = 'Rogue'


class Sorcerer(CharacterClass):
    def __init__(self, level):
        super(Sorcerer, self).__init__()
        self.name = 'Sorcerer'


class Warlock(CharacterClass):
    def __init__(self, level):
        super(Warlock, self).__init__()
        self.name = 'Warlock'


class Wizard(CharacterClass):
    def __init__(self, level):
        super(Wizard, self).__init__()
        self.name = 'Wizard'
