NumNations = 5
N = 125
Nations = ['Brit', 'Swede', 'Dane', 'German', 'Norwegian']
Houses = ['house1', 'house2', 'house3', 'house4', 'house5']
Colors = ['red', 'green', 'white', 'yellow', 'blue']
Pets = ['dog', 'bird', 'cat', 'horse', 'fish']
Drinks = ['tea', 'coffee', 'milk', 'beer', 'water']
Smokes = ['Pall Mall', 'Dunhill', 'Blends', 'Bluemasters', 'Prince']

Index = {'Brit': 0,
         'Swede': 1,
         'Dane': 2,
         'German': 3,
         'Norwegian': 4}

KeyList = Houses + Colors + Pets + Drinks + Smokes

Dicts = []
for i in range(NumNations):
    Dicts.append({key: None for key in KeyList})

NumClauses = 0
k = 1
for i in range(NumNations):
    for key in KeyList:
        Dicts[i][key] = str(k)
        k += 1

print(Dicts[Index['German']])

f = open('Einstein.cnf', 'w')
f.write('c The CNF file\n')
f.write('p cnf 125 1075\n')

# The Brit lives in the red house
f.write(' '.join([Dicts[Index['Brit']]['red'], '0']))
f.write('\n')
NumClauses += 1

# The Swede keeps dogs as pets
f.write(' '.join([Dicts[Index['Swede']]['dog'], '0']))
f.write('\n')
NumClauses += 1

# The Dane drinks tea
f.write(' '.join([Dicts[Index['Dane']]['tea'], '0']))
f.write('\n')
NumClauses += 1

# The green house is on the left of the white house
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(4):
                f.write(' '.join(['-'+Dicts[Index[nation1]]['house'+str(i+1)], '-'+Dicts[Index[nation1]]['green'],
                                  '-'+Dicts[Index[nation2]]['house'+str(i+2)], Dicts[Index[nation2]]['white'], '0']))
                f.write('\n')
                NumClauses += 1
# The white house cannot be the leftmost one
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['white'], '-'+Dicts[Index[nation]]['house1'], '0']))
    f.write('\n')
    NumClauses += 1
# The green house cannot be the rightmost one
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['green'], '-'+Dicts[Index[nation]]['house5'], '0']))
    f.write('\n')
    NumClauses += 1

# The green house’s owner drinks coffee
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['green'], Dicts[Index[nation]]['coffee'], '0']))
    f.write('\n')
    NumClauses += 1

# The person who smokes Pall Mall rears birds
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['Pall Mall'], Dicts[Index[nation]]['bird'], '0']))
    f.write('\n')
    NumClauses += 1

# The owner of the yellow house smokes Dunhill
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['yellow'], Dicts[Index[nation]]['Dunhill'], '0']))
    f.write('\n')
    NumClauses += 1

# The man living in the center house drinks milk
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['house3'], Dicts[Index[nation]]['milk'], '0']))
    f.write('\n')
    NumClauses += 1

# The Norwegian lives in the first house
f.write(' '.join([Dicts[Index['Norwegian']]['house1'], '0']))
f.write('\n')
NumClauses += 1

# The man who smokes Blends lives next to the one who keeps cats
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(5):
                if i == 0:
                    f.write(
                        ' '.join(['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                                  '-' + Dicts[Index[nation2]]['cat'], Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
                elif i == 4:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                             '-' + Dicts[Index[nation2]]['cat'], Dicts[Index[nation2]]['house' + str(i)], '0']))
                    f.write('\n')
                    NumClauses += 1
                else:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                             '-' + Dicts[Index[nation2]]['cat'], Dicts[Index[nation2]]['house' + str(i)],
                             Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
# The man who smokes Blends cannot keep cats
for nation in Nations:
    f.write(' '.join(['-' + Dicts[Index[nation]]['Blends'], '-' + Dicts[Index[nation]]['cat'], '0']))
    f.write('\n')
    NumClauses += 1
'''
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(4):
                f.write(' '.join(['-'+Dicts[Index[nation1]]['house'+str(i+1)], '-'+Dicts[Index[nation1]]['Blends'],
                                  '-'+Dicts[Index[nation2]]['house'+str(i+2)], Dicts[Index[nation2]]['cat'], '0']))
                f.write('\n')
                NumClauses += 1
                f.write(' '.join(['-'+Dicts[Index[nation1]]['house'+str(i+2)], '-'+Dicts[Index[nation1]]['Blends'],
                                  '-'+Dicts[Index[nation2]]['house'+str(i+1)], Dicts[Index[nation2]]['cat'], '0']))
                f.write('\n')
                NumClauses += 1
'''

