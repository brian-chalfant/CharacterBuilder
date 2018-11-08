import sqlite3
from modifiers import get_maneuvers_desc, get_elemental_disciplines_desc


def build_sheet(character_data: dict):
    width = 80  # standard width of character sheet
    filename = character_data.get('name') + '-' + character_data.get('race') + " " \
                                          + character_data.get('klass') + '.txt'

    with open('characters\\' + filename, 'w', encoding='utf-16') as outfile:

        lines = str()
        lines += 'Name:> ' + str(character_data.get('name')) + (' ' * (int((width/2)) -
                                                                       int(len(character_data.get('name'))) - 7)
                                                                ) + '         ________     ____   ________   ' + '\n'
        lines += 'Race:> ' + str(character_data.get('race')) + (' ' * (int((width/2)) -
                                                                       int(len(character_data.get('race'))) - 7)
                                                                ) + '         \______ \   /  _ \  \______ \  ' + '\n'
        lines += 'Class:> ' + str(character_data.get('klass')) + "  (" + str(character_data.get('classpath')) + ")" \
                            + (' ' * (int((width/2)) - int(len(character_data.get('klass')) +
                                      len(character_data.get('classpath'))) - 12)
                               ) + '          |    |  \  >  _ </\ |    |  \ ' + '\n'
        lines += 'Background:> ' + str(character_data.get('background')) + (' ' * (int((width/2)) -
                                                                            int(len(character_data.get('background')))
                                                                            - 13)
                                                                            ) + \
                 '          |  __`   \/  <_\ \/ |  __`   \\' + '\n'
        lines += 'Alignment:> ' + str(character_data.get('alignment')) + (' ' * (int((width/2)) -
                                                                          int(len(character_data.get('alignment')))
                                                                            - 12)
                                                                          ) + \
                 '         /_______  /\_____\ \/_______  /' + '\n'
        lines += 'Level & XP:> Level ' + str(character_data.get('level')) + "    " + str(character_data.get('xp')) + \
                 (' ' * (int((width/2)) - (int(len(str(character_data.get('level')))) +
                                           len(str(character_data.get('xp'))) +
                                           23))) + '                 \/        \/        \/ ' + '\n'
        # CHARACTER SECTION

        lines += '+-Age--+-Height-+-Weight-+--+-Eyes---------+-Skin-----------+-Hair-------------+ \n'
        lines += '|{:6}|{:8}|{:8}|  |{:14}|{:16}|{:18}| \n'.format(character_data.get('age'),
                                                                   character_data.get('height'),
                                                                   character_data.get('weight'),
                                                                   character_data.get('eyes'),
                                                                   character_data.get('skin'),
                                                                   character_data.get('hair'))
        lines += '+------+--------+--------+--+--------------+----------------+------------------+ \n'
        lines += '+-Personality Traits-----------------------------------------------------------+ \n'
        for j in string_format(character_data.get('pers_trait1')):
            lines += j + '\n'
        for j in string_format(character_data.get('pers_trait2')):
            lines += j + '\n'
        lines += '+------------------------------------------------------------------------------+ \n'
        lines += '+-Ideals-----------------------------------------------------------------------+ \n'
        for j in string_format(character_data.get('ideals')):
            lines += j + '\n'
        lines += '+------------------------------------------------------------------------------+ \n'
        lines += '+-Bonds-----------------------------------------------------------------------+ \n'
        for j in string_format(character_data.get('bonds')):
            lines += j + '\n'
        lines += '+------------------------------------------------------------------------------+ \n'
        lines += '+-Flaws-----------------------------------------------------------------------+ \n'
        for j in string_format(character_data.get('flaws')):
            lines += j + '\n'
        lines += '+------------------------------------------------------------------------------+ \n'
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
            character_data.get('con_save'), character_data.get('constitution'), character_data.get('constitution_mod'),
            character_data.get('hit_dice'))
        lines += '|[{}] INTELLIGENCE           [{:02}] [{}] |  +-Death Saves-------------------------+ \n'.format(
            character_data.get('int_save'), character_data.get('intelligence'), character_data.get('intelligence_mod'))
        lines += '|[{}] WISDOM                 [{:02}] [{}] |  | Successes               [ ] [ ] [ ] | \n'.format(
            character_data.get('wis_save'), character_data.get('wisdom'), character_data.get('wisdom_mod'))
        lines += '|[{}] CHARISMA               [{:02}] [{}] |  | Failures                [ ] [ ] [ ] | \n'.format(
            character_data.get('char_save'), character_data.get('charisma'), character_data.get('charisma_mod'))
        lines += '+-Skills------------------------------+  +-------------------------------------+ \n'
        lines += '| Acrobatics (Dex)           [{}] [{}] |  +-Other Proficiencies & Languages-----+ \n'.format(
            character_data.get('acrobatics_skill'), character_data.get('acrobatics_mod'))
        try:
            lines += '| Animal Handling (Wis)      [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('animal_handling_skill'), character_data.get('animal_handling_mod'),
                character_data.get('proficiencies')[0])
        except IndexError:
            lines += '| Animal Handling (Wis)      [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('animal_handling_skill'), character_data.get('animal_handling_mod'),
                " ")
        try:
            lines += '| Arcana (Int)               [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('arcana_skill'), character_data.get('arcana_mod'),
                character_data.get('proficiencies')[1])
        except IndexError:
            lines += '| Arcana (Int)               [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('arcana_skill'), character_data.get('arcana_mod'),
                " ")
        try:
            lines += '| Athletics (Str)            [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('athletics_skill'), character_data.get('athletics_mod'),
                character_data.get('proficiencies')[2])
        except IndexError:
            lines += '| Athletics (Str)            [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('athletics_skill'), character_data.get('athletics_mod'),
                " ")
        try:
            lines += '| Deception (Cha)            [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('deception_skill'), character_data.get('deception_mod'),
                character_data.get('proficiencies')[3])
        except IndexError:
            lines += '| Athletics (Str)            [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('athletics_skill'), character_data.get('athletics_mod'),
                " ")
        try:
            lines += '| History (Int)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('history_skill'), character_data.get('history_mod'),
                character_data.get('proficiencies')[4])
        except IndexError:
            lines += '| History (Int)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('history_skill'), character_data.get('history_mod'),
                character_data.get('proficiencies')[4])
        try:
            lines += '| Insight (Wis)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('insight_skill'), character_data.get('insight_mod'),
                character_data.get('proficiencies')[5])
        except IndexError:
            lines += '| Insight (Wis)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('insight_skill'), character_data.get('insight_mod'),
                " ")
        try:
            lines += '| Intimidation (Cha)         [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('intimidation_skill'), character_data.get('intimidation_mod'),
                character_data.get('proficiencies')[6])
        except IndexError:
            lines += '| Insight (Wis)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('insight_skill'), character_data.get('insight_mod'),
                " ")
        try:
            lines += '| Investigation (Int)        [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('investigation_skill'), character_data.get('investigation_mod'),
                character_data.get('proficiencies')[7])
        except IndexError:
            lines += '| Investigation (Int)        [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('investigation_skill'), character_data.get('investigation_mod'),
                " ")
        try:
            lines += '| Medicine (Wis)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('medicine_skill'), character_data.get('medicine_mod'),
                character_data.get('proficiencies')[8])
        except IndexError:
            lines += '| Medicine (Wis)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('medicine_skill'), character_data.get('medicine_mod'),
                " ")
        try:
            lines += '| Nature (Int)               [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('nature_skill'), character_data.get('nature_mod'),
                character_data.get('proficiencies')[9])
        except IndexError:
            lines += '| Nature (Int)               [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('nature_skill'), character_data.get('nature_mod'),
                " ")
        try:
            lines += '| Perception (Wis)           [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('perception_skill'), character_data.get('perception_mod'),
                character_data.get('proficiencies')[10])
        except IndexError:
            lines += '| Perception (Wis)           [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('perception_skill'), character_data.get('perception_mod'),
                " ")
        try:
            lines += '| Performance (Cha)          [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('performance_skill'), character_data.get('performance_mod'),
                character_data.get('proficiencies')[11])
        except IndexError:
            lines += '| Performance (Cha)          [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('performance_skill'), character_data.get('performance_mod'),
                " ")
        try:
            lines += '| Persuasion (Cha)           [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('persuasion_skill'), character_data.get('persuasion_mod'),
                character_data.get('proficiencies')[12])
        except IndexError:
            lines += '| Persuasion (Cha)           [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('persuasion_skill'), character_data.get('persuasion_mod'),
                " ")
        try:
            lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('religion_skill'), character_data.get('religion_mod'),
                character_data.get('proficiencies')[13])
        except IndexError:
            lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('religion_skill'), character_data.get('religion_mod'),
                " ")
        try:
            lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('religion_skill'), character_data.get('religion_mod'),
                character_data.get('proficiencies')[14])
        except IndexError:
            lines += '| Religion (Int)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('religion_skill'), character_data.get('religion_mod'),
                " ")
        try:
            lines += '| Stealth (Dex)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('stealth_skill'), character_data.get('stealth_mod'),
                character_data.get('proficiencies')[15])
        except IndexError:
            lines += '| Stealth (Dex)              [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('stealth_skill'), character_data.get('stealth_mod'),
                " ")
        try:
            lines += '| Survival (Wis)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('survival_skill'), character_data.get('survival_mod'),
                character_data.get('proficiencies')[16])
        except IndexError:
            lines += '| Survival (Wis)             [{}] [{}] |  |{:37}| \n'.format(
                character_data.get('survival_skill'), character_data.get('survival_mod'),
                " ")
        try:
            lines += '|                                     |  |{:37}| \n'.format(
                character_data.get('proficiencies')[17])
        except IndexError:
            lines += '|                                     |  |{:37}| \n'.format(" ")
        try:
            lines += '+-Currency-+-Treasure-----------------+  |{:37}| \n'.format(
                character_data.get('proficiencies')[18])
        except IndexError:
            lines += '+-Currency-+-Treasure-----------------+  |{:37}| \n'.format(" ")
        try:
            lines += '| CP [   ] |                          |  |{:37}| \n'.format(
                character_data.get('proficiencies')[19])
        except IndexError:
            lines += '| CP [   ] |                          |  |{:37}| \n'.format(" ")
        try:
            lines += '| SP [   ] |                          |  |{:37}| \n'.format(
                character_data.get('proficiencies')[20])
        except IndexError:
            lines += '| SP [   ] |                          |  |{:37}| \n'.format(" ")
        try:
            lines += '| EP [   ] |                          |  |{:37}| \n'.format(
                character_data.get('proficiencies')[21])
        except IndexError:
            lines += '| EP [   ] |                          |  |{:37}| \n'.format(
                " ")
        try:
            lines += '| GP [{}] |                          |  |{:37}| \n'.format(
                character_data.get('starting_gp'), character_data.get('proficiencies')[22])
        except IndexError:
            lines += '| GP [{} ] |                          |  |{:37}| \n'.format(
                character_data.get('starting_gp'), " ")
        try:
            lines += '| PP [   ] |                          |  |{:37}| \n'.format(
                character_data.get('proficiencies')[23])
        except IndexError:
            lines += '| PP [   ] |                          |  |{:37}| \n'.format(
                " ")
        lines += '+-Attack--------+-HIT+-Damage/Typ-----+-Properties--------------------+-Weight-+ \n'
        if 'wep0_name' in character_data:
            lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('wep0_name'),
                                                               character_data.get('wep0_hit'),
                                                               character_data.get('wep0_damage'),
                                                               character_data.get('wep0_properties'),
                                                               character_data.get('wep0_weight'))
        if 'wep1_name' in character_data:
            lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('wep1_name'),
                                                               character_data.get('wep1_hit'),
                                                               character_data.get('wep1_damage'),
                                                               character_data.get('wep1_properties'),
                                                               character_data.get('wep1_weight'))
        if 'wep2_name' in character_data:
            lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('wep2_name'),
                                                               character_data.get('wep2_hit'),
                                                               character_data.get('wep2_damage'),
                                                               character_data.get('wep2_properties'),
                                                               character_data.get('wep2_weight'))
        if 'wep3_name' in character_data:
            lines += '|{:15}|{:4}|{:16}|{:31}|{:8}| \n'.format(character_data.get('wep3_name'),
                                                               character_data.get('wep3_hit'),
                                                               character_data.get('wep3_damage'),
                                                               character_data.get('wep3_properties'),
                                                               character_data.get('wep3_weight'))

        lines += '+-Features---------------------------------------------------------------------+ \n'
        for i in character_data.get('abilities'):
            try:
                x = read_features(i)
                for j in string_format(x):
                    lines += j + '\n'
                lines += string_decorator('*' + ('-' * 76) + '*') + '\n'
            except AttributeError:
                x = str(i) + '' \
                             ': No Data Available (FEATURE)'
                for j in string_format(x):
                    lines += j + '\n'
                lines += string_decorator('*' + ('-' * 76) + '*') + '\n'
        if character_data.get('klass') == 'Fighter':
                try:
                    for k in character_data.get('maneuver'):
                        for j in string_format(str(character_data.get('maneuver').upper()) + ": " +
                                               str(get_maneuvers_desc(character_data.get('maneuver'))[0])):
                            lines += j + '\n'
                        lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
                except AttributeError:
                    x = str(k) + ': No Data Available (MANEUVER)'
                    for j in string_format(x):
                        lines += j + '\n'
                    lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
        if character_data.get('klass') == 'Monk':
                try:
                    for m in character_data.get('elemental_discipline'):
                        print(get_elemental_disciplines_desc(m))
                        for j in string_format(str(m) + ": " +
                                               str(get_elemental_disciplines_desc(m)[0])):
                            lines += j + '\n'
                        lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
                except AttributeError as e:
                    x = str(m) + ': No Data Available (ELEMENTAL DISCIPLINE)' + str(e)
                    for j in string_format(x):
                        lines += j + '\n'
                    lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
        if character_data.get('spells'):
            lines += '+-Spells-----------------------------------------------------------------------+ \n'
            for i in character_data.get('spells'):
                try:
                    x = read_spells(i)
                    for j in string_format(x):
                        lines += j + '\n'
                    lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
                except AttributeError:
                    x = str(i) + ": No Data Available (SPELL)"
                    for j in string_format(x):
                        lines += j + '\n'
                    lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
            if character_data.get('klass') == 'Warlock':
                for i in character_data.get('Eldritch Invocation Spells'):
                    try:
                        x = read_spells(i)
                        for j in string_format(x):
                            lines += j + '\n'
                        lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
                    except AttributeError:
                        x = str(i) + ': No Data Available (INVOCATION'
                        for j in string_format(x):
                            lines += j + '\n'
                        lines += string_decorator('*' + (' - ' * 25) + '*') + '\n'
        lines += '|                                                                   D&DCB 2018 | \n'
        lines += '+------------------------------------------------------------------------------+'
        print(lines)
        outfile.writelines(lines)


