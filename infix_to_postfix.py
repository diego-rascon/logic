from Atom import Atom
from Clause import Clause
from Formula import Formula


def infix_to_postfix(infix):
    postfix = []
    stack = []

    for char in infix:
        priority = get_priority(char)

        if priority == -1:
            stack.append(char)
        elif priority == -2:
            while len(stack) > 0:
                top_stack = stack.pop()
                if top_stack != "(":
                    postfix.append(top_stack)
                else:
                    break
        elif priority > 0:
            if len(stack) == 0 or priority > get_priority(stack[-1]):
                stack.append(char)
            else:
                while len(stack) > 0 and priority < get_priority(stack[-1]):
                    top_stack = stack.pop()
                    postfix.append(top_stack)
                stack.append(char)
        else:
            postfix.append(char)

    while len(stack) > 0:
        postfix.append(stack.pop())

    return postfix


def get_priority(operator):
    match operator:
        case '|':
            return 1
        case '&':
            return 2
        case '>':
            return 3
        case '=':
            return 4
        case '-':
            return 5
        case '(':
            return -1
        case ')':
            return -2
        case _:
            return 0


def evaluate(postfix):
    stack = []

    for char in postfix:
        priority = get_priority(char)

        if priority == 0:
            atom = Atom(char)
            clause = Clause()
            formula = Formula()
            clause = clause.or_atom(atom)
            clause = formula.and_clause(clause)
            stack.append(clause)
        elif priority == 1:
            top_stack = stack.pop()
            atom = stack.pop()
            clause = atom.or_formula(top_stack)
            stack.append(clause)
        elif priority == 2:
            top_stack = stack.pop()
            atom = stack.pop()
            clause = atom.and_formula(top_stack)
            stack.append(clause)
        elif priority == 3:
            top_stack = stack.pop()
            atom = stack.pop()
            atom = atom.invert()
            clause = atom.or_formula(top_stack)
            stack.append(clause)
        elif priority == 4:
            top_stack = stack.pop()
            atom = stack.pop()
            inverted_atom = atom.invert()
            inverted_formula = top_stack.invert()
            clause = atom.or_formula(inverted_formula)
            inverted_formula = top_stack.or_formula(inverted_atom)
            clause = clause.and_formula(inverted_formula)
            stack.append(clause)
        elif priority == 5:
            atom = stack.pop()
            clause = atom.invert()
            stack.append(clause)

    return stack.pop()
