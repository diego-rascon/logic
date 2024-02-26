from Atom import Atom
from Clause import Clause

clause = Clause()
atom_1 = Atom('atom_1')
atom_2 = Atom('atom_2')
atom_2.invert()

clause.add_atom(atom_1)
clause.add_atom(atom_2)

print(clause)
