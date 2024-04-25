import copy


class Atom:
    def __init__(self, name):
        self.name = name
        self.inverted = False

    def invert_atom(self):
        new_atom = Atom(self.name)
        new_atom.inverted = not self.inverted

        return new_atom

    def __str__(self):
        result = ""

        if self.inverted:
            result += "-"

        result += self.name

        return result

    def copy(self):
        return copy.copy(self)

    def __copy__(self):
        new_atom = Atom(self.name)
        new_atom.inverted = self.inverted
        return new_atom