def text_format(textlist, width=78):
    a = textlist
    b = ''
    for i in a:
        if len(i + b) < width:
            b += i + ", "
        else:
            yield decorator(b)
            b = '' + i + ", "
    return decorator(b)


def string_format(text, width=78):
    a = text.split()
    b = ''
    for i in a:
        if len(i + b) < width:
            b += i + " "
        else:
            yield string_decorator(b)
            b = '' + i + " "
    yield string_decorator(b)


def string_decorator(linetext):
    a = '|{:78}|'.format(linetext)
    return a


def decorator(linetext):
    a = '|{:78}| \n'.format(linetext)
    return a


def read_features(name):
    conn = sqlite3.connect('CharacterBuilder.db')
    cur = conn.cursor()

    cur.execute('SELECT description FROM features WHERE NAME = \"{na}\"'.format(na=name))

    x = cur.fetchall()
    conn.close()

    try:
        print(x[0][0])
        return name + ": " + x[0][0]
    except IndexError:
        print(name + 'Spell not in database')


def read_spells(name):
    conn = sqlite3.connect('CharacterBuilder.db')
    cur = conn.cursor()

    cur.execute('SELECT description, level FROM spells WHERE NAME = \"{na}\"'.format(na=name))

    x = cur.fetchall()
    conn.close()

    try:
        if x[0][1] == 0:
            prompt_string = " (Cantrip): "
        else:
            prompt_string = " (Level " + str(x[0][1]) + " Spell): "
        return name + prompt_string + x[0][0]
    except IndexError:
        print(str(name) + ': nope')


# if __name__ == '__main__':