# The man who keeps the horse lives next to the man who smokes Dunhill
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(5):
                if i == 0:
                    f.write(
                        ' '.join(['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['horse'],
                                  '-' + Dicts[Index[nation2]]['Dunhill'], Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
                elif i == 4:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['horse'],
                             '-' + Dicts[Index[nation2]]['Dunhill'], Dicts[Index[nation2]]['house' + str(i)], '0']))
                    f.write('\n')
                    NumClauses += 1
                else:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['horse'],
                             '-' + Dicts[Index[nation2]]['Dunhill'], Dicts[Index[nation2]]['house' + str(i)],
                             Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
#The man who keeps the horse cannot smoke Dunhill
for nation in Nations:
    f.write(' '.join(['-' + Dicts[Index[nation]]['horse'], '-' + Dicts[Index[nation]]['Dunhill'], '0']))
    f.write('\n')
    NumClauses += 1
'''
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(4):
                f.write(' '.join(['-'+Dicts[Index[nation1]]['house'+str(i+1)], '-'+Dicts[Index[nation1]]['horse'],
                                  '-'+Dicts[Index[nation2]]['house'+str(i+2)], Dicts[Index[nation2]]['Dunhill'], '0']))
                f.write('\n')
                NumClauses += 1
                f.write(' '.join(['-'+Dicts[Index[nation1]]['house'+str(i+2)], '-'+Dicts[Index[nation1]]['horse'],
                                  '-'+Dicts[Index[nation2]]['house'+str(i+1)], Dicts[Index[nation2]]['Dunhill'], '0']))
                f.write('\n')
                NumClauses += 1
'''

# The owner who smokes Bluemasters drinks beer
for nation in Nations:
    f.write(' '.join(['-'+Dicts[Index[nation]]['Bluemasters'], Dicts[Index[nation]]['beer'], '0']))
    f.write('\n')
    NumClauses += 1

# The German smokes Prince
f.write(' '.join([Dicts[Index['German']]['Prince'], '0']))
f.write('\n')
NumClauses += 1

# The Norwegian lives next to the blue house
for nation in Nations:
    if nation != 'Norwegian':
        for i in range(5):
            if i == 0:
                f.write(' '.join(['-' + Dicts[Index[nation]]['house' + str(i + 1)], '-' + Dicts[Index[nation]]['blue'],
                                  Dicts[Index['Norwegian']]['house' + str(i + 2)], '0']))
                f.write('\n')
                NumClauses += 1
            elif i == 4:
                f.write(' '.join(['-' + Dicts[Index[nation]]['house' + str(i + 1)], '-' + Dicts[Index[nation]]['blue'],
                                  Dicts[Index['Norwegian']]['house' + str(i)], '0']))
                f.write('\n')
                NumClauses += 1
            else:
                f.write(' '.join(['-' + Dicts[Index[nation]]['house' + str(i + 1)], '-' + Dicts[Index[nation]]['blue'],
                                  Dicts[Index['Norwegian']]['house' + str(i)],
                                  Dicts[Index['Norwegian']]['house' + str(i + 2)], '0']))
                f.write('\n')
                NumClauses += 1
# The Norwegian himself cannot live in the blue house
f.write(' '.join(['-' + Dicts[Index['Norwegian']]['blue'], '0']))
f.write('\n')
NumClauses += 1

# The man who smokes Blends has a neighbor who drinks water
for nation1 in Nations:
    for nation2 in Nations:
        if nation1 != nation2:
            for i in range(5):
                if i == 0:
                    f.write(
                        ' '.join(['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                                  '-' + Dicts[Index[nation2]]['water'], Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
                elif i == 4:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                             '-' + Dicts[Index[nation2]]['water'], Dicts[Index[nation2]]['house' + str(i)], '0']))
                    f.write('\n')
                    NumClauses += 1
                else:
                    f.write(
                        ' '.join(
                            ['-' + Dicts[Index[nation1]]['house' + str(i + 1)], '-' + Dicts[Index[nation1]]['Blends'],
                             '-' + Dicts[Index[nation2]]['water'], Dicts[Index[nation2]]['house' + str(i)],
                             Dicts[Index[nation2]]['house' + str(i + 2)], '0']))
                    f.write('\n')
                    NumClauses += 1
