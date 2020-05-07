import sqlite3


def read_spells(name):
    conn = sqlite3.connect('CharacterBuilder.db')
    cur = conn.cursor()

    cur.execute(
        'SELECT name, casting_time, range, components, duration, school, description, level FROM spells WHERE NAME = \"{na}\"'.format(
            na=name))

    x = cur.fetchall()
    conn.close()
    return x


def build_html(character_data: dict):
    spell_count = 0
    for key, value in character_data.items():
        print(key, value)
    width = 80  # standard width of character sheet
    filename = character_data.get('name') + '-' + character_data.get('race') + " " \
               + character_data.get('klass') + '.html'

    with open('characters\\' + filename, 'w', encoding='utf-16') as outfile:
        lines = ""
        lines += """       <html>

    <head>

        <title>Character Sheet - {} </title>
        <META name = "description" content = "Dungeons & Dragons 5e Player Character">
    
        <link rel="Stylesheet" type="text/css" href="css/gaming.css">
        

        
    </head>

    <body>

        <form>
        <table width="100%" cellspacing="0" cellpadding="1" class="bordered">
            <tr>
                <th colspan="6" align="center" class="bordered">
                    <table width="100%">
                        <tr>
                            <td valign="top" align="left" width="50%">
                            </td>
                            <span><i>Dungeons & Dragons 5th Edition</i></span>									
                            <td valign="top" align="right" width="50%">
                            </td>							
                        </tr>
                    </table>
                </th>
            </tr>		
            <tr>
                <td colspan="6" valign="top">
                    <table cellspacing="0" cellpadding="0" width="100%">
                        <tr>
                            <td width="50%"><span class="worm">Name: {} </span> </td> <!---NAME --->
                            <td width="50%"><span class="worm">Alignment: {}</span> </td> <!---ALIGNMENT --->
                        </tr>
                        <tr>
                            <td width="50%"><span class="worm">Race: {} </span> </td> <!--- GENDER & RACE --->
                            <td width="50%"><span class="worm">Background: {} </span> </td> <!---BACKGROUND --->
                        </tr>
                        <tr>
                            <td width="50%"><span class="worm">Classes: {}</span>  </td>
                            <td width="50%"><span class="worm">Character Level: {}</span>  	 </td>
                        </tr>
                    </table> """.format(character_data.get('name'), character_data.get('name'),
                                        character_data.get('alignment'), character_data.get('race'),
                                        character_data.get('background'), character_data.get('klass'),
                                        character_data.get('level'))
        lines += """</td>
            </tr>
            <tr>
                <td colspan="6" valign="top" width="100%">
                    <table cellspacing="0" cellpadding="0" width="100%" border="1">
                        <tr>
                            <th valign="top">Age</th>
                            <th valign="top">Height</th>
                            <th valign="top">Weight</th>
                            <th valign="top">Eyes</th>
                            <th valign="top">Skin</th>
                            <th valign="top">Hair</th>
                        </tr>
                        <tr>
                            <td align="center">{}</td>
                            <td align="center">{}</td>
                            <td align="center">{}</td>
                            <td align="center">{}</td>
                            <td align="center">{}</td>
                            <td align="center">{}</td
                        </tr>
                    </table>
                </td>
            </tr>""".format(character_data.get('age'), character_data.get('height'),
                            character_data.get('weight'), character_data.get('eyes'),
                            character_data.get('skin'), character_data.get('hair'))
        lines += """
            <tr>
                <td colspan="6" valign="top" width="100%">
                    <table cellspacing="0" cellpadding="0" width="100%" border="1">
                        <tr>
                            <th valign="top">Hit Dice</th>

                            <td rowspan="2">
                                            <b>Max Hit Points</b> <span class="hilite">{}</span><br>
                                            <b>Current Hit Points</b> <span class="hilite">&nbsp;</span></td>
                        </tr>
                        <tr>
                            <td width="50%" align="center">{}</td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td colspan="6" valign="top" width="100%">
                    <table cellpadding="0" cellspacing="0" width="100%">
                        <tr>

                            <th class="smaller" width="9%">AC</th>
                            <th class="smaller" width="7%">Initiative</th>
                            <th class="smaller" width="7%">Speed</th>
                        </tr>
                        <tr>

                            <td class="stat-hilite">{}</td> <!--- TOTAL AC --->
                            <td class="stat-hilite">{}</td> <!--- INITIATIVE --->
                            <td class="stat-hilite">{}</td> <!--- SPEED --->
                        </tr>
                    </table>
                </td>
                </tr>""".format(character_data.get('hp_maximum'), character_data.get('hit_dice'),
                                character_data.get('ac'),
                                character_data.get('initiative'), character_data.get('speed'))
        lines += """
            <tr>
                <td colspan="4" width="50%" valign="top" class="bordered">
                    <table border="0" width="100%" cellspacing="0" cellpadding="0">
                        <tr>
                            <th width="11%" class="smaller">Ability</th>
                            <th width="11%" class="smaller">Total</th>
                            <th width="11%" class="smaller">Mod</th>			

                        </tr>	   
                        <tr class="odd-row">
                            <td align="center" class="smaller"><b>STR</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->	

                        </tr>
                        <tr>
                            <td align="center" class="smaller"><b>DEX</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->	

                        </tr>				
                        <tr class="odd-row">
                            <td align="center" class="smaller"><b>CON</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->	


                        </tr>
                        <tr>
                            <td align="center" class="smaller"><b>INT</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->	


                        </tr>
                        <tr class="odd-row">
                            <td align="center" class="smaller"><b>WIS</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->	


                        </tr>									
                        <tr>
                            <td align="center" class="smaller"><b>CHA</b></td>
                            <td class="stat"><b>{}</b></td>	<!--- TOTAL --->
                            <td class="stat-hilite">{}</td>			<!--- MODIFIER --->							

                        </tr>				
                    </table>""".format(character_data.get('strength'), character_data.get('strength_mod'),
                                       character_data.get('dexterity'), character_data.get('dexterity_mod'),
                                       character_data.get('constitution'), character_data.get('constitution_mod'),
                                       character_data.get('intelligence'), character_data.get('intelligence_mod'),
                                       character_data.get('wisdom'), character_data.get('wisdom_mod'),
                                       character_data.get('charisma'), character_data.get('charisma_mod'))
        lines += """
                    <table border="0" cellpadding="0" cellpadding="0" width="100%">
                        <tr>
                            <th class="smaller">Armor Proficiencies</th>
                        </tr>
                        <tr>
                            <td>{}<br></td>
                        </tr>
                    </table>
                    <table border="0" cellpadding="0" cellpadding="0" width="100%">
                        <tr>
                            <th class="smaller">Weapon Proficiencies</th>
                        </tr>
                        <tr>
                            <td>{}<br></td>
                        </tr>
                    </table>
                    <table border="0" cellpadding="0" cellpadding="0" width="100%">
                        <tr>
                            <th class="smaller">Tool Proficiencies</th>
                        </tr>
                        <tr>
                            <td>{}<br></td>
                        </tr>
                    </table>
                    <table border="0" cellpadding="0" cellpadding="0" width="100%">
                        <tr>
                            <th class="smaller">Language Proficiencies</th>
                        </tr>
                        <tr>
                            <td>{}<br></td>
                        </tr>
                    </table>
                    
                </td>""".format(
            ", ".join(character_data.get('armor_pro') if character_data.get('armor_pro') is not None else "None"),
            ", ".join(character_data.get('weapon_pro') if character_data.get('weapon_pro') is not None else "None"),
            ", ".join(character_data.get('tool_pro') if character_data.get('tool_pro') is not None else ""),
            ", ".join(character_data.get('languages') if character_data.get('languages') is not None else "None")
        )
        lines += """
                
                <td valign="top" class="bordered">				
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr>
                            <th class="smaller" width="15%">Skills</th>
                            <th class="smaller" width="10%">Proficiency</th>
                            <th class="smaller" width="10%">Modifier</th>

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Acrobatics (Dex)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr>
                            <td class="smaller"><b>Animal Handling (Wis)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Arcana (Int)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                        <tr>
                            <td class="smaller"><b>Athletics (Str)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Deception (Cha)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>History (Int)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Insight (Wis)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>Intimidation (Cha)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Investigation (Int)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>Medicine (Wis)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Nature (Int)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>Perception (Wis)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Performance (Cha)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>Persuasion (Cha)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Religion (Int)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller">Slight of Hand (Dex)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->

                        </tr>
                        <tr class="odd-row">
                            <td class="smaller"><b>Stealth (Dex)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                        </tr>
                            <tr>
                            <td class="smaller"><b>Survival (Wis)</b></td>
                            <td class="smaller">{}</td>	<!--- TOTAL --->
                            <td align="center" class="stat-hilite">{}</td>			<!--- BASE --->
                            </tr>
                        </tr>		
                    </table>
                </td>
            </tr>
            """.format(character_data.get('acrobatics_skill'), character_data.get('acrobatics_mod'),
                       character_data.get('animal_handling_skill'), character_data.get('animal_handling_mod'),
                       character_data.get('arcana_skill'), character_data.get('arcana_mod'),
                       character_data.get('athletics_skill'), character_data.get('athletics_mod'),
                       character_data.get('deception_skill'), character_data.get('deception_mod'),
                       character_data.get('history_skill'), character_data.get('history_mod'),
                       character_data.get('insight_skill'), character_data.get('insight_mod'),
                       character_data.get('intimidation_skill'), character_data.get('intimidation_mod'),
                       character_data.get('investigation_skill'), character_data.get('investigation_mod'),
                       character_data.get('medicine_skill'), character_data.get('medicine_mod'),
                       character_data.get('nature_skill'), character_data.get('nature_mod'),
                       character_data.get('perception_skill'), character_data.get('perception_mod'),
                       character_data.get('performance_skill'), character_data.get('performance_mod'),
                       character_data.get('persuasion_skill'), character_data.get('persuasion_mod'),
                       character_data.get('religion_skill'), character_data.get('religion_mod'),
                       character_data.get('sleight_of_hand_skill'), character_data.get('sleight_of_hand_mod'),
                       character_data.get('stealth_skill'), character_data.get('stealth_mod'),
                       character_data.get('survival_skill'), character_data.get('survival_mod'))
        lines += """
            <tr>
                <td colspan="6" valign="top">
                    <table border="0" width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                            <th width="40%" class="smaller">Weapon</th>
                            <th width="10%" class="smaller">Hit</th>
                            <th width="50%" class="smaller">Damage</th>

                        </tr>"""
        if "wep0_name" in character_data:
            lines += """
                        <tr>
                            <td valign="top"><b><i>{}</i></b></td> <!--- WEAPON NAME --->
                            <td valign="top" align="center" class="smaller"><b>{}</b></td> <!---TO HIT --->
                            <td valign="top" align="center" class="smaller">{}</td> <!--- DAMAGE ROLL --->

                        </tr>
                        <tr>
                            <td valign="top" align="left" class="smaller"><b>{}</b></td> <!--- PROPERTIES --->
                            <td valign="top" align="center" class="smaller"></td>
                            <td valign="top" align="center" class="smaller"></td>

                        </tr>""".format(character_data.get('wep0_name'),
                                        character_data.get('wep0_hit'),
                                        character_data.get('wep0_damage'),
                                        character_data.get('wep0_properties'))
        if "wep1_name" in character_data:
            lines += """
                        <tr class="odd-row">
                            <td valign="top"<b><i>{}</i></b></td>
                            <td valign="top" align="center" class="smaller"><b>{}</b></td>
                            <td valign="top" align="center" class="smaller">{}</td>


                        </tr>
                        <tr class="odd-row">
                            <td valign="top" align="left" class="smaller"><b>{}</b></td>
                            <td valign="top" align="center" class="smaller"></td>
                            <td valign="top" align="center" class="smaller"></td>
                        </tr>""".format(character_data.get('wep1_name'),
                                        character_data.get('wep1_hit'),
                                        character_data.get('wep1_damage'),
                                        character_data.get('wep1_properties'))
        if "wep2_name" in character_data:
            lines += """
                        <tr>
                            <td valign="top"><b><i>{}</i></b></td>
                            <td valign="top" align="center" class="smaller"><b>{}</b></td>
                            <td valign="top" align="center" class="smaller">{}</td>

                        </tr>
                        <tr>
                            <td valign="top" align="left" class="smaller"><b>{}</b></td>
                            <td valign="top" align="center" class="smaller"></td>
                            <td valign="top" align="center" class="smaller"></td>

                        </tr>""".format(character_data.get('wep2_name'),
                                        character_data.get('wep2_hit'),
                                        character_data.get('wep2_damage'),
                                        character_data.get('wep2_properties'))
        if "wep3_name" in character_data:
            lines += """
                                <tr>
                                    <td valign="top"><b><i>{}</i></b></td>
                                    <td valign="top" align="center" class="smaller"><b>{}</b></td>
                                    <td valign="top" align="center" class="smaller">{}</td>

                                </tr>
                                <tr>
                                    <td valign="top" align="left" class="smaller"><b>{}</b></td>
                                    <td valign="top" align="center" class="smaller"></td>
                                    <td valign="top" align="center" class="smaller"></td>

                                </tr>""".format(character_data.get('wep3_name'),
                                                character_data.get('wep3_hit'),
                                                character_data.get('wep3_damage'),
                                                character_data.get('wep3_properties'))
        lines += """
                    </table>
                </td>
            </tr>
            <tr>
                <th colspan="6" class="bordered">Combat Options</th>
            </tr>
            <tr>
                <td colspan="6" class="bordered">
                    <ul class="indent">
                    </ul>
                </td>
            </tr>
            <tr>
                <td colspan="6">
                    <table cellspacing="0" cellpadding="0" width="100%">
                        <tr>
                            <th class="bordered" width="10%" class="smaller">Spell/Effect</th>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller" align="center">&nbsp;</td>
                        </tr>
                        <tr>
                            <th class="bordered" width="10%" class="smaller">Duration</th>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                        </tr>
                        <tr>
                            <th class="bordered" width="10%" class="smaller">Caster/Level</th>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                            <td class="bordered" width="15%" class="smaller">&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>"""

        lines += """
            <tr>
                <td colspan="6" valign="top" class="bordered">
                    &nbsp;<b>Inventory:</b>
                    {}<br>	
                </td>
            </tr>
            
        </table>

        <table width="100%" cellspacing="0" cellpadding="1" class="bordered">	
            <tr>
                <th colspan="6" class="bordered"><span class="worm">Spellcasting and Spell-Like Abilities</span></th>
            </tr>	
            <tr>
                <td colspan="6" valign="top" class="bordered">
                    <p>
                    <dl class="round">
                        <dt class="round"><b>Spellcasting Modifiers:</dt>
                        <dd class="round"><b>DC to Resist</b> <span class="hilite">!!!! SPELLCASTING MODIFIER</span></dd>
                        <dd class="round"><b>Domains</b> </dd>
                        <dd class="round"><b>Primary Ability</b> <span class="hilite">{}</span></dd>
                    </dl>
                    <p>""".format(
            ", ".join(character_data.get('inventory') if character_data.get('inventory') is not None else ""),
            character_data.get('primary_ability'))
        lines += """
                                    
                    <table width="100%" cellpadding="1" cellspacing="0">
                        <tr>
                            <td class="stat-header" width="10%" align="center">0-level<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">1st<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">2nd<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">3rd<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">4th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">5th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">6th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">7th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">8th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                            <td class="stat-header" width="10%" align="center">9th<br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span><br>
                                <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span> <span class="box">&nbsp;&nbsp;&nbsp;</span></td>

                        </tr>
                    </table><p>		
                    
                </td>
            </tr>	
            <tr>
                <th colspan="6" class="bordered"><span class="worm">Equipment & Possessions</span></th>
            </tr>	
            <tr>
                <td colspan="6" valign="top" class="bordered">
                    &nbsp;<b>Magical Items</b>
                        <p>

                    &nbsp;<b>Potions</b>
                        <p>

                    &nbsp;<b>Platinum (pp)</b> 0, <b>Gold (gp)</b> 0, <b>Silver (sp)</b> 0, <b>Copper (cp)</b> 0 <br>
                    &nbsp;<b>Other Wealth</b>				
                    </td>
            </tr>
            
            </table><p>
            </form>
            <p style="page-break-after: always;"><tr><table>"""

        for i in character_data.get('spells'):
            try:
                spell_count += 1
                x = read_spells(i)
                print(x)
                print("0: " + x[0][0], "1: " + x[0][1], "2: " + x[0][2], "3: " + x[0][3], "4: " + x[0][4],
                      "5: " + x[0][5], "6: " + x[0][6])
                lines += """
                
                    <td>
                        <div class="background">
                            <div class="title-row l t b r">
                                <!--
                                <div class="title-level white-text">
                                    1
                                </div>
                                -->
                                <div class="title-right">
                                    <div class="title-name black-text">
                                        {}   <!--- SPELL NAME --->
                                    </div>
                                </div>
                            </div>
                            <div class="properties l r b">
                                <div class="property-row">
                                    <div class="property r2">
                                        <div class="r10 icon"></div>
                                        <div class="property-text2  black-text">
                                            {}    <!---CASTING TIME --->
                                        </div>
                                    </div>
                                    <div class="property">
                                        
                                        <div class="property-text2  black-text">
                                            {}    <!--- RANGE --->
                                        </div>  
                                        <div class="l10 icon"></div>
                                    </div>
                                </div>
                                <div class="property-row">
                                    <div class="property r2">
                                        <div class="r10 icon"></div>
                                        <div class="property-text black-text">
                                        {}    <!--- COMPONENTS --->
                                        </div>
                                    </div>
                                    <div class="property">
                                        
                                        <div class="property-text2 black-text">
                                            {}   <!--- DURATION --->
                                        </div>   
                                        <div class="l10 icon"></div>
                                    </div>
                                </div>
                            </div>
                            <div class="content l r black-text">
                                {}   <!--- SPELL DESCRIPTION --->
                            </div>
                            <div class="footer white-text">
                                <div class="l footer-left">ARCANE</div>
                                <div class="r footer-right {}">{}</div>  <!---SPELL SCHOOL--->
                            </div>
                        </div>
                    </td>
                """.format(x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[0][6], x[0][5], str(x[0][5]).upper())
                if spell_count % 3 == 0:
                    lines += "</tr><tr>"
            except AttributeError as e:
                print(e)

        lines += """
            </table>
        
            </body>

            </html>"""
        # print(lines)
        outfile.writelines(lines)


