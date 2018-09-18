def simple_melee_weapons():

    simple_melee_weapons_list = {
        "Club":  {"Cost": "1sp", "Damage": "1d4 Bludgeoning", "Weight": 2, "Properties":  "Light"},
        "Dagger": {"Cost": "2gp", "Damage": "1d4 Piercing", "Weight": 1, "Properties":  "Light, Finesse, "
                                                                                        "Thrown(range 20/60)"},
        "Greatclub": {"Cost": "2sp", "Damage": "1d8 Bludgeoning", "Weight": 10, "Properties":  "Two-Handed"},
        "Handaxe": {"Cost": "5gp", "Damage": "1d6 Slashing", "Weight": 2, "Properties":  "Light, Thrown(range 20/60"},
        "Javelin": {"Cost": "5sp", "Damage": "1d6 Piercing", "Weight": 2, "Properties":  "Thrown(range 30/120)"},
        "Light Hammer": {"Cost": "2gp", "Damage": "1d4 Bludgeoning", "Weight": 2, "Properties":  "Light, "
                                                                                                 "Thrown(range 20/60)"},
        "Mace": {"Cost": "5gp", "Damage": "1d6 Bludgeoning", "Weight": 4, "Properties":  None},
        "Quarterstaff": {"Cost": "2sp", "Damage": "1d6 Bludgeoning", "Weight": 4, "Properties":  "Versatile(1d8)"},
        "Sickle": {"Cost": "1gp", "Damage": "1d4 Slashing", "Weight": 2, "Properties":  "Light"},
        "Spear": {"Cost": "1gp", "Damage": "1d6 Piercing", "Weight": 3, "Properties":
                                                                        "Thrown(range 20/60), Versatile(1d8)"}}

    return simple_melee_weapons_list


def simple_ranged_weapons():
    simple_ranged_weapons_list = {
        "Crossbow, light": {"Cost": "25gp", "Damage": "1d8 Piercing", "Weight": 5, "Properties":  "Ammunition, "
                                                      "(range 80/320), Loading, Two-Handed"},
        "Dart": {"Cost": "5cp", "Damage": "1d4 Piercing", "Weight": 1/4, "Properties":  "Finesse, Thrown(20/60)"},
        "Shortbow": {"Cost": "25gp", "Damage": "1d6 Piercing", "Weight": 2, "Properties":  "Ammunition, (range 80/320),"
                                                                                           " Two-Handed"},
        "Sling": {"Cost": "1sp", "Damage": "1d4 Bludgeoning", "Weight": None, "Properties":
                                                                              "Ammunition, (range 30/120)"}}
    return simple_ranged_weapons_list


def martial_melee_weapons():
    martial_melee_weapons_list = {
        "Battleaxe": {"Cost": "10gp", "Damage": "1d8 Slashing", "Weight": 4, "Properties":  "Versatile(1d10)"},
        "Flail": {"Cost": "10gp", "Damage": "1d8 Bludgeoning", "Weight": 2, "Properties":  None},
        "Glaive": {"Cost": "20gp", "Damage": "1d10 Slashing", "Weight": 6, "Properties":  "Heavy, Reach, Two-handed"},
        "Greataxe": {"Cost": "30gp", "Damage": "1d12 Slashing", "Weight": 6, "Properties":  "Reach, Special"},
        "Greatsword": {"Cost": "50gp", "Damage": "2d6 Slashing", "Weight": 6, "Properties":  "Heavy, Two-handed"},
        "Halberd": {"Cost": "20gp", "Damage": "1d10 Slashing", "Weight": 6, "Properties":  "Heavy, Reach, Two-handed"},
        "Lance": {"Cost": "10gp", "Damage": "1d12 Piercing", "Weight": 6, "Properties":  "Reach, Special"},
        "Longsword": {"Cost": "15gp", "Damage": "1d8 Slashing", "Weight": 3, "Properties":  "Versatile(1d10"},
        "Maul": {"Cost": "10gp", "Damage": "2d6 Bludgeoning", "Weight": 10, "Properties":  "Heavy, Two-handed"},
        "Morningstar": {"Cost": "15gp", "Damage": "1d8 Piercing", "Weight": 4, "Properties":  None},
        "Pike": {"Cost": "5gp", "Damage": "1d10 Piercing", "Weight": 18, "Properties":  "Heavy, Reach, Two-handed"},
        "Rapier": {"Cost": "25gp", "Damage": "1d8 Piercing", "Weight": 2, "Properties": "Finesse"},
        "Scimitar": {"Cost": "25gp", "Damage": "1d6 Slashing", "Weight": 3, "Properties": "Light, Finesse"},
        "Shortsword": {"Cost": "10gp", "Damage": "1d6 Piercing", "Weight": 2, "Properties": "Light, Finesse"},
        "Trident": {"Cost": "5gp", "Damage": "1d6 Piercing", "Weight": 4, "Properties": "Thrown (range 20/60), "
                                                                                        "Versatile(1d8)"},
        "War Pick": {"Cost": "5gp", "Damage": "1d8 Piercing", "Weight": 2, "Properties": None},
        "Warhammer": {"Cost": "15gp", "Damage": "1d8 Bludgeoning", "Weight": 2, "Properties": "Versatile(1d8)"},
        "Whip": {"Cost": "2gp", "Damage": "1d4 Slashing", "Weight": 3, "Properties": "Finesse, Reach"},
        }
    return martial_melee_weapons_list


def martial_ranged_weapons():
    martial_ranged_weapons_list = {
        "Blowgun": {"Cost": "10gp", "Damage": "1 Piercing", "Weight": 1, "Properties": "Ammunition (range 25/100), "
                                                                                       "Loading"},
        "Crossbow, hand": {"Cost": "75gp", "Damage": "1d6 Piercing", "Weight": 3, "Properties":
                                                     "Ammunition (range 30/120), Light, Loading"},
        "Crossbow, heavy": {"Cost": "50gp", "Damage": "1d10 Piercing", "Weight": 18, "Properties":
                                            "Ammunition (range 100/400), Heavy, Loading, Two-handed"},
        "Longbow": {"Cost": "50gp", "Damage": "1d8 Piercing", "Weight": 2, "Properties":
                                              "Ammunition (range 150/600), Heavy, Two-handed"},
        "Net": {"Cost": "1gp", "Damage": None, "Weight": 3, "Properties": "Special, Thrown (range 5/15)"},
    }
    return martial_ranged_weapons_list


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
        "Woodcarver's Tools": {"Cost": "1gp", "Weight": 5},}
    return artisan_tool_list


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
