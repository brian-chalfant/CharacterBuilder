from DiceRoll import diceroll


class CharacterClass:
    def __init__(self, level=None):
        if level is None:
            level = 1
        self.level = level


class Barbarian(CharacterClass):
    def __init__(self):
        super(Barbarian, self).__init__()
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
