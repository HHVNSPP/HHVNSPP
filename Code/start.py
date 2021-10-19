import os
from sys import stderr
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = True
replicas = 3
prefixes = [ 'P', 'o', 'C' ] # we conserve the filenames of the cited authors 
filetypes = [ '.dat', '.txt', '.txt' ] # however inconsistent those may be
load = { 'A': loadA, 'B': loadB, 'C': loadC } # parsing routines
skip = '' # in case only partial experiments are desired

for s in 'ABC':
    directory = r'../Data/' + s + '/'
    output = f'../Results/{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    if s in skip:
        continue
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(ending):
            instance = directory + filename
            # we use the set C both WITH and WITHOUT synergies, the others only without
            syn = [ True, False ] if s == 'C' else [ False ]
            for act in syn:
                portfolio = load[s](instance, act)
                n = len(portfolio.projects)
                for r in range(1, replicas + 1):
                    print(f'Executing replica {r} for {filename} in {directory}', file = stderr)
                    with open(output + f'r{r}_' + filename, 'w') as target:
                        Adjustment(portfolio, target).run()
