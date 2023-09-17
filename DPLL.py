import copy
import numpy as np

def DPLL(N, L, cnf, lit, unassigned):
    HasUnit = True
    Satisfied = False
    formula = copy.deepcopy(cnf)
    TruthTable = lit
    UnAssig = copy.deepcopy(unassigned)

    # Check unit clauses
    while HasUnit:
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True
                prop = clause[0]
                # Set the value for lit[abs(prop)]
                TruthTable[abs(prop)] = (prop > 0)
                UnAssig.remove(abs(prop))
                DeleteList = []
                for cl in formula:
                    # Record all the clauses with prop
                    if prop in cl:
                        DeleteList.append(cl)
                    # Delete all the -prop in the clauses
                    elif (prop * -1) in cl:
                        cl.remove((prop * -1))
                # Delete all the clauses with prop
                for deleted in DeleteList:
                    formula.remove(deleted)
        HasUnit = False
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True

    # Check if formula is empty. If so, return True
    if len(formula) == 0:
        Satisfied = True
        print('The right assignment is')
        for i in range(1,126):
            print(i, TruthTable[i])
        return Satisfied, TruthTable

    # Check null clause. If so, return False
    for clause in formula:
        if len(clause) == 0:
            Satisfied = False
            return Satisfied, TruthTable

    # Select a literal in UnAssig
    # Jeroslow-Wang Heuristics
    PosWeights = np.zeros(N + 1)
    NegWeights = np.zeros(N + 1)
    for clause in formula:
        for y in clause:
            if y > 0:
                PosWeights[y] += 2 ** (-len(clause))
            else:
                NegWeights[abs(y)] += 2 ** (-len(clause))
    TotWeights = PosWeights + NegWeights
    x = np.argmax(TotWeights)
    # Assign the sign
    if NegWeights[x] > PosWeights[x]:
        x = x * (-1)
    # Assign it to be True
    newformula = copy.deepcopy(formula + [[x]])
    Satisfied, TruthTable = DPLL(N, L, newformula, TruthTable, UnAssig)
    if Satisfied:
        return Satisfied, TruthTable

    # Assign the other sign to it
    newformula = copy.deepcopy(formula + [[x * (-1)]])
    Satisfied, TruthTable = DPLL(N, L, newformula, TruthTable, UnAssig)
    if Satisfied:
        return Satisfied, TruthTable

    return Satisfied, TruthTable
