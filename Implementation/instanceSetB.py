import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from project import ProjectAR
from portfolio import Portfolio
from datetime import datetime

def load(filename):
    with open(filename) as f:
        projectCount = int(f.readline())
        budget = float(f.readline())
        areaLimits = {'LowerBound': [0.3 * budget, 0.25 * budget, 0.2 * budget],
                      'UpperBound': [0.4 * budget, 0.35 * budget, 0.3 * budget]}
        regionLimits = {'LowerBound': [0.4 * budget, 0.4 * budget],
                        'UpperBound': [0.6 * budget, 0.6 * budget]}
        w = [int(t) for i in (f.readline()).split()]
        k = len(weights)
        projects = []
        for pID in range(projectCount):
            d = f.readline().split()
            req = float(d.pop(0))
            area = int(d.pop(0)) - 1
            region = int(d.pop(0)) - 1            
            impacts = [float(d.pop(0)) for i in range(k)]
            projects.append(ProjectAR(pID, impacts, req, area, region))
        return Portfolio(budget, w, projects, areaLimits, regionLimits)

def executeB(instance, limit, maxiter, target, sep, mod = True):
    h1 = hr.SwapRandom(1, 1, 0, 5)
    h2 = hr.SwapQuarter(2, 1, 0, 5)
    h3 = hr.SwapThird(3, 1, 0, 5)
    h4 = hr.SwapHalf(4, 1, 0, 5)      
    h13 = hr.ShakeArea(13, 1, 0, 5)
    h20 = hr.ShakeRegion(20, 1, 0, 5)
    h5 = hr.Swap1(5, 2, 0, 1)
    h6 = hr.DrawHightBgt(6, 2, 0, 1)
    h7 = hr.AddRandom(7, 2, 0, 1)
    h8 = hr.AddLowBgt(8, 2, 0, 1)
    h9 = hr.DrawRandom(9, 2, 0, 1)
    h10 = hr.DrawHightBgt(10, 2, 0, 1)
    h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
    h12 = hr.AddMaxBgt(12, 2, 0, 1)
    h14 = hr.SwapArea(14, 3, 0, 1)
    h15 = hr.IncreseBgtArea(15, 3, 0, 1)
    h16 = hr.DecreaseBgtArea(16, 3, 0, 1)
    h17 = hr.SwapRegion(17, 4, 0, 1)
    h18 = hr.IncreseBgtRegion(18, 4, 0, 1)
    h19 = hr.DecreaseBgtRegion(19, 4, 1, 1)
    h21=hr.UseBudgetAT(21, 2, 0, 1)   
    shake = [h1, h2, h3, h4, h13, h20]
    local = [h5, h6, h7, h8, h9, h10, h11, h12, h14, h15, h16, h17, h18, h21]
    counter = 0
    iterate = 1 #num iteracion
    stop = 1
    heuristics_data = ""
    timestamp = datetime.now()
    a = load(instance)
    b = a.initial()
    b.feasible()
    adjustment = Adjustment(b, b, shake, a.weights, [], 4, 0, counter, heuristics_data)
    while adjustment.nim > adjustment.nima:
        if datetime.now() - timestamp > limit:
            break # out of time
        if stop >= maxiter:
            break # out of permitted iterations
        lsearch = ls.LocalSearch(adjustment.shaked, 20, local, mod)
        lista = lsearch.apply()
        adjustment.apply(lista)
        if stop == iterate:
            diff = datetime.now() - timestamp
            for sol in adjustment.solutions:
                print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                                                    
            stop *= 2
        iterate += iterate
    print('# electre', file = target)        
    adjustment.apply_electre()
    diff = datetime.now() - timestamp
    for sol in adjustment.solutions:
        print(timestamp, SEP, iterate, SEP, mod, SEP, diff, SEP, sol.info(), file = target)                                        
        shake.sort(key = lambda x: x.ID, reverse = False)
        local.sort(key = lambda x: x.ID, reverse = False)
        print('# shake', SEP.join([str(h.in_use) for h in shake]), file = target)
        print('# local', SEP.join([str(h.in_use) for h in local]), file = target)
        print('# time', 'timestamp', file = target)
