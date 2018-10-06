from DiceRoll import diceroll
from modifiers import *
from spells import spell_queue
from language import choose_language


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
        self.language = []
        self.spells = []

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
        self.language = []
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
        self.language = []
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
        self.spells = spell_queue("Bard", level)


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
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Wisdom"
        self.language = []

        print("pick two(2) skills from this list")
        for key, value in cleric_skill_list().items():
            print(key, value)
        s = input("Enter one number:")
        s = int(s)
        r = input("Enter the second number:")
        r = int(r)
        if (s == 1) or (r == 1):
            self.history_skill = True

        if (s == 2) or (r == 2):
            self.insight_skill = True

        if (s == 3) or (r == 3):
            self.medicine_skill = True

        if (s == 4) or (r == 4):
            self.persuasion_skill = True

        if (s == 5) or (r == 5):
            self.religion_skill = True
        # Start Level Stuff

        if level >= 1:
            print("Choose one of the following Divine Domains:")
            print(divine_domains())
            selection = int(input(": "))
            self.classpath = divine_domains().get(selection)
            self.magic = True

            if self.classpath == "Knowledge Domain":
                self.spells.append("Command")
                self.spells.append("Identify")
                self.language.append(choose_language())
                self.language.append(choose_language())
                knowledge_domain_skills = {1: "Arcana", 2: "History", 3: "Nature", 4: "Religion"}
                print("pick two(2) skills from this list")
                for key, value in knowledge_domain_skills.items():
                    print(key, value)
                s = input("Enter one number:")
                s = int(s)
                r = input("Enter the second number:")
                r = int(r)
                if (s == 1) or (r == 1):
                    self.arcana_skill = True

                if (s == 2) or (r == 2):
                    self.history_skill = True

                if (s == 3) or (r == 3):
                    self.nature_skill = True

                if (s == 4) or (r == 4):
                    self.religion_skill = True

            elif self.classpath == "Life Domain":
                self.spells.append("Bless")
                self.spells.append("Cure Wounds")
                self.armorpro.append("Heavy Armor")
                self.abilities.append("DISCIPLE OF LIFE")

            elif self.classpath == "Light Domain":
                self.spells.append("Burning Hands")
                self.spells.append("Faerie Fire")
                self.spells.append("Light")
                self.abilities.append("WARDING FLAME")

            elif self.classpath == "Nature Domain":
                self.spells.append("Animal Friendship")
                self.spells.append("Speak with Animals")
                self.spells.append("ONE DRUID CANTRIP")
                self.armorpro.append("Heavy Armor")

            elif self.classpath == "Tempest Domain":
                self.spells.append("Fog Cloud")
                self.spells.append("Thunderwave")
                self.armorpro.append("Heavy Armor")
                self.weaponpro.append("Martial Weapons")
                self.abilities.append("WRATH OF THE STORM")

            elif self.classpath == "Trickery Domain":
                self.spells.append("Charm Person")
                self.spells.append("Disguise Self")
                self.abilities.append("BLESSING OF THE TRICKSTER")

            elif self.classpath == "War Domain":
                self.spells.append("Divine Favor")
                self.spells.append("Shield of Faith")
                self.armorpro.append("Heavy Armor")
                self.weaponpro.append("Martial Weapons")
                self.abilities.append("WAR PRIEST")
        if level >= 2:
            self.abilities.append("CHANNEL DIVINITY 1/REST")
            if self.classpath == "Knowledge Domain":
                self.abilities.append("KNOWLEDGE OF THE AGES")
                self.spells.append("Augury")
                self.spells.append("Suggestion")

            elif self.classpath == "Life Domain":
                self.abilities.append("PRESERVE LIFE")
                self.spells.append("Lesser Restoration")
                self.spells.append("Spiritual Weapon")

            elif self.classpath == "Light Domain":
                self.abilities.append("RADIANCE OF THE DAWN")
                self.spells.append("Flaming Sphere")
                self.spells.append("Scorching Ray")

            elif self.classpath == "Nature Domain":
                self.abilities.append("CHARM ANIMALS AND PLANTS")
                self.spells.append("Barkskin")
                self.spells.append("Spike Growth")

            elif self.classpath == "Tempest Domain":
                self.abilities.append("DESTRUCTIVE WRATH")
                self.spells.append("Gust of Wind")
                self.spells.append("Shatter")

            elif self.classpath == "Trickery Domain":
                self.abilities.append("INVOKE DUPLICITY")
                self.spells.append("Mirror Image")
                self.spells.append("Pass Without Trace")

            elif self.classpath == "War Domain":
                self.abilities.append("GUIDED STRIKE")
                self.spells.append("Magic Weapon")
                self.spells.append("Spiritual Weapon")

        if level >= 4:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)

        if level >= 5:
            self.abilities.append("DESTROY UNDEAD 1/2")
            if self.classpath == "Knowledge Domain":
                self.spells.append("Nondetection")
                self.spells.append("Speak with Dead")

            elif self.classpath == "Life Domain":
                self.spells.append("Beacon of Hope")
                self.spells.append("Revivify")

            elif self.classpath == "Light Domain":
                self.spells.append("Daylight")
                self.spells.append("Fireball")

            elif self.classpath == "Nature Domain":
                self.spells.append("Plant Growth")
                self.spells.append("Wind Wall")

            elif self.classpath == "Tempest Domain":
                self.spells.append("Call Lightning")
                self.spells.append("Sleet Storm")

            elif self.classpath == "Trickery Domain":
                self.spells.append("Blink")
                self.spells.append("Dispel Magic")

            elif self.classpath == "War Domain":
                self.spells.append("Crusader\'s Mantle")
                self.spells.append("Spirit Guardian")

        if level >= 6:
            self.abilities.remove("CHANNEL DIVINITY 1/REST")
            self.abilities.append("CHANNEL DIVINITY 2/REST")
            if self.classpath == "Knowledge Domain":
                self.abilities.append("READ THOUGHTS")

            elif self.classpath == "Life Domain":
                self.abilities.append("BLESSED HEALER")

            elif self.classpath == "Light Domain":
                self.abilities.remove("WARDING FLAME")
                self.abilities.append("IMPROVED FLARE")

            elif self.classpath == "Nature Domain":
                self.abilities.append("DAMPEN ELEMENTS")

            elif self.classpath == "Tempest Domain":
                self.abilities.append("THUNDERBOLT STRIKE")

            elif self.classpath == "Trickery Domain":
                self.abilities.append("CLOAK OF SHADOWS")

            elif self.classpath == "War Domain":
                self.abilities.append("WAR GOD\'S BLESSING")

        if level >= 8:
            self.abilities.remove("DESTROY UNDEAD 1/2")
            self.abilities.append("DESTROY UNDEAD 1")

            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
            if self.classpath == "Knowledge Domain":
                self.abilities.append("POTENT SPELLCASTING")

            elif self.classpath == "Life Domain":
                self.abilities.append("DIVINE STRIKE")

            elif self.classpath == "Light Domain":
                self.abilities.append("POTENT SPELLCASTING")

            elif self.classpath == "Nature Domain":
                self.abilities.append("DIVINE STRIKE")

            elif self.classpath == "Tempest Domain":
                self.abilities.append("DIVINE STRIKE")

            elif self.classpath == "Trickery Domain":
                self.abilities.append("DIVINE STRIKE")

            elif self.classpath == "War Domain":
                self.abilities.append("DIVINE STRIKE")

        if level >= 10:
            self.abilities.append("DIVINE INTERVENTION")

        if level >= 11:
            self.abilities.remove("DESTROY UNDEAD 1")
            self.abilities.append("DESTROY UNDEAD 2")

        if level >= 12:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)

        if level >= 14:
            self.abilities.remove("DESTROY UNDEAD 2")
            self.abilities.append("DESTROY UNDEAD 3")

        if level >= 16:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)

        if level >= 17:
            self.abilities.remove("DESTROY UNDEAD 3")
            self.abilities.append("DESTROY UNDEAD 4")
            if self.classpath == "Knowledge Domain":
                self.abilities.append("VISIONS OF THE PAST")

            elif self.classpath == "Life Domain":
                self.abilities.append("SUPREME HEALING")

            elif self.classpath == "Light Domain":
                self.abilities.append("CORONA OF LIGHT")

            elif self.classpath == "Nature Domain":
                self.abilities.append("MASTER OF NATURE")

            elif self.classpath == "Tempest Domain":
                self.abilities.append("STORMBORN")

            elif self.classpath == "Trickery Domain":
                self.abilities.remove("INVOKE DUPLICITY")
                self.abilities.append("IMPROVED DUPLICITY")

            elif self.classpath == "War Domain":
                self.abilities.append("AVATAR OF BATTLE")
        if level >= 18:
            self.abilities.remove("CHANNEL DIVINITY 2/REST")
            self.abilities.append("CHANNEL DIVINITY 3/REST")

        if level >= 19:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)

        if level >= 20:
            self.abilities.remove("DIVINE INTERVENTION")
            self.abilities.append("IMPROVED DIVINE INTERVENTION")
        self.spells = spell_queue("Cleric", level)


