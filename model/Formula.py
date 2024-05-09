class Formula:
    def __init__(self):
        self.clauses = []
        self.certificate = {}
        self.counter = 0

    def invert_formula(self):
        new_formula = Formula()

        for clause in self.clauses:
            inverted_clause = clause.invert_clause()
            new_formula = new_formula.or_formula(inverted_clause) if new_formula.clauses else inverted_clause

        return new_formula

    def and_clause(self, input_clause):
        new_formula = Formula()

        for clause in self.clauses:
            new_formula.clauses.append(clause.__copy__())

        new_formula.clauses.append(input_clause.__copy__())

        return new_formula

    def or_formula(self, input_formula):
        new_formula = Formula()

        for clause in self.clauses:
            for inner_clause in input_formula.clauses:
                new_formula.clauses.append(clause.or_clause(inner_clause))

        return new_formula

    def and_formula(self, input_formula):
        new_formula = Formula()

        for clause in self.clauses:
            new_formula.clauses.append(clause.__copy__())

        for clause in input_formula.clauses:
            new_formula.clauses.append(clause.__copy__())

        return new_formula

    def davis_putnam(self):
        return self.davis_putnam_recursion(self.clauses.copy(), {})

    def davis_putnam_recursion(self, clauses, assignment):
        if len(clauses) == 0:
            return True, assignment

        if any(len(clause.atoms) == 0 for clause in clauses):
            return False, {}

        for atom in self.get_all_atoms(clauses):
            new_assignment = assignment.copy()
            new_assignment[atom.name] = True

            from model.Atom import Atom

            simplified_clauses = self.simplify(clauses, Atom(atom.name))
            result, new_assignment = self.davis_putnam_recursion(simplified_clauses, new_assignment)
            if result:
                return True, new_assignment

            new_assignment[atom.name] = False
            simplified_clauses = self.simplify(clauses, Atom(atom.name).invert_atom())
            result, new_assignment = self.davis_putnam_recursion(simplified_clauses, new_assignment)
            if result:
                return True, new_assignment

        return False, {}

    def simplify(self, clauses, assignment):
        simplified_clauses = []
        for clause in clauses:
            if assignment.name not in [atom.name for atom in clause.atoms]:
                simplified_clauses.append(clause)
            else:
                if assignment.inverted:
                    from model.Clause import Clause
                    new_clause = Clause()
                    for atom in clause.atoms:
                        if atom.name != assignment.name:
                            new_clause.atoms.append(atom)
                    simplified_clauses.append(new_clause)
        return simplified_clauses

    def get_all_atoms(self, clauses):
        atoms = []
        for clause in clauses:
            for atom in clause.atoms:
                if atom not in atoms:
                    atoms.append(atom)
        return atoms

    def __str__(self):
        result = "["

        for index, clause in enumerate(self.clauses):
            result += clause.__str__()

            if index != len(self.clauses) - 1:
                result += " \n "

        result += "]"

        return result
