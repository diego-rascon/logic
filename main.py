from infix_postfix import infix_to_postfix

file = open('formulas/formula_1.txt')
rows = file.readlines()


for row in rows:
    row = row.rstrip()
    infix_to_postfix(row)
    '''
    print(f'Row: {row}')
    infix = re.findall('(\\w+|\\||\\&|\\>|\\-|\\(|\\)|\\=)', row)
    print(f'Infix: {row}')
    postfix = infix_to_postfix(row)
    print(f'Postfix: {postfix}')
    '''
