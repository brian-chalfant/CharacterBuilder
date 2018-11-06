from modifiers import validate_choice

from Race import *


def looks(race):
    print('Appearance Personalization')
    print('The Average age for a {} is between {} and {} years'.format(race.name, race.age[0], race.age[1]))
    race.age = int(validate_choice(1000, message='Please enter an Age: '))
    print('The Average height for a {} is between {} and {} inches'.format(race.name, race.height[0], race.height[1]))
    race.height = int(validate_choice(1000, message='Please enter a Height: '))
    print('The Average weight for a {} is between {} and {} pounds'.format(race.name, race.weight[0], race.weight[1]))
    race.weight = int(validate_choice(1000, message='Please enter a Weight: '))
    if race.skin:
        print('The following are some example Skin Color options for {}s '.format(race.name))
        for i in range(len(race.skin)):
            print(race.skin[i])
        race.skin = input('Please enter any skin color you wish: ')
    else:
        race.skin = " "
    if race.hair:
        print('The following are some example Hair Color options for {}s '.format(race.name))
        for i in range(len(race.hair)):
            print(race.hair[i])
        race.hair = input('Please enter any hair color you wish: ')
    else:
        race.hair = " "
    print('The following are some example Eye Color options for {}s '.format(race.name))
    for i in range(len(race.eyes)):
        print(race.eyes[i])
    race.eyes = input('Please enter any eye color you wish: ')

    return race


if __name__ == '__main__':
    looks(race=Aarakocra())