# The man who smokes Blends cannot drink water
for nation in Nations:
    f.write(' '.join(['-' + Dicts[Index[nation]]['Blends'], '-' + Dicts[Index[nation]]['water'], '0']))
    f.write('\n')
    NumClauses += 1

# Each man must live in exactly one house
for nation in Nations:
    # Each man must live in at least one house
    f.write(' '.join([Dicts[Index[nation]]['house1'], Dicts[Index[nation]]['house2'], Dicts[Index[nation]]['house3'],
                      Dicts[Index[nation]]['house4'], Dicts[Index[nation]]['house5'], '0']))
    f.write('\n')
    NumClauses += 1
    # Each man must live in at most house
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[nation]][Houses[i]],
                                  '-' + Dicts[Index[nation]][Houses[j]], '0']))
                f.write('\n')
                NumClauses += 1

# No two men live in the same house
for house in Houses:
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[Nations[i]]][house],
                                  '-' + Dicts[Index[Nations[j]]][house], '0']))
                f.write('\n')
                NumClauses += 1

# Each man must live in a house of exactly one color
for nation in Nations:
    # Each man must live in a house of at least one house
    f.write(' '.join([Dicts[Index[nation]]['red'], Dicts[Index[nation]]['green'], Dicts[Index[nation]]['white'],
                      Dicts[Index[nation]]['yellow'], Dicts[Index[nation]]['blue'], '0']))
    f.write('\n')
    NumClauses += 1
    # Each man must live in a house of at most one color
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[nation]][Colors[i]],
                                  '-' + Dicts[Index[nation]][Colors[j]], '0']))
                f.write('\n')
                NumClauses += 1

# No two men live in the house of the same color
for color in Colors:
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[Nations[i]]][color],
                                  '-' + Dicts[Index[Nations[j]]][color], '0']))
                f.write('\n')
                NumClauses += 1

# Each man must have exactly one pet
for nation in Nations:
    # Each man must have at least one pet
    f.write(' '.join([Dicts[Index[nation]][Pets[0]], Dicts[Index[nation]][Pets[1]], Dicts[Index[nation]][Pets[2]],
                      Dicts[Index[nation]][Pets[3]], Dicts[Index[nation]][Pets[4]], '0']))
    f.write('\n')
    NumClauses += 1
    # Each man must have at most one pet
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[nation]][Pets[i]],
                                  '-' + Dicts[Index[nation]][Pets[j]], '0']))
                f.write('\n')
                NumClauses += 1

# No two men have the same pet
for pet in Pets:
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[Nations[i]]][pet],
                                  '-' + Dicts[Index[Nations[j]]][pet], '0']))
                f.write('\n')
                NumClauses += 1

# Each man must drink exactly one drink
for nation in Nations:
    # Each man must drink at least one drink
    f.write(' '.join([Dicts[Index[nation]][Drinks[0]], Dicts[Index[nation]][Drinks[1]], Dicts[Index[nation]][Drinks[2]],
                      Dicts[Index[nation]][Drinks[3]], Dicts[Index[nation]][Drinks[4]], '0']))
    f.write('\n')
    NumClauses += 1
    # Each man must drink at most one drink
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[nation]][Drinks[i]],
                                  '-' + Dicts[Index[nation]][Drinks[j]], '0']))
                f.write('\n')
                NumClauses += 1

# No two men drink the same drink
for drink in Drinks:
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[Nations[i]]][drink],
                                  '-' + Dicts[Index[Nations[j]]][drink], '0']))
                f.write('\n')
                NumClauses += 1

# Each man must smoke exactly one smoke
for nation in Nations:
    # Each man must smoke at least one smoke
    f.write(' '.join([Dicts[Index[nation]][Smokes[0]], Dicts[Index[nation]][Smokes[1]], Dicts[Index[nation]][Smokes[2]],
                      Dicts[Index[nation]][Smokes[3]], Dicts[Index[nation]][Smokes[4]], '0']))
    f.write('\n')
    NumClauses += 1
    # Each man must smoke at most one smoke
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[nation]][Smokes[i]],
                                  '-' + Dicts[Index[nation]][Smokes[j]], '0']))
                f.write('\n')
                NumClauses += 1

# No two men smoke the same smoke
for smoke in Smokes:
    for i in range(4):
        for j in range(5):
            if i < j:
                f.write(' '.join(['-' + Dicts[Index[Nations[i]]][smoke],
                                  '-' + Dicts[Index[Nations[j]]][smoke], '0']))
                f.write('\n')
                NumClauses += 1

f.close()

print(NumClauses)
