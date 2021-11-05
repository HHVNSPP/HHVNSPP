import os
from sys import stderr
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = True
replicas = 3
prefixes = [ 'P', 'k', 'C' ] 
load = { 'A': loadA, 'B': loadB, 'C': loadC } # parsing routines
skip = 'BC' # in case only partial experiments are desired
suffix = '.txt'
# for A, we also run mono-objective variants for comparison for the set A
keep = { 'A': [ [], [ False, True ], [ True, False ] ],
         'B': [ [] ],
         'C': [ [] ] }
synergies = { 'C': [ True, False ] } # with and without for set C

for s in 'ABC':
    directory = r'../Data/' + s + '/'
    output = f'../Results/{s}/'
    prefix = prefixes.pop(0)
    if s in skip:
        continue
    for filename in os.listdir(directory):
        print(filename)
        if filename.startswith(prefix) and filename.endswith(suffix):
            instance = directory + filename
            for k in keep[s]:
                ks = ''.join(f'{1 * b}' for b in k) if False in k else ''
                # we use the set C both WITH and WITHOUT synergies, the others only without
                for act in syn.get(s, [ True ]): # A and B just run as they are (A has them, B does not)
                    ss = 's_' if act else '_'
                    print(f'Instance {instance} with{"" if act else "out"} synergies')
                    portfolio = load[s](instance, act, k)
                    n = len(portfolio.projects)
                    for r in range(1, replicas + 1):
                        print(f'Executing replica {r} for {filename} in {directory}', file = stderr)
                        with open(output + f'r{r}' + ss + ks + filename, 'w') as target:
                            Adjustment(portfolio, target).run()

