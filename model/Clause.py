from model.Atom import Atom
from model.Formula import Formula


class Clause:
    def __init__(self):
        self.atoms = []

    def invert_clause(self):
        new_formula = Formula()

        for atom in self.atoms:
            new_clause = Clause()
            atom_copy: Atom = atom.__copy__()
            atom_copy = atom_copy.invert_atom()
            new_clause = new_clause.or_atom(atom_copy)
            new_formula = new_formula.and_clause(new_clause)

        return new_formula

    def or_clause(self, input_clause):
        new_formula = Clause()

        for atom in self.atoms:
            new_formula = new_formula.or_atom(atom.__copy__())

        for atom in input_clause.atoms:
            new_formula = new_formula.or_atom(atom.__copy__())

        return new_formula

    def and_clause(self, input_clause):
        new_formula = Formula()
        new_formula = new_formula.and_clause(self)
        new_formula = new_formula.and_clause(input_clause)

        return new_formula

    def or_atom(self, input_atom):
        new_clause = Clause()

        for atom in self.atoms:
            new_clause = new_clause.or_atom(atom.__copy__())

        if self.compare(input_atom):
            new_clause.atoms.append(input_atom.__copy__())

        return new_clause

    def and_atom(self, input_atom):
        new_formula = Formula()
        new_formula = new_formula.and_clause(self.__copy__())

        new_clause = Clause()
        new_clause = new_clause.or_atom(input_atom.__copy__())

        new_formula = new_formula.and_clause(new_clause)

        return new_formula

    def compare(self, input_atom):
        for a in self.atoms:
            if input_atom.name == a.name:
                if input_atom.inverted == a.inverted:
                    return False

        return True

    def __str__(self):
        result = "("

        for index, atom in enumerate(self.atoms):
            result += atom.__str__()

            if index != len(self.atoms) - 1:
                result += " | "

        result += ")"

        return result

    def __copy__(self):
        clause_copy = Clause()

        for atom in self.atoms:
            clause_copy.atoms.append(atom.__copy__())

        return clause_copy
