def bard_slots(level):
    slots = {
        1: {0: 2, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {0: 3, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {0: 3, 1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {0: 3, 1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }
    return slots.get(level)


def bard(level):
    spell_list_0 = {
        0: 'CANTRIPS',
        1: 'Blade Ward',
        2: 'Dancing Lights',
        3: 'Friends',
        4: 'Light',
        5: 'Mage Hand',
        6: 'Mending',
        7: 'Message',
        8: 'Message',
        9: 'Minor Illusion',
        10: 'Prestidigitation',
        11: 'True Strike'
    }

    spell_list_1 = {
        0: 'LEVEL 1 SPELLS',
        1: 'Animal Friendship',
        2: 'Bane',
        3: 'Charm Person',
        4: 'Comprehend Languages',
        5: 'Cure',
        6: 'Detect Magic',
        7: 'Wounds',
        8: 'Detect Magic',
        9: 'Disguise Self',
        10: 'Dissonant Whispers',
        11: 'Faerie Fire',
        12: 'Feather Fall',
        13: 'Healing Word',
        14: 'Heroism',
        15: 'Identify',
        16: 'Illusory Script',
        17: 'Longstrider',
        18: 'Silent Image',
        19: 'Sleep',
        20: 'Speak with Animals',
        21: 'Tasha\'s Hideous Laughter',
        22: 'Thunderwave',
        23: 'Unseen Servant'
    }

    spell_list_2 = {
        0: 'LEVEL 2 SPELLS',
        1: 'Animal Messenger',
        2: 'Blindness/Deafness',
        3: 'Calm Emotions',
        4: 'Cloud of Daggers',
        5: 'Crown of Madness',
        6: 'Detect Thoughts',
        7: 'Enhance Ability',
        8: 'Enthrall',
        9: 'Heat Metal',
        10: 'Hold Person',
        11: 'Invisibility',
        12: 'Knock',
        13: 'Lesser Restoration',
        14: 'Locate Animals or Plants',
        15: 'Locate Object',
        16: 'Magic Mouth',
        17: 'Phantasmal Force',
        18: 'See Invisibility',
        19: 'Shatter',
        20: 'Silence',
        21: 'Suggestion',
        22: 'Zone of Truth'
    }

    spell_list_3 = {
        0: 'LEVEL 3 SPELLS',
        1: 'Bestow Curse',
        2: 'Clairvoyance',
        3: 'Dispel Magic',
        4: 'Fear',
        5: 'Feign Death',
        6: 'Glyph of Warding',
        7: 'Hypnotic Pattern',
        8: 'Leomund\'s Tiny Hut',
        9: 'Major Image',
        10: 'Nondetection',
        11: 'Plant Growth',
        12: 'Sending',
        13: 'Speak with Dead',
        14: 'Speak with Plants',
        15: 'Stinking Cloud',
        16: 'Tongues'
    }

    spell_list_4 = {
        0: 'LEVEL 4 SPELLS',
        1: 'Compulsion',
        2: 'Confusion',
        3: 'Dimension Door',
        4: 'Freedom of Movement',
        5: 'Greater Invisibility',
        6: 'Hallucinatory Terrain',
        7: 'Locate Creature',
        8: 'Polymorph'
    }

    spell_list_5 = {
        0: 'LEVEL 5 SPELLS',
        1: 'Animate Objects',
        2: 'Awaken',
        3: 'Dominate Person',
        4: 'Dream',
        5: 'Geas',
        6: 'Greater Restoration',
        7: 'Hold Monster',
        8: 'Legend Lore',
        9: 'Mass Cure Wounds',
        10: 'Mislead',
        11: 'Modify Memory',
        12: 'Planar Binding',
        13: 'Raise Dead',
        14: 'Scrying',
        15: 'Seeming',
        16: 'Teleportation Circle'
    }

    spell_list_6 = {
        0: 'LEVEL 6 SPELLS',
        1: 'Eyebite',
        2: 'Find the Path',
        3: 'Guards and Wards',
        4: 'Mass Suggestion',
        5: 'Otto\'s Irresistible Dance',
        6: 'Programmed Illusion',
        7: 'True Seeing'
    }

    spell_list_7 = {
        0: 'LEVEL 7 SPELLS',
        1: 'Etherealness',
        2: 'Forcecage',
        3: 'Mirage Arcane',
        4: 'Mordenkainen\'s Magnificent Mansion',
        5: 'Mordenkainen\'s Sword',
        6: 'Project Image',
        7: 'Regenerate',
        8: 'Resurrection',
        9: 'Symbol',
        10: 'Teleport'
    }

    spell_list_8 = {
        0: 'LEVEL 8 SPELLS',
        1: 'Dominate Monster',
        2: 'Feeblemind',
        3: 'Glibness',
        4: 'Mind Blank',
        5: 'Power Word Stun'
    }

    spell_list_9 = {
        0: 'LEVEL 9 SPELLS',
        1: 'Foresight',
        2: 'Power Word Heal',
        3: 'Power Word Kill',
        4: 'True Polymorph'
    }

    if level == 0:
        return spell_list_0
    elif level == 1:
        return spell_list_1
    elif level == 2:
        return spell_list_2
    elif level == 3:
        return spell_list_3
    elif level == 4:
        return spell_list_4
    elif level == 5:
        return spell_list_5
    elif level == 6:
        return spell_list_6
    elif level == 7:
        return spell_list_7
    elif level == 8:
        return spell_list_8
    elif level == 9:
        return spell_list_9


def bard_magic_selection(spell_dict):
    spell_list = []
    for j in range(10):
        x = bard(j)
        for i in range(spell_dict.get(j)):
            for keys, values in x.items():
                print(keys, values)
            print("you have", (spell_dict.get(j) - i), "Spells in this Level Remaining")
            item_number = int(input("Please choose a Spell: "))
            selection = x.pop(item_number)
            spell_list.append(str(selection))
    return spell_list


# a = magic_selection(bard_slots(10))
# print(a)
def cleric_slots(level):
    slots = {
        1: {0: 3, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {0: 3, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {0: 3, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {0: 4, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {0: 4, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {0: 4, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {0: 4, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {0: 4, 1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {0: 5, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }
    return slots.get(level)


def cleric(level):
    spell_list_0 = {
        0: 'CANTRIPS',
        1: 'Guidance',
        2: 'Light',
        3: 'Mending',
        4: 'Resistance',
        5: 'Sacred Flame',
        6: 'Spare the Dying',
        7: 'Thaumaturgy',
    }

    spell_list_1 = {
        0: 'LEVEL 1 SPELLS',
        1: 'Bane',
        2: 'Bless',
        3: 'Command',
        4: 'Create or Destroy Water',
        5: 'Cure Wounds',
        6: 'Detect Evil and Good',
        7: 'Detect Magic',
        8: 'Detect Poison and Disease',
        9: 'Guiding Bolt',
        10: 'Healing Word',
        11: 'Inflict Wounds',
        12: 'Protection from Evil and Good',
        13: 'Purify Food and Drink',
        14: 'Sanctuary',
        15: 'Shield of Faith',
    }

    spell_list_2 = {
        0: 'LEVEL 2 SPELLS',
        1: 'Aid',
        2: 'Augury',
        3: 'Blindness/Deafness',
        4: 'Calm Emotions',
        5: 'Continual Flame',
        6: 'Enhance Ability',
        7: 'Find Traps',
        8: 'Gentle Repose',
        9: 'Hold Person',
        10: 'Lesser Restoration',
        11: 'Locate Object',
        12: 'Prayer of Healing',
        13: 'Protection from Poison',
        14: 'Silence',
        15: 'Spiritual Weapon',
        16: 'Warding Bond',
        17: 'Zone of Truth',
    }

    spell_list_3 = {
        0: 'LEVEL 3 SPELLS',
        1: 'Animate Dead',
        2: 'Beacon of Hope',
        3: 'Bestow Curse',
        4: 'Clairvoyance',
        5: 'Create Food and Water',
        6: 'Daylight',
        7: 'Dispel Magic',
        8: 'Feign Death',
        9: 'Glyph of Warding',
        10: 'Magic Circle',
        11: 'Mass Healing Word',
        12: 'Meld into Stone',
        13: 'Protection from Energy',
        14: 'Remove Curse',
        15: 'Revivify',
        16: 'Sending',
        17: 'Speak with Dead',
        18: 'Spirit Guardians',
        19: 'Tongues',
        20: 'Water Walk'
    }

    spell_list_4 = {
        0: 'LEVEL 4 SPELLS',
        1: 'Banishment',
        2: 'Control Water',
        3: 'Death Ward',
        4: 'Divination',
        5: 'Freedom of Movement',
        6: 'Guardian of Faith',
        7: 'Locate Creature',
        8: 'Stone Shape'
    }

    spell_list_5 = {
        0: 'LEVEL 5 SPELLS',
        1: 'Commune',
        2: 'Contagion',
        3: 'Dispel Evil and Good',
        4: 'Flame Strike',
        5: 'Geas',
        6: 'Greater Restoration',
        7: 'Hallow',
        8: 'Insect Plague',
        9: 'Legend Lore',
        10: 'Mass Cure Wounds',
        11: 'Planar Binding',
        12: 'Raise Dead',
        13: 'Scrying',
    }

    spell_list_6 = {
        0: 'LEVEL 6 SPELLS',
        1: 'Blade Barrier',
        2: 'Create Undead',
        3: 'Find the Path',
        4: 'Forbiddance',
        5: 'Harm',
        6: 'Heal',
        7: 'Heroes\'s Feast',
        8: 'Planar Ally',
        9: 'True Seeing',
        10: 'Word of Recall'
    }

    spell_list_7 = {
        0: 'LEVEL 7 SPELLS',
        1: 'Conjure Celestial',
        2: 'Divine Word',
        3: 'Etherealness',
        4: 'Fire Storm',
        5: 'Plane Shift',
        6: 'Regenerate',
        7: 'Resurrection',
        8: 'Symbol',
    }

    spell_list_8 = {
        0: 'LEVEL 8 SPELLS',
        1: 'Anti-magic Field',
        2: 'Control Weather',
        3: 'Earthquake',
        4: 'Holy Aura',
    }

    spell_list_9 = {
        0: 'LEVEL 9 SPELLS',
        1: 'Astral Projection',
        2: 'Gate',
        3: 'Mass Heal',
        4: 'True Resurrection'
    }

    if level == 0:
        return spell_list_0
    elif level == 1:
        return spell_list_1
    elif level == 2:
        return spell_list_2
    elif level == 3:
        return spell_list_3
    elif level == 4:
        return spell_list_4
    elif level == 5:
        return spell_list_5
    elif level == 6:
        return spell_list_6
    elif level == 7:
        return spell_list_7
    elif level == 8:
        return spell_list_8
    elif level == 9:
        return spell_list_9


def cleric_magic_selection(spell_dict):
    spell_list = []
    for j in range(10):
        x = cleric(j)
        for i in range(spell_dict.get(j)):
            for keys, values in x.items():
                print(keys, values)
            print("you have", (spell_dict.get(j) - i), "Spells in this Level Remaining")
            item_number = int(input("Please choose a Spell: "))
            selection = x.pop(item_number)
            spell_list.append(str(selection))
    return spell_list


def druid_slots(level):
    slots = {
        1: {0: 2, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {0: 3, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {0: 3, 1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {0: 3, 1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }
    return slots.get(level)


def druid(level):
    spell_list_0 = {
        0: 'CANTRIPS',
        1: 'Druidcraft',
        2: 'Guidance',
        3: 'Mending',
        4: 'Poison Spray',
        5: 'Produce Flame',
        6: 'Resistance',
        7: 'Shillelagh',
        8: 'Thorn Whip'
    }

    spell_list_1 = {
        0: 'LEVEL 1 SPELLS',
        1: 'Animal Friendship',
        2: 'Charm Person',
        3: 'Create or Destroy Water',
        4: 'Cure Wounds',
        5: 'Detect Magic',
        6: 'Detect Poison and Disease',
        7: 'Entangle',
        8: 'Faerie Fire',
        9: 'Fog Cloud',
        10: 'Goodberry',
        11: 'Healing Word',
        12: 'Jump',
        13: 'Longstrider',
        14: 'Purify Food and Drink',
        15: 'Speak with Animals',
        16: 'Thunderwave'
    }

    spell_list_2 = {
        0: 'LEVEL 2 SPELLS',
        1: 'Animal Messenger',
        2: 'Barkskin',
        3: 'Beast Sense',
        4: 'Darkvision',
        5: 'Enhance Ability',
        6: 'Find Traps',
        7: 'Flame Blade',
        8: 'Flaming Sphere',
        9: 'Gust of Wind',
        10: 'Heat Metal',
        11: 'Hold Person',
        12: 'Lesser Restoration',
        13: 'Locate Animals or Plants',
        14: 'Locate Object',
        15: 'Moonbeam',
        16: 'Pass Without Trace',
        17: 'Protection from Poison',
        18: 'Spike Growth'
    }

    spell_list_3 = {
        0: 'LEVEL 3 SPELLS',
        1: 'Call Lightning',
        2: 'Conjure Animals',
        3: 'Daylight',
        4: 'Dispel Magic',
        5: 'Feign Death',
        6: 'Meld into Stone',
        7: 'Plant Growth',
        8: 'Protection from Energy',
        9: 'Sleet Storm',
        10: 'Speak with Plants',
        11: 'Water Breathing',
        12: 'Water Walk',
        13: 'Wind Wall',
    }

    spell_list_4 = {
        0: 'LEVEL 4 SPELLS',
        1: 'Blight',
        2: 'Confusion',
        3: 'Conjure Minor Elementals',
        4: 'Conjure Woodland Beings',
        5: 'Control Water',
        6: 'Dominate Beast',
        7: 'Freedom of Movement',
        8: 'Giant Insect',
        9: 'Grasping Vine',
        10: 'Hallucinatory Terrain',
        11: 'Ice Storm',
        12: 'Locate Creature',
        13: 'Polymorph',
        14: 'Stoneskin',
        15: 'Wall of Fire'
    }

    spell_list_5 = {
        0: 'LEVEL 5 SPELLS',
        1: 'Antilife Shell',
        2: 'Awaken',
        3: 'Commune with Nature',
        4: 'Conjure Elemental',
        5: 'Contagion',
        6: 'Geas',
        7: 'Greater Restoration',
        8: 'Insect Plague',
        9: 'Mass Cure Wounds',
        10: 'Planar Binding',
        11: 'Reincarnate',
        12: 'Scrying',
        13: 'Tree Stride',
        14: 'Wall of Stone'
    }

    spell_list_6 = {
        0: 'LEVEL 6 SPELLS',
        1: 'Conjure Fey',
        2: 'Find the Path',
        3: 'Heal',
        4: 'Heroes\'s Feast',
        5: 'Move Earth',
        6: 'Sunbeam',
        7: 'Transport via Plants',
        8: 'Wall of Thorns',
        9: 'Wind Walk',
    }

    spell_list_7 = {
        0: 'LEVEL 7 SPELLS',
        1: 'Fire Storm',
        2: 'Mirage Arcane',
        3: 'Plane Shift',
        4: 'Regenerate',
        5: 'Reverse Gravity',
    }

    spell_list_8 = {
        0: 'LEVEL 8 SPELLS',
        1: 'Animal Shapes',
        2: 'Antipathy/Sympathy',
        3: 'Control Weather',
        4: 'Earthquake',
        5: 'Feeblemind',
        6: 'Sunburst',
        7: 'Tsunami'
    }

    spell_list_9 = {
        0: 'LEVEL 9 SPELLS',
        1: 'Foresight',
        2: 'Shapechange',
        3: 'Storm of Vengeance',
        4: 'True Resurrection'
    }

    if level == 0:
        return spell_list_0
    elif level == 1:
        return spell_list_1
    elif level == 2:
        return spell_list_2
    elif level == 3:
        return spell_list_3
    elif level == 4:
        return spell_list_4
    elif level == 5:
        return spell_list_5
    elif level == 6:
        return spell_list_6
    elif level == 7:
        return spell_list_7
    elif level == 8:
        return spell_list_8
    elif level == 9:
        return spell_list_9


def druid_magic_selection(spell_dict):
    spell_list = []
    for j in range(10):
        x = cleric(j)
        for i in range(spell_dict.get(j)):
            for keys, values in x.items():
                print(keys, values)
            print("you have", (spell_dict.get(j) - i), "Spells in this Level Remaining")
            item_number = int(input("Please choose a Spell: "))
            selection = x.pop(item_number)
            spell_list.append(str(selection))
    return spell_list


def fighter_slots(level):
    slots = {
        3: {0: 2, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        12: {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        13: {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        14: {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        15: {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        16: {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        17: {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        18: {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        19: {0: 3, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        20: {0: 3, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
    }
    return slots.get(level)


def fighter(level):
    spell_list_0 = {
        0: 'CANTRIPS',
        1: 'Acid Splash',
        2: 'Blade Ward',
        3: 'Chill Touch',
        4: 'Dancing Lights',
        5: 'Fire Bolt',
        6: 'Friends',
        7: 'Light',
        8: 'Mage Hand',
        9: 'Mending',
        10: 'Message',
        11: 'Minor Illusion',
        12: 'Poison Spray',
        13: 'Prestidigitation',
        14: 'Ray of Frost',
        15: 'Shocking Grasp',
        16: 'True Strike'
    }

    spell_list_1 = {
        0: 'LEVEL 1 SPELLS',
        1: 'Alarm',
        2: 'Burning Hands',
        3: 'Charm Person',
        4: 'Chromatic Orb',
        5: 'Color Spray',
        6: 'Comprehend Languages',
        7: 'Detect Magic',
        8: 'Disguise Self',
        9: 'Expeditious Retreat',
        10: 'False Life',
        11: 'Feather Fall',
        12: 'Find Familiar',
        13: 'Fog Cloud',
        14: 'Grease',
        15: 'Identify',
        16: 'Illusory Script',
        17: 'Jump',
        18: 'Longstrider',
        19: 'Mage Armor',
        20: 'Magic Missile',
        21: 'Protection from Evil and Good',
        22: 'Ray of Sickness',
        23: 'Shield',
        24: 'Silent Image',
        25: 'Sleep',
        26: 'Tasha\'s Hideous Laughter',
        27: 'Tenser\'s Floating Disk',
        28: 'Thunderwave',
        29: 'Unseen Servant',
        30: 'Witch Bolt'
    }

    spell_list_2 = {
        0: 'LEVEL 2 SPELLS',
        1: 'Alter Self',
        2: 'Arcane Lock',
        3: 'Blindness/Deafness',
        4: 'Blur',
        5: 'Cloud of Daggers',
        6: 'Continual Flame',
        7: 'Crown of Madness',
        8: 'Darkness',
        9: 'Darkvision',
        10: 'Detect Thoughts',
        11: 'Enlarge/Reduce',
        12: 'Flaming Sphere',
        13: 'Gentle Repose',
        14: 'Gust of Wind',
        15: 'Hold Person',
        16: 'Invisibility',
        17: 'Knock',
        18: 'Levitate',
        19: 'Locate Object',
        20: 'Magic Mouth',
        21: 'Magic Weapon',
        22: 'Melf\'s Acid Arrow',
        23: 'Mirror Image',
        24: 'Misty Step',
        25: 'Nystul\'s Magic Aura',
        26: 'Phantasmal Force',
        27: 'Ray of Enfeeblement',
        28: 'Rope Trick',
        29: 'Scorching Ray',
        30: 'See Invisibility',
        31: 'Shatter',
        32: 'Spider Climb',
        33: 'Suggestion',
        34: 'Web'
    }

    spell_list_3 = {
        0: 'LEVEL 3 SPELLS',
        1: 'Animate Dead',
        2: 'Bestow Curse',
        3: 'Blink',
        4: 'Clairvoyance',
        5: 'Counterspell',
        6: 'Dispel Magic',
        7: 'Fear',
        8: 'Feign Death',
        9: 'Fireball',
        10: 'Fly',
        11: 'Gaseous Form',
        12: 'Glyph of Warding',
        13: 'Haste',
        14: 'Hypnotic Pattern',
        15: 'Leomund\'s Tiny Hut',
        16: 'Lightning Bolt',
        17: 'Magic Circle',
        18: 'Major Image',
        19: 'Nondetection',
        20: 'Phantom Seed',
        21: 'Protection from Energy',
        22: 'Remove Curse',
        23: 'Sending',
        24: 'Sleet Storm',
        25: 'Slow',
        26: 'Stinking Cloud',
        27: 'Tongues',
        28: 'Vampiric Touch',
        29: 'Water Breathing',

    }

    spell_list_4 = {
        0: 'LEVEL 4 SPELLS',
        1: 'Arcane Eye',
        2: 'Banishment',
        3: 'Blight',
        4: 'Confusion',
        5: 'Conjure Major Elementals',
        6: 'Control Water',
        7: 'Dimension Door',
        8: 'Evard\'s Black Tentacles',
        9: 'Fabricate',
        10: 'Fire Shield',
        11: 'Greater Invisibility',
        12: 'Hallucinatory Terrain',
        13: 'Ice Storm',
        14: 'Leomund\'s Secret Chest',
        15: 'Locate Creature',
        16: 'Mordenkainen\'s Faithful Hound',
        17: 'Mordenkainen\'s Private Sanctum',
        18: 'Otiluke\'s Resilient Sphere',
        19: 'Phantasmal Killer',
        20: 'Polymorph',
        21: 'Stone Shape',
        22: 'Stoneskin',
        23: 'Wall of Fire.',
    }

    spell_list_5 = {
        0: 'LEVEL 5 SPELLS',
        1: 'Animate Objects',
        2: 'Bigby\'s Hand',
        3: 'Cloudkill',
        4: 'Cone of Cold',
        5: 'Conjure Elemental',
        6: 'Contact Other Plane',
        7: 'Creation',
        8: 'Dominate Person',
        9: 'Dream',
        11: 'Geas',
        10: 'Hold Monster',
        12: 'Legend Lore',
        13: 'Mislead',
        14: 'Modify Memory',
        15: 'Passwall',
        16: 'Planar Binding',
        17: 'Rary\'s Telepathic Bond',
        18: 'Scrying',
        19: 'Seeming',
        20: 'Telekinesis',
        21: 'Teleportation Circle',
        22: 'Wall of Force',
        23: 'Wall of Stone',
    }

    spell_list_6 = {
        0: 'LEVEL 6 SPELLS',
        1: 'Arcane Gate',
        2: 'Chain Lightning',
        3: 'Circle of Death',
        4: 'Contingency',
        5: 'Create Undead',
        6: 'Disintegrate',
        7: 'Drawmij\'s Instant Summons',
        8: 'Eyebite',
        9: 'Flesh to Stone',
        10: 'Globe of Invulnerability',
        11: 'Guards and Wards',
        12: 'Magic Jar',
        13: 'Mass Suggestion',
        14: 'Move Earth',
        15: 'Otiluke\'s Freezing Sphere',
        16: 'Otto\'s Irresistible Dance',
        17: 'Programmed Illusion',
        18: 'Sunbeam',
        19: 'True Seeing',
        20: 'Wall of Ice',
    }

    spell_list_7 = {
        0: 'LEVEL 7 SPELLS',
        1: 'Delayed Blast Fireball',
        2: 'Etherealness',
        3: 'Finger of Death',
        4: 'Forcecage',
        5: 'Mirage Arcane',
        6: 'Mordenkainen\'s Magnificent Mansion',
        7: 'Mordenkainen\'s Sword',
        8: 'Plane Shift',
        9: 'Prismatic Spray',
        10: 'Project Image',
        11: 'Reverse Gravity',
        12: 'Sequester',
        13: 'Simulacrum',
        14: 'Symbol',
        15: 'Teleport'
    }

    spell_list_8 = {
        0: 'LEVEL 8 SPELLS',
        1: 'Antimagic Field',
        2: 'Antipathy/Sympathy',
        3: 'Clone',
        4: 'Control Weather',
        5: 'Demiplane',
        6: 'Dominate Monster',
        7: 'Feeblemind',
        8: 'Incendiary Cloud',
        9: 'Maze',
        10: 'Mind Blank',
        11: 'Power Word Stun',
        12: 'Sunburst',
        13: 'Telepathy'
    }

    spell_list_9 = {
        0: 'LEVEL 9 SPELLS',
        1: 'Astral Projection',
        2: 'Foresight',
        3: 'Gate',
        4: 'Imprisonment',
        5: 'Meteor Swarm',
        6: 'Power Word Kill',
        7: 'Prismatic Wall',
        8: 'Shapechange',
        9: 'Time Stop',
        10: 'True Polymorph',
        11: 'Weird',
        12: 'Wish'
    }

    if level == 0:
        return spell_list_0
    elif level == 1:
        return spell_list_1
    elif level == 2:
        return spell_list_2
    elif level == 3:
        return spell_list_3
    elif level == 4:
        return spell_list_4
    elif level == 5:
        return spell_list_5
    elif level == 6:
        return spell_list_6
    elif level == 7:
        return spell_list_7
    elif level == 8:
        return spell_list_8
    elif level == 9:
        return spell_list_9


def fighter_magic_selection(spell_dict):
    spell_list = []
    for j in range(10):
        x = cleric(j)
        for i in range(spell_dict.get(j)):
            for keys, values in x.items():
                print(keys, values)
            print("you have", (spell_dict.get(j) - i), "Spells in this Level Remaining")
            item_number = int(input("Please choose a Spell: "))
            selection = x.pop(item_number)
            spell_list.append(str(selection))
    return spell_list

# There has to be a better way to do this.  maybe make the spells an array and
# link them with classes that they are associated with
