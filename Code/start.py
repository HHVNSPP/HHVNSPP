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
synergies = { 'A': [ False, True ], # without and with for set A 
              'B': [ False ], # set B has no synergies so without only
              'C': [ False, True ] } #  without and wit for set C 

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
            for act in synergies.get(s):
                portfolio = load[s](instance, act)
                if s == 'A' and not act: # only for set A and when there are no synergies active
                    portfolio.ideal() # compute ideal points optimizing each objective individually
                ss = 's_' if act else '_'
                print(f'Instance {instance} with{"" if act else "out"} synergies')                        
                for r in range(1, replicas + 1):
                    print(f'Executing replica {r} for {filename} in {directory}', file = stderr)
                    with open(output + f'r{r}' + ss + filename, 'w') as target:
                        a = Adjustment(portfolio, target)
                        a.run()
