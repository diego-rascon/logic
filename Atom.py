class Atom:
    def __init__(self, name):
        self.name = name
        self.inverted = False

    def invert(self):
        self.inverted = not self.inverted

    def __copy__(self):
        atom_copy = Atom(self.name)
        atom_copy.inverted = self.inverted
        return atom_copy

    def __str__(self):
        return f'-{self.name}' if self.inverted else self.name
