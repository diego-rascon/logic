import re

from infix_to_postfix import infix_to_postfix, evaluate

file = open("formulas/fnc/fnc_2.txt")
lines = file.readlines()

for line in lines:
    print(f'Line: {line}')
    infix_exp = re.findall("(\\w+|\\||&|>|-|\\(|\\)|=)", line)
    print(f'Infijo: {infix_exp}')

    postfix_exp = infix_to_postfix(infix_exp)
    print(f'Postfijo: {postfix_exp}')

    fnc = evaluate(postfix_exp)
    print(f'FNC: {fnc}')
