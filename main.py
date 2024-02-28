from Formula import Formula
from Atom import Atom
from Clause import Clause

atom_a = Atom('A')
atom_b = Atom('B')
atom_b.invert()
clause_1 = Clause()
clause_1.or_atom(atom_a)
clause_1.or_atom(atom_b)

formula_1 = clause_1.and_atom(atom_b)

print(formula_1)