class Druid(CharacterClass):
    def __init__(self, level):
        super(Druid, self).__init__()
        self.name = 'Druid'
        self.hit_die = diceroll(1, 8)  # Hit die is 1d8
        self.primary_ability = "Wisdom"  # primary ability is Strength
        self.saves = ["Intelligence", "Wisdom"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles",
                          "Slings", "Spears"]
        self.toolpro = ["Herbalism Kit"]
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Wisdom"
        self.language = ["Druidic"]
        print("Where did you become a druid")
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
        for key, value in druidic_lands.items():
            print(key, ": ", value)
        self.land_type = druidic_lands.pop(int(input("Enter a Number: ")))
        print("pick two(2) skills from this list")
        for key, value in druid_skill_list().items():
            print(key, value)
        s = input("Enter one number:")
        s = int(s)
        r = input("Enter the second number:")
        r = int(r)
        if (s == 1) or (r == 1):
            self.arcana_skill = True

        if (s == 2) or (r == 2):
            self.animal_handling_skill = True

        if (s == 3) or (r == 3):
            self.insight_skill = True

        if (s == 4) or (r == 4):
            self.medicine_skill = True

        if (s == 5) or (r == 5):
            self.nature_skill = True

        if (s == 6) or (r == 6):
            self.perception_skill = True

        if (s == 7) or (r == 7):
            self.religion_skill = True

        if (s == 8) or (r == 8):
            self.survival_skill = True

        if level >= 1:
            self.abilities.append("WILD SHAPE (1/4)")
        if level >= 2:
            print("you must now choose your Druid Circle, you have the following options: \n"
                  "1: Circle of the Land ('NATURAL RECOVERY', 'CIRCLE SPELLS', 'LANDS STRIDE') \n"
                  "2: Circle of the Moon ('COMBAT WILD SHAPE', 'CIRCLE FORMS', 'PRIMAL STRIKE')")
            a = int(input("Choose your Path: "))
            if a == 1:
                self.classpath = "Circle of the Land"
                self.abilities.append("BONUS CANTRIP")
            else:
                self.classpath = "Circle of the Moon"
                self.abilities.append("COMBAT WILD SHAPE")
                self.abilities.append("CIRCLE FORMS")
        if level >= 3:
            if self.classpath == "Circle of the Land":
                self.spells += circle_spells(self.land_type, 3)
        if level >= 4:
            self.abilities.remove("WILD SHAPE (1/4)")
            self.abilities.append("WILD SHAPE (1/2)")
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 6:
            if self.classpath == "Circle of the Land":
                self.abilities.append("LAND\'S STRIDE")
            else:
                self.abilities.append("PRIMAL STRIKE")
        if level >= 7:
            if self.classpath == "Circle of the Land":
                self.spells += circle_spells(self.land_type, 7)
        if level >= 8:
            self.abilities.remove("WILD SHAPE (1/2)")
            self.abilities.append("WILD SHAPE (1)")
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 9:
            if self.classpath == "Circle of the Land":
                self.spells += circle_spells(self.land_type, 9)
        if level >= 10:
            if self.classpath == "Circle of the Land":
                self.abilities.append("NATURE\'S WARD")
            else:
                self.abilities.append("ELEMENTAL WILD SHAPE")
        if level >= 12:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 14:
            if self.classpath == "Circle of the Land":
                self.abilities.append("NATURE\'S SANCTUARY")
            else:
                self.abilities.append("THOUSAND FORMS")
        if level >= 16:
            ability_dict = levelup_ability_increase()
            self.strength_addition += ability_dict.get(1)
            self.dexterity_addition += ability_dict.get(2)
            self.constitution_addition += ability_dict.get(3)
            self.intelligence_addition += ability_dict.get(4)
            self.wisdom_addition += ability_dict.get(5)
            self.charisma_addition += ability_dict.get(6)
        if level >= 18:
            self.abilities.append("TIMELESS BODY")
            self.abilities.append("BEAST SPELLS")
        if level >= 20:
            self.abilities.append("ARCHDRUID")
        self.spells = spell_queue("Druid", level)


