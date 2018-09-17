def choose_language():
    languages = {
        1: "Abyssal",
        2: "Aquan",
        3: "Auran",
        4: "Celestial",
        5: "Common",
        6: "Deep Speech",
        7: "Draconic",
        8: "Druidic",
        9: "Dwarvish",
        10: "Elvish",
        11: "Giant",
        12: "Gnomish",
        13: "Goblin",
        14: "Gnoll",
        15: "Halfling",
        16: "Ignan",
        17: "Infernal",
        18: "Orc",
        19: "Primordial",
        20: "Sylvan",
        21: "Terran",
        22: "Undercommon"
    }
    try:
        for key, value in languages.items():
            print(key, value)

        return languages.get(int(input("What Language? (Enter a number):")))
    except TypeError:
        print("ERROR!!!! Enter a numerical value within range")
        for key, value in languages.items():
            print(key, value)

        return languages.get(int(input("What Language? (Enter a number):")))
