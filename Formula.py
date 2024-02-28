class Formula:
    def __init__(self):
        self.clauses = []

    def and_clause(self, new_clause):
        formula = Formula()

        for clause in self.clauses:
            formula.clauses.append(clause.__copy__())

        formula.clauses.append(new_clause.__copy__())

        return formula

    def __str__(self):
        result = '['

        for index, clause in enumerate(self.clauses):
            result += clause.__str__()
            if index != len(self.clauses) - 1:
                result += ' & '
        result += ']'

        return result
