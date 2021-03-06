from write_backgrounds import read_backgrounds
from modifiers import validate_choice, alignment


class Background:
    def __init__(self, name):
        x = read_backgrounds(name)
        self.name = x.get('NAME')
        self.featurename = x.get('FEATURE')
        self.skillpro = x.get('SKILLPROF')
        self.language = x.get('LANGUAGES')
        self.toolpro = x.get('LANGUAGES')
        self.personalitytraits = dict()
        self.alignment = ''
        for i in range(1, 9):
            self.personalitytraits[i] = x.get('PERSTRAIT' + str(i))
        self.ideals = {}
        for i in range(1, 7):
            self.ideals[i] = x.get('IDEAL' + str(i))
        self.bonds = {}
        for i in range(1, 7):
            self.bonds[i] = x.get('BOND' + str(i))
        self.flaws = {}
        for i in range(1, 7):
            self.flaws[i] = x.get('FLAW' + str(i))

        self.personalitytraits = process_selection(self.print_personality_traits())
        self.ideals = process_selection(self.print_ideals())
        self.bonds = process_selection(self.print_bonds())
        self.flaws = process_selection(self.print_flaws())

        self.set_alignment()

    def print_personality_traits(self):
        print('PERSONALITY TRAITS')
        for key, value in self.personalitytraits.items():
            print(key, value)
        return self.personalitytraits

    def print_ideals(self):
        print('IDEALS')
        for key, value in self.ideals.items():
            print(key, value)
        return self.ideals

    def print_bonds(self):
        print('BONDS')
        for key, value in self.bonds.items():
            print(key, value)
        return self.bonds

    def print_flaws(self):
        print('FLAWS')
        for key, value in self.flaws.items():
            print(key, value)
        return self.flaws

    def set_alignment(self):
        for key, value in alignment().items():
            print(key, value)
        a = validate_choice(len(alignment().items()), message='Choose your character\'s alignment: ')
        self.alignment = alignment().get(a)


def process_selection(argument):
    complete = False
    rtnlist = []
    if len(argument) > 6:
        while complete is False:
            a = argument
            x = validate_choice(len(argument), message='Select Traits (1 of 2)')
            y = validate_choice(len(argument), message='Select Traits (2 of 2)')
            if x == y:
                complete = False
            else:
                complete = True
                rtnlist.append(a.get(x))
                rtnlist.append(a.get(y))
    else:
        a = argument
        x = validate_choice(len(argument), message='Select one trait')
        rtnlist.append(a[x])
    return rtnlist


# if __name__ == '__main__':
