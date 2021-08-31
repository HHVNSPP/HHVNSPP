import numpy as np
import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from portfolio import PortfolioSyn
from project import ProjectAR
from synergy import Synergy
from datetime import datetime

def load(filename):
    with open(filename) as f:
        numberOfProjects = int(f.readline())
        b = float(f.readline())
        areaLimits = {'LowerBounds': [0.25 * b, 0.3 * b, 0.3 * b], 
                      'UpperBounds': [0.45 * b, 0.45 * b,0.45 * b]}
        regionLimits = {'LowerBounds': [0.4 * b, 0.4 * b],
                        'UpperBounds': [0.6 * b, 0.6 * b]}
        weights = [int(i) for i in (f.readline()).split(" ")]
        n = len(weights)
        numberOfSynergies = int(f.readline())
        synergies = []
        for i in range(numberOfSynergies):
            line = f.readline()
            line = line.split()
            synergies.append(Synergy(int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), []))
            line = f.readline()
            line = line.split()
            for j in line:
                synergies[i].include(int(j))                
        projects = []
        for pID in range(numberOfProjects):
            p = f.readline()
            p = p.split()
            minB = float(p.pop(0))
            maxB = float(p.pop(0))
            area = int(p.pop(0)) - 1
            region = int(p.pop(0)) - 1
            impact = [float(p.pop(0)) for i in range(n)] # the contributions for the n objectives
            projects.append(ProjectAR(pID, impact, minB, maxB, area, region))
    return PortfolioSyn(b, weights, projects, areaLimits, regionLimits, syn) 

def executeC(instance, limit, maxiter, target, sep, mod = True):
    h1 = hr.SwapRandom(1, 1, 0, 5)
    h2 = hr.SwapQuarter(2, 1, 0, 5)
    h3 = hr.SwapThird(3, 1, 0, 5)
    h4 = hr.SwapHalf(4, 1, 0, 5)      
    h13 = hr.ShakeArea(13, 1, 0, 5)
    h20 = hr.ShakeRegion(20, 1, 0, 5)
    h21 = hr.AllRandN(21, 1, 0, 5)
    h5 = hr.Swap1(5, 2, 0, 1)
    h6 = hr.DrawHightBgt(6, 2, 0, 1)
    h7 = hr.MUseBudget(7, 2, 0, 1)
    h8 = hr.MMoreProj(8, 2, 0, 1)
    h9 = hr.DrawRandom(9, 2, 0, 1)
    h10 = hr.SetPrjMinFill(10, 2, 0, 1)
    h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
    h12 = hr.SetPrjRndFill(12, 2, 0, 1)
    shake = [h1, h2, h3, h4, h13, h20,h21]
    local = [h5, h6, h7, h8, h9, h11, h12]
    counter = 0
    iterate = 1
    stop = 1
    heuristics_data = ''
    timestamp = datetime.now()
    a = load(instance)
    b = a.initialize()
    b.feasible()
    adjustment = Adjustment(b, b, shake, a.weights, [], 4, 0, counter, heuristics_data)
    while adjustment.nim > adjustment.nima: # TO BE DONE: need better names than nim and nima
        if datetime.now() - timestamp > limit:
            break # out of time
        if stop >= maxiter:
            break # out of permitted iterations
        lsearch = ls.LocalSearch(adjustment.shaked, 20, local, mod)
        lista = lsearch.execute()
        adjustment.execute(lista)
        if stop == iterate:    
            diff = datetime.now() - timestamp
            for sol in adjustment.solutions:            
                print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                                    
            stop *= 2                       
        iterate += 1
    print('# electre', file = target)        
    adjustment.electre()
    for sol in adjustment.solutions:
        print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                        
    shake.sort(key = lambda x: x.ID, reverse = False)
    local.sort(key = lambda x: x.ID, reverse = False)
    print('# shake', sep.join([str(h.in_use) for h in shake]), file = target)
    print('# local', sep.join([str(h.in_use) for h in local]), file = target)
    print('# time', 'timestamp', file = target)
