import os
import heuristic as hr
from datetime import timedelta
from search import LocalSearch
from adjustment import Adjustment
from parser import loadA, loadB, loadC
from portfolio import Portfolio, Project, Activity, Synergy, initial

limit = timedelta (seconds = 15) # maximum runtime for each individual execution
maxiter = 2**10 # maximum iterations
replicas = 30 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = ['P', 'o', 'm'] 
filetypes = ['.dat', '.txt', '.txt'] 

# heuristics used by more than one instance set
h1 = hr.SwapRandom(1, 1, 0, 5)
h2 = hr.SwapQuarter(2, 1, 0, 5)
h3 = hr.SwapThird(3, 1, 0, 5)
h4 = hr.SwapHalf(4, 1, 0, 5)
h5 = hr.ShakeArea(5, 1, 0, 5)
h6 = hr.DrawHightBgt(6, 2, 0, 1)
h9 = hr.DrawRandom(9, 2, 0, 1)
h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
h13 = hr.ShakeArea(13, 1, 0, 5)
h20 = hr.ShakeRegion(20, 1, 0, 5)

shake = {'A': [hr.AllRandN(0, 1, 0, 5),
               h1, h2, h3, h4, h5],
         'B': [h1, h2, h3, h4, h13, h20],
         'C': [h1, h2, h3, h4, h13, h20,
               hr.AllRandN(21, 1, 0, 5)]}
         
local = {'A': [hr.Swap1(6, 2, 0, 1),
               hr.DrawHightBgtAndFill(7, 2, 0, 1),
               hr.DrawRandFill(8, 1, 0, 1),
               hr.MoreProj(9, 4, 0, 1),
               hr.SetPrjMinFill(10, 4, 0, 1),
               hr.UseBudget(11, 4, 0, 1),
               hr.SetPrjRndFill(12, 4, 0, 1),
               hr.QuitBad(13, 4, 0, 1)], 
         'B': [h5, h6, hr.AddRandom(7, 2, 0, 1),
               hr.AddLowBgt(8, 2, 0, 1),
               h9,
               hr.DrawHightBgt(10, 2, 0, 1),
               h11,
               hr.AddMaxBgt(12, 2, 0, 1),
               hr.SwapArea(14, 3, 0, 1),
               hr.IncreseBgtArea(15, 3, 0, 1),
               hr.DecreaseBgtArea(16, 3, 0, 1),
               hr.SwapRegion(17, 4, 0, 1),
               hr.IncreseBgtRegion(18, 4, 0, 1),
               hr.UseBudgetAT(21, 2, 0, 1)],
         'C': [hr.Swap1(5, 2, 0, 1), h6,
               hr.MUseBudget(7, 2, 0, 1),
               hr.MMoreProj(8, 2, 0, 1), h9, h11,
               hr.SetPrjRndFill(12, 2, 0, 1)]}

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    print('Reading instances from', directory)
    for filename in os.listdir(directory):
        print('Examining file', filename)        
        if filename.startswith(prefix) and filename.endswith(ending):
            print('Processing instance at', filename)
            sh = shake[s]
            lo = local[s]
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}')                
                with open(output + f'r{r}_' + filename, 'w') as target:
                    iteration = 1
                    stop = 1
                    timestamp = datetime.now()
                    pool = None
                    i = initial(load(instance, skipSyn)).feasible()
                    if s == 'A':
                        pool = Adjustment(i, sh, 5)
                    else: # B and C use 4
                        pool = Adjustment(i, sh, 4) # TO BE DONE: why 4 for those and 5 for A?
                    while sol.nim > sol.nima: # TO BE DONE: we need better names for nim and nima
                        if datetime.now() - timestamp > limit:
                            break # out of time
                        sol.execute(LocalSearch(sol.shaked, 20, lo, mod).execute())
                        if stop == iteration:    
                            diff = datetime.now() - timestamp
                            for s in pool.solutions:
                                print(f'working;{timestamp};{iteration};{mod};{diff};{s}', file = target)
                            stop *= 2
                            if stop >= maxiter:
                                break # out of permitted iterations
                        iteration += 1
                    sol.apply_electre()
                    diff = datetime.now() - timestamp
                    for s in pool.solutions:
                        print(f'postproc;{timestamp};{iteration};{mod};{diff};{s}', file = target)                        
                    sh.sort(key = lambda x: x.ID, reverse = False)
                    lo.sort(key = lambda x: x.ID, reverse = False)
                    print('# shake', sep.join([str(h.uses) for h in sh]), file = target)
                    print('# local', sep.join([str(h.uses) for h in lo]), file = target)
                    print(f'# done at {timestamp}', file = target)
                    




