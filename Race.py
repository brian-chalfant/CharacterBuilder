from random import randrange

from DiceRoll import initial_diceroll
from language import choose_language
from modifiers import draconic_lines, clearscreen, validate_choice
from spells import single_spell_select


# character_name = input("Enter Character Name: ")
# character_name = character_name.strip()
# print(character_name.upper())


class Race:
    def __init__(self, level=None):
        self.name = ''
        self.intelligence = 0
        self.dexterity = 0
        self.wisdom = 0
        self.charisma = 0
        self.constitution = 0
        self.strength = 0
        self.language = ["Common"]
        self.weaponpro = []
        self.cantrip = []
        self.abilities = []
        self.speed = 25
        self.size = 'Medium'
        self.height = 0
        self.weight = 0
        self.eyes = ''
        self.skin = ''
        self.hair = ''

        if level is None:
            level = 1
        self.level = level

    def get_intelligence(self):
        return self.intelligence

    def get_dexterity(self):
        return self.dexterity

    def get_wisdom(self):
        return self.wisdom

    def get_strength(self):
        return self.strength

    def get_charisma(self):
        return self.charisma

    def get_constitution(self):
        return self.constitution

# Start Aarokocra --------------------------------------------------


class Aarakocra(Race):
    def __init__(self):
        super(Aarakocra, self).__init__()
        self.name = 'Aarakocra'
        self.dexterity += 1
        self.wisdom += 1
        self.abilities = []
        self.attacks = ["TALONS, 1d4 Slashing"]
        self.language.append("Aarakocra")
        self.language.append("Auran")
        self.speed = 25
        self.height = randrange(45, 57)
        self.weight = randrange(80, 100)
        self.size = "Medium"


# Start Dragonborn --------------------------------------------------
class Dragonborn(Race):
    def __init__(self, character_name):
        super(Dragonborn, self).__init__()
        self.name = 'Dragonborn'
        self.strength += 2
        self.charisma += 1
        self.speed = 30
        self.abilities = ["DAMAGE RESISTANCE"]
        clearscreen()
        print("What type of Dragonborn is {}".format(character_name))
        for key, value in draconic_lines().items():
            print(key, value)
        x = validate_choice(len(draconic_lines().items()))
        if x <= 5:
            xtype = "5 by 30 ft. line (Dex Save)"
        else:
            xtype = "15 ft. Cone (Dex Save)"
        self.attacks = ["BREATH WEAPON" + xtype]
        self.language.append("Draconic")

# Start Dwarf --------------------------------------------------


class Dwarf(Race):
    def __init__(self):
        super(Dwarf, self).__init__()
        self.constitution += 2
        self.abilities = ["DARKVISION", "DWARVEN RESILIENCE", "DWARVEN COMBAT TRAINING", "STONECUNNING"]
        self.language.append("Dwarvish")
        self.weaponpro = ['Battleaxe', 'Handaxe', 'Light hammer', 'Warhammer']
        self.speed = 25


class HillDwarf(Dwarf):
    def __init__(self):
        super(HillDwarf, self).__init__()
        self.wisdom += 1
        self.abilities.append("DWARVEN TOUGHNESS")
        self.name = 'Hill Dwarf'


class MountainDwarf(Dwarf):
    def __init__(self):
        super(MountainDwarf, self).__init__()
        self.strength += 2
        self.abilities.append("DWARVEN ARMOUR TRAINING")
        self.name = 'Mountain Dwarf'


# Start Elf --------------------------------------------------
class Elf(Race):
    def __init__(self):
        super(Elf, self).__init__()
        self.dexterity += 2
        self.name = 'Elf'
        self.abilities = ["FEY ANCESTRY", "TRANCE"]
        self.language.append("Elvish")
        self.speed = 30


class HighElf(Elf):
    def __init__(self):
        super(HighElf, self).__init__()
        self.intelligence += 1
        self.name = 'High Elf'
        self.magic = True
        x = single_spell_select('Wizard', 0)
        self.cantrip = [x]
        clearscreen()
        self.language.append(str(choose_language(self.language)))


class WoodElf(Elf):
    def __init__(self):
        super(WoodElf, self).__init__()
        self.wisdom += 1
        self.name = 'Wood Elf'
        self.abilities = ["ELF WEAPON TRAINING", "FLEET OF FOOT", "MASK OF THE WILD"]


class Eladrin(Elf):
    def __init__(self):
        super(Eladrin, self).__init__()
        self.intelligence += 1
        self.name = 'Eladrin'
        self.abilities = ["ELF WEAPON TRAINING", "FEY STEP"]


class DrowElf(Elf):
    def __init__(self, level):
        super(DrowElf, self).__init__()
        self.charisma += 1
        self.name = 'Drow Elf'
        self.abilities = ["SUPERIOR DARKVISION", "DROW MAGIC", "DROW WEAPON TRAINING", "SUNLIGHT SENSITIVITY"]
        self.magic = True
        self.cantrip = ["DANCING LIGHTS"]
        if level > 3:
            self.cantrip.append("FAIRIE FIRE")
        elif level > 5:
            self.cantrip.append("FAIRIE FIRE")
            self.cantrip.append("DARKNESS")


# Start Genasi --------------------------------------------------
class Genasi(Race):
    def __init__(self):
        super(Genasi, self).__init__()
        self.constitution += 2
        self.name = 'Genasi'
        self.speed = 30
        self.abilities = []
        self.language.append("Primordial")


