from DiceRoll import diceroll, stat_selection
from equipment import tool, artisan_tools, musical_instruments
from modifiers import *
from invocations import *
from spells import spell_queue, warlock_spell_queue
from language import choose_language

# Class listing
# # CharacterClass
# # Barbarian
# # Bard
# # Cleric
# # Druid
# # Fighter
# # Monk
# # Paladin
# # Ranger
# # Rogue
# # Sorcerer
# # Warlock
# # Wizard


class CharacterClass:
    def __init__(self, character_name):
        self.char_name = character_name
        self.name = ''
        self.statblock = {}
        self.hit_die = 6
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
        self.classpath = ''
        self.armor = 'None'
        self.speed_addition = 0
        self.saves = []
        self.abilities = []
        self.language = []
        self.spells = []
        self.classpath = ''
        self.armorpro = []
        self.weaponpro = []
        self.toolpro = []
        self.wealth = 0

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
        return self.statblock['Strength']

    def get_dexterity_addition(self):
        return self.statblock['Dexterity']

    def get_constitution_addition(self):
        return self.statblock['Constitution']

    def get_intelligence_addition(self):
        return self.statblock['Intelligence']

    def get_wisdom_addition(self):
        return self.statblock['Wisdom']

    def get_charisma_addition(self):
        return self.statblock['Charisma']

    def get_speed_addition(self):
        return self.speed_addition

    def ability_up(self, statblock):
        ability_dict = levelup_ability_increase(statblock)
        self.statblock['Strength'] += ability_dict.get(1)
        self.statblock['Dexterity'] += ability_dict.get(2)
        self.statblock['Constitution'] += ability_dict.get(3)
        self.statblock['Intelligence'] += ability_dict.get(4)
        self.statblock['Wisdom'] += ability_dict.get(5)
        self.statblock['Charisma'] += ability_dict.get(6)

    def get_classpath(self):
        return self.classpath

    def myname(self):
        return self.char_name


class Barbarian(CharacterClass):
    def __init__(self, level, character_name):  # initiate
        super(Barbarian, self).__init__(character_name=character_name)
        self.name = 'Barbarian'  # class name
        self.hit_die = 12  # Hit die is 1d12
        self.primary_ability = "Strength"  # primary ability is Strength
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Strength", "Constitution"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]  # Proficient in Simple and Martial Weapons
        self.toolpro = []
        self.language = []
        self.wealth = (diceroll(2, 4) * 10)
        print(BColors.ENDC + "pick two(2) skills from this list")
        for key, value in barbarian_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(barbarian_skill_list().items()))
            r = validate_choice(len(barbarian_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

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
            a = validate_choice(2, message='Choose Your Path: ')
            if a == 1:
                self.classpath = "Berzerker"
                self.abilities.append("FRENZY")
            else:
                self.classpath = "Totem"
                self.abilities.append("SPIRIT SEEKER")
        if level >= 4:  # First Stat Increase
            self.ability_up(self.statblock)
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
            self.ability_up(self.statblock)
        if level >= 9:
            self.abilities.append("BRUTAL CRITICAL")
        if level >= 10:
            if self.classpath == "Berzerker":
                self.abilities.append("INTIMIDATING PRESENCE")
            else:
                self.abilities.append("SPIRIT WALKER")
        if level >= 11:
            self.abilities.append("RELENTLESS RAGE")
        if level >= 12:
                self.ability_up(self.statblock)
        if level >= 16:
            if self.classpath == "Totem":
                self.abilities.append("TOTEMIC ATTUNEMENT")
        if level >= 15:
            self.abilities.append("PERSISTANT RAGE")
        if level >= 16:  # Fourth Stat Increase
            self.ability_up(self.statblock)
        if level >= 18:
            self.abilities.append("INDOMITABLE MIGHT")
        if level >= 19:  # Fifth Stat Increase
            self.ability_up(self.statblock)
        if level == 20:
            self.strength_addition += 4
            self.constitution_addition += 4


class Bard(CharacterClass):
    def __init__(self, level, character_name):
        super(Bard, self).__init__(character_name=character_name)
        self.name = 'Bard'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Charisma"  # primary ability is Strength
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Dexterity", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
        for i in range(3):
            self.toolpro.append(tool(musical_instruments())[0])
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(5, 4) * 10)
        valid = False
        while valid is not True:
            self.skill_list = full_skill_list()
            clearscreen()
            for key, value in self.skill_list.items():
                print(key, value)
            print("Please Choose 3 Skill Proficiencies:")
            answers = []
            skill_1 = validate_choice(len(full_skill_list().items()), message='Skill 1:')
            answers.append(skill_1)
            skill_2 = validate_choice(len(full_skill_list().items()), message='Skill 2:')
            answers.append(skill_2)
            skill_3 = validate_choice(len(full_skill_list().items()), message='Skill 3:')
            answers.append(skill_3)
            if len(set(answers)) < 2:
                valid = False
            else:
                valid = True

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
            self.abilities.append("BARDIC INSPIRATION (D6)")
        if level >= 2:
            self.abilities.append("JACK OF ALL TRADES")
            self.abilities.append("SONG OF REST (D6)")
        if level >= 3:
            self.abilities.append("EXPERTISE")
            # Level 3 Choose your class path, either Path of the Berzerker or Path of the Totem Warrior
            print("you must now choose your Bard College, you have the following options: \n"
                  "1: College of Lore ('CUTTING WORDS', 'ADDITIONAL MAGICAL SECRETS', 'PEERLESS SKILL') \n"
                  "2: College of Valor ('BONUS PROFICIENCIES', 'COMBAT INSPIRATION', 'EXTRA ATTACK')")
            a = validate_choice(2, message='Choose Your Path')
            if a == 1:
                self.classpath = "Lore"
                self.abilities.append("CUTTING WORDS")
                #  Bonus Proficiencies
            valid = False
            while valid is not True:
                for key, value in self.skill_list.items():
                    print(key, value)
                print("Please Choose 3 Additional Skill Proficiencies:")
                answers = []
                skill_1 = validate_choice(len(full_skill_list().items()), message='Skill 1:')
                answers.append(skill_1)
                skill_2 = validate_choice(len(full_skill_list().items()), message='Skill 2:')
                answers.append(skill_2)
                skill_3 = validate_choice(len(full_skill_list().items()), message='Skill 3:')
                answers.append(skill_3)
                if len(set(answers)) < 3:
                    valid = False
                else:
                    valid = True
                try:
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
                except KeyError:
                    valid = False
                    print('YOUR SELECTIONS WERE INVALID PLEASE TRY AGAIN')
            else:
                self.classpath = "Valor"
                self.abilities.append("COMBAT INSPIRATION")
                self.armorpro.append("Medium Armor")
                self.armorpro.append("Shields")
                self.weaponpro.append("Martial Weapons")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.remove("BARDIC INSPIRATION (D6)")
            self.abilities.append("BARDIC INSPIRATION (D8)")
            self.abilities.append("FONT OF INSPIRATION")
        if level >= 6:
            self.abilities.append("COUNTERCHARM")
            if self.classpath == "Lore":
                self.abilities.append("********more spells*********")
            else:
                self.abilities.append("EXTRA ATTACK")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 9:
            self.abilities.remove("SONG OF REST (D6)")
            self.abilities.append("SONG OF REST (D8)")

        if level >= 10:
            self.abilities.remove("BARDIC INSPIRATION (D8)")
            self.abilities.append("BARDIC INSPIRATION (D10)")
            self.abilities.append("****magical secrets ****")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 13:
            self.abilities.remove("SONG OF REST (D8)")
            self.abilities.append("SONG OF REST (D10)")
        if level >= 14:
            self.abilities.append("*****magical secrets 2*****")
            if self.classpath == "Lore":
                self.abilities.append("PEERLESS SKILL")
            else:
                self.abilities.append("BATTLE MAGIC")
        if level >= 15:
            self.abilities.remove("BARDIC INSPIRATION (D10)")
            self.abilities.append("BARDIC INSPIRATION (D12)")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            self.abilities.remove("SONG OF REST (D10)")
            self.abilities.append("SONG OF REST (D12)")
        if level >= 18:
            self.abilities.append("*****magical secrets 3*****")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("SUPERIOR INSPIRATION")
        self.spells = spell_queue("Bard", level)


class Cleric(CharacterClass):
    def __init__(self, level, character_name):
        super(Cleric, self).__init__(character_name=character_name)
        self.name = 'Cleric'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Wisdom"  # primary ability is Strength
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Wisdom", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Simple Weapons"]
        self.toolpro = []  # None
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Wisdom"
        self.language = []
        self.wealth = (diceroll(5, 4) * 10)
        clearscreen()
        print("pick two(2) skills from this list")
        for key, value in cleric_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(cleric_skill_list().items()), message='Skill 1: ')
            r = validate_choice(len(cleric_skill_list().items()), message='Skill 2: ')
            if r == s:
                valid = False
            else:
                valid = True

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
            clearscreen()
            for key, value in divine_domains().items():
                print(key, value)
            selection = validate_choice(len(divine_domains().items()), message='Choose a Divine Domain')
            self.classpath = divine_domains().get(selection)
            self.magic = True

            if self.classpath == "Knowledge Domain":
                self.spells.append("Command")
                self.spells.append("Identify")
                self.language.append(choose_language(self.language))
                self.language.append(choose_language(self.language))
                knowledge_domain_skills = {1: "Arcana", 2: "History", 3: "Nature", 4: "Religion"}
                print("pick two(2) skills from this list")
                clearscreen()
                for key, value in knowledge_domain_skills.items():
                    print(key, value)
                valid = False
                while valid is not True:
                    s = validate_choice(len(knowledge_domain_skills.items()), message='Skill 1: ')
                    r = validate_choice(len(knowledge_domain_skills.items()), message='Skill 2: ')
                    if r == s:
                        valid = False
                    else:
                        valid = True

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
            self.abilities.append("CHANNEL DIVINITY (1/REST)")
            if self.classpath == "Knowledge Domain":
                self.abilities.append("KNOWLEDGE OF THE AGES")
                self.spells.append("Augury")
                self.spells.append("Suggestion")

            elif self.classpath == "Life Domain":
                self.abilities.append("PRESERVE LIFE")
                self.spells.append("Lesser Restoration")
                self.spells.append("Spiritual Weapon")

            elif self.classpath == "Light Domain":
                self.abilities.append("CHANNEL DIVINITY: RADIANCE OF THE DAWN")
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
                self.abilities.append("CHANNEL DIVINITY: GUIDED STRIKE")
                self.spells.append("Magic Weapon")
                self.spells.append("Spiritual Weapon")

        if level >= 4:
            self.ability_up(self.statblock)

        if level >= 5:
            self.abilities.append("DESTROY UNDEAD (CR 1/2 OR BELOW)")
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
            self.abilities.remove("CHANNEL DIVINITY (1/REST)")
            self.abilities.append("CHANNEL DIVINITY (2/REST)")
            if self.classpath == "Knowledge Domain":
                self.abilities.append("READ THOUGHTS")

            elif self.classpath == "Life Domain":
                self.abilities.append("BLESSED HEALER")

            elif self.classpath == "Light Domain":
                self.abilities.remove("WARDING FLARE")
                self.abilities.append("IMPROVED FLARE")

            elif self.classpath == "Nature Domain":
                self.abilities.append("DAMPEN ELEMENTS")

            elif self.classpath == "Tempest Domain":
                self.abilities.append("THUNDERBOLT STRIKE")

            elif self.classpath == "Trickery Domain":
                self.abilities.append("CLOAK OF SHADOWS")

            elif self.classpath == "War Domain":
                self.abilities.append("CHANNEL DIVINITY: WAR GOD\'S BLESSING")

        if level >= 8:
            self.abilities.remove("DESTROY UNDEAD (CR 1/2 OR BELOW)")
            self.abilities.append("DESTROY UNDEAD (CR 1 OR BELOW)")
            self.ability_up(self.statblock)
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
            self.abilities.remove("DESTROY UNDEAD (CR 1 OR BELOW)")
            self.abilities.append("DESTROY UNDEAD (CR 2 OR BELOW)")

        if level >= 12:
            self.ability_up(self.statblock)

        if level >= 14:
            self.abilities.remove("DESTROY UNDEAD (CR 2 OR BELOW)")
            self.abilities.append("DESTROY UNDEAD (CR 3 OR BELOW)")

        if level >= 16:
            self.ability_up(self.statblock)

        if level >= 17:
            self.abilities.remove("DESTROY UNDEAD (CR 3 OR BELOW)")
            self.abilities.append("DESTROY UNDEAD (CR 4 OR BELOW)")
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
            self.abilities.remove("CHANNEL DIVINITY (2/REST)")
            self.abilities.append("CHANNEL DIVINITY (3/REST)")

        if level >= 19:
            self.ability_up(self.statblock)

        if level >= 20:
            self.abilities.remove("DIVINE INTERVENTION")
            self.abilities.append("DIVINE INTERVENTION IMPROVEMENT")
        self.spells = spell_queue("Cleric", level)


