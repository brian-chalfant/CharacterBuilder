from write_backgrounds import read_backgrounds


class Background:
    def __init__(self, name):
        x = read_backgrounds(name)
        self.name = x.get('NAME')
        self.featurename = x.get('FEATURE')
        self.skillpro = x.get('SKILLPROF')
        self.language = x.get('LANGUAGES')
        self.toolpro = x.get('LANGUAGES')
        self.personalitytraits = []
        for i in range(1, 9):
            self.personalitytraits.append(x.get('PERSTRAIT' + str(i)))
        self.ideals = []
        for i in range(1, 7):
            self.ideals.append(x.get('IDEAL' + str(i)))
        self.bonds = []
        for i in range(1, 7):
            self.bonds.append(x.get('BOND' + str(i)))
        self.flaws = []
        for i in range(1, 7):
            self.flaws.append(x.get('FLAW' + str(i)))

    def print_personality_traits(self):
        for i in range(len(self.personalitytraits)):
            print(str(i + 1) + ": " + self.personalitytraits[i])

    def print_ideals(self):
        for i in range(len(self.ideals)):
            print(str(i + 1) + ": " + self.ideals[i])

    def print_bonds(self):
        for i in range(len(self.bonds)):
            print(str(i + 1) + ": " + self.bonds[i])

    def print_flaws(self):
        for i in range(len(self.flaws)):
            print(str(i + 1) + ": " + self.flaws[i])


    def process_selection(self,argument):
        argument()


