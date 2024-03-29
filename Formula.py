from typing import Self


class Formula:
    def __init__(self):
        self.clauses = []

    def invert(self) -> Self:
        formula = Formula()

        for clause in self.clauses:
            inverted_clause = clause.invert()
            formula = formula.and_formula(inverted_clause)

        return formula

    def or_formula(self, origin_formula: Self) -> Self:
        formula = Formula()

        for clause in self.clauses:
            for formula_clause in origin_formula.clauses:
                formula.clauses.append(clause.or_clause(formula_clause))

        return formula

    def and_formula(self, origin_formula: Self) -> Self:
        formula = Formula()

        for clause in self.clauses:
            formula.clauses.append(clause.__copy__())

        for clause in origin_formula.clauses:
            formula.clauses.append(clause.__copy__())

        return formula

    def and_clause(self, origin_clause) -> Self:
        formula = Formula()

        for clause in self.clauses:
            formula.clauses.append(clause.__copy__())

        formula.clauses.append(origin_clause.__copy__())

        return formula

    def __str__(self) -> str:
        result = '['

        for index, clause in enumerate(self.clauses):
            result += clause.__str__()
            if index != len(self.clauses) - 1:
                result += ' & '
        result += ']'

        return result