class Druid(CharacterClass):
    def __init__(self, level, character_name):
        super(Druid, self).__init__(character_name=character_name)
        self.name = 'Druid'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Wisdom"  # primary ability is Strength
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Intelligence", "Wisdom"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Shields"]  # Proficient in Light, Medium Armor and Shields
        self.weaponpro = ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles",
                          "Slings", "Spears"]
        self.toolpro = ["Herbalism Kit"]
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Wisdom"
        self.language = ["Druidic"]
        self.wealth = (diceroll(2, 4) * 10)
        clearscreen()
        print("Where did you become a Druid?:")
        lands = druidic_lands()
        for key, value in druidic_lands().items():
            print(key, value)
        self.land_type = lands.pop(validate_choice(len(druidic_lands().items()), message='Choose a Land Type: '))
        clearscreen()
        print("pick two(2) skills from this list")
        for key, value in druid_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(druid_skill_list().items()), message='Skill 1: ')
            r = validate_choice(len(druid_skill_list().items()), message='Skill 2: ')
            if r == s:
                valid = False
            else:
                valid = True

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
            self.abilities.append("WILD SHAPE (CR 1/4 OR BELOW, NO FLYING OR SWIM SPEED)")
        if level >= 2:
            clearscreen()
            print("you must now choose your Druid Circle, you have the following options: \n"
                  "1: Circle of the Land ('NATURAL RECOVERY', 'CIRCLE SPELLS 1', 'LANDS STRIDE') \n"
                  "2: Circle of the Moon ('COMBAT WILD SHAPE', 'CIRCLE FORMS', 'PRIMAL STRIKE')")
            a = validate_choice(2, message='Choose Your Path: ')
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
            self.abilities.remove("WILD SHAPE (CR 1/4 OR BELOW, NO FLYING OR SWIM SPEED)")
            self.abilities.append("WILD SHAPE (CR 1/2 OR BELOW, NO FLYING SPEED)")
            self.ability_up(self.statblock)
        if level >= 6:
            if self.classpath == "Circle of the Land":
                self.abilities.append("LAND\'S STRIDE")
            else:
                self.abilities.append("PRIMAL STRIKE")
        if level >= 7:
            if self.classpath == "Circle of the Land":
                self.spells += circle_spells(self.land_type, 7)
        if level >= 8:
            self.abilities.remove("WILD SHAPE (CR 1/2 OR BELOW, NO FLYING SPEED)")
            self.abilities.append("WILD SHAPE (CR 1 OR BELOW)")
            self.ability_up(self.statblock)
        if level >= 9:
            if self.classpath == "Circle of the Land":
                self.spells += circle_spells(self.land_type, 9)
        if level >= 10:
            if self.classpath == "Circle of the Land":
                self.abilities.append("NATURE\'S WARD")
            else:
                self.abilities.append("ELEMENTAL WILD SHAPE")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 14:
            if self.classpath == "Circle of the Land":
                self.abilities.append("NATURE\'S SANCTUARY")
            else:
                self.abilities.append("THOUSAND FORMS")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 18:
            self.abilities.append("TIMELESS BODY")
            self.abilities.append("BEAST SPELLS")
        if level >= 20:
            self.abilities.append("ARCHDRUID")
        self.spells = spell_queue("Druid", level)


