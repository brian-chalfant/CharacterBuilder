
def build_sheet(character_data: dict):
    width = 80
    filename = character_data.get('name') + '-' + character_data.get('race') + " " + character_data.get('klass')
    with open(filename, 'w') as outfile:

        lines = str()
        lines += 'Name:__' + str(character_data.get('name')) + ('_' * (int((width/2)) -
                                                                       int(len(character_data.get('name'))) - 7)
                                                                ) + '         ________     ____   ________   ' + '\n'
        lines += 'Race:__' + str(character_data.get('race')) + ('_' * (int((width/2)) -
                                                                       int(len(character_data.get('race'))) - 7)
                                                                ) + '         \______ \   /  _ \  \______ \  ' + '\n'
        lines += 'Class:__' + str(character_data.get('klass')) + ('_' * (int((width/2)) -
                                                                         int(len(character_data.get('klass'))) - 8)
                                                                ) + '          |    |  \  >  _ </\ |    |  \ ' + '\n'
        lines += 'Background:__' + str(character_data.get('klass')) + ('_' * (int((width/2)) -
                                                                         int(len(character_data.get('klass'))) - 13)
                                                                ) + '          |  __`   \/  <_\ \/ |  __`   \\' + '\n'
        lines += 'Alignment:__' + str(character_data.get('alignment')) + ('_' * (int((width/2)) -
                                                                         int(len(character_data.get('alignment'))) - 12)
                                                                ) + '         /_______  /\_____\ \/_______  /' + '\n'
        lines += 'Level & XP:__Level ' + str(character_data.get('level')) + "____" + str(character_data.get('xp')) + \
                 ('_' * (int((width/2)) - (int(len(character_data.get('level'))) + int(len(character_data.get('xp')))
                                           + 23))) + '                 \/        \/        \/ ' + '\n'
        lines += '+-------------------------------------+  +-AC-------+ +-Ini------+ +-Speed-----+' + '\n'
        lines += '| Inspiration                    [  ] |  |   {}     | |     {}   | |    {}     | \n'.format(
            character_data.get('ac'), character_data.get('initiative'), character_data.get('speed'))
        lines += '| Proficiency Bonus              [{}] |  +----------+ +----------+ +-----------+ \n'.format(
            character_data.get('probonus'))
        lines += '| Passive Wisdom (Perception)    [{}] |  +-Hit Points--------------------------+ \n'.format(
            character_data.get('passive_perception'))
        lines += '+-Stat Block -------------------------+  | Maximum: {}                         | \n'.format(
            character_data.get('hp_maximum'))
        lines += '|[{}] STRENGTH               [{:02}] [{}] |  | Modifier: {}                        | \n'.format(
            character_data.get('str_save'), character_data.get('strength'), character_data.get('strength_mod'),
            character_data.get('hp_modifier'))
        lines += '|[{}] DEXTERITY              [{:02}] [{}] |  | Current:                            | \n'.format(
            character_data.get('dex_save'), character_data.get('dexterity'), character_data.get('dexterity_mod'))
        lines += '|[{}] CONSTITUTION           [{:02}] [{}] |  | Hit Dice: {:26}| \n'.format(
            character_data.get('con_save'), character_data.get('constitution'), character_data.get('constitution_mod'), character_data.get('hit_dice'))
        lines += '|[{}] INTELLIGENCE           [{:02}] [{}] |  +-Death Saves-------------------------+ \n'.format(
            character_data.get('int_save'), character_data.get('intelligence'), character_data.get('intelligence_mod'))
        lines += '|[{}] WISDOM                 [{:02}] [{}] |  | Successes               [ ] [ ] [ ] | \n'.format(
            character_data.get('wis_save'), character_data.get('wisdom'), character_data.get('wisdom_mod'))
        lines += '|[{}] CHARISMA               [{:02}] [{}] |  | Failures                [ ] [ ] [ ] | \n'.format(
            character_data.get('cha_save'), character_data.get('charisma'), character_data.get('charisma_mod'))
        lines += '+-Skills------------------------------+  +-------------------------------------+ \n'
        lines += '| Acrobatics (Dex)           [{}] [{}] |  +-Other Proficiencies & Languages-----+ \n'.format(
            character_data.get('acrobatics_skill'), character_data.get('acrobatics_mod'))
        lines += '| Animal Handling (Wis)      [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('animal_handling_skill'), character_data.get('animal_handling_mod'),
            character_data.get('proficiencies')[0])
        lines += '| Arcana (Int)               [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('arcana_skill'), character_data.get('arcana_mod'),
            character_data.get('proficiencies')[1])
        lines += '| Athletics (Str)            [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('athletics_skill'), character_data.get('athletics_mod'),
            character_data.get('proficiencies')[2])
        lines += '| Deception (Cha)            [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('deception_skill'), character_data.get('deception_mod'),
            character_data.get('proficiencies')[3])
        lines += '| History (Int)              [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('history_skill'), character_data.get('history_mod'),
            character_data.get('proficiencies')[4])
        lines += '| Insight (Wis)              [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('insight_skill'), character_data.get('insight_mod'),
            character_data.get('proficiencies')[5])
        lines += '| Intimidation (Cha)         [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('intimidation_skill'), character_data.get('intimidation_mod'),
            character_data.get('proficiencies')[6])
        lines += '| Investigation (Int)        [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('investigation_skill'), character_data.get('investigation_mod'),
            character_data.get('proficiencies')[7])
        lines += '| Medicine (Wis)             [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('medicine_skill'), character_data.get('medicine_mod'),
            character_data.get('proficiencies')[8])
        lines += '| Nature (Int)               [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('nature_skill'), character_data.get('nature_mod'),
            character_data.get('proficiencies')[9])
        lines += '| Perception (Wis)           [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('perception_skill'), character_data.get('perception_mod'),
            character_data.get('proficiencies')[10])
        lines += '| Performance (Cha)          [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('performance_skill'), character_data.get('performance_mod'),
            character_data.get('proficiencies')[11])
        lines += '| Persuasion (Cha)           [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('persuasion_skill'), character_data.get('persuasion_mod'),
            character_data.get('proficiencies')[12])
        lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('religion_skill'), character_data.get('religion_mod'),
            character_data.get('proficiencies')[13])
        lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('religion_skill'), character_data.get('religion_mod'),
            character_data.get('proficiencies')[14])
        lines += '| Stealth (Dex)              [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('stealth_skill'), character_data.get('stealth_mod'),
            character_data.get('proficiencies')[15])
        lines += '| Survival (Wis)             [{}] [{}] |  |{:37}| \n'.format(
            character_data.get('survival_skill'), character_data.get('survival_mod'),
            character_data.get('proficiencies')[16])
        lines += '|                                     |  |{:37}| \n'.format(character_data.get('proficiencies')[17])
        lines += '+-Currency-+-Treasure-----------------+  |{:37}| \n'.format(character_data.get('proficiencies')[18])
        lines += '| CP [{}]  |                          |  |{:37}| \n'.format(character_data.get('currency_cp'),character_data.get('proficiencies')[18])
        lines += '| SP [{}]  |                          |  |{:37}| \n'.format(character_data.get('currency_cp'),character_data.get('proficiencies')[18])
        lines += '| EP [{}]  |                          |  |{:37}| \n'.format(character_data.get('currency_cp'),character_data.get('proficiencies')[18])
        lines += '| GP [{}]  |                          |  |{:37}| \n'.format(character_data.get('currency_cp'),character_data.get('proficiencies')[18])
        lines += '| PP [{}]  |                          |  |{:37}| \n'.format(character_data.get('currency_cp'),character_data.get('proficiencies')[18])
        lines += '+-Attack--------+-HIT+-Damage/Typ-----+-Properties--------------------+-Weight-+ \n'
        lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('prim_weap_name'),
                                                           character_data.get('prim_weap_hit'),
                                                           character_data.get('prim_weap_dmg'),
                                                           character_data.get('prim_weap_properties'),
                                                           character_data.get('prim_weap_weight'))
        lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('second_weap_name'),
                                                           character_data.get('second_weap_hit'),
                                                           character_data.get('second_weap_dmg'),
                                                           character_data.get('second_weap_properties'),
                                                           character_data.get('second_weap_weight'))
        lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('third_weap_name'),
                                                           character_data.get('third_weap_hit'),
                                                           character_data.get('third_weap_dmg'),
                                                           character_data.get('third_weap_properties'),
                                                           character_data.get('third_weap_weight'))
        lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('fourth_weap_name'),
                                                           character_data.get('fourth_weap_hit'),
                                                           character_data.get('fourth_weap_dmg'),
                                                           character_data.get('fourth_weap_properties'),
                                                           character_data.get('fourth_weap_weight'))
        lines += '+-Features---------------------------------------------------------------------+'
        print(lines)
        for i in text_format(character_data.get('abilities')):
            print(i)
        outfile.writelines(lines)


