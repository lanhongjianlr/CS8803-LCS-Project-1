import numpy as np
import matplotlib.pyplot as plt

# Load the data in the csv files
JW100call = np.loadtxt('Backup/N100JWcall.csv',
                 delimiter=",", dtype=float)
JW100time = np.loadtxt('Backup/N100JWtime.csv',
                 delimiter=",", dtype=float)
JW100sat = np.loadtxt('Backup/N100JWsat.csv',
                 delimiter=",", dtype=float)
JW150call = np.loadtxt('Backup/N150JWcall.csv',
                 delimiter=",", dtype=float)
JW150time = np.loadtxt('Backup/N150JWtime.csv',
                 delimiter=",", dtype=float)
JW150sat = np.loadtxt('Backup/N150JWsat.csv',
                 delimiter=",", dtype=float)
TC100call = np.loadtxt('Backup/N100TCcall.csv',
                 delimiter=",", dtype=float)
TC100time = np.loadtxt('Backup/N100TCtime.csv',
                 delimiter=",", dtype=float)
TC100sat = np.loadtxt('Backup/N100TCsat.csv',
                 delimiter=",", dtype=float)
TC150call = np.loadtxt('Backup/N150TCcall.csv',
                 delimiter=",", dtype=float)
TC150time = np.loadtxt('Backup/N150TCtime.csv',
                 delimiter=",", dtype=float)
TC150sat = np.loadtxt('Backup/N150TCsat.csv',
                 delimiter=",", dtype=float)
R100call = np.loadtxt('Backup/N100Rcall.csv',
                 delimiter=",", dtype=float)
R100time = np.loadtxt('Backup/N100Rtime.csv',
                 delimiter=",", dtype=float)
R100sat = np.loadtxt('Backup/N100Rsat.csv',
                 delimiter=",", dtype=float)
R150call = np.loadtxt('Backup/N150Rcall.csv',
                 delimiter=",", dtype=float)
R150time = np.loadtxt('Backup/N150Rtime.csv',
                 delimiter=",", dtype=float)
R150sat = np.loadtxt('Backup/N150Rsat.csv',
                 delimiter=",", dtype=float)

x = np.arange(3, 6.2, 0.2)

plt.plot(x, JW100call, label="N=100")
plt.plot(x, JW150call, label="N=150")
plt.legend()
plt.title("Number of Calls v.s. L/N (JW)")
plt.xlabel("L/N")
plt.ylabel("Number of Calls")
plt.show()

plt.plot(x, JW100time, label="N=100")
plt.plot(x, JW150time, label="N=150")
plt.legend()
plt.title("Compute Time v.s. L/N (JW)")
plt.xlabel("L/N")
plt.ylabel("Compute Time (s)")
plt.show()

plt.plot(x, JW100sat, label="N=100")
plt.plot(x, JW150sat, label="N=150")
plt.legend()
plt.title("Ratio of Satisfiability v.s. L/N (JW)")
plt.xlabel("L/N")
plt.ylabel("Ratio of Satisfiability")
plt.show()

plt.plot(x, JW100call / R100call, label="N=100, Number of Calls")
plt.plot(x, JW100time / R100time, label="N=100, Compute Time")
plt.plot(x, JW150call / R150call, label="N=150, Number of Calls")
plt.plot(x, JW150time / R150time, label="N=150, Compute Time")
plt.legend()
plt.title("Ratios of Performance v.s. L/N (JW v.s. RAND)" )
plt.xlabel("L/N")
plt.ylabel("Ratio of Performance")
plt.show()

plt.plot(x, JW100call / TC100call, label="N=100, Number of Calls")
plt.plot(x, JW100time / TC100time, label="N=100, Compute Time")
plt.plot(x, JW150call / TC150call, label="N=150, Number of Calls")
plt.plot(x, JW150time / TC150time, label="N=150, Compute Time")
plt.legend()
plt.title("Ratios of Performance v.s. L/N (JW v.s. 2 Clause)")
plt.xlabel("L/N")
plt.ylabel("Ratio of Performance")
plt.show()