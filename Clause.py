class Clause:
    def __init__(self):
        self.atoms = []

    def add_atom(self, new_atom):
        self.atoms.append(new_atom)

    def __str__(self):
        result = '('

        for index, atom in enumerate(self.atoms):
            result += atom.__str__()
            if index != len(self.atoms) - 1:
                result += ' | '

        result += ')'
        return result
