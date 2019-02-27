from modifiers import primary_abilities, validate_choice, clearscreen, BColors


def initial_diceroll():
    from random import randrange

    a = []
    for i in range(4):
        a.append(randrange(1, 7))
    a.sort()
    total = a[1] + a[2] + a[3]
    return total


def diceroll(number_of_dice, number_of_sides):
    from random import randrange
    a = 0
    for i in range(number_of_dice):
        a += randrange(1, (number_of_sides + 1))
    return a


def manual_stat_entry():
    abilities = primary_abilities()
    rtndict = {}
    for i in abilities.values():
        rtndict[i] = validate_choice(18, message="Enter value for {} stat: ".format(i))
    return rtndict

def stat_selection(classname, highest):
    # abilities = primary_abilities()
    yesno = {1: 'Re-roll', 2: 'Save'}
    manualentry = False
    # display choices
    mode = {1: "Roll Stats", 2: "Manually Enter Stats"}
    for key, value in mode.items():
        print(key, value)
    mychoice = validate_choice(2, message="Choose a method for choosing stats")
    if mychoice == 2:
        manualentry = True
    if manualentry == True:
        rtndict = manual_stat_entry()
        return rtndict
    else:
        roll = []
        reroll = True
        complete = False
        rtndict = {}
        while reroll is not False:
            roll = []
            for i in range(6):
                roll.append(initial_diceroll())
            roll.sort(reverse=True)
            print(roll)
            for key, value in yesno.items():
                print(key, value)
            accept = validate_choice(2, message='Re-Roll?')
            if accept == 1:
                reroll = True
            elif accept == 2:
                reroll = False
            else:
                reroll = True
        clearscreen()
        print('Values are sorted highest first, as a {classname}, \n '
              'your highest stat should be {highest}\n'
              .format(classname=BColors.HEADER + classname + BColors.ENDC,
                      highest=BColors.HEADER + highest + BColors.ENDC))
        print(BColors.ENDC)
        yesno = {1: 'Re-Assign', 2: 'Save'}

        while complete is False:
            try:
                abilities = primary_abilities()
                print(roll)
                for i in roll:
                    print(BColors.OKGREEN + str(i))
                    print(BColors.ENDC)
                    for key, value in abilities.items():
                        print(key, value)
                    valid = False
                    while valid is not True:
                        x = validate_choice(6, message='Choose a Primary Ability to Assign this Roll To.')
                        if abilities[x] in rtndict.values():
                            valid = False
                        else:
                            rtndict[abilities[x]] = i
                            abilities.pop(x)
                            valid = True
                for key, value in rtndict.items():
                    print(key, value)
                print('\n')
                for key, value in yesno.items():
                    print(key, value)
                a = validate_choice(2, message='')
                if a == 1:
                    complete = False
                elif a == 2:
                    complete = True
                else:
                    complete = False
            except KeyError:
                print('ENTER A VALID NUMBER')
                complete = False
            except ValueError:
                print('ENTER A VALID NUMBER')
                complete = False
        return rtndict


if __name__ == '__main__':
    a = stat_selection("Druid", "Strength")
    print(a)
