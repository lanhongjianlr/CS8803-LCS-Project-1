from ReadCNF import ReadCNF
from DPLL import DPLL

N, L, cnf = ReadCNF('Einstein.cnf')
lit = [None] * (N + 1)
lit[0] = True
unassigned = list(range(N + 1))
unassigned.remove(0)
Satisfied, truthtable = DPLL(N, L, cnf, lit, unassigned)
if Satisfied:
    print("The CNF is satisfiable.")
else:
    print("The CNF is unsatisfiable.")
