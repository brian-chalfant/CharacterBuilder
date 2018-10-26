from write_backgrounds import read_backgrounds
from modifiers import validate_choice


class Background:
    def __init__(self, name):
        x = read_backgrounds(name)
        self.name = x.get('NAME')
        self.featurename = x.get('FEATURE')
        self.skillpro = x.get('SKILLPROF')
        self.language = x.get('LANGUAGES')
        self.toolpro = x.get('LANGUAGES')
        self.personalitytraits = {}
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

    def print_personality_traits(self):
        for key, value in self.personalitytraits.items():
            print(key, value)
        return self.personalitytraits

    def print_ideals(self):
        for key, value in self.ideals.items():
            print(key, value)
        return self.ideals

    def print_bonds(self):
        for key, value in self.bonds.items():
            print(key, value)
        return self.bonds

    def print_flaws(self):
        for key, value in self.flaws.items():
            print(key, value)
        return self.flaws

    def process_selection(self, argument):
        complete = False
        rtnlist = []
        if len(argument) > 6:
            while complete is False:
                a = argument
                x = validate_choice(len(argument), message='Select Traits (1 of 2)')
                rtnlist.append(a.get(x))
                y = validate_choice(len(argument), message='Select Traits (2 of 2)')
                rtnlist.append(a.get(y))
                if x == y:
                    complete = False
                else:
                    complete = True
        else:
            a = argument
            x = validate_choice(len(argument), message='Select one trait')
            rtnlist.append(a[x-1])
        print(rtnlist)



b = Background('Acolyte')

x = b.process_selection(b.print_personality_traits())

print(x)