from DiceRoll import diceroll


class CharacterClass:
    def __init__(self, level=None):
        if level is None:
            level = 1
        self.level = level


class Barbarian(CharacterClass):
    def __init__(self):
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

        self.skillpro = [skill_list.get(s), skill_list.get(r)]
        self.abilities = ["RAGE", "UNARMORED DEFENSE"]
        if self.level >= 2:
            self.abilities.append("RECKLESS ATTACK")
            self.abilities.append("DANGER SENSE")
        if self.level >= 3:
            self.abilities.append("PRIMAL PATH")
#        if self.level >= 4:


class Bard(CharacterClass):
    def __init__(self):
        super(Bard, self).__init__()
        self.name = 'Bard'

class Cleric(CharacterClass):
    def __init__(self):
        super(Cleric, self).__init__()
        self.name = 'Cleric'
class Druid(CharacterClass):
    def __init__(self):
        super(Druid, self).__init__()
        self.name = 'Druid'
class Fighter(CharacterClass):
    def __init__(self):
        super(Fighter, self).__init__()
        self.name = 'Fighter'
class Monk(CharacterClass):
    def __init__(self):
        super(Monk, self).__init__()
        self.name = 'Monk'
class Paladin(CharacterClass):
    def __init__(self):
        super(Paladin, self).__init__()
        self.name = 'Paladin'
class Ranger(CharacterClass):
    def __init__(self):
        super(Ranger, self).__init__()
        self.name = 'Ranger'
class Rogue(CharacterClass):
    def __init__(self):
        super(Rogue, self).__init__()
        self.name = 'Rogue'
class Sorcerer(CharacterClass):
    def __init__(self):
        super(Sorcerer, self).__init__()
        self.name = 'Sorcerer'
class Warlock(CharacterClass):
    def __init__(self):
        super(Warlock, self).__init__()
        self.name = 'Warlock'
class Wizard(CharacterClass):
    def __init__(self):
        super(Wizard, self).__init__()
        self.name = 'Wizard'
