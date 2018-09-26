def choose_wizard_cantrip():
    cantrips = {
        1: "Acid Splash",
        2: "Blade Ward",
        3: "Chill Touch",
        4: "Dancing Lights",
        5: "Fire Bolt",
        6: "Friends",
        7: "Light",
        8: "Mage Hand",
        9: "Mending",
        10: "Message",
        11: "Minor Illusion",
        12: "Poison Spray",
        13: "Prestidigitation",
        14: "Ray of Frost",
        15: "Shocking Grasp",
        16: "Shocking Grasp",
        17: "True Strike",
    }
    try:
        for key, value in cantrips.items():
            print(key, value)

        return cantrips.get(int(input("Which Cantrip? (Enter a number):")))
    except TypeError:
        print("ERROR!!!! Enter a numerical value within range")
        for key, value in cantrips.items():
            print(key, value)
        return cantrips.get(int(input("Which Cantrip? (Enter a number):")))

