
from modifiers import validate_choice, clearscreen


def starting_equipment(klass, background, proficiencies):
    clearscreen()
    print('Choose Starting Equipment for your Class:' + str(klass))
    equipment_list = []

# BARBARIAN
    if klass == "Barbarian":
        print('1: A Greataxe')
        print('2: Any Martial Melee Weapon')
        a = validate_choice(2, message="Enter 1 or 2:")
        if a == 1:
            equipment_list.append("Greataxe")
            print('Greataxe added to inventory')
        else:
            x = martial_melee_names()
            equipment_list.append(x)
            print("{} added to inventory".format(x))
        for i in packs().get("Explorer's Pack"):
            equipment_list.append(i)
        equipment_list.append('Javelin')
        equipment_list.append('Javelin')
        equipment_list.append('Javelin')
        equipment_list.append('Javelin')

# BARD
    if klass == "Bard":
        print('1: A Rapier')
        print('2: Longsword')
        print('3: Any Simple Weapon')
        a = validate_choice(3)
        if a == 1:
            equipment_list.append("Rapier")
            print('Rapier added to inventory')
        if a == 2:
            equipment_list.append("Longsword")
            print('Longsword added to inventory')
        if a == 3:
            x = simple_melee_names()
            equipment_list.append(x)
            print("{} added to inventory".format(x))
        clearscreen()
        print("1: Diplomat\'s Pack")
        print("2: Entertainer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Diplomat's Pack"):
                equipment_list.append(i)
        else:
            for i in packs().get("Entertainer's Pack"):
                equipment_list.append(i)
        clearscreen()
        print("1: Lute")
        print("2: Any Other Musical Instrument")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Lute")
        else:
            x = musical_instruments_names()
            equipment_list.append(x)
        equipment_list.append("Light Leather Armor")
        equipment_list.append("Dagger")