class Fighter(CharacterClass):
    def __init__(self, level, character_name):
        super(Fighter, self).__init__(character_name=character_name)
        self.name = 'Fighter'
        self.hit_die = 10  # Hit die is 1d8
        self.primary_ability = "Strength"  # primary ability is Strength
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Strength", "Constitution"]  # Saving throws are Strength and Constitution
        self.armorpro = ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"]
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = False
        self.spellcasting_ability = "Wisdom"
        self.language = []
        self.wealth = (diceroll(5, 4) * 10)
        self.maneuver = []
        manu = get_maneuvers()
        x = fighter_fighting_style()
        if level >= 1:
            self.abilities.append("SECOND WIND")
            clearscreen()
            print("pick two(2) skills from this list")
            for key, value in fighter_skill_list().items():
                print(key, value)
            valid = False
            while valid is not True:
                s = validate_choice(len(fighter_skill_list().items()), message='Skill 1: ')
                r = validate_choice(len(fighter_skill_list().items()), message='Skill 2: ')
                if r == s:
                    valid = False
                else:
                    valid = True

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

            clearscreen()
            print("Fighting Styles:")
            for key, value in x.items():
                print(key, value)

            a = validate_choice(len(x.items()), message="Choose a Fighting Style: ")
            self.fighting_style = x.pop(a)
        if level >= 2:
            self.abilities.append("ACTION SURGE (1 USE)")
        if level >= 3:
            clearscreen()
            print("you must now choose your Martial Archtype, you have the following options: \n"
                  "1: Champion ('IMPROVED CRITICAL', 'REMARKABLE ATHLETE', 'ADDITIONAL FIGHTING STYLE') \n"
                  "2: Battle Master ('COMBAT SUPERIORITY', 'STUDENT OF WAR', 'KNOW YOUR ENEMY') \n"
                  "3: Eldritch Knight ('SPELLCASTING', 'WEAPON BOND', 'WAR MAGIC')")
            a = validate_choice(3, message='Choose Your Path: ')
            if a == 1:
                self.classpath = "Champion"
                self.abilities.append("IMPROVED CRITICAL")
            elif a == 2:
                self.classpath = "Battle Master"

                self.superiority_die = 4
                self.superiority_die_type = 'd8'
                i = 0
                while i < 3:
                    print('Select Combat Superiority:')
                    for key, value in manu.items():
                        print(key, value)
                    a = validate_choice(len(get_maneuvers().items()),
                                        message='Choose one Maneuver ({} of {}'.format(i+1, 3))
                    try:
                        del manu[a]
                    except KeyError:
                        pass
                    self.maneuver = get_maneuvers().get(a)
                    i += 1
            elif a == 3:
                self.classpath = "Eldritch Knight"
                self.abilities.append("SPELLCASTING")
                self.abilities.append("WEAPON BOND")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.append("EXTRA ATTACK")
        if level >= 6:
            self.ability_up(self.statblock)
        if level >= 7:
            if self.classpath == "Champion":
                self.abilities.append("REMARKABLE ATHLETE")
            elif self.classpath == "Battle Master":
                self.abilities.append("KNOW YOUR ENEMY")
                i = 0
                while i < 2:
                    print('Select Combat Superiority:')
                    for key, value in manu.items():
                        print(key, value)
                    a = validate_choice(len(get_maneuvers().items()),
                                        message='Choose one Maneuver ({} of {}'.format(i+1, 2))
                    try:
                        del manu[a]
                    except KeyError:
                        pass
                    self.maneuver = get_maneuvers().get(a)
                    i += 1
                self.superiority_die += 1
            elif self.classpath == "Eldritch Knight":
                self.abilities.append("WAR MAGIC")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 9:
            self.abilities.append("INDOMITABLE")
        if level >= 10:
            if self.classpath == "Champion":
                clearscreen()
                for key, value in x.items():
                    print(key, value)
                a = validate_choice(len(x.items()), message='Choose an Additional Fighting Style: ')
                self.fighting_style += x.pop(a)
            elif self.classpath == "Battle Master":
                i = 0
                while i < 2:
                    print('Select Combat Superiority:')
                    for key, value in manu.items():
                        print(key, value)
                    a = validate_choice(len(get_maneuvers().items()),
                                        message='Choose one Maneuver ({} of {}'.format(i+1, 2))
                    try:
                        del manu[a]
                    except KeyError:
                        pass
                    self.maneuver = get_maneuvers().get(a)
                    i += 1
                self.superiority_die_type = 'd10'
            elif self.classpath == "Eldritch Knight":
                self.abilities.append("ELDRITCH STRIKE")
        if level >= 11:
            self.abilities.remove("EXTRA ATTACK")
            self.abilities.append("EXTRA ATTACK (2)")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 13:
            self.abilities.remove("INDOMITABLE")
            self.abilities.append("INDOMITABLE (2)")
        if level >= 14:
            self.ability_up(self.statblock)
        if level >= 15:
            if self.classpath == "Champion":
                self.abilities.remove("IMPROVED CRITICAL")
                self.abilities.append("SUPERIOR CRITICAL")
            elif self.classpath == "Battle Master":
                i = 0
                while i < 2:
                    print('Select Combat Superiority:')
                    for key, value in manu.items():
                        print(key, value)
                    a = validate_choice(len(get_maneuvers().items()),
                                        message='Choose one Maneuver ({} of {}'.format(i+1, 2))
                    try:
                        del manu[a]
                    except KeyError:
                        pass
                    self.maneuver = get_maneuvers().get(a)
                    i += 1
                self.superiority_die += 1
                self.abilities.append("RELENTLESS")
            elif self.classpath == "Eldritch Knight":
                self.abilities.append("ARCANE CHARGE")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            self.abilities.remove("ACTION SURGE (1 USE)")
            self.abilities.append("ACTION SURGE (2 USES)")
            self.abilities.remove("INDOMITABLE (2)")
            self.abilities.append("INDOMITABLE (3)")
        if level >= 18:
            if self.classpath == "Champion":
                self.abilities.append("SURVIVOR")
            elif self.classpath == "Eldritch Knight":
                self.abilities.remove("WAR MAGIC")
                self.abilities.append("IMPROVED WAR MAGIC")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.remove("EXTRA ATTACK (2)")
            self.abilities.append("EXTRA ATTACK (3)")
        if self.classpath == "Eldritch Knight" and level >= 3:
            self.spells += spell_queue("Wizard", level, school='abjuration', school2='evocation')


