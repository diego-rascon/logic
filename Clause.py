from typing import Self

from Atom import Atom
from Formula import Formula


class Clause:
    def __init__(self):
        self.atoms = []

    def invert(self) -> Formula:
        formula = Formula()

        for atom in self.atoms:
            clause = Clause()
            atom = atom.__copy__()
            atom.invert()
            clause.atoms.append(atom)
            formula = formula.and_clause(clause)

        return formula

    def or_atom(self, origin_atom: Atom) -> Self:
        for atom in self.atoms:
            if atom.name == origin_atom.name and atom.inverted == origin_atom.inverted:
                return self

        clause = Clause()

        for atom in self.atoms:
            clause.atoms.append(atom.__copy__())

        clause.atoms.append(origin_atom.__copy__())

        return clause

    def and_atom(self, atom) -> Formula:
        formula = Formula()
        formula = formula.and_clause(self.__copy__())

        clause = Clause()
        clause = clause.or_atom(atom.__copy__())

        formula = formula.and_clause(clause)

        return formula

    def or_clause(self, clause) -> Self:
        new_clause = Clause()

        for atom in self.atoms:
            new_clause.atoms.append(atom.__copy__())

        for atom in clause.atoms:
            new_clause.atoms.append(atom.__copy__())

        return new_clause

    def and_clause(self, clause) -> Formula:
        formula = Formula()
        formula = formula.and_clause(self)
        formula = formula.and_clause(clause)
        return formula

    def is_tautology(self) -> bool:
        temp_atoms = [self.atoms[0]]

        for next_atom in self.atoms[1:]:
            for temp_atom in temp_atoms:
                if temp_atom.name == next_atom.name and temp_atom.inverted != next_atom.inverted:
                    return True
            temp_atoms.append(next_atom)

        return False

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