class AirGenasi(Genasi):
    def __init__(self):
        super(AirGenasi, self).__init__()
        self.dexterity += 1
        self.name = 'Air Genasi'
        self.abilities.append("UNENDING BREATH")
        self.abilities.append("MINGLE WITH THE WIND")
        self.magic = True
        self.cantrip = ["LEVITATE"]


class EarthGenasi(Genasi):
    def __init__(self):
        super(EarthGenasi, self).__init__()
        self.strength += 1
        self.name = 'Earth Genasi'
        self.abilities.append("EARTH WALK")
        self.abilities.append("MERGE WITH STONE")
        self.magic = True
        self.cantrip = ["PASS WITHOUT TRACE"]


class FireGenasi(Genasi):
    def __init__(self):
        super(FireGenasi, self).__init__()
        self.intelligence += 1
        self.name = 'Fire Genasi'
        self.abilities.append("DARKVISION")
        self.abilities.append("FIRE RESISTANCE")
        self.abilities.append("REACH THE BLAZE")
        self.magic = True
        self.cantrip = ["PRODUCE FLAME"]


class WaterGenasi(Genasi):
    def __init__(self):
        super(WaterGenasi, self).__init__()
        self.wisdom += 1
        self.name = 'Water Genasi'
        self.abilities.append("ACID RESISTANCE")
        self.abilities.append("AMPHIBIOUS")
        self.abilities.append("SWIM")
        self.abilities.append("CALL TO THE WAVE")
        self.magic = True
        self.cantrip = ["SHAPE WATER"]


# Start Gnome --------------------------------------------------
class Gnome(Race):
    def __init__(self):
        super(Gnome, self).__init__()
        self.intelligence += 2
        self.name = 'Gnome'
        self.speed = 25
        self.abilities = ["DARKVISION", "GNOME CUNNING"]
        self.language.append("Gnomish")


class RockGnome(Gnome):
    def __init__(self):
        super(RockGnome, self).__init__()
        self.constitution += 1
        self.name = 'Rock Gnome'
        self.abilities.append("ARTIFICER'S LORE")
        self.abilities.append("TINKER")


class DeepGnome(Gnome):
    def __init__(self):
        super(DeepGnome, self).__init__()
        self.dexterity += 1
        self.name = 'Deep Gnome'
        self.abilities.append("SUPERIOR DARKVISION")
        self.abilities.append("STONE CAMOUFLAGE")
        self.language.append("Undercommon")


# Start Goliath --------------------------------------------------
class Goliath(Race):
    def __init__(self):
        super(Goliath, self).__init__()
        self.strength += 2
        self.constitution += 1
        self.name = 'Goliath'
        self.speed = 30
        self.abilities = ["NATURAL ATHLETE", "STONE'S ENDURANCE", "POWERFUL BUILD", "MOUNTAIN BORN"]
        self.language.append("Giant")


# Start Half-Elf --------------------------------------------------
class HalfElf(Race):
    def __init__(self):
        super(HalfElf, self).__init__()
        self.charisma += 2
        self.name = 'Half-Elf'
        self.speed = 30
        self.abilities = ["DARKVISION", "FEY ANCESTRY", "SKILL VERSATILITY"]
        self.language.append("Elvish")
        clearscreen()
        self.language.append(str(choose_language(self.language)))


# Start HalfOrc --------------------------------------------------
class HalfOrc(Race):
    def __init__(self):
        super(HalfOrc, self).__init__()
        self.strength += 2
        self.strength += 1
        self.name = 'Half-Orc'
        self.speed = 30
        self.abilities = ["DARKVISION", "MENACING", "RELENTLESS ENDURANCE", "SAVAGE ATTACKS"]
        self.language.append("Orc")


# Start Halfling --------------------------------------------------
class Halfling(Race):
    def __init__(self):
        super(Halfling, self).__init__()
        self.dexterity += 2
        self.name = 'Halfling'
        self.speed = 25
        self.abilities = ["LUCKY", "BRAVE", "HALFLING NIMBLENESS"]
        self.language.append("Halfling")


class LightfootHalfling(Halfling):
    def __init__(self):
        super(LightfootHalfling, self).__init__()
        self.charisma += 1
        self.name = 'Lightfoot Halfling'
        self.abilities.append("NATURALLY STEALTHY")


class StoutHalfling(Halfling):
    def __init__(self):
        super(StoutHalfling, self).__init__()
        self.constitution += 1
        self.name = 'Stout Halfling'
        self.abilities.append("STOUT RESILIENCE")


# Start Human --------------------------------------------------
class Human(Race):
    def __init__(self):
        super(Human, self).__init__()
        self.constitution += 1
        self.charisma += 1
        self.dexterity += 1
        self.intelligence += 1
        self.wisdom += 1
        self.strength += 1
        self.name = 'Human'
        self.speed = 30
        self.language.append(str(choose_language(self.language)))
        self.abilities = []


# Start Tiefling --------------------------------------------------
class Tiefling(Race):
    def __init__(self):
        super(Tiefling, self).__init__()
        self.intelligence += 1
        self.charisma += 2
        self.name = 'Tiefling'
        self.speed = 30
        self.abilities = ["DARKVISION", "HELLISH RESISTANCE", "INFERNAL LEGACY"]
        self.magic = True
        self.cantrip = ["THAUMATURGY"]
        self.language.append("Infernal")