class Monk(CharacterClass):
    def __init__(self, level, character_name):
        super(Monk, self).__init__(character_name=character_name)
        self.name = 'Monk'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Dexterity"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Strength", "Dexterity"]  # Saving throws are Strength and Constitution
        self.armorpro = []
        self.weaponpro = ["Simple Weapons", "Shortswords"]
        self.toolpro.append(tool(artisan_tools())[0])
        self.toolpro.append(tool(musical_instruments())[0])
        self.spells = []
        self.spellcasting = False
        self.spellcasting_ability = "Wisdom"
        self.language = []
        self.wealth = diceroll(5, 4)
        self.elemental_discipline = []
        clearscreen()
        for key, value in monk_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(monk_skill_list().items()))
            r = validate_choice(len(monk_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

        if (s == 1) or (r == 1):
            self.acrobatics_skill = True

        if (s == 2) or (r == 2):
            self.athletics_skill = True

        if (s == 3) or (r == 3):
            self.history_skill = True

        if (s == 4) or (r == 4):
            self.insight_skill = True

        if (s == 5) or (r == 5):
            self.religion_skill = True

        if (s == 6) or (r == 6):
            self.stealth_skill = True
        if level >= 1:
            self.abilities.append("UNARMORED DEFENSE")
            self.abilities.append("MARTIAL ARTS")
        if level >= 2:
            self.ki_points = 2
            self.abilities.append("FLURRY OF BLOWS")
            self.abilities.append("PATIENT DEFENSE")
            self.abilities.append("STEP OF THE WIND")
            self.abilities.append("UNARMORED MOVEMENT 1")
        if level >= 3:
            self.abilities.append("DEFLECT MISSILES")
            clearscreen()
            print("you must now choose your Monastic Tradition, you have the following options: \n"
                  "1: Way of the Open Hand ('OPEN HAND TECHNIQUE', 'WHOLENESS OF BODY', 'TRANQUILITY') \n"
                  "2: The Way of Shadow ('SHADOW ARTS', 'SHADOW STEP', 'CLOAK OF SHADOWS') \n"
                  "3: Way of the Four Elements ('DISCIPLE OF THE ELEMENTS', 'ELEMENTAL DISCIPLINE', 'WAR MAGIC')")
            a = validate_choice(3, message='Choose Your Path:')
            if a == 1:
                self.classpath = "Way of the Open Hand"
                self.abilities.append("OPEN HAND TECHNIQUE")
            elif a == 2:
                self.classpath = "The Way of Shadow"
                self.abilities.append("SHADOW ARTS")
            elif a == 3:
                self.classpath = "Way fo the Four Elements"
                x = get_elemental_disciplines(3)
                done = False
                while done is False:
                    for key, value in x.items():
                        print(key, value)
                    a = validate_choice(len(x.items()), message='Pick an Elemental Discipline')
                    print(get_elemental_disciplines_desc(x.get(a))[0])
                    y = input('Confirm Selection (y/n):')
                    if y.lower() == ('n' or 'no'):
                        continue
                    else:
                        self.elemental_discipline.append(x.get(a))
                        done = True
        if level >= 4:
            self.abilities.append("SLOW FALL")
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.append("EXTRA ATTACK")
            self.abilities.append("STUNNING STRIKE")
        if level >= 6:
            self.abilities.append("KI EMPOWERED STRIKES")
            if self.classpath == "Way of the Open Hand":
                self.abilities.append("WHOLENESS OF BODY")
            if self.classpath == "The Way of Shadow":
                self.abilities.append("SHADOW STEP")
            if self.classpath == "Way fo the Four Elements":
                x = get_elemental_disciplines(6)
                done = False
                while done is False:
                    for key, value in x.items():
                        print(key, value)
                    a = validate_choice(len(x.items()), message='Pick an Elemental Discipline')
                    print(get_elemental_disciplines_desc(x.get(a))[0])
                    y = input('Confirm Selection (y/n):')
                    if y.lower() == ('n' or 'no'):
                        continue
                    else:
                        self.elemental_discipline.append(x.get(a))
                        done = True
        if level >= 7:
            self.abilities.append("EVASION")
            self.abilities.append("STILLNESS OF MIND")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 9:
            self.abilities.remove("UNARMORED MOVEMENT 1")
            self.abilities.append("UNARMORED MOVEMENT 2")
        if level >= 10:
            self.abilities.append("PURITY OF BODY")
        if level >= 11:
            if self.classpath == "Way of the Open Hand":
                self.abilities.append("TRANQUILITY")
            if self.classpath == "The Way of Shadow":
                self.abilities.append("CLOAK OF SHADOWS")
            if self.classpath == "Way fo the Four Elements":
                x = get_elemental_disciplines(11)
                done = False
                while done is False:
                    for key, value in x.items():
                        print(key, value)
                    a = validate_choice(len(x.items()), message='Pick an Elemental Discipline')
                    print(get_elemental_disciplines_desc(x.get(a))[0])
                    y = input('Confirm Selection (y/n):')
                    if y.lower() == ('n' or 'no'):
                        continue
                    else:
                        self.elemental_discipline.append(x.get(a))
                        done = True
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 13:
            self.abilities.append("TONGUE OF THE SUN AND MOON")
        if level >= 14:
            self.abilities.append("DIAMOND SOUL")
        if level >= 15:
            self.abilities.append("TIMELESS BODY")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            if self.classpath == "Way of the Open Hand":
                self.abilities.append("QUIVERING PALM")
            if self.classpath == "The Way of Shadow":
                self.abilities.append("OPPORTUNIST")
            if self.classpath == "Way fo the Four Elements":
                x = get_elemental_disciplines(11)
                done = False
                while done is False:
                    for key, value in x.items():
                        print(key, value)
                    a = validate_choice(len(x.items()), message='Pick an Elemental Discipline')
                    print(get_elemental_disciplines_desc(x.get(a))[0])
                    y = input('Confirm Selection (y/n):')
                    if y.lower() == ('n' or 'no'):
                        continue
                    else:
                        self.elemental_discipline.append(x.get(a))
                        done = True
        if level >= 18:
            self.abilities.append("EMPTY BODY")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("PERFECT SELF")


class Paladin(CharacterClass):
    def __init__(self, level, character_name):
        super(Paladin, self).__init__(character_name=character_name)
        self.name = 'Paladin'
        self.hit_die = 10  # Hit die is 1d8
        self.primary_ability = "Strength"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Wisdom", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ['All Armor', 'Shields']
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(5, 4) * 10)
        clearscreen()
        for key, value in paladin_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(paladin_skill_list().items()))
            r = validate_choice(len(paladin_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

        if (s == 1) or (r == 1):
            self.athletics_skill = True

        if (s == 2) or (r == 2):
            self.insight_skill = True

        if (s == 3) or (r == 3):
            self.intimidation_skill = True

        if (s == 4) or (r == 4):
            self.medicine_skill = True

        if (s == 5) or (r == 5):
            self.persuasion_skill = True

        if (s == 6) or (r == 6):
            self.religion_skill = True

        if level >= 1:
            self.abilities.append("DIVINE SENSE")
            self.abilities.append("LAY ON HANDS")
        if level >= 2:
            self.abilities.append("fighting style")
            self.abilities.append("DIVINE SMITE")
        if level >= 3:
            self.abilities.append("DIVINE HEALTH")
            clearscreen()
            print("you must now choose your Sacred Oath, you have the following options: \n"
                  "1: Oath of Devotion ('AURA OF DEVOTION', 'PURITY OF SPIRIT', 'HOLY NIMBUS') \n"
                  "2: Oath of the Ancients ('AURA OF WARDING', 'UNDYING SENTINEL', 'ELDER CHAMPION') \n"
                  "3: Oath of Vengeance ('RELENTLESS AVENGER', 'SOUL OF VENGEANCE', 'AVENGING ANGEL')")
            a = validate_choice(3, message='Choose Your Path')
            if a == 1:
                self.classpath = "Oath of Devotion"
                self.abilities.append("CHANNEL DIVINITY: SACRED WEAPON")
                self.abilities.append("CHANNEL DIVINITY: TURN THE UNHOLY")
            elif a == 2:
                self.classpath = "Oath of the Ancients"
                self.abilities.append("CHANNEL DIVINITY: NATURE'S WRATH")
                self.abilities.append("CHANNEL DIVINITY: TURN THE FAITHLESS")
            elif a == 3:
                self.classpath = "Oath of Vengeance"
                self.abilities.append("CHANNEL DIVINITY: ABJURE ENEMY")
                self.abilities.append("CHANNEL DIVINITY: VOW OF ENMITY")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.append("EXTRA ATTACK")
        if level >= 6:
            self.abilities.append("AURA OF PROTECTION")
        if level >= 7:
            if self.classpath == "Oath of Devotion":
                self.abilities.append("AURA OF DEVOTION")
            if self.classpath == "Oath to the Ancients":
                self.abilities.append("AURA OF WARDING")
            if self.classpath == "Oath of Vengeance":
                self.abilities.append("RELENTLESS AVENGER")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 10:
            self.abilities.append("AURA OF COURAGE")
        if level >= 11:
            self.abilities.remove("DIVINE SMITE")
            self.abilities.append("IMPROVED DIVINE SMITE")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 14:
            self.abilities.append("CLEANSING TOUCH")
        if level >= 15:
            if self.classpath == "Oath of Devotion":
                self.abilities.append("PURITY OF SPIRIT")
            if self.classpath == "Oath to the Ancients":
                self.abilities.append("UNDYING SENTINEL")
            if self.classpath == "Oath of Vengeance":
                self.abilities.append("SOUL OF VENGEANCE")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 18:
            self.abilities.remove("AURA OF PROTECTION")
            self.abilities.append("IMPROVED AURA OF PROTECTION")
            self.abilities.remove("AURA OF COURAGE")
            self.abilities.append("IMPROVED AURA OF COURAGE")
            if self.classpath == "Oath of Devotion":
                self.abilities.remove("AURA OF DEVOTION")
                self.abilities.append("IMPROVED AURA OF DEVOTION")
            if self.classpath == "Oath to the Ancients":
                self.abilities.remove("AURA OF WARDING")
                self.abilities.append("IMPROVED AURA OF WARDING")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            if self.classpath == "Oath of Devotion":
                self.abilities.append("HOLY NIMBUS")
            if self.classpath == "Oath to the Ancients":
                self.abilities.append("ELDER CHAMPION")
            if self.classpath == "Oath of Vengeance":
                self.abilities.append("AVENGING ANGEL")
        self.spells += spell_queue("Paladin", level)


class Ranger(CharacterClass):
    def __init__(self, level, character_name):
        super(Ranger, self).__init__(character_name=character_name)
        self.name = 'Ranger'
        self.hit_die = 10  # Hit die is 1d8
        self.primary_ability = "Dexterity"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Strength", "Dexterity"]  # Saving throws are Strength and Constitution
        self.armorpro = ['Light Armor', 'Medium Armor', 'Shields']
        self.weaponpro = ["Simple Weapons", "Martial Weapons"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(5, 4) * 10)
        x = ranger_fighting_style()
        lands = druidic_lands()
        if level >= 1:
            fav_enemy = favored_enemy(['Pidgeons'])
            for i in fav_enemy:
                print(i[0], i[1])
                self.abilities.append("FAVORED ENEMY " + "(" + i[0] + ")")

                if i[1] != 'No Language':
                    self.language.append(i[1])
            clearscreen()
            valid = False
            while valid is not True:
                self.skill_list = full_skill_list()
                for key, value in self.skill_list.items():
                    print(key, value)
                print("Please Choose 3 Skill Proficiencies:")
                answers = []
                skill_1 = validate_choice(len(self.skill_list.items()), message='Skill 1:')
                answers.append(skill_1)
                skill_2 = validate_choice(len(self.skill_list.items()), message='Skill 2:')
                answers.append(skill_2)
                skill_3 = validate_choice(len(self.skill_list.items()), message='Skill 3:')
                answers.append(skill_3)
                if len(set(answers)) < 2:
                    valid = False
                else:
                    valid = True

            if (skill_1 == 1) or (skill_2 == 1) or (skill_3 == 1):
                self.acrobatics_skill = True

            if (skill_1 == 2) or (skill_2 == 2) or (skill_3 == 2):
                self.animal_handling_skill = True

            if (skill_1 == 3) or (skill_2 == 3) or (skill_3 == 3):
                self.athletics_skill = True

            if (skill_1 == 4) or (skill_2 == 4) or (skill_3 == 4):
                self.history_skill = True

            if (skill_1 == 5) or (skill_2 == 5) or (skill_3 == 5):
                self.insight_skill = True

            if (skill_1 == 6) or (skill_2 == 6) or (skill_3 == 6):
                self.intimidation_skill = True

            if (skill_1 == 7) or (skill_2 == 7) or (skill_3 == 7):
                self.perception_skill = True

            if (skill_1 == 8) or (skill_2 == 8) or (skill_3 == 8):
                self.survival_skill = True

            clearscreen()
            print("What land type is {} familiar with?".format(self.myname()))
            for key, value in lands.items():
                print(key, value)
            selection = "NATURAL EXPLORER " + "(" + str(lands.pop(validate_choice(
                                                    len(lands.items()), message='Choose a Land Type: ')) + ")")
            self.abilities.append(selection)
        if level >= 2:
            clearscreen()
            for key, value in x.items():
                print(key, value)
            a = validate_choice(len(x.items()), message='Choose a Fighting Style: ')
            self.fighting_style = x.pop(a)
            self.abilities.append("SPELLCASTING")
        if level >= 3:
            clearscreen()
            print("you must now choose your Ranger Archtype, you have the following options: \n"
                  "1: Hunter ('HUNTER\'S PREY', 'DEFENSIVE TACTICS', 'MULTIATTACK') \n"
                  "2: Beast Master ('RANGER\'S COMPANION', 'EXCEPTIONAL TRAINING', 'BESTIAL FURY') \n")
            a = validate_choice(2, message='Choose Your Path')
            if a == 1:
                self.classpath = "Hunter"
                for key, value in hunter_prey_options().items():
                    print(key, value)
                a = validate_choice(len(hunter_prey_options().items()), message='Choose a Hunter\'s Prey Option')
                if a == 1:
                    self.abilities.append("HUNTER'S PREY: COLOSSUS SLAYER")
                if a == 2:
                    self.abilities.append("HUNTER'S PREY: GIANT KILLER")
                if a == 3:
                    self.abilities.append("HUNTER'S PREY: HORDE BREAKER")
            elif a == 2:
                self.classpath = "Beast Master"
                self.abilities.append("RANGER\'s COMPANION")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.append("EXTRA ATTACK")
        if level >= 6:
            fav_enemy = favored_enemy(fav_enemy)
            for i in fav_enemy:
                self.abilities.append("FAVORED ENEMY " + "(" + i[0] + ")")
                if i[1] != 'No Language':
                    self.language.append(i[1])
        if level >= 7:
            if self.classpath == "Hunter":
                for key, value in defensive_tactics_options().items():
                    print(key, value)
                a = validate_choice(len(defensive_tactics_options().items()),
                                    message='Choose a Defensive Tactic\'s Option')
                if a == 1:
                    self.abilities.append("DEFENSIVE TACTICS: ESCAPE THE HORDE")
                if a == 2:
                    self.abilities.append("DEFENSIVE TACTICS: MULTIATTACK DEFENSE")
                if a == 3:
                    self.abilities.append("DEFENSIVE TACTICS: STEEL WILL")
            elif self.classpath == "Beast Master":
                self.abilities.append("EXCEPTIONAL TRAINING")
        if level >= 8:
            self.abilities.append("LAND\'S STRIDE")
            self.ability_up(self.statblock)
        if level >= 10:
            self.abilities.append("HIDE IN PLAIN SIGHT")
            for key, value in lands.items():
                print(key, ":", value)
            selection = "NATURAL EXPLORER " + "(" + str(lands.pop(validate_choice(
                                                        lands.items(), message='Choose a Land Type: ')) + ")")
            self.abilities.append(selection)
        if level >= 11:
            if self.classpath == "Hunter":
                for key, value in multiattack_options().items():
                    print(key, value)
                a = validate_choice(len(multiattack_options().items()),
                                    message='Choose a Multi-Attack Option')
                if a == 1:
                    self.abilities.append("MULTIATTACK: VOLLEY")
                if a == 2:
                    self.abilities.append("MULTIATTACK: WHIRLWIND ATTACK")
            elif self.classpath == "Beast Master":
                self.abilities.append("BESTIAL FURY")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 14:
            fav_enemy = favored_enemy(fav_enemy)
            for i in fav_enemy:
                self.abilities.append("FAVORED ENEMY " + "(" + i[0] + ")")
                if i[1] != 'No Language':
                    self.language.append(i[1])
        if level >= 15:
            if self.classpath == "Hunter":
                for key, value in superior_hunters_defense_options().items():
                    print(key, value)
                a = validate_choice(len(superior_hunters_defense_options().items()),
                                    message='Choose a Superior Hunter\'s Defense Option')
                if a == 1:
                    self.abilities.append("SUPERIOR HUNTER'S DEFENSE: EVASION")
                if a == 2:
                    self.abilities.append("SUPERIOR HUNTER'S DEFENSE: STAND AGAINST THE TIDE")
                if a == 3:
                    self.abilities.append("SUPERIOR HUNTER'S DEFENSE: UNCANNY DODGE")
            elif self.classpath == "Beast Master":
                self.abilities.append("SHARE SPELLS")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 18:
            self.abilities.append("FERAL SENSES")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("FOE SLAYER")


class Rogue(CharacterClass):
    def __init__(self, level, character_name):
        super(Rogue, self).__init__(character_name=character_name)
        self.name = 'Rogue'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Dexterity"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Dexterity", "Intelligence"]  # Saving throws are Strength and Constitution
        self.armorpro = ['Light Armor']
        self.weaponpro = ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
        self.toolpro = ["Thieves' Tools"]
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(4, 4) * 10)
        if level >= 1:
            clearscreen()
            print("pick four(4) skills from this list")
            valid = False
            while valid is not True:
                clearscreen()
                for key, value in rogue_skill_list().items():
                    print(key, value)
                print("Please Choose 3 Skill Proficiencies:")
                answers = []
                skill_1 = validate_choice(len(rogue_skill_list().items()), message='Skill 1:')
                answers.append(skill_1)
                skill_2 = validate_choice(len(rogue_skill_list().items()), message='Skill 2:')
                answers.append(skill_2)
                skill_3 = validate_choice(len(rogue_skill_list().items()), message='Skill 3:')
                answers.append(skill_3)
                skill_4 = validate_choice(len(rogue_skill_list().items()), message='Skill 4:')
                answers.append(skill_3)
                print(len(set(answers)))
                if len(set(answers)) < 3:
                    valid = False
                else:
                    valid = True

            if (skill_1 == 1) or (skill_2 == 1) or (skill_3 == 1) or (skill_4 == 1):
                self.acrobatics_skill = True

            if (skill_1 == 2) or (skill_2 == 2) or (skill_3 == 2) or (skill_4 == 2):
                self.athletics_skill = True

            if (skill_1 == 3) or (skill_2 == 3) or (skill_3 == 3) or (skill_4 == 3):
                self.deception_skill = True

            if (skill_1 == 4) or (skill_2 == 4) or (skill_3 == 4) or (skill_4 == 4):
                self.insight_skill = True

            if (skill_1 == 5) or (skill_2 == 5) or (skill_3 == 5) or (skill_4 == 5):
                self.intimidation_skill = True

            if (skill_1 == 6) or (skill_2 == 6) or (skill_3 == 6) or (skill_4 == 6):
                self.investigation_skill = True

            if (skill_1 == 7) or (skill_2 == 7) or (skill_3 == 7) or (skill_4 == 7):
                self.perception_skill = True

            if (skill_1 == 8) or (skill_2 == 8) or (skill_3 == 8) or (skill_4 == 8):
                self.performance_skill = True

            if (skill_1 == 9) or (skill_2 == 9) or (skill_3 == 9) or (skill_4 == 9):
                self.persuasion_skill = True

            if (skill_1 == 10) or (skill_2 == 10) or (skill_3 == 10) or (skill_4 == 10):
                self.sleight_of_hand_skill = True

            if (skill_1 == 11) or (skill_2 == 11) or (skill_3 == 11) or (skill_4 == 11):
                self.stealth_skill = True
            self.abilities.append("EXPERTISE")
            self.abilities.append("SNEAK ATTACK (D6)")
            self.language.append("Thieves' Cant")
        if level >= 2:
            self.abilities.append("CUNNING ACTION")
        if level >= 3:
            self.abilities.remove("SNEAK ATTACK (D6)")
            self.abilities.append("SNEAK ATTACK (2d6)")
            clearscreen()
            print("you must now choose your Rogue Archtype, you have the following options: \n"
                  "1: Thief ('FAST HANDS', 'SECOND-STORY WORK', 'SUPREME SNEAK') \n"
                  "2: Assassin ('BONUS PROFICIENCIES', 'ASSASSINATE', 'INFILTRATION EXPERTISE') \n"
                  "3: Arcane Trickster ('SPELLCASTING', 'MAGE HAND LEGERDEMAIN', 'MAGICAL AMBUSH')")

            a = validate_choice(3, message='Choose Your Path: ')
            if a == 1:
                self.classpath = "Thief"
                self.abilities.append("FAST HANDS")
                self.abilities.append("SECOND-STORY WORK")
            elif a == 2:
                self.classpath = "Assassin"
                self.toolpro.append("Disguise Kit")
                self.toolpro.append("Poisoner's Kit")
                self.abilities.append("ASSASSINATE")
            elif a == 3:
                self.classpath = "Arcane Trickster"
                self.abilities.append("SPELLCASTING")
                self.abilities.append("MAGE HAND LEGERDEMAIN")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 5:
            self.abilities.append("UNCANNY DODGE")
            self.abilities.remove("SNEAK ATTACK (2d6)")
            self.abilities.append("SNEAK ATTACK (3d6)")
        if level >= 6:
            self.abilities.remove("EXPERTISE")
            self.abilities.append("IMPROVED EXPERTISE")
        if level >= 7:
            self.abilities.append("EVASION")
            self.abilities.remove("SNEAK ATTACK (3d6)")
            self.abilities.append("SNEAK ATTACK (4d6)")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 9:
            self.abilities.remove("SNEAK ATTACK (4d6)")
            self.abilities.append("SNEAK ATTACK (5d6)")
            if self.classpath == "Thief":
                self.abilities.append("SUPREME SNEAK")
            elif self.classpath == "Assassin":
                self.abilities.append("INFILTRATION EXPERTISE")
            elif self.classpath == "Arcane Trickster":
                self.abilities.append("MAGICAL AMBUSH")
        if level >= 10:
            self.ability_up(self.statblock)
        if level >= 11:
            self.abilities.append("RELIABLE TALENT")
            self.abilities.remove("SNEAK ATTACK (5d6)")
            self.abilities.append("SNEAK ATTACK (6d6)")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 13:
            self.abilities.remove("SNEAK ATTACK (6d6)")
            self.abilities.append("SNEAK ATTACK (7d6)")
            if self.classpath == "Thief":
                self.abilities.append("USE MAGIC DEVICE")
            elif self.classpath == "Assassin":
                self.abilities.append("IMPOSTER")
            elif self.classpath == "Arcane Trickster":
                self.abilities.append("VERSATILE TRICKSTER")
        if level >= 14:
            self.abilities.append("BLINDSENSE")
        if level >= 15:
            self.abilities.append("SLIPPERY MIND")
            self.abilities.remove("SNEAK ATTACK (7d6)")
            self.abilities.append("SNEAK ATTACK (8d6)")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            self.abilities.remove("SNEAK ATTACK (8d6)")
            self.abilities.append("SNEAK ATTACK (9d6)")
            if self.classpath == "Thief":
                self.abilities.append("THIEF'S REFLEXES")
            elif self.classpath == "Assassin":
                self.abilities.append("DEATH STRIKE")
            elif self.classpath == "Arcane Trickster":
                self.abilities.append("SPELL THIEF")
        if level >= 18:
            self.abilities.append("ELUSIVE")
        if level >= 19:
            self.abilities.remove("SNEAK ATTACK (9d6)")
            self.abilities.append("SNEAK ATTACK (10d6)")
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("STROKE OF LUCK")
        if self.classpath == "Arcane Trickster":
            self.spells = spell_queue("Rogue", level, school='enchantment', school2='illusion')


