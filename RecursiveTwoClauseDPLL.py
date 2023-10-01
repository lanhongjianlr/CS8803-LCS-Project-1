import copy
import numpy as np
import time

def TCDPLLRec(N, L, cnf, lit, unassigned, splitting, starttime):
    TimeLimit = 120
    HasUnit = True
    #HasNull = False
    Satisfied = False
    #lit = [None] * (N + 1)
    #lit[0] = True
    formula = copy.deepcopy(cnf)
    TruthTable = lit
    UnAssig = copy.deepcopy(unassigned)

    #print(formula)
    #print(UnAssig)

    # If the runtime exceeds the limit, stop the process
    if (time.time() - starttime) > TimeLimit:
        return Satisfied, TruthTable, splitting, time.time() - starttime

    # Check unit clauses
    while HasUnit:
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True
                prop = clause[0]
                # Set the value for lit[abs(prop)]
                TruthTable[abs(prop)] = (prop > 0)
                # Remove abs(prop) from UnAssig
                #print(formula)
                #print(UnAssig)
                #print(prop)
                UnAssig.remove(abs(prop))
                DeleteList = []
                for cl in formula:
                    # Record all the clauses with prop
                    if prop in cl:
                        #formula.remove(cl)
                        DeleteList.append(cl)
                    # Delete all the -prop in the clauses
                    elif (prop * -1) in cl:
                        cl.remove((prop * -1))
                # Delete all the clauses with prop
                for deleted in DeleteList:
                    formula.remove(deleted)
                #break
        HasUnit = False
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True

    # Check if formula is empty. If so, return True
    if len(formula) == 0:
        Satisfied = True
        print('The right assignment is')
        for i in range(1, N + 1):
            print(i, TruthTable[i])
        return Satisfied, TruthTable, splitting, time.time() - starttime

    # Check null clause. If so, return False
    for clause in formula:
        if len(clause) == 0:
            Satisfied = False
            return Satisfied, TruthTable, splitting, time.time() - starttime

    # Keep a record of the original formula
    #formularecord = formula.copy()
    # Select a literal in UnAssig
    splitting += 1
    # 2 Clause Heuristics
    TwoClausePosNum = np.zeros(N + 1)
    TwoClauseNegNum = np.zeros(N + 1)
    for clause in formula:
        if len(clause) == 2:
            for i in range(len(clause)):
                if clause[i] in UnAssig:
                    TwoClausePosNum[clause[i]] += 1
                elif (clause[i] * (-1)) in UnAssig:
                    TwoClauseNegNum[abs(clause[i])] += 1
    TwoClauseNum = TwoClausePosNum + TwoClauseNegNum
    if max(TwoClauseNum) == 0:
        x = UnAssig[0]
    else:
        x = np.argmax(TwoClauseNum)
    # Assign the sign
    if TwoClauseNegNum[x] > TwoClausePosNum[x]:
        x = x * (-1)

    #UnAssig.remove(x)
    # Assign it to be True
    newformula = copy.deepcopy(formula + [[x]])
    #newformula = (formula + [[x]]).copy()
    #print('try pos', x)
    #print(UnAssig)
    #print('pos form', formula)
    Satisfied, TruthTable, splitting, _ = TCDPLLRec(N, L, newformula, TruthTable, UnAssig, splitting, starttime)
    if Satisfied:
        return Satisfied, TruthTable, splitting, time.time() - starttime
    #
    #formula = formularecord.copy()
    # Assign the other sign to it
    newformula = copy.deepcopy(formula + [[x * (-1)]])
    #newformula = (formula + [[x*(-1)]]).copy()
    #print('try neg', x*(-1))
    #print(UnAssig)
    #print('neg form', formula)
    Satisfied, TruthTable, splitting, _ = TCDPLLRec(N, L, newformula, TruthTable, UnAssig, splitting, starttime)
    if Satisfied:
        return Satisfied, TruthTable, splitting, time.time() - starttime

    #print(formula)
    return Satisfied, TruthTable, splitting, time.time() - starttime