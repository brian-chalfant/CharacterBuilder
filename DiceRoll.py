from modifiers import primary_abilities, validate_choice, clearscreen, BColors


def initial_diceroll():
    from random import randrange

    a = []
    for i in range(4):
        a.append(randrange(1,7))
    a.sort()
    total = a[1] + a[2] + a[3]
    return total


def diceroll(number_of_dice, number_of_sides):
    from random import randrange
    a = 0
    for i in range(number_of_dice):
        a += randrange(1, (number_of_sides + 1))
    return a


def stat_selection(classname, highest):
    abilities = primary_abilities()
    yesno = {1: 'Re-roll', 2: 'Save'}
    begin = input("Press Enter to Roll 4d6 for Stats")
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
          .format(classname=BColors.HEADER + classname + BColors.ENDC, highest=BColors.HEADER + highest))
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