class Sorcerer(CharacterClass):
    def __init__(self, level, character_name):
        super(Sorcerer, self).__init__(character_name=character_name)
        self.name = 'Sorcerer'
        self.hit_die = 6  # Hit die is 1d8
        self.primary_ability = "Charisma"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Constitution", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = []
        self.weaponpro = ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(3, 4) * 10)
        self.meta = metamagic()
        clearscreen()
        print("pick two(2) skills from this list")
        for key, value in sorcerer_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(sorcerer_skill_list().items()))
            r = validate_choice(len(sorcerer_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

        if (s == 1) or (r == 1):
            self.arcana_skill = True

        if (s == 2) or (r == 2):
            self.deception_skill = True

        if (s == 3) or (r == 3):
            self.insight_skill = True

        if (s == 4) or (r == 4):
            self.intimidation_skill = True

        if (s == 5) or (r == 5):
            self.persuasion_skill = True

        if (s == 6) or (r == 6):
            self.religion_skill = True

        if level >= 1:
            self.abilities.append("SPELLCASTING")
            self.abilities.append("FLEXIBLE CASTING: CREATING SPELL SLOTS")
            self.abilities.append("FLEXIBLE CASTING: CONVERTING SPELL SLOT")
            clearscreen()
            print("you must now choose your Sorcerous Origin, you have the following options: \n"
                  "1: Draconic Bloodline ('DRAGON ANCESTOR', 'DRACONIC RESILIENCE', 'ELEMENTAL AFFINITY') \n"
                  "2: Wild Magic ('WILD MAGIC SURGE', 'TIDES OF CHAOS', 'BEND LUCK') \n")
            a = validate_choice(2, message='Choose Your Path')
            if a == 1:
                self.classpath = "Draconic Bloodline"
                for key, value in draconic_lines().items():
                    print(key, value)
                a = validate_choice(len(draconic_lines().items()), message='Choose Your Draconic Bloodline')
                self.dragontype = draconic_lines().get(a)
                self.abilities.append("DRACONIC RESILIENCE")
            elif a == 2:
                self.classpath = "Wild Magic"
                self.abilities.append("WILD MAGIC SURGE")
        if level >= 2:
            self.abilities.append("FONT OF MAGIC")
        if level >= 3:
            clearscreen()
            print("METAMAGIC SELECTION: Select two(2) abilities.")
            for key, value in self.meta.items():
                print(key, value)
            for i in range(2):
                a = validate_choice(len(metamagic().items()))
                self.meta.pop(a)
                name = 'METAMAGIC (' + str(metamagic_names().get(a)) + ')'
                self.abilities.append(name)
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 6:
            if self.classpath == "Draconic Bloodline":
                self.abilities.append("ELEMENTAL AFFINITY")
            elif self.classpath == "Wild Magic":
                self.abilities.append("BEND LUCK")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 10:
            print("METAMAGIC SELECTION: Select one(1) abilities.")
            for key, value in self.meta.items():
                print(key, value)
            for i in range(1):
                a = validate_choice(len(metamagic().items()))
                self.meta.pop(a)
                name = 'METAMAGIC (' + str(metamagic_names().get(a)) + ')'
                self.abilities.append(name)
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 14:
            if self.classpath == "Draconic Bloodline":
                self.abilities.append("DRAGON WINGS")
            elif self.classpath == "Wild Magic":
                self.abilities.append("CONTROLLED CHAOS")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            print("METAMAGIC SELECTION: Select one(1) abilities.")
            for key, value in self.meta.items():
                print(key, value)
            for i in range(1):
                a = validate_choice(len(metamagic().items()))
                self.meta.pop(a)
                name = 'METAMAGIC (' + str(metamagic_names().get(a)) + ')'
                self.abilities.append(name)
        if level >= 18:
            if self.classpath == "Draconic Bloodline":
                self.abilities.append("DRACONIC PRESENCE")
            elif self.classpath == "Wild Magic":
                self.abilities.append("SPELL BOMBARDMENT")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("SORCEROUS RESTORATION")
        self.spells = spell_queue("Sorcerer", level)


class Warlock(CharacterClass):
    def __init__(self, level, character_name):
        super(Warlock, self).__init__(character_name=character_name)
        self.name = 'Warlock'
        self.hit_die = 8  # Hit die is 1d8
        self.primary_ability = "Charisma"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Wisdom", "Charisma"]  # Saving throws are Strength and Constitution
        self.armorpro = ['Light Armor']
        self.weaponpro = ["Simple Weapons"]
        self.toolpro = []
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Charisma"
        self.language = []
        self.wealth = (diceroll(4, 4) * 10)
        print("pick two(2) skills from this list")
        for key, value in warlock_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(warlock_skill_list().items()))
            r = validate_choice(len(warlock_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

        if (s == 1) or (r == 1):
            self.history_skill = True

        if (s == 2) or (r == 2):
            self.intimidation_skill = True

        if (s == 3) or (r == 3):
            self.investigation_skill = True

        if (s == 4) or (r == 4):
            self.nature_skill = True

        if (s == 5) or (r == 5):
            self.religion_skill = True

        if level >= 1:
            self.abilities.append("expanded spell list")
            print("you must now choose your Otherworldly Patron, you have the following options: \n"
                  "1: The Archfey ('EXPANDED SPELL LIST', 'FEY PRESENCE', 'MISTY ESCAPE') \n"
                  "2: The Fiend ('EXPANDED SPELL LIST', 'DARK ONE\'S BLESSING', 'DARK ONE\'S OWN LUCK') \n"
                  "3: The Great Old One ('EXPANDED SPELL LIST', 'AWAKENED MIND', 'ENTROPIC WARD')")

            a = validate_choice(3, message='Choose Your Path: ')
            if a == 1:
                self.classpath = "The Archfey"
                self.abilities.append("FEY PRESENCE")
            elif a == 2:
                self.classpath = "The Fiend"
                self.abilities.append("DARK ONE\'S BLESSING")
            elif a == 3:
                self.classpath = "The Great Old One"
                self.abilities.append("AWAKENED MIND")
        if level >= 2:
            self.abilities.append("ELDRITCH INVOCATIONS")
        if level >= 3:
            print("Your Otherworldly Patron bestowed a boon upon you, Choose one of the following: \n"
                  "1: Pact of the Chain \n"
                  "2: Pact of the Blade \n"
                  "3: Pact of the Tome \n")

            a = validate_choice(3, message='Choose Your Boon: ')
            if a == 1:
                self.pact = "Pact of the Chain"
                self.abilities.append("PACT OF THE CHAIN")
            elif a == 2:
                self.pact = "Pact of the Blade"
                self.abilities.append("PACT OF THE BLADE")
            elif a == 3:
                self.pact = "Pact of the Tome"
                self.abilities.append("PACT OF THE TOME")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 6:
            if self.classpath == "The Archfey":
                self.abilities.append("MISTY ESCAPE")
            elif self.classpath == "The Fiend":
                self.abilities.append("DARK ONE\'S OWN LUCK")
            elif self.classpath == "The Great Old One":
                self.abilities.append("ENTROPIC WARD")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 10:
            if self.classpath == "The Archfey":
                self.abilities.append("BEGUILING DEFENSES")
            elif self.classpath == "The Fiend":
                self.abilities.append("FIENDISH RESISTANCE")
            elif self.classpath == "The Great Old One":
                self.abilities.append("THOUGHT SHIELD")
        if level >= 11:
            self.abilities.append("MYSTIC ARCANUM (6th Level)")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 13:
            self.abilities.append("MYSTIC ARCANUM (7th Level)")
        if level >= 14:
            if self.classpath == "The Archfey":
                self.abilities.append("DARK DELIRIUM")
            elif self.classpath == "The Fiend":
                self.abilities.append("HURL THROUGH HELL")
            elif self.classpath == "The Great Old One":
                self.abilities.append("CREATE THRALL")
        if level >= 15:
            self.abilities.append("MYSTIC ARCANUM (8th Level)")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 17:
            self.abilities.append("MYSTIC ARCANUM (9th Level)")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("ELDRITCH MASTER")
        self.invocations = invocation_cycling(warlock_slots(level))
        self.spells = spell_queue("Warlock", level)
        self.spells = warlock_spell_queue(level)


class Wizard(CharacterClass):
    def __init__(self, level, character_name):
        super(Wizard, self).__init__(character_name=character_name)
        self.name = 'Wizard'
        self.hit_die = 6  # Hit die is 1d8
        self.primary_ability = "Intelligence"  # primary ability is Dex
        self.statblock = stat_selection(self.name, self.primary_ability)
        self.saves = ["Intelligence", "Wisdom"]  # Saving throws are Strength and Constitution
        self.armorpro = []
        self.weaponpro = ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows']
        self.toolpro = []
        self.spells = []
        self.spellcasting = True
        self.spellcasting_ability = "Intelligence"
        self.language = []
        self.wealth = (diceroll(4, 4) * 10)
        x = magic_schools()
        print("pick two(2) skills from this list")
        for key, value in wizard_skill_list().items():
            print(key, value)
        valid = False
        while valid is not True:
            s = validate_choice(len(wizard_skill_list().items()))
            r = validate_choice(len(wizard_skill_list().items()))
            if r == s:
                valid = False
            else:
                valid = True

        if (s == 1) or (r == 1):
            self.arcana_skill = True

        if (s == 2) or (r == 2):
            self.history_skill = True

        if (s == 3) or (r == 3):
            self.insight_skill = True

        if (s == 4) or (r == 4):
            self.investigation_skill = True

        if (s == 5) or (r == 5):
            self.medicine_skill = True

        if (s == 6) or (r == 6):
            self.religion_skill = True

        if level >= 1:
            self.abilities.append("ARCANE RECOVERY")
        if level >= 2:
            clearscreen()
            print("you must now choose your Arcane Tradition, you have the following options:\n")
            for key, value in x.items():
                print(key, value)
            a = validate_choice(len(x.items()), message='Choose Your Arcane Tradition')
            if a == 1:
                self.classpath = "Abjuration"
                self.abilities.append("ABJURATION SAVANT")
                self.abilities.append("ARCANE WARD")
            elif a == 2:
                self.classpath = "Conjuration"
                self.abilities.append("CONJURATION SAVANT")
                self.abilities.append("MINOR CONJURATION")
            elif a == 3:
                self.classpath = "Divination"
                self.abilities.append("DIVINATION SAVANT")
                self.abilities.append("PORTENT")
            elif a == 4:
                self.classpath = "Enchantment"
                self.abilities.append("ENCHANTMENT SAVANT")
                self.abilities.append("HYPNOTIC GAZE")
            elif a == 5:
                self.classpath = "Evocation"
                self.abilities.append("EVOCATION SAVANT")
                self.abilities.append("SCULPT SPELLS")
            elif a == 6:
                self.classpath = "Illusion"
                self.abilities.append("ILLUSION SAVANT")
                self.spells.append("Minor Illusion (Improved)")
            elif a == 7:
                self.classpath = "Necromancy"
                self.abilities.append("NECROMANCY SAVANT")
                self.abilities.append("GRIM HARVEST")
            elif a == 8:
                self.classpath = "Transmutation"
                self.abilities.append("TRANSMUTATION SAVANT")
                self.abilities.append("MINOR ALCHEMY")
        if level >= 4:
            self.ability_up(self.statblock)
        if level >= 6:
            if self.classpath == "Abjuration":
                self.abilities.append("PROJECTED WARD")
            elif self.classpath == "Conjuration":
                self.abilities.append("BENIGN TRANSPOSITION")
            elif self.classpath == "Divination":
                self.abilities.append("EXPERT DIVINATION")
            elif self.classpath == "Enchantment":
                self.abilities.append("INSTINCTIVE CHARM")
            elif self.classpath == "Evocation":
                self.abilities.append("POTENT CANTRIP")
            elif self.classpath == "Illusion":
                self.abilities.append("MALLEABLE ILLUSIONS")
            elif self.classpath == "Necromancy":
                self.abilities.append("UNDEAD THRALLS")
                self.spells.append("Animate Dead")
            elif self.classpath == "Transmutation":
                self.abilities.append("TRANSMUTER\'S STONE")
        if level >= 8:
            self.ability_up(self.statblock)
        if level >= 10:
            if self.classpath == "Abjuration":
                self.abilities.append("IMPROVED ABJURATION")
            elif self.classpath == "Conjuration":
                self.abilities.append("FOCUSED CONJURATION")
            elif self.classpath == "Divination":
                self.abilities.append("THE THIRD EYE")
            elif self.classpath == "Enchantment":
                self.abilities.append("SPLIT ENCHANTMENT")
            elif self.classpath == "Evocation":
                self.abilities.append("EMPOWERED EVOCATION")
            elif self.classpath == "Illusion":
                self.abilities.append("ILLUSORY SELF")
            elif self.classpath == "Necromancy":
                self.abilities.append("INURED TO UNDEATH")
            elif self.classpath == "Transmutation":
                self.abilities.append("SHAPECHANGER")
                self.spells.append("Polymorph")
        if level >= 12:
            self.ability_up(self.statblock)
        if level >= 14:
            if self.classpath == "Abjuration":
                self.abilities.append("SPELL RESISTANCE")
            elif self.classpath == "Conjuration":
                self.abilities.append("DURABLE SUMMONS")
            elif self.classpath == "Divination":
                self.abilities.append("GREATER PORTENT")
            elif self.classpath == "Enchantment":
                self.abilities.append("ALTER MEMORIES")
            elif self.classpath == "Evocation":
                self.abilities.append("OVERCHANNEL")
            elif self.classpath == "Illusion":
                self.abilities.append("ILLUSORY REALITY")
            elif self.classpath == "Necromancy":
                self.abilities.append("COMMAND UNDEAD")
            elif self.classpath == "Transmutation":
                self.abilities.append("MASTER TRANSMUTER")
        if level >= 16:
            self.ability_up(self.statblock)
        if level >= 18:
            self.abilities.append("SPELL MASTERY")
        if level >= 19:
            self.ability_up(self.statblock)
        if level >= 20:
            self.abilities.append("SIGNATURE SPELLS")
        self.spells = spell_queue("Wizard", level)


# Notes to yourself:  Add in Proficiency bonus for each level.
