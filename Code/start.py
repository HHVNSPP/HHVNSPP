import os
from sys import stderr
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = True
replicas = 3
prefixes = [ 'P', 'k', 'C' ]
# parsing routines for instance sets
load = { 'A': loadA, 'B': loadB, 'C': loadC } 
suffix = '.txt'

for s in 'ABC': 
    directory = r'../Data/' + s + '/'
    output = f'../Results/{s}/'
    prefix = prefixes.pop(0)
    for filename in os.listdir(directory):
        print(filename)
        if filename.startswith(prefix) and filename.endswith(suffix):
            instance = directory + filename
            print(f'Instance {instance}')
            portfolio = load[s](instance)
            if s == 'A': # we only make use of this for Set A in our work
                # compute ideal points optimizing each objective individually                
                print(f'Determining the ideal point for instance {instance} of set A')
                portfolio.ideal()
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}',
                      file = stderr)
                with open(output + f'r{r}-original-' + filename, 'w') as target:
                    a = Adjustment(portfolio, target)
                    a.run()
            if len(portfolio.synergies) > 0: # if there were synergies
                portfolio.synergies = [] # also run without them present
                for r in range(1, replicas + 1):
                    print(f'Executing replica {r} without synergies', file = stderr)
                    with open(output + f'r{r}-reduced-' + filename, 'w') as target:
                        a = Adjustment(portfolio, target)
                        a.run()
