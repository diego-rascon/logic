class Atom:
    def __init__(self, name: str):
        self.name = name.upper()
        self.inverted = False

    def invert(self):
        self.inverted = not self.inverted
        atom_copy = Atom(self.name)
        atom_copy.inverted = not atom_copy.inverted
        return atom_copy

    def __copy__(self):
        atom_copy = Atom(self.name)
        atom_copy.inverted = self.inverted
        return atom_copy

    def __str__(self):
        string = ''
        if self.inverted:
            string += '-'
        string += self.name
        return string
