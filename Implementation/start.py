import os
from electre import Electre
from datetime import timedelta, datetime
from search import LocalSearch
from adjustment import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy
from solution import initial

def electre(weights, pool):
    score = zip(pool, Electre(weights, [sol.impact for sol in pool]))
    score.sort(key = lambda x: x[1], reverse = True)
    return score

limit = timedelta (seconds = 15) # maximum runtime for each individual execution
maxiter = 2**10 # maximum iterations
replicas = 30 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = [ 'P', 'o', 'm' ] # we conserve the filenames of the cited authors 
filetypes = [ '.dat', '.txt', '.txt' ] 
load = { 'A': loadA, 'B': loadB, 'C': loadC }

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    print('Reading instances from', directory)
    for filename in os.listdir(directory):
        print('Examining file', filename)        
        if filename.startswith(prefix) and filename.endswith(ending):
            instance = directory + filename
            print(f'Processing instance {instance}')
            pf = load[s](instance)         
            for r in range(1, replicas + 1):
                iteration = 1
                stop = 1
                timestamp = datetime.now()
                pool = None
                print(f'Executing replica {r} for {filename} in {directory}')
                curr = initial(pf).feasible()
                with open(output + f'r{r}_' + filename, 'w') as target:
                    pool = Adjustment()
                    while pool.active():
                        if datetime.now() - timestamp > limit:
                            break # out of time
                        curr = pool.execute(LocalSearch(curr))
                        if stop == iteration:    
                            diff = datetime.now() - timestamp
                            for s in pool.solutions:
                                print(f'working;{timestamp};{iteration};{diff};{s}', file = target)
                            stop *= 2
                            if stop >= maxiter:
                                break # out of permitted iterations
                        iteration += 1
                    electre(sol, pf.weights)
                    diff = datetime.now() - timestamp
                    for s in pool.solutions:
                        print(f'postproc;{timestamp};{iteration};{diff};{s}', file = target)
                    print(pool.usage(target))




