

def skill_check(skill):
    skill_list = {
        "Acrobatics": "Dexterity",
        "Animal Handling": "Wisdom",
        "Arcana": "Intelligence",
        "Athletics": "Strength",
        "Deception": "Charisma",
        "History": "Intelligence",
        "Insight": "Wisdom",
        "Intimidation": "Charisma",
        "Investigation": "Intelligence",
        "Medicine": "Wisdom",
        "Nature": "Intelligence",
        "Perception": "Wisdom",
        "Performance": "Charisma",
        "Religion": "Intelligence",
        "Slight of Hand": "Dexterity",
        "Stealth": "Dexterity",
        "Survival": "Wisdom"
    }
    return skill_list.get(skill)
