from DiceRoll import diceroll


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
        print("user entered", r, s)
        if (s == 1) or (r == 1):
            self.animal_handling_skill = True
            print("Animal Handling", self.animal_handling_skill)
        if (s == 2) or (r == 2):
            self.athletics_skill = True
            print("Athletics", self.athletics_skill)
        if (s == 3) or (r == 3):
            self.intimidation_skill = True
            print("Intimidation", self.intimidation_skill)
        if (s == 4) or (r == 4):
            self.nature_skill = True
            print("Nature", self.nature_skill)
        if (s == 5) or (r == 5):
            self.perception_skill = True
            print("Perception", self.perception_skill)
        if (s == 6) or (r == 6):
            self.survival_skill = True
            print("Survival")
            print(self.survival_skill)

        self.skillpro = [skill_list.get(s), skill_list.get(r)]
        self.abilities = ["RAGE", "UNARMORED DEFENSE"]
        if level >= 2:
            self.abilities.append("RECKLESS ATTACK")
            self.abilities.append("DANGER SENSE")
        if level >= 3:
            self.abilities.append("PRIMAL PATH")
#        if self.level >= 4:


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
