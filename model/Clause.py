from model.Atom import Atom
from model.Formula import Formula


class Clause:
    def __init__(self):
        self.atomos = []

    def invert_clause(self):
        new_formula = Formula()

        for atom in self.atomos:
            new_clause = Clause()
            atom_copy: Atom = atom.__copy__()
            atom_copy = atom_copy.invert_atom()
            new_clause = new_clause.or_atom(atom_copy)
            new_formula = new_formula.and_clause(new_clause)

        return new_formula

    def or_clause(self, input_clause):
        new_formula = Clause()

        for atom in self.atomos:
            new_formula = new_formula.or_atom(atom.__copy__())

        for atom in input_clause.atomos:
            new_formula = new_formula.or_atom(atom.__copy__())

        return new_formula

    def and_clause(self, input_clause):
        new_formula = Formula()
        new_formula = new_formula.and_clause(self)
        new_formula = new_formula.and_clause(input_clause)

        return new_formula

    def or_atom(self, input_atom):
        new_clause = Clause()

        for atom in self.atomos:
            new_clause = new_clause.or_atom(atom.__copy__())

        if self.compare(input_atom):
            new_clause.atomos.append(input_atom.__copy__())

        return new_clause

    def and_atom(self, input_atom):
        new_formula = Formula()
        new_formula = new_formula.and_clause(self.__copy__())

        new_clause = Clause()
        new_clause = new_clause.or_atom(input_atom.__copy__())

        new_formula = new_formula.and_clause(new_clause)

        return new_formula

    def compare(self, input_atom):
        for a in self.atomos:
            if input_atom.name == a.name:
                if input_atom.inverted == a.inverted:
                    return False

        return True

    def __str__(self):
        result = "("

        for index, atom in enumerate(self.atomos):
            result += atom.__str__()

            if index != len(self.atomos) - 1:
                result += " | "

        result += ")"

        return result

    def __copy__(self):
        clause_copy = Clause()

        for atom in self.atomos:
            clause_copy.atomos.append(atom.__copy__())

        return clause_copy
