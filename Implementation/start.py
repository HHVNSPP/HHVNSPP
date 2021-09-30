import os
from time import time
from solution import initial
from adjustment import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy

def electre(weights, pool):
    score = zip(pool, Electre(weights, [sol.impact for sol in pool]))
    score.sort(key = lambda x: x[1], reverse = True)
    return score

limit = 15 # maximum runtime for each individual execution in seconds
maxiter = 2**10 # maximum iterations
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
                iteration = 1
                stop = 1
                timestamp = time()
                print(f'Executing replica {r} for {filename} in {directory}')
                with open(output + f'r{r}_' + filename, 'w') as target:
                    p = Adjustment(initial(pf))
                    while p.active():
                        p.step()
                        diff = time() - timestamp                        
                        if stop == iteration or diff > limit:
                            print(f'w;{iteration};{diff}', file = target)
                            p.output(target)
                            stop *= 2
                            if diff > limit or stop >= maxiter:
                                p.postprocess(pf.weights, target)                                
                                break # stop condition met
                        iteration += 1

