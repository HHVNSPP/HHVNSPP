import os
from time import time
from solution import initial
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

limit = 5 # maximum runtime for each individual execution in seconds
maxiter = 1030 # maximum iterations
replicas = 30 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = [ 'P', 'o', 'm' ] # we conserve the filenames of the cited authors 
filetypes = [ '.dat', '.txt', '.txt' ] 
load = { 'A': loadA, 'B': loadB, 'C': loadC }
verbose = False

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    if verbose:
        print('Reading instances from', directory)
    for filename in os.listdir(directory):
        print('Examining file', filename)
        if filename.startswith(prefix) and filename.endswith(ending):
            instance = directory + filename
            if verbose:
                print(f'Processing instance {instance}')
            pf = load[s](instance)         
            for r in range(1, replicas + 1):
                timestamp = time()
                print(f'Executing replica {r} for {filename} in {directory}')
                with open(output + f'r{r}_' + filename, 'w') as target:                
                    adj = Adjustment(initial(pf))
                    if adj is None:
                        print(f'ERROR: no feasible initial solution')
                        break
                    o = 1
                    for i in range(maxiter):
                        if not adj.step():
                            break # stalled
                        diff = time() - timestamp
                        if i == o: # output on iterations that are powers of two
                            print(f'w;{i};{diff}', file = target)
                            adj.output(target)
                            o *= 2
                        if diff > limit:
                            print('Time limit exceeded')
                            break
                    adj.postprocess(pf.weights, target) 
