import copy
import numpy as np
import time

def UnitPropagation(formula, TruthTable, UnAssig):
    HasUnit = True
    # Check unit clauses
    while HasUnit:
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True
                prop = clause[0]
                # Set the value for lit[abs(prop)]
                TruthTable[abs(prop)] = (prop > 0)
                # Remove abs(prop) from UnAssig
                # print(formula)
                # print(UnAssig)
                # print(prop)
                UnAssig.remove(abs(prop))
                DeleteList = []
                for cl in formula:
                    # Record all the clauses with prop
                    if prop in cl:
                        # formula.remove(cl)
                        DeleteList.append(cl)
                    # Delete all the -prop in the clauses
                    elif (prop * -1) in cl:
                        cl.remove((prop * -1))
                # Delete all the clauses with prop
                for deleted in DeleteList:
                    formula.remove(deleted)
                # break
        HasUnit = False
        for clause in formula:
            if len(clause) == 1:
                HasUnit = True

    return formula, TruthTable, UnAssig

def RDPLL(N, L, cnf, lit, unassigned, splitting, starttime):
    TimeLimit = 60
    #HasNull = False
    Satisfied = False
    #lit = [None] * (N + 1)
    #lit[0] = True
    formula = copy.deepcopy(cnf)
    TruthTable = lit
    UnAssig = copy.deepcopy(unassigned)
    # Create stacks for storing the status
    TruthTableStack = []
    UnAssigStack = []
    formulaStack = []
    xStack = []

    formula, TruthTable, UnAssig = UnitPropagation(formula, TruthTable, UnAssig)
    #UnitPropagation(formula, TruthTable, UnAssig)
    # Check if formula is empty. If so, return True
    if len(formula) == 0:
        Satisfied = True
        #print('The right assignment is')
        #for i in range(1, N + 1):
        #    print(i, TruthTable[i])
        return Satisfied, TruthTable, splitting, time.time() - starttime

    # Check null clause. If so, return False
    for clause in formula:
        if len(clause) == 0:
            Satisfied = False
            return Satisfied, TruthTable, splitting, time.time() - starttime

    while len(UnAssig) > 0:
        # Push the current status into the stacks
        TruthTableStack.append(copy.deepcopy(TruthTable))
        UnAssigStack.append(copy.deepcopy(UnAssig))
        formulaStack.append(copy.deepcopy(formula))
        # If the runtime exceeds the limit, stop the process
        if (time.time() - starttime) > TimeLimit:
            return Satisfied, TruthTable, splitting, time.time() - starttime

        # Select a literal in UnAssig
        splitting += 1
        # RAND
        x = UnAssig[0]
        # Assign the sign
        sign = np.random.random(1)
        if sign > 0.5:
            x = x * (-1)
        xStack.append(x)
        formula = copy.deepcopy(formula + [[x]])
        formula, TruthTable, UnAssig = UnitPropagation(formula, TruthTable, UnAssig)
        #UnitPropagation(formula, TruthTable, UnAssig)
        # Check if formula is empty. If so, return True
        if len(formula) == 0:
            Satisfied = True
            #print('The right assignment is')
            #for i in range(1, N + 1):
            #    print(i, TruthTable[i])
            return Satisfied, TruthTable, splitting, time.time() - starttime
        HasNull = False
        # Check null clause. If so, roll the status back to Stack[-1].
        for clause in formula:
            if len(clause) == 0:
                HasNull = True
        while HasNull == True:
            # If there is no previous status in the stacks, then the cnf is nonsatisfiable.
            if len(UnAssigStack) == 0:
                Satisfied = False
                return Satisfied, TruthTable, splitting, time.time() - starttime
            formula = copy.deepcopy(formulaStack[-1])
            TruthTable = copy.deepcopy(TruthTableStack[-1])
            UnAssig = copy.deepcopy(UnAssigStack[-1])
            x = xStack[-1]
            # Pop the last element in the stacks.
            formulaStack.remove(formulaStack[-1])
            TruthTableStack.remove(TruthTableStack[-1])
            UnAssigStack.remove(UnAssigStack[-1])
            xStack.remove(xStack[-1])
            # Assign the other sign to it
            x = x * -1
            formula = copy.deepcopy(formula + [[x]])
            formula, TruthTable, UnAssig = UnitPropagation(formula, TruthTable, UnAssig)
            #UnitPropagation(formula, TruthTable, UnAssig)
            # Check if formula is empty. If so, return True
            if len(formula) == 0:
                Satisfied = True
                #print('The right assignment is')
                #for i in range(1, N + 1):
                #    print(i, TruthTable[i])
                return Satisfied, TruthTable, splitting, time.time() - starttime
            HasNull = False
            # Check null clause. If so, roll the status back to Stack[-1].
            for clause in formula:
                if len(clause) == 0:
                    HasNull = True


    return Satisfied, TruthTable, splitting, time.time() - starttime