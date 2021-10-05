import os
from solution import initial
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = True
limit = 20 if not verbose else 5 # maximum runtime for each individual execution in seconds
maxiter = 1030 if not verbose else 100 # maximum iterations
replicas = 30 if not verbose else 3 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = [ 'P', 'o', 'm' ] # we conserve the filenames of the cited authors 
filetypes = [ '.dat', '.txt', '.txt' ] 
load = { 'A': loadA, 'B': loadB, 'C': loadC }

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    if s in 'A': # debugging later groups
        continue
    if verbose:
        print('Reading instances from', directory)
    for filename in os.listdir(directory):
#        if 'obj4' not in filename: # debugging later groups
#            continue
        print('Examining file', filename)
        if filename.startswith(prefix) and filename.endswith(ending):
            instance = directory + filename
            if verbose:
                print(f'Processing instance {instance}')
            pf = load[s](instance)         
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}')
                with open(output + f'r{r}_' + filename, 'w') as target:                
                    adj = Adjustment(initial(pf), limit)
                    assert adj is not None
                    o = 1
                    for i in range(maxiter):
                        if i == o: # output on iterations that are powers of two 
                            print(f'w;{i}', file = target)                           
                            adj.output(target)
                            o *= 2
                        if not adj.step():
                            break # out of time or stalled
                    adj.postprocess(pf.weights, target) 
