def ReadCNF(file):
    f = open(file, 'r')
    comment = f.readline()
    # Read the metadata in the cnf file
    meta = f.readline().split()
    N = int(meta[2])
    L = int(meta[3])
    # Read the clauses
    cnf = []
    clause = []
    while line := f.readline():
        for word in line.split():
            prop = int(word)
            if prop != 0:
                clause.append(prop)
            else:
                cnf.append(clause)
                clause = []

    #print(cnf)
    return N, L, cnf
