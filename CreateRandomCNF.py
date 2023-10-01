import numpy as np

K = 3



def CreateRandomCNF(N, L, filename):
    f = open(filename, 'w')
    f.write('c The CNF file\n')
    f.write('p cnf ' + str(int(N)) + ' ' + str(int(L)) + '\n')
    Prop = np.array(range(N))

    for i in range(L):
        np.random.shuffle(Prop)
        for j in range(K):
            sign = np.random.random(1)
            if sign > 0.5:
                f.write(str(Prop[j] + 1) + ' ')
            else:
                f.write('-' + str(Prop[j] + 1) + ' ')
        f.write('0\n')

    f.close()


for i in range(16):
    l = int(300 + 20 * i)
    print(l)
    for j in range(100):
       CreateRandomCNF(N=100, L=l, filename='CNFs/N=100/L=' + str(l) + '/' + str(j+1) + '.cnf')

for i in range(16):
    l = int(450 + 30 * i)
    print(l)
    for j in range(100):
       CreateRandomCNF(N=150, L=l, filename='CNFs/N=150/L=' + str(l) + '/' + str(j+1) + '.cnf')