if __name__ == '__main__':
    character_data = {
        'name': "Yoho",
        'race': 'Tiefling',
        'age': '23',
        'height': '46',
        'weight': '123',
        'skin': 'Pink',
        'hair': 'Azure',
        'eyes': 'Black',
        'level': '3',
        'xp': '900',
        'klass': 'Barbarian',
        'background': 'Acolyte',
        'pers_trait1': '-I can find common ground between the fiercest enemies, empathizing with them and ' +
                       'always working toward peace.',
        'pers_trait2': '-I see omens in every event and action. The gods try to speak to us, we just need to listen.',
        'ideals': '-Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)',
        'bonds': '-I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.',
        'flaws': '-I judge others harshly, and myself even more severely.',
        'alignment': 'Lawful Neutral',
        'classpath': 'Berzerker',
        'ac': '16',
        'initiative': '2',
        'starting_gp': '50',
        'speed': '30',
        'probonus': '2',
        'hp_maximum': '27',
        'hp_modifier': '+1',
        'hit_dice': '3d12',
        'strength': '15',
        'str_save': 'X',
        'wisdom': '10',
        'wis_save': ' ',
        'dexterity': '14',
        'dex_save': '',
        'constitution': '13',
        'con_save': 'X',
        'charisma': '10',
        'char_save': '',
        'intelligence': '13',
        'int_save': '',
        'strength_mod': '+2',
        'wisdom_mod': '+0',
        'dexterity_mod': '+2',
        'constitution_mod': '+1',
        'charisma_mod': '+0',
        'intelligence_mod': '+1',
        'athletics_skill': 'X',
        'athletics_mod': '+2',
        'acrobatics_skill': '',
        'acrobatics_mod': '+2',
        'sleight_of_hand_skill': '',
        'sleight_of_hand_mod': '+2',
        'stealth_skill': '',
        'stealth_mod': '+2',
        'arcana_skill': '',
        'arcana_mod': '+1',
        'history_skill': '',
        'history_mod': '+1',
        'investigation_skill': '',
        'investigation_mod': '+1',
        'nature_skill': '',
        'nature_mod': '+1',
        'religion_skill': '',
        'religion_mod': '+1',
        'animal_handling_skill': 'X',
        'animal_handling_mod': '+0',
        'insight_skill': '',
        'insight_mod': '+0',
        'medicine_skill': '',
        'medicine_mod': '+0',
        'perception_skill': '',
        'perception_mod': '+0',
        'survival_skill': '',
        'survival_mod': '+0',
        'deception_skill': '',
        'deception_mod': '+0',
        'intimidation_skill': '',
        'intimidation_mod': '+0',
        'performance_skill': '',
        'performance_mod': '+0',
        'persuasion_skill': '',
        'persuasion_mod': '+0',
        'passive_perception': '10',
        'primary_ability': 'Strength',
        'abilities': ['RAGE', 'UNARMORED DEFENSE', 'RECKLESS ATTACK', 'DANGER SENSE', 'FRENZY', 'DARKVISION',
                      'HELLISH RESISTANCE', 'INFERNAL LEGACY'],
        'languages': ['Common', 'Infernal'],
        'spells': ['Thaumaturgy', 'Burning Hands', 'Witch Bolt', 'Healing Word'],
        'armor_pro': ['Light Armor', 'Medium Armor', 'Shields'],
        'weapon_pro': ['Simple Weapons', 'Martial Weapons'],
        'proficiencies': ['ARMOR:', '-Light Armor', '-Medium Armor', '-Shields', 'WEAPONS:', '-Simple Weapons',
                          '-Martial Weapons', 'TOOLS:', 'LANGUAGES:', '-Common', '-Infernal', '', '', '', '', '', '',
                          '', '', '', '', '', ''],
        'wealth': '50',
        'equipment': ['Greataxe', 'backpack', 'bedroll', 'mess kit', 'tinderbox', '10 torches', '10 days of rations',
                      'waterskin', '50 feet of hempen rope', 'Javelin', 'Javelin', 'Javelin', 'Javelin', 'Holy Symbol',
                      'Prayer Book or Prayer Wheel', '5 Sticks of Incense', 'vestments', 'Set of Common Clothes',
                      'Pouch containing 15gp'],
        'wep0_name': 'Greataxe',
        'wep0_damage': '1d12 Slashing+2',
        'wep0_hit': '+4',
        'wep0_weight': '6 lbs',
        'wep0_properties': 'Reach, Special',
        'wep1_name': 'Javelin',
        'wep1_damage': '1d6 Piercing+2',
        'wep1_hit': '+4',
        'wep1_weight': '2 lbs',
        'wep1_properties': 'Thrown(range 30/120)', }

    build_html(character_data)
