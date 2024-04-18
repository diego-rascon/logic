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
    pila = []
    for ch in postfix:
        p = get_priority(ch)
        if p == 0:  # operando
            a = Atom(ch)
            c = Clause()
            f = Formula()
            c = c.or_atom(a)
            c = f.and_clause(c)
            pila.append(c)
        elif p == 1:  # or
            b = pila.pop()
            a = pila.pop()
            c = a.or_formula(b)
            pila.append(c)
        elif p == 2:  # and
            b = pila.pop()
            a = pila.pop()
            c = a.and_formula(b)
            pila.append(c)
        elif p == 3:  # entonces
            b = pila.pop()
            a = pila.pop()
            a = a.invert()
            c = a.or_formula(b)
            pila.append(c)
        elif p == 4:  # si y solo si
            b = pila.pop()
            a = pila.pop()
            an = a.invert()
            bn = b.invert()
            c = a.or_formula(bn)
            d = b.or_formula(an)
            c = c.and_formula(d)
            pila.append(c)
        elif p == 5:  # not
            a = pila.pop()
            c = a.invert()
            pila.append(c)

    return pila.pop()
