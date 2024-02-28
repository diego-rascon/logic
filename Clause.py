from Formula import Formula


class Clause:
    def __init__(self):
        self.atoms = []

    def invert(self):
        formula = Formula()

        for atom in self.atoms:
            new_atom = atom.__copy__()
            new_atom.invert()
            new_clause = Clause()
            new_clause.atoms.append(new_atom)
            formula = formula.and_clause(new_clause)

        return formula

    def or_atom(self, new_atom):
        new_clause = Clause()

        for atom in self.atoms:
            new_clause.atoms.append(atom.__copy__())

        new_clause.atoms.append(new_atom.__copy__())

        return new_clause

    def and_atom(self, atom):
        formula = Formula()
        formula.and_clause(self.__copy__())

        clause = Clause()
        clause.or_atom(atom.__copy__())

        formula.and_clause(clause)

        return formula

    def or_clause(self, clause):
        new_clause = Clause()

        for atom in self.atoms:
            new_clause.atoms.append(atom.__copy__())

        for atom in clause.atoms:
            new_clause.atoms.append(atom.__copy__())

        return new_clause

    def and_clause(self, clause):
        formula = Formula()
        formula = formula.and_clause(self)
        formula = formula.and_clause(clause)
        return formula

    def __copy__(self):
        clause_copy = Clause()

        for atom in self.atoms:
            clause_copy.atoms.append(atom.__copy__())

        return clause_copy

    def __str__(self):
        result = '('

        for index, atom in enumerate(self.atoms):
            result += atom.__str__()
            if index != len(self.atoms) - 1:
                result += ' | '

        result += ')'
        return result
