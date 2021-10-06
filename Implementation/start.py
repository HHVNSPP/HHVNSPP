import os
from tools import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

verbose = False
limit = 60 if not verbose else 5 # max runtime per replica in seconds
maxiter = 70 if not verbose else 5 # maximum iterations
replicas = 30 if not verbose else 3 
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
            pf = load[s](instance)
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}')
                with open(output + f'r{r}_' + filename, 'w') as target:
                    adj = Adjustment(pf, limit, target)
                    o = 1
                    for i in range(maxiter):
                        out = i == o
                        if out:
                            print(f'w;{i}', file = target) 
                            o *= 2
                        if not adj.step(out):
                            pl = 's' if i > 0 else ''
                            print(f'Terminated after {i+1} iteration{pl}') 
                            break # out of time or stalled
                    adj.postprocess()
