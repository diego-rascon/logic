from Formula import Formula
from Atom import Atom


class Clause:
    def __init__(self):
        self.atoms = []

    def or_atom(self, new_atom):
        self.atoms.append(new_atom)

    def and_atom(self, atom):
        formula = Formula()
        formula.and_clause(self.__copy__())
        clause = Clause()
        clause.or_atom(atom.__copy__())
        formula.and_clause(clause)
        return formula

    def or_clause(self, clause):
        for atom in clause.atoms:
            self.atoms.append(atom.__copy__())

    def __copy__(self):
        clause_copy = Clause()
        for atom in self.atoms:
            clause_copy.atoms.append(atom.__copy__())

    def __str__(self):
        result = '('

        for index, atom in enumerate(self.atoms):
            result += atom.__str__()
            if index != len(self.atoms) - 1:
                result += ' | '

        result += ')'
        return result
