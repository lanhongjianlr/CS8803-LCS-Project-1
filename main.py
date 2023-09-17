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
#print(lit)
'''
for i in range(126):
    print(i, truthtable[i])
print(lit)
print((lit[15], lit[40], lit[65], lit[90], lit[115]))
print(lit[1+25*0:26+25*0])
'''