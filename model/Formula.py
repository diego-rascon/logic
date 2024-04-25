class Formula:
    def __init__(self):
        self.clauses = []

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

    def __str__(self):
        result = "["

        for index, clause in enumerate(self.clauses):
            result += clause.__str__()

            if index != len(self.clauses) - 1:
                result += " \n "

        result += "]"

        return result
