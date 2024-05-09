import re

from model.Atom import Atom
from model.Clause import Clause
from model.Formula import Formula
from modules.gsat import gsat


def infix_to_postfix(infix):
    postfix = []
    stack = []

    for char in infix:
        p = get_priority(char)

        if p == -1:
            stack.append(char)
        elif p == -2:
            while len(stack) > 0:
                top = stack.pop()
                if top != "(":
                    postfix.append(top)
                else:
                    break

        elif p > 0:
            if len(stack) == 0 or p > get_priority(stack[-1]):
                stack.append(char)
            else:
                while len(stack) > 0 and p < get_priority(stack[-1]):
                    top = stack.pop()
                    postfix.append(top)

                stack.append(char)
        else:
            postfix.append(char)

    while len(stack) > 0:
        postfix.append(stack.pop())

    return postfix


def get_priority(a):
    if a == "|":
        return 1
    if a == "&":
        return 2
    if a == ">":
        return 3
    if a == "=":
        return 4
    if a == "-":
        return 5
    if a == "(":
        return -1
    if a == ")":
        return -2
    else:
        return 0


def valuate(postfix):
    stack = []
    for ch in postfix:
        p = get_priority(ch)
        if p == 0:
            a = Atom(ch)
            c = Clause()
            f = Formula()
            c = c.or_atom(a)
            c = f.and_clause(c)
            stack.append(c)
        elif p == 1:
            b = stack.pop()
            a = stack.pop()
            c = a.or_formula(b)
            stack.append(c)
        elif p == 2:
            b = stack.pop()
            a = stack.pop()
            c = a.and_formula(b)
            stack.append(c)
        elif p == 3:
            b = stack.pop()
            a = stack.pop()
            a = a.invert_formula()
            c = a.or_formula(b)
            stack.append(c)
        elif p == 4:
            b = stack.pop()
            a = stack.pop()
            an = a.invert_formula()
            bn = b.invert_formula()
            c = a.or_formula(bn)
            d = b.or_formula(an)
            c = c.and_formula(d)
            stack.append(c)
        elif p == 5:
            a = stack.pop()
            c = a.invert_formula()
            stack.append(c)

    return stack.pop()


def read_file():
    file = open("formulas/davis_putnam.txt")
    lines = file.readlines()

    for line in lines:
        print(f'Linea: {line}')
        infix_exp = re.findall("(\\w+|\\||&|>|-|\\(|\\)|=)", line)
        print(f'Infijo: {infix_exp}')
        postfix_exp = infix_to_postfix(infix_exp)
        print(f'Postfijo: {postfix_exp}')
        fnc = valuate(postfix_exp)
        print(f'FNC: {fnc}')
        # max_tries = int(input('Introduce el máximo de intentos: '))
        # max_flips = int(input('Introduce el máximo de flips: '))
        # print(f'GSAT: {gsat(fnc, max_tries, max_flips)}')
        # if fnc.david_and_putnam():
        #     fnc.get_certificate()
        # else:
        #     print('La formula es insatisfactible')
        satisfiable, assignment = fnc.davis_putnam()
        if satisfiable:
            print("La formula es satisfactible con:")
            print(assignment)
        else:
            print("La formula es insatisfactible")
        print()


read_file()
