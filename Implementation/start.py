import os
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = True
replicas = 30 if not verbose else 5 # testing with less
prefixes = [ 'P', 'o', 'm' ] # we conserve the filenames of the cited authors 
filetypes = [ '.dat', '.txt', '.txt' ] # however inconsistent those may be
load = { 'A': loadA, 'B': loadB, 'C': loadC } # parsing routines

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    if verbose:
        print('Reading instances from', directory)
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(ending):
            instance = directory + filename
            if verbose:
                print(f'Processing instance {instance}')
            portfolio = load[s](instance)
            n = len(portfolio.projects)
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}')
                with open(output + f'r{r}_' + filename, 'w') as target:
                    Adjustment(portfolio, target).run()