def text_format(textlist, width=78):
    a = textlist
    print(a)
    b = ''
    for i in a:
        if len(i + b) < width:
            b += " " + i
        else:
            yield decorater(b)
            b = '' + i
    return decorater(b)


def decorater(linetext):
    a = '|{:78}|'.format(linetext)
    return a



if __name__ == '__main__':
    build_sheet({'name': 'Kaelen',
                 'race': 'Orc',
                 'klass': 'Bard',
                 'background': 'Acolyte',
                 'alignment': 'Chaotic Neutral',
                 'level': '3',
                 'xp': '17000',
                 'ac': '12',
                 'initiative': '+1',
                 'speed': '25',
                 'probonus': '+3',
                 'passive_perception': '12',
                 'hp_maximum': '24',
                 'hp_modifier': '+4',
                 'hit_dice': '1d10',
                 'strength': 9,
                 'strength_mod': '+2',
                 'str_save': ' ',
                 'dexterity': 15,
                 'dexterity_mod': '+3',
                 'dex_save': ' ',
                 'constitution': 11,
                 'constitution_mod': '+1',
                 'con_save': ' ',
                 'intelligence': 11,
                 'intelligence_mod': '-1',
                 'int_save': 'X',
                 'wisdom': 10,
                 'wisdom_mod': '+2',
                 'wis_save': ' ',
                 'charisma': 12,
                 'charisma_mod': '+4',
                 'cha_save': 'X',
                 'proficiencies': ['ARMOR:', '-Light Armor', '-Medium Armor', '-Shields', 'WEAPONS:', '-Simple Weapons', '-Martial Weapons',
                                   '-Crossbows', '-Daggers','TOOLS:', 'Artisan Tools', 'LANGUAGE:', '-Abyssal', '-Orcish','','','','','','','', ],
                 'acrobatics_skill': 'X',
                 'acrobatics_mod': '+3',
                 'animal_handling_skill': ' ',
                 'animal_handling_mod': '+2',
                 'arcana_skill': 'X',
                 'arcana_mod': '+3',
                 'athletics_skill': 'X',
                 'athletics_mod': '+3',
                 'deception_skill': ' ',
                 'deception_mod': '+3',
                 'history_skill': ' ',
                 'history_mod': '+3',
                 'insight_skill': 'X',
                 'insight_mod': '+3',
                 'intimidation_skill': 'X',
                 'intimidation_mod': '+3',
                 'investigation_skill': ' ',
                 'investigation_mod': '+1',
                 'medicine_skill': ' ',
                 'medicine_mod': '+1',
                 'nature_skill': ' ',
                 'nature_mod': '+1',
                 'perception_skill': ' ',
                 'perception_mod': '+1',
                 'performance_skill': 'X',
                 'performance_mod': '+4',
                 'persuasion_skill': ' ',
                 'persuasion_mod': '+2',
                 'religion_skill': ' ',
                 'religion_mod': '+2',
                 'sleight_of_hand_skill': ' ',
                 'sleight_of_hand_mod': '+2',
                 'stealth_skill': ' ',
                 'stealth_mod': '+2',
                 'survival_skill': ' ',
                 'survival_mod': '+2',
                 'currency_cp': 20,
                 'currency_sp': 20,
                 'currency_ep': 20,
                 'currency_gp': 20,
                 'currency_pp': 20,
                 'prim_weap_name': 'Greataxe',
                 'prim_weap_hit': '+5',
                 'prim_weap_dmg': '1d12+3 Slashing',
                 'prim_weap_properties': 'Martial, Heavy, Two-Handed',
                 'prim_weap_weight': '3lbs',
                 'second_weap_name': 'Handaxe',
                 'second_weap_hit': '+5',
                 'second_weap_dmg': '1d6+3 Slashing',
                 'second_weap_properties': 'Light, Thrown, Range (20/60)',
                 'second_weap_weight': '2lbs',
                 'third_weap_name': 'Javelin',
                 'third_weap_hit': '+5',
                 'third_weap_dmg': '1d6+3 Piercing',
                 'third_weap_properties': 'Thrown, Range (30/120)',
                 'third_weap_weight': '8lbs',
                 'fourth_weap_name': 'Unarmed Strike',
                 'fourth_weap_hit': '+5',
                 'fourth_weap_dmg': '4 Bludgeoning',
                 'fourth_weap_properties': '',
                 'fourth_weap_weight': '',
                 'abilities': ["RAGE", "UNARMORED DEFENSE", "FLIGHT"]
                 })
