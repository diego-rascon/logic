class Formula:
    def __init__(self):
        self.clauses = []

    def and_clause(self, clause):
        self.clauses.append(clause)

    def __str__(self):
        result = '['

        for index, clause in enumerate(self.clauses):
            result += clause.__str__()
            if index != len(self.clauses) - 1:
                result += ' & '
        result += ']'

        return result