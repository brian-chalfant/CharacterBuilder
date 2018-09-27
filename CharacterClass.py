from DiceRoll import diceroll
from modifiers import levelup_ability_increase, barbarian_skill_list, full_skill_list, cleric_skill_list
from spells import bard_magic_selection, bard_slots


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
    def __init__(self, level):  # initiate
        super(Barbarian, self).__init__()
        self.name = 'Barbarian'  # class name
        self.hit_die = diceroll(1, 12)  # Hit die is 1d12
        self.primary_ability = "Strength"  # primary ability is Strength
        self.saves = ["Strength", "Constitution"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]  # Proficient in Simple and Martial Weapons
        self.toolpro = []

        print("pick two(2) skills from this list")
        for key, value in barbarian_skill_list().items():
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
            # Level 2 Add two Abilities, Reckless attack and Danger Sense
            self.abilities.append("RECKLESS ATTACK")
            self.abilities.append("DANGER SENSE")
        if level >= 3:
            # Level 3 Choose your class path, either Path of the Berzerker or Path of the Totem Warrior
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
        if level >= 4:  # First Stat Increase
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
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
        if level >= 8:  # Second Stat Increase
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
            if self.classpath == "Berzerker":
                self.abilities.append("INTIMIDATING PRESENCE")
            else:
                self.abilities.append("SPIRIT WALKER")
        if level >= 11:
            self.abilities.append("RELENTLESS RAGE")
        if level >= 12:  # Third Stat Increase
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
        if level >= 16:  # Fourth Stat Increase
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 18:
            self.abilities.append("INDOMITABLE MIGHT")
        if level >= 19:  # Fifth Stat Increase
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
        self.hit_die = diceroll(1, 8)  # Hit die is 1d8
        self.primary_ability = "Charisma"  # primary ability is Strength
        self.saves = ["Dexterity", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
        self.toolpro = []  # any three musical instruments
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"

        # assign equipment in here somewhere
        self.skill_list = full_skill_list()
        for key, value in self.skill_list.items():
            print(key, value)
        print("Please Choose 3 Skill Proficiencies:")
        skill_1 = int(input("Skill 1: "))
        skill_2 = int(input("Skill 2: "))
        skill_3 = int(input("Skill 3: "))
        if (skill_1 == 1) or (skill_2 == 1) or (skill_3 == 1):
            self.athletics_skill = True
            self.skill_list.pop(1)
        if (skill_1 == 2) or (skill_2 == 2) or (skill_3 == 2):
            self.acrobatics_skill = True
            self.skill_list.pop(2)
        if (skill_1 == 3) or (skill_2 == 3) or (skill_3 == 3):
            self.sleight_of_hand_skill = True
            self.skill_list.pop(3)
        if (skill_1 == 4) or (skill_2 == 4) or (skill_3 == 4):
            self.stealth_skill = True
            self.skill_list.pop(4)
        if (skill_1 == 5) or (skill_2 == 5) or (skill_3 == 5):
            self.arcana_skill = True
            self.skill_list.pop(5)
        if (skill_1 == 6) or (skill_2 == 6) or (skill_3 == 6):
            self.history_skill = True
            self.skill_list.pop(6)
        if (skill_1 == 7) or (skill_2 == 7) or (skill_3 == 7):
            self.investigation_skill = True
            self.skill_list.pop(7)
        if (skill_1 == 8) or (skill_2 == 8) or (skill_3 == 8):
            self.nature_skill = True
            self.skill_list.pop(8)
        if (skill_1 == 9) or (skill_2 == 9) or (skill_3 == 9):
            self.religion_skill = True
            self.skill_list.pop(9)
        if (skill_1 == 10) or (skill_2 == 10) or (skill_3 == 10):
            self.animal_handling_skill = True
            self.skill_list.pop(10)
        if (skill_1 == 11) or (skill_2 == 11) or (skill_3 == 11):
            self.insight_skill = True
            self.skill_list.pop(11)
        if (skill_1 == 12) or (skill_2 == 12) or (skill_3 == 12):
            self.medicine_skill = True
            self.skill_list.pop(12)
        if (skill_1 == 13) or (skill_2 == 13) or (skill_3 == 13):
            self.perception_skill = True
            self.skill_list.pop(13)
        if (skill_1 == 14) or (skill_2 == 14) or (skill_3 == 14):
            self.survival_skill = True
            self.skill_list.pop(14)
        if (skill_1 == 15) or (skill_2 == 15) or (skill_3 == 15):
            self.deception_skill = True
            self.skill_list.pop(15)
        if (skill_1 == 16) or (skill_2 == 16) or (skill_3 == 16):
            self.intimidation_skill = True
            self.skill_list.pop(16)
        if (skill_1 == 17) or (skill_2 == 17) or (skill_3 == 17):
            self.performance_skill = True
            self.skill_list.pop(17)
        if (skill_1 == 18) or (skill_2 == 18) or (skill_3 == 18):
            self.persuasion_skill = True
            self.skill_list.pop(18)
        # Start Level stuff

        if level >= 1:
            self.abilities.append("BARDIC INSPIRATION (1d6)")
        if level >= 2:
            self.abilities.append("JACK OF ALL TRADES")
            self.abilities.append("SONG OF REST (1d6)")
        if level >= 3:
            self.abilities.append("EXPERTISE")
            # Level 3 Choose your class path, either Path of the Berzerker or Path of the Totem Warrior
            print("you must now choose your Bard College, you have the following options: \n"
                  "1: College of Lore ('CUTTING WORDS', 'ADDITIONAL MAGICAL SECRETS', 'PEERLESS SKILL') \n"
                  "2: College of Valor ('BONUS PROFICIENCIES', 'COMBAT INSPIRATION', 'EXTRA ATTACK')")
            a = int(input("Choose your Path: "))
            if a == 1:
                self.classpath = "Lore"
                self.abilities.append("CUTTING WORDS")
                #  Bonus Proficiencies
                print(self.skill_list)
                print("Please Choose 3 Additional Skill Proficiencies:")
                skill_1 = int(input("Skill 1: "))
                skill_2 = int(input("Skill 2: "))
                skill_3 = int(input("Skill 3: "))
                if (skill_1 == 1) or (skill_2 == 1) or (skill_3 == 1):
                    self.athletics_skill = True
                    self.skill_list.pop(1)
                if (skill_1 == 2) or (skill_2 == 2) or (skill_3 == 2):
                    self.acrobatics_skill = True
                    self.skill_list.pop(2)
                if (skill_1 == 3) or (skill_2 == 3) or (skill_3 == 3):
                    self.sleight_of_hand_skill = True
                    self.skill_list.pop(3)
                if (skill_1 == 4) or (skill_2 == 4) or (skill_3 == 4):
                    self.stealth_skill = True
                    self.skill_list.pop(4)
                if (skill_1 == 5) or (skill_2 == 5) or (skill_3 == 5):
                    self.arcana_skill = True
                    self.skill_list.pop(5)
                if (skill_1 == 6) or (skill_2 == 6) or (skill_3 == 6):
                    self.history_skill = True
                    self.skill_list.pop(6)
                if (skill_1 == 7) or (skill_2 == 7) or (skill_3 == 7):
                    self.investigation_skill = True
                    self.skill_list.pop(7)
                if (skill_1 == 8) or (skill_2 == 8) or (skill_3 == 8):
                    self.nature_skill = True
                    self.skill_list.pop(8)
                if (skill_1 == 9) or (skill_2 == 9) or (skill_3 == 9):
                    self.religion_skill = True
                    self.skill_list.pop(9)
                if (skill_1 == 10) or (skill_2 == 10) or (skill_3 == 10):
                    self.animal_handling_skill = True
                    self.skill_list.pop(10)
                if (skill_1 == 11) or (skill_2 == 11) or (skill_3 == 11):
                    self.insight_skill = True
                    self.skill_list.pop(11)
                if (skill_1 == 12) or (skill_2 == 12) or (skill_3 == 12):
                    self.medicine_skill = True
                    self.skill_list.pop(12)
                if (skill_1 == 13) or (skill_2 == 13) or (skill_3 == 13):
                    self.perception_skill = True
                    self.skill_list.pop(13)
                if (skill_1 == 14) or (skill_2 == 14) or (skill_3 == 14):
                    self.survival_skill = True
                    self.skill_list.pop(14)
                if (skill_1 == 15) or (skill_2 == 15) or (skill_3 == 15):
                    self.deception_skill = True
                    self.skill_list.pop(15)
                if (skill_1 == 16) or (skill_2 == 16) or (skill_3 == 16):
                    self.intimidation_skill = True
                    self.skill_list.pop(16)
                if (skill_1 == 17) or (skill_2 == 17) or (skill_3 == 17):
                    self.performance_skill = True
                    self.skill_list.pop(17)
                if (skill_1 == 18) or (skill_2 == 18) or (skill_3 == 18):
                    self.persuasion_skill = True
                    self.skill_list.pop(18)
            else:
                self.classpath = "Valor"
                self.abilities.append("COMBAT INSPIRATION")
                self.armorpro.append("Medium Armor")
                self.armorpro.append("Shields")
                self.armorpro.append("Martial Weapons")
        if level >= 4:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 5:
            self.abilities.remove("BARDIC INSPIRATION (1d6)")
            self.abilities.append("BARDIC INSPIRATION (1d8)")
            self.abilities.append("FONT OF INSPIRATION")
        if level >= 6:
            self.abilities.append("COUNTERCHARM")
            if self.classpath == "Lore":
                self.abilities.append("********MORE SPELLS*********")
            else:
                self.abilities.append("EXTRA ATTACK")
        if level >= 8:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 9:
            self.abilities.remove("SONG OF REST (1d6)")
            self.abilities.append("SONG OF REST (1d8)")

        if level >= 10:
            self.abilities.remove("BARDIC INSPIRATION (1d8)")
            self.abilities.append("BARDIC INSPIRATION (1d10)")
            self.abilities.append("EXPERTISE 2")
            self.abilities.append("****MAGICAL SECRETS ****")
        if level >= 12:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 13:
            self.abilities.remove("SONG OF REST (1d8)")
            self.abilities.append("SONG OF REST (1d10)")
        if level >= 14:
            self.abilities.append("*****MAGICAL SECRETS 2*****")
            if self.classpath == "Lore":
                self.abilities.append("PEERLESS SKILL")
            else:
                self.abilities.append("BATTLE MAGIC")
        if level >= 15:
            self.abilities.remove("BARDIC INSPIRATION (1d10)")
            self.abilities.append("BARDIC INSPIRATION (1d12)")
        if level >= 16:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 17:
            self.abilities.remove("SONG OF REST (1d10)")
            self.abilities.append("SONG OF REST (1d12)")
        if level >= 18:
            self.abilities.append("*****MAGICAL SECRETS 3*****")
        if level >= 19:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 20:
            self.abilities.append("SUPERIOR INSPIRATION")
        self.spells = bard_magic_selection(bard_slots(level))


class Cleric(CharacterClass):
    def __init__(self, level):
        super(Cleric, self).__init__()
        self.name = 'Cleric'
        self.hit_die = diceroll(1, 8)  # Hit die is 1d8
        self.primary_ability = "Wisdom"  # primary ability is Strength
        self.saves = ["Wisdom", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons"]
        self.toolpro = []  # None
        self.spellcasting = True
        self.spellcasting_ability = "Wisdom"

        print("pick two(2) skills from this list")
        for key, value in cleric_skill_list().items():
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