class Fighter(CharacterClass):
    def __init__(self, level):
        super(Fighter, self).__init__()
        self.name = 'Fighter'
        self.hit_die = diceroll(1, 10)  # Hit die is 1d8
        self.primary_ability = "Strength"  # primary ability is Strength
        self.saves = ["Strength", "Constitution"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"]
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = False
        self.spellcasting_ability = "Wisdom"
        self.language = []
        if level >= 1:
            self.abilities.append("SECOND WIND")
            x = fighter_fighting_style()
            print("pick two(2) skills from this list")
            for key, value in fighter_skill_list().items():
                print(key, value)
            s = input("Enter one number:")
            s = int(s)
            r = input("Enter the second number:")
            r = int(r)
            if (s == 1) or (r == 1):
                self.acrobatics_skill = True

            if (s == 2) or (r == 2):
                self.animal_handling_skill = True

            if (s == 3) or (r == 3):
                self.athletics_skill = True

            if (s == 4) or (r == 4):
                self.history_skill = True

            if (s == 5) or (r == 5):
                self.insight_skill = True

            if (s == 6) or (r == 6):
                self.intimidation_skill = True

            if (s == 7) or (r == 7):
                self.perception_skill = True

            if (s == 8) or (r == 8):
                self.survival_skill = True

            for key, value in x.item():
                print(key, value)
            print("Pick a fighting style:")
            a = int(input(": "))
            self.fighting_style = x.pop(a)
        if level >= 2:
            self.abilities.append("ACTION SURGE")
        if level >= 3:
            print("you must now choose your Martial Archtype, you have the following options: \n"
                  "1: Champion ('IMPROVED CRITICAL', 'REMARKABLE ATHLETE', 'ADDITIONAL FIGHTING STYLE') \n"
                  "2: Battle Master ('COMBAT SUPERIORITY', 'STUDENT OF WAR', 'KNOW YOUR ENEMY') \n"
                  "3: Eldritch Knight ('SPELLCASTING', 'WEAPON BOND', 'WAR MAGIC')")
            a = int(input("Choose your Path: "))
            if a == 1:
                self.classpath = "Champion"
                self.abilities.append("IMPROVED CRITICAL")
            elif a == 2:
                self.classpath = "Battle Master"
                self.abilities.append("COMBAT SUPERIORITY")
                self.superiority_die = 4
                #  choose Maneuvers
            elif a == 3:
                self.classpath = "Eldritch Knight"


class Monk(CharacterClass):
    def __init__(self, level):
        super(Monk, self).__init__()
        self.name = 'Monk'
        if level > 1:
            self.abilities.append("")


class Paladin(CharacterClass):
    def __init__(self, level):
        super(Paladin, self).__init__()
        self.name = 'Paladin'
        if level > 1:
            self.abilities.append("")


class Ranger(CharacterClass):
    def __init__(self, level):
        super(Ranger, self).__init__()
        self.name = 'Ranger'
        if level > 1:
            self.abilities.append("")


class Rogue(CharacterClass):
    def __init__(self, level):
        super(Rogue, self).__init__()
        self.name = 'Rogue'
        if level > 1:
            self.abilities.append("")


class Sorcerer(CharacterClass):
    def __init__(self, level):
        super(Sorcerer, self).__init__()
        self.name = 'Sorcerer'
        if level > 1:
            self.abilities.append("")


class Warlock(CharacterClass):
    def __init__(self, level):
        super(Warlock, self).__init__()
        self.name = 'Warlock'
        if level > 1:
            self.abilities.append("")


class Wizard(CharacterClass):
    def __init__(self, level):
        super(Wizard, self).__init__()
        self.name = 'Wizard'
        if level > 1:
            self.abilities.append("")


# Notes to yourself:  Add in Proficiency bonus for each level.
