from Atom import Atom
from Clause import Clause

atom_a = Atom('A')
atom_b = Atom('B')
atom_b.invert()
atom_c = Atom('c')

clause_1 = Clause()
clause_2 = Clause()

clause_1 = clause_1.or_atom(atom_a)
clause_1 = clause_1.or_atom(atom_b)
clause_1 = clause_1.or_atom(atom_c)

formula_1 = clause_1.invert()

print(formula_1)