# CLERIC
    if klass == "Cleric":
        if "-Warhammer" in proficiencies:
            print('1: A Mace')
            print('2: A Warhammer')
            a = validate_choice(2)
            if a == 1:
                equipment_list.append('Mace')
            else:
                equipment_list.append('Warhammer')
        else:
            equipment_list.append("Mace")
        clearscreen()
        if "-Heavy Armor" in proficiencies:
            print('1: Scale Mail')
            print('2: Leather Armor')
            print('3: Chain Mail')
            a = validate_choice(3)
            if a == 1:
                equipment_list.append('Medium Scale Mail Armor')
            if a == 2:
                equipment_list.append('Light Leather Armor')
            else:
                equipment_list.append('Heavy Chain Mail Armor')
        else:
            print('1: Scale Mail')
            print('2: Leather Armor')
            a = validate_choice(2)
            if a == 1:
                equipment_list.append('Medium Scale Mail Armor')
            if a == 2:
                equipment_list.append('Light Leather Armor')
        clearscreen()
        print('1: Light Crossbow and 20 Bolts')
        print('2: Any Simple Weapon')
        a = validate_choice(2)
        if a == 1:
            equipment_list.append('Crossbow, light')
            equipment_list.append('20 bolts')
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        clearscreen()
        print("1: Priest's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Priest's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        equipment_list.append("Shield")
        equipment_list.append("Holy Symbol")
# DRUID
    if klass == 'Druid':
        print("1: Wooden Shield")
        print("2: Any Simple Melee Weapon")
        print("3: Any Simple Ranged Weapon")
        a = validate_choice(3)
        if a == 1:
            equipment_list.append("Wooden Shield")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = simple_ranged_names()
            equipment_list.append(x)
        clearscreen()
        print("1: A Scimitar")
        print("2: Any Simple Melee Weapon")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Scimitar")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        equipment_list.append("Light Leather Armor")
        equipment_list.append("Druidic Focus")
        for i in packs().get("Explorer's Pack"):
            equipment_list.append(i)
# FIGHTER
    if klass == 'Fighter':
        print("1: Chain Mail")
        print("2: Leather Armor, Longbow, 20 Arrows")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Heavy Chain Mail Armor")
        if a == 2:
            equipment_list.append("Light Leather Armor")
            equipment_list.append("Longbow")
            equipment_list.append("20 Arrows")
        clearscreen()
        print("1: A Martial Ranged Weapon and a Shield")
        print("2: A Martial Melee Weapon and a Shield")
        print("3: Two Martial Melee Weapons")
        print("4: Two Martial Ranged Weapons")
        print("5: A Martial Ranged and A Martial Melee Weapon")
        a = validate_choice(5)
        if a == 1:
            equipment_list.append("Metal Shield")
            x = martial_ranged_names()
            equipment_list.append(x)
        if a == 2:
            equipment_list.append("Metal Shield")
            x = martial_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = martial_melee_names()
            y = martial_melee_names()
            equipment_list.append(x)
            equipment_list.append(y)
        if a == 4:
            x = martial_ranged_names()
            y = martial_ranged_names()
            equipment_list.append(x)
            equipment_list.append(y)
        if a == 5:
            x = martial_ranged_names()
            y = martial_melee_names()
            equipment_list.append(x)
            equipment_list.append(y)
        clearscreen()
        print("1: A Light Crossbow and 20 bolts")
        print("2: 2 Handaxes")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Crossbow, light")
            equipment_list.append("20 bolts")
        if a == 2:
            equipment_list.append("Handaxe")
            equipment_list.append("Handaxe")
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        clearscreen()
# MONK
    if klass == 'Monk':
        print("1: A Shortsword")
        print("2: Any Simple Melee Weapon")
        print("3: Any Simple Ranged Weapon")
        a = validate_choice(3)
        if a == 1:
            equipment_list.append("Shortsword")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = simple_ranged_names()
            equipment_list.append(x)
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        for i in range(10):
            equipment_list.append("Dart")
# PALADIN
    if klass == "Paladin":
        print("1: A Martial Ranged Weapon and a Shield")
        print("2: A Martial Melee Weapon and a Shield")
        print("3: Two Martial Melee Weapons")
        print("4: Two Martial Ranged Weapons")
        print("5: A Martial Ranged and A Martial Melee Weapon")
        a = validate_choice(5)
        if a == 1:
            equipment_list.append("Metal Shield")
            x = martial_ranged_names()
            equipment_list.append(x)
        if a == 2:
            equipment_list.append("Metal Shield")
            x = martial_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = martial_melee_names()
            y = martial_melee_names()
            equipment_list.append(x)
            equipment_list.append(y)
        if a == 4:
            x = martial_ranged_names()
            y = martial_ranged_names()
            equipment_list.append(x)
            equipment_list.append(y)
        if a == 5:
            x = martial_ranged_names()
            y = martial_melee_names()
            equipment_list.append(x)
            equipment_list.append(y)
        clearscreen()
        print("1: 5 Javelins")
        print("2: Any Simple Melee Weapon")
        a = validate_choice(2)
        if a == 1:
            for i in range(5):
                equipment_list.append("Javelin")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        clearscreen()
        print("1: Priest's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Priest's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        equipment_list.append("Heavy Chain Mail Armor")
        equipment_list.append("Holy Symbol")
# RANGER
    if klass == 'Ranger':
        print("1: Scale Mail")
        print("2: Leather Armor")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Medium Scale Mail Armor")
        if a == 2:
            equipment_list.append("Light Leather Armor")
        clearscreen()
        print("1: 2 Shortswords")
        print("2: 2 Simple Melee Weapons")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Shortsword")
            equipment_list.append("Shortsword")
        if a == 2:
            x = simple_melee_names()
            y = simple_melee_names()
            equipment_list.append(x)
            equipment_list.append(y)
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        equipment_list.append("Longbow")
        equipment_list.append("20 Arrows")
# ROGUE
    if klass == 'Rogue':
        print("1: Rapier")
        print("2: Shortsword")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Rapier")
        if a == 2:
            equipment_list.append("Shortsword")
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Explorer's Pack")
        print("3: Burglar's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        if a == 3:
            for i in packs().get("Burgler's Pack"):
                equipment_list.append(i)
        equipment_list.append("Light Leather Armor")
        equipment_list.append("Dagger")
        equipment_list.append("Dagger")
# SORCERER
    if klass == 'Sorcerer':
        print("1: A Light Crossbow and 20 bolts")
        print("2: Any Simple Melee Weapon")
        print("3: Any Simple Ranged Weapon")
        a = validate_choice(3)
        if a == 1:
            equipment_list.append("Crossbow, light")
            equipment_list.append("20 bolts")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = simple_ranged_names()
            equipment_list.append(x)
        clearscreen()
        print("1: A Component Pouch")
        print("2: An Arcane Focus")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Component Pouch")
        if a == 2:
            equipment_list.append("Arcane Focus")
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Explorer's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Explorer's Pack"):
                equipment_list.append(i)
        equipment_list.append("Dagger")
        equipment_list.append("Dagger")
# WARLOCK
    if klass == 'Warlock':
        print("1: A Light Crossbow and 20 bolts")
        print("2: Any Simple Melee Weapon")
        print("3: Any Simple Ranged Weapon")
        a = validate_choice(3)
        if a == 1:
            equipment_list.append("Crossbow, light")
            equipment_list.append("20 bolts")
        if a == 2:
            x = simple_melee_names()
            equipment_list.append(x)
        if a == 3:
            x = simple_ranged_names()
            equipment_list.append(x)
        clearscreen()
        print("1: A Component Pouch")
        print("2: An Arcane Focus")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Component Pouch")
        if a == 2:
            equipment_list.append("Arcane Focus")
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Scholar's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Scholar's Pack"):
                equipment_list.append(i)
        equipment_list.append("Light Leather Armor")
        equipment_list.append("Dagger")
        equipment_list.append("Dagger")
        print("1: Simple Melee Weapon")
        print("2: Simple Ranged Weapon")
        a = validate_choice(2)
        if a == 1:
            x = simple_melee_names()
            equipment_list.append(x)
        if a == 2:
            x = simple_ranged_names()
            equipment_list.append(x)
# WIZARD
    if klass == "Wizard":
        print("1: A Quarterstaff")
        print("2: A Dagger")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Quarterstaff")
        if a == 2:
            equipment_list.append("Dagger")
        clearscreen()
        print("1: A Component Pouch")
        print("2: An Arcane Focus")
        a = validate_choice(2)
        if a == 1:
            equipment_list.append("Component Pouch")
        if a == 2:
            equipment_list.append("Arcane Focus")
        clearscreen()
        print("1: Dungeoneer's Pack")
        print("2: Scholar's Pack")
        a = validate_choice(2)
        if a == 1:
            for i in packs().get("Dungeoneer's Pack"):
                equipment_list.append(i)
        if a == 2:
            for i in packs().get("Scholar's Pack"):
                equipment_list.append(i)
        equipment_list.append("Spellbook")
# ACOLYTE
    if background == "Acolyte":
        equipment_list.append("Holy Symbol")
        equipment_list.append("Prayer Book or Prayer Wheel")
        equipment_list.append("5 Sticks of Incense")
        equipment_list.append("vestments")
        equipment_list.append("Set of Common Clothes")
        equipment_list.append("Pouch containing 15gp")
# CHARLATAN
    if background == "Charlatan":
        equipment_list.append("Set of Fine Clothes")
        equipment_list.append("Disguise Kit")
        print("1: Ten Stoppered Bottles Filled with Colored liquid")
        print("2: A Set of Weighted Dice")
        print("3: A Deck of Marked Cards")
        print("4: A Signet Ring of an Imaginary Duke")
        a = validate_choice(4)
        if a == 1:
            equipment_list.append("Ten Stoppered Bottles Filled with Colored Liquid")
        if a == 2:
            equipment_list.append("Set of Weighted Dice")
        if a == 3:
            equipment_list.append("Deck of Marked Cards")
        if a == 4:
            equipment_list.append("Signet Ring of an Imaginary Duke")
        equipment_list.append("Poucn containing 15gp")
# CRIMINAL
    if background == "Criminal / Spy":
        equipment_list.append("Crowbar")
        equipment_list.append("Set of Dark Common Clothes including a Hood")
        equipment_list.append("a pouch containing 15gp")
# ENTERTAINER
    if background == "Entertainer":
        x = musical_instruments_names()
        equipment_list.append(x)
        equipment_list.append("Favor of an Admirer")
        equipment_list.append("Costume")
        equipment_list.append("a pouch containing 15gp")
# GUILD ARTISAN
    if background == "Guild Artisan":
        x = artisan_tools_names()
        equipment_list.append(x)
        equipment_list.append("A Letter of Introduction from your Guild")
        equipment_list.append("A Set of Traveler's Clothes")
        equipment_list.append("a pouch containing 15gp")
# HERMIT
    if background == "Hermit":
        equipment_list.append("A scroll case stuffed full of notes from your studies or prayers")
        equipment_list.append("A Winter Blanket")
        equipment_list.append("Set of Common Clothes")
        equipment_list.append("An Herbalism Kit")
        equipment_list.append("5gp")
# NOBLE
    if background == "Noble":
        equipment_list.append("Set of Fine Clothes")
        equipment_list.append("Signet Ring")
        equipment_list.append("Scroll of Pedigree")
        equipment_list.append("Purse containing 25gp")
# OUTLANDER
    if background == "Outlander":
        equipment_list.append("Staff")
        equipment_list.append("Hunting Trap")
        equipment_list.append("Trophy from an animal you killed")
        equipment_list.append("Set of Traveler's Clothes")
        equipment_list.append("Pouch containing 10gp")
# SAGE
    if background == "Sage":
        equipment_list.append("Bottle of Black Ink")
        equipment_list.append("Quill")
        equipment_list.append("Small Knife")
        equipment_list.append("Letter from a dead colleague posing a question you have not yet been able to answer")
        equipment_list.append("Set of Common Clothes")
        equipment_list.append("Pouch containing 10gp")
# SAILOR
    if (background == "Sailor") or (background == "Pirate"):
        equipment_list.append("Club")
        equipment_list.append("50 Feet of Silk Rope")
        equipment_list.append("Lucky Charm")
        equipment_list.append("Set of Common Clothes")
        equipment_list.append("Pouch containing 10gp")
# SOLDIER
    if background == "Soldier":
        equipment_list.append("Insignia of Rank")
        equipment_list.append("A trophy taken from a fallen enemy")
        equipment_list.append("A set of bone dice or deck of cards")
        equipment_list.append("A set of Common Clothes")
        equipment_list.append("Pouch containing 10gp")
# URCHIN
    if background == "Urchin":
        equipment_list.append("Small Knife")
        equipment_list.append("Map of the city you grew up in")
        equipment_list.append("Pet Mouse")
        equipment_list.append("Token to remember your parents by")
        equipment_list.append("Set of Common Clothes")
        equipment_list.append("Pouch containing 10gp")

    return equipment_list


def simple_melee_names():
    names = {
        1: "Club",
        2: "Dagger",
        3: "Greatclub",
        4: "Handaxe",
        5: "Javelin",
        6: "Light Hammer",
        7: "Mace",
        8: "Quarterstaff",
        9: "Sickle",
        10: "Spear"
    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def simple_melee_weapons():

    simple_melee_weapons_list = {
        "Club":  {"Cost": "1sp", "Damage": "1d4 Bludgeoning", "Weight": '2 lbs', "Properties":  "Light"},
        "Dagger": {"Cost": "2gp", "Damage": "1d4 Piercing", "Weight": '1lb', "Properties":  "Light, Finesse, "
                   "Thrown(range 20/60)"},
        "Greatclub": {"Cost": "2sp", "Damage": "1d8 Bludgeoning", "Weight": '10 lbs', "Properties":  "Two-Handed"},
        "Handaxe": {"Cost": "5gp", "Damage": "1d6 Slashing", "Weight": '2 lbs', "Properties":
                    "Light, Thrown(range 20/60"},
        "Javelin": {"Cost": "5sp", "Damage": "1d6 Piercing", "Weight": '2 lbs', "Properties":  "Thrown(range 30/120)"},
        "Light Hammer": {"Cost": "2gp", "Damage": "1d4 Bludgeoning", "Weight": '2 lbs', "Properties":  "Light, "
                         "Thrown(range 20/60)"},
        "Mace": {"Cost": "5gp", "Damage": "1d6 Bludgeoning", "Weight": '4 lbs', "Properties":  " "},
        "Quarterstaff": {"Cost": "2sp", "Damage": "1d6 Bludgeoning", "Weight": '4 lbs', "Properties":
                         "Versatile(1d8)"},
        "Sickle": {"Cost": "1gp", "Damage": "1d4 Slashing", "Weight": '2 lbs', "Properties":  "Light"},
        "Spear": {"Cost": "1gp", "Damage": "1d6 Piercing", "Weight": '3 lbs', "Properties":
                  "Thrown(range 20/60), Versatile(1d8)"}}

    return simple_melee_weapons_list


def simple_ranged_names():
    names = {
        1: "Crossbow, light",
        2: "Dart",
        3: "Shortbow",
        4: "Sling",

    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def simple_ranged_weapons():
    simple_ranged_weapons_list = {
        "Crossbow, light": {"Cost": "25gp", "Damage": "1d8 Piercing", "Weight": '5 lbs', "Properties":  "Ammunition, "
                                                      "(range 80/320), Loading, Two-Handed"},
        "Dart": {"Cost": "5cp", "Damage": "1d4 Piercing", "Weight": '1/4 lbs', "Properties":  "Finesse, Thrown(20/60)"},
        "Shortbow": {"Cost": "25gp", "Damage": "1d6 Piercing", "Weight": '2 lbs', "Properties":
                     "Ammunition, (range 80/320), Two-Handed"},
        "Sling": {"Cost": "1sp", "Damage": "1d4 Bludgeoning", "Weight": '0 lbs', "Properties":
                  "Ammunition, (range 30/120)"}}
    return simple_ranged_weapons_list


def martial_melee_names():
    names = {
        1: "Battleaxe",
        2: "Flail",
        3: "Glaive",
        4: "Greataxe",
        5: "Greatsword",
        6: "Halberd",
        7: "Lance",
        8: "Longsword",
        9: "Maul",
        10: "Morningstar",
        11: "Pike",
        12: "Rapier",
        13: "Scimitar",
        14: "Trident",
        15: "War Pick",
        16: "Warhammer",
        17: "Whip",
    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def martial_melee_weapons():
    martial_melee_weapons_list = {
        "Battleaxe": {"Cost": "10gp", "Damage": "1d8 Slashing", "Weight": '4 lbs', "Properties":  "Versatile(1d10)"},
        "Flail": {"Cost": "10gp", "Damage": "1d8 Bludgeoning", "Weight": '2 lbs', "Properties":  " "},
        "Glaive": {"Cost": "20gp", "Damage": "1d10 Slashing", "Weight": '6 lbs', "Properties":
                   "Heavy, Reach, Two-handed"},
        "Greataxe": {"Cost": "30gp", "Damage": "1d12 Slashing", "Weight": '6 lbs', "Properties":  "Reach, Special"},
        "Greatsword": {"Cost": "50gp", "Damage": "2d6 Slashing", "Weight": '6 lbs', "Properties":  "Heavy, Two-handed"},
        "Halberd": {"Cost": "20gp", "Damage": "1d10 Slashing", "Weight": '6 lbs', "Properties":
                    "Heavy, Reach, Two-handed"},
        "Lance": {"Cost": "10gp", "Damage": "1d12 Piercing", "Weight": '6 lbs', "Properties":  "Reach, Special"},
        "Longsword": {"Cost": "15gp", "Damage": "1d8 Slashing", "Weight": '3 lbs', "Properties":  "Versatile(1d10)"},
        "Maul": {"Cost": "10gp", "Damage": "2d6 Bludgeoning", "Weight": '10 lbs', "Properties":  "Heavy, Two-handed"},
        "Morningstar": {"Cost": "15gp", "Damage": "1d8 Piercing", "Weight": '4 lbs', "Properties":  " "},
        "Pike": {"Cost": "5gp", "Damage": "1d10 Piercing", "Weight": '18 lbs', "Properties":
                 "Heavy, Reach, Two-handed"},
        "Rapier": {"Cost": "25gp", "Damage": "1d8 Piercing", "Weight": '2 lbs', "Properties": "Finesse"},
        "Scimitar": {"Cost": "25gp", "Damage": "1d6 Slashing", "Weight": '3 lbs', "Properties": "Light, Finesse"},
        "Shortsword": {"Cost": "10gp", "Damage": "1d6 Piercing", "Weight": '2 lbs', "Properties": "Light, Finesse"},
        "Trident": {"Cost": "5gp", "Damage": "1d6 Piercing", "Weight": '4 lbs', "Properties": "Thrown (range 20/60), "
                    "Versatile(1d8)"},
        "War Pick": {"Cost": "5gp", "Damage": "1d8 Piercing", "Weight": '2 lbs', "Properties": " "},
        "Warhammer": {"Cost": "15gp", "Damage": "1d8 Bludgeoning", "Weight": '2 lbs', "Properties": "Versatile(1d8)"},
        "Whip": {"Cost": "2gp", "Damage": "1d4 Slashing", "Weight": '3 lbs', "Properties": "Finesse, Reach"},
        }
    return martial_melee_weapons_list


def martial_ranged_names():
    names = {
        1: "Blowgun",
        2: "Crossbow, hand",
        3: "Crossbow, heavy",
        4: "Longbow",
        5: "Net",

    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def martial_ranged_weapons():
    martial_ranged_weapons_list = {
        "Blowgun": {"Cost": "10gp", "Damage": "1 Piercing", "Weight": '1 lbs', "Properties":
                    "Ammunition (range 25/100), Loading"},
        "Crossbow, hand": {"Cost": "75gp", "Damage": "1d6 Piercing", "Weight": '3 lbs', "Properties":
                                                     "Ammunition (range 30/120), Light, Loading"},
        "Crossbow, heavy": {"Cost": "50gp", "Damage": "1d10 Piercing", "Weight": '18 lbs', "Properties":
                                            "Ammunition (range 100/400), Heavy, Loading, Two-handed"},
        "Longbow": {"Cost": "50gp", "Damage": "1d8 Piercing", "Weight": '2 lbs', "Properties":
                                              "Ammunition (range 150/600), Heavy, Two-handed"},
        "Net": {"Cost": "1gp", "Damage": '0', "Weight": '0 lbs', "Properties": "Special, Thrown (range 5/15)"},
    }
    return martial_ranged_weapons_list


def armor_names():
    names = {
        1: "Light Padded Armor",
        2: "Light Leather Armor",
        3: "Light Studded Leather Armor",
        4: "Medium Hide Armor",
        5: "Medium Chain Shirt Armor",
        6: "Medium Scale Mail Armor",
        7: "Heavy Ring Mail Armor",
        8: "Heavy Chain Mail Armor",

    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def armor():
    arm = {
        "Light Padded Armor": {"Cost": "5gp", "AC": 11, "Weight": "8 lbs", "STR-REQ": 0},
        "Light Leather Armor": {"Cost": "10gp", "AC": 11, "Weight": "10 lbs", "STR-REQ": 0},
        "Light Studded Leather Armor": {"Cost": "45gp", "AC": 12, "Weight": "13 lbs", "STR-REQ": 0},
        "Medium Hide Armor": {"Cost": "10gp", "AC": 12, "Weight": "12 lbs", "STR-REQ": 0},
        "Medium Chain Shirt Armor": {"Cost": "50gp", "AC": 13, "Weight": "13 lbs", "STR-REQ": 0},
        "Medium Scale Mail Armor": {"Cost": "50gp", "AC": 11, "Weight": "10 lbs", "STR-REQ": 0},
        "Heavy Ring Mail Armor": {"Cost": "30gp", "AC": 14, "Weight": "40 lbs", "STR-REQ": 0},
        "Heavy Chain Mail Armor": {"Cost": "75gp", "AC": 16, "Weight": "40 lbs", "STR-REQ": 13}
    }
    return arm


def artisan_tools_names():
    names = {
        1: "Alchemist's Supplies",
        2: "Brewer's Supplies",
        3: "Calligrapher's Tools",
        4: "Carpenter's Tools",
        5: "Cartographer's Tools",
        6: "Cobbler's Tools",
        7: "Cook's Utensils",
        8: "Glassblower's Tools",
        9: "Jeweler's Tools",
        10: "Leatherworker's Tool",
        11: "Mason's Tools",
        12: "Painter's Supplies",
        13: "Potter's Tools",
        14: "Smith's Tools",
        15: "Tinker's Tools",
        16: "Weaver's Tools",
        17: "Woodcarver's Tools"

    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def artisan_tools():
    artisan_tool_list = {

        "Alchemist's Supplies": {"Cost": "50gp", "Weight": 8},
        "Brewer's Supplies": {"Cost": "20gp", "Weight": 9},
        "Calligrapher's Tools": {"Cost": "10gp", "Weight": 5},
        "Carpenter's Tools": {"Cost": "8gp", "Weight": 6},
        "Cartographer's Tools": {"Cost": "15gp", "Weight": 6},
        "Cobbler's Tools": {"Cost": "5gp", "Weight": 5},
        "Cook's Utensils": {"Cost": "1gp", "Weight": 8},
        "Glassblower's Tools": {"Cost": "30gp", "Weight": 5},
        "Jeweler's Tools": {"Cost": "25gp", "Weight": 2},
        "Leatherworker's Tools": {"Cost": "5gp", "Weight": 5},
        "Mason's Tools": {"Cost": "10gp", "Weight": 8},
        "Painter's Supplies": {"Cost": "10gp", "Weight": 5},
        "Potter's Tools": {"Cost": "10gp", "Weight": 3},
        "Smith's Tools": {"Cost": "20gp", "Weight": 8},
        "Tinker's Tools": {"Cost": "50gp", "Weight": 10},
        "Weaver's Tools": {"Cost": "1gp", "Weight": 5},
        "Woodcarver's Tools": {"Cost": "1gp", "Weight": 5}}
    return artisan_tool_list


def musical_instruments_names():
    names = {
        1: "Bagpipes",
        2: "Drum",
        3: "Dulcimer",
        4: "Flute",
        5: "Lute",
        6: "Lyre",
        7: "Horn",
        8: "Pan Flute",
        9: "Shawm",
        10: "Viol",
        11: "Didgeridoo"

    }
    for key, value in names.items():
        print(key, value)
    a = validate_choice(len(names.items()))
    return names.get(a)


def musical_instruments():
    musical_instruments_list = {
        "Bagpipes": {"Cost": "30gp", "Weight": 6},
        "Drum": {"Cost": "6gp", "Weight": 3},
        "Dulcimer": {"Cost": "25gp", "Weight": 3},
        "Flute": {"Cost": "2gp", "Weight": 1},
        "Lute": {"Cost": "35gp", "Weight": 2},
        "Lyre": {"Cost": "30gp", "Weight": 2},
        "Horn": {"Cost": "3gp", "Weight": 2},
        "Pan Flute": {"Cost": "12gp", "Weight": 2},
        "Shawm": {"Cost": "2gp", "Weight": 1},
        "Viol": {"Cost": "30gp", "Weight": 1},
        "Didgeridoo": {"Cost": "2gp", 'Weight': 6}

    }
    return musical_instruments_list


def misc_tools():
    misc_tools_list = {
        "Disguise Kit": {"Cost": " 25gp", "Weight": 3},
        "Forgery Kit": {"Cost": " 15gp", "Weight": 5},
        "Herbalism Kit": {"Cost": " 5gp", "Weight": 3},
        "Navigator's Tools": {"Cost": " 25gp", "Weight": 2},
        "Poisoner's Kit": {"Cost": " 50gp", "Weight": 2},
        "Thieves Tools": {"Cost": " 25gp", "Weight": 1}
    }
    return misc_tools_list


def gaming_sets():
    gaming_sets_list = {
        "Dice Set": {"Cost": " 1sp", "Weight": None},
        "Dragonchess Set ": {"Cost": " 1gp", "Weight": 1/2},
        "Playing Card Set": {"Cost": " 5sp", "Weight": None},
        "Three-Dragon Ante Set": {"Cost": " 1gp", "Weight": None}
                  }
    return gaming_sets_list


def packs():
    packs = {
       "Burglar's Pack": ['backpack', 'bag of 1,000 ball bearings', '10 feet of string', 'bell', '5 candles',
                          'crowbar', 'hammer', '10 pitons', 'hooded lantern', '2 flasks of oil', '5 days rations',
                          'tinderbox', 'waterskin', '50 feet of hempen rope'],
       "Diplomat's Pack": ['chest', '2 cases for maps and scrolls', 'set of fine clothes', 'bottle of ink', 'ink pen',
                           'lamp', '2 flasks of oil', '5 sheets of paper', 'vial of perfume', 'sealing wax', 'soap'],
       "Dungeoneer's Pack": ['backpack', 'crowbar', 'hammer', '10 pitons', '10 torches', 'tinderbox',
                             '10 days of rations', 'waterskin', '50 feet of hempen rope'],
       "Entertainer's Pack": ['backpack', 'bedroll', '2 costumes', '5 candles', '5 days of rations',
                              'waterskin', 'disguise kit'],
       "Explorer's Pack": ['backpack', 'bedroll', 'mess kit', 'tinderbox', '10 torches', '10 days of rations',
                           'waterskin', '50 feet of hempen rope'],
       "Priest's Pack": ['backpack', 'blanket', '10 candles', 'tinderbox', 'alms box', '2 blocks of incense',
                         'censer', 'vestments', '2 days of rations', 'waterskin'],
       "Scholar's Pack": ['backpack', 'book of lore', 'bottle of ink', 'ink pen', '10 sheets of parchment',
                          'little bag of sand', 'a small knife'],
    }
    return packs


def tool(selection):
    x = selection
    rtnlist = []
    selldict = {}
    count = 1
    for key, value in x.items():
        print(count, key)
        selldict[count] = key
        count += 1
    a = validate_choice(len(x.items()), message='Choose an item: ')
    return selldict.get(a)


def in_sheath(name, lst):
    count = 0
    for i in range(len(lst)):
        if name in lst[count].get('name'):
            return True
        else:
            pass
        count += 1
    return False


# if __name__ == '__main__':
