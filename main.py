import re

from Atom import Atom
from Clause import Clause
from infix_to_postfix import infix_to_postfix, evaluate


def read_file():
    file = open("formulas/fnc.txt")
    lines = file.readlines()

    for line in lines:
        print(f'Line: {line}')
        infix_exp = re.findall("(\\w+|\\||&|>|-|\\(|\\)|=)", line)
        print(f'Infijo: {infix_exp}')

        postfix_exp = infix_to_postfix(infix_exp)
        print(f'Postfijo: {postfix_exp}')

        fnc = evaluate(postfix_exp)
        print(f'FNC: {fnc}')


def new_clause():
    c1 = Clause()
    c1 = c1.or_atom(Atom('a'))
    c1 = c1.or_atom(Atom('b').invert())
    c1 = c1.or_atom(Atom('b'))

    print(c1)


read_file()
# new_clause()
