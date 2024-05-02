from model.Formula import Formula
from model.Clause import Clause
from model.Atom import Atom
import random


def gsat(formula: Formula, max_tries, max_flips):
    for current_try in range(max_tries):
        atoms = {}

        for clause in formula.clauses:
            for atom in clause.atoms:
                atoms[atom.name] = True if random.random() >= 0.5 else False
        
        print(atoms)

        for flip in range(max_flips):
            last_value = None

            for clause in formula.clauses:

                for atom in clause.atoms:
                    value = atoms[atom.name] 
                    value = not value if atom.inverted else value
                    last_value = value

                    print(atom.name)
                    print(f'Inverted: {atom.inverted}')
                    print(f'Valor: {value}')
                    print()

                    if value:
                        break

                if not last_value:
                    print('No se cumple la clausula')
                    break

                print('Se cumplió la clausula')

            if last_value:
                return atoms
            else:
                random_atom = random.choice(list(atoms))
                atoms[random_atom] = not atoms[random_atom]
                print(f'Random atom: {random_atom}')
                print(atoms)
            print('------------------------------------')

    return 'No se encontró solución a la formula'
