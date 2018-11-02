from weapons import *
from modifiers import validate_choice


def display_menu(type, gold):
    print('*' * 20)
    list = {}
    count = 1
    for key, value in type.items():
        print(key, value.get('Cost'))
        list[count] = str(key) + " " + str(value.get('Cost'))
        count += 1
    for key, value in list.items():
        print(key, value)
    print('You have {} gold remaining.'.format(gold))
    a = int(input(validate_choice(len(list.items()), message='Please make a selection')))

    gold -= int(type.get(str(list[a])))
    print(gold)


def money(value):
    print(value.strip('cp'))
    



money('25cp')





