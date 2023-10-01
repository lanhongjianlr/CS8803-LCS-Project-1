from DPLL import DPLL
from TwoClauseDPLL import TCDPLL
from RandomDPLL import RDPLL
from ReadCNF import ReadCNF
import time
import numpy as np

def RunExperiment(heuristic):
    if heuristic == 'R':
        # Run N=100 formulas
        N100Rtime = np.zeros(16)
        N100Rcall = np.zeros(16)
        N100Rsat = np.zeros(16)

        N = 100
        Ls = []
        for i in range(16):
            Ls.append(300 + 20 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = RDPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N100Rtime[i] = np.median(times)
            N100Rcall[i] = np.median(calls)
            N100Rsat[i] = np.sum(sats) / 100

        np.savetxt('N100Rtime.csv', N100Rtime, delimiter=',')
        np.savetxt('N100Rcall.csv', N100Rcall, delimiter=',')
        np.savetxt('N100Rsat.csv', N100Rsat, delimiter=',')
        # Run N=150 formulas
        N150Rtime = np.zeros(16)
        N150Rcall = np.zeros(16)
        N150Rsat = np.zeros(16)

        N = 150
        Ls = []
        for i in range(16):
            Ls.append(450 + 30 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = RDPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N150Rtime[i] = np.median(times)
            N150Rcall[i] = np.median(calls)
            N150Rsat[i] = np.sum(sats) / 100

        np.savetxt('N150Rtime.csv', N150Rtime, delimiter=',')
        np.savetxt('N150Rcall.csv', N150Rcall, delimiter=',')
        np.savetxt('N150Rsat.csv', N150Rsat, delimiter=',')

    elif heuristic == 'TC':
        # Run N=100 formulas
        N100TCtime = np.zeros(16)
        N100TCcall = np.zeros(16)
        N100TCsat = np.zeros(16)

        N = 100
        Ls = []
        for i in range(16):
            Ls.append(300 + 20 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = TCDPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N100TCtime[i] = np.median(times)
            N100TCcall[i] = np.median(calls)
            N100TCsat[i] = np.sum(sats) / 100

        np.savetxt('N100TCtime.csv', N100TCtime, delimiter=',')
        np.savetxt('N100TCcall.csv', N100TCcall, delimiter=',')
        np.savetxt('N100TCsat.csv', N100TCsat, delimiter=',')
        # Run N=150 formulas
        N150TCtime = np.zeros(16)
        N150TCcall = np.zeros(16)
        N150TCsat = np.zeros(16)

        N = 150
        Ls = []
        for i in range(16):
            Ls.append(450 + 30 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = TCDPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N150TCtime[i] = np.median(times)
            N150TCcall[i] = np.median(calls)
            N150TCsat[i] = np.sum(sats) / 100

        np.savetxt('N150TCtime.csv', N150TCtime, delimiter=',')
        np.savetxt('N150TCcall.csv', N150TCcall, delimiter=',')
        np.savetxt('N150TCsat.csv', N150TCsat, delimiter=',')

    elif heuristic == 'JW':
        # Run N=100 formulas
        N100JWtime = np.zeros(16)
        N100JWcall = np.zeros(16)
        N100JWsat = np.zeros(16)

        N = 100
        Ls = []
        for i in range(16):
            Ls.append(300 + 20 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = DPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N100JWtime[i] = np.median(times)
            N100JWcall[i] = np.median(calls)
            N100JWsat[i] = np.sum(sats) / 100

        np.savetxt('N100JWtime.csv', N100JWtime, delimiter=',')
        np.savetxt('N100JWcall.csv', N100JWcall, delimiter=',')
        np.savetxt('N100JWsat.csv', N100JWsat, delimiter=',')
        # Run N=150 formulas
        N150JWtime = np.zeros(16)
        N150JWcall = np.zeros(16)
        N150JWsat = np.zeros(16)

        N = 150
        Ls = []
        for i in range(16):
            Ls.append(450 + 30 * i)

        for i in range(16):
            print(Ls[i])
            times = np.zeros(100)
            calls = np.zeros(100)
            sats = np.zeros(100)
            for j in range(100):
                print(j)
                n, l, cnf = ReadCNF('CNFs/N=' + str(N) + '/L=' + str(Ls[i]) + '/' + str(j + 1) + '.cnf')
                lit = [None] * (N + 1)
                lit[0] = True
                unassigned = list(range(n + 1))
                unassigned.remove(0)
                Satisfied, truthtable, splitting, runtime = DPLL(n, l, cnf, lit, unassigned, splitting=0,
                                                                  starttime=time.time())
                times[j] = runtime
                calls[j] = splitting
                if Satisfied:
                    sats[j] = 1
                else:
                    sats[j] = 0
            N150JWtime[i] = np.median(times)
            N150JWcall[i] = np.median(calls)
            N150JWsat[i] = np.sum(sats) / 100

        np.savetxt('N150JWtime.csv', N150JWtime, delimiter=',')
        np.savetxt('N150JWcall.csv', N150JWcall, delimiter=',')
        np.savetxt('N150JWsat.csv', N150JWsat, delimiter=',')

    else:
        print('No corresponding heuristic. Please check your input. ')