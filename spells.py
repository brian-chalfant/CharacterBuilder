def bard_slots(level):
    slots = {
        1:  {0: 2, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2:  {0: 2, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3:  {0: 2, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4:  {0: 3, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5:  {0: 3, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6:  {0: 3, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7:  {0: 3, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8:  {0: 3, 1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9:  {0: 3, 1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
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
    else:
        TypeError


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
        1:  {0: 3, 1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2:  {0: 3, 1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3:  {0: 3, 1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4:  {0: 4, 1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5:  {0: 4, 1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6:  {0: 4, 1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7:  {0: 4, 1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8:  {0: 4, 1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9:  {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
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
    else:
        TypeError


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
