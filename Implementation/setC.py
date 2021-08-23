# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:03:00 2019
@author: Madys
"""

import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from project import ProjectC
from project import Activity
from portfolio import PortfolioC
from portfolio import Synergy
from datetime import datetime

def load(filename):
    with open(filename) as data:
        budget = None
        areas = None
        areaCount = 0
        projects = None
        projectCount = 0
        activityCount = None
        synergies = None
        synergyCount = 0
        while True:
            line = data.readline()
            if len(line) == 0: # no more data
                return PortfolioC(budget,
                             projectCount, areaCount, activityCount, synergyCount, projects, areas, synergies)                
            if '=' in line:
                f = (line.strip()).split('=')
                header = f[0]
                content = (f[1].split(';'))[0]
                if 'budget' in header:
                    budget = float(content)
                elif 'nareas' in header:
                    areaCount = int(content)
                elif 'nprojects' in header:
                    projectCount = int(content)
                elif 'nactivities' in header:
                    activityCount = int(content)
                elif 'nsynergies' in header:
                    synergyCount = int(content)                
                elif "Areas" in content:
                    assert areaCount != 0
                    areas = []
                    for i in range(areaCount):
                        d = data.readline().strip()
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        areas.append([float(d[0]), float(d[1]), 0]) # min_bdg, max_bgt, real_bgt
                    assert len(areas) == areaCount
                elif 'Projects' in content:
                    assert projectCount != 0
                    projects = []
                    for i in range(projectCount):
                        d = data.readline().strip()
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        projects.append(ProjectC(count,
                                                 float(d[0]),
                                                 float(d[1]),
                                                 int(d[2]) - 1,
                                                 float(d[3]), [], 0, 0, False))
                    assert len(projects) == projectCount
                elif 'Activities' in content:
                    assert activityCount is not None
                    for i in range(projectCount):
                        d = data.readline().strip()
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        projects[int(d[0]) - 1].activities.append(
                            Activity(int(d[1]) - 1, float(d[2]), float(d[3]), float(d[4]), 0, 0))
                        activityCount -= 1
                    assert activityCount == 0
                elif 'Synergies' in content:
                    assert synergyCount != 0
                    synergies = []
                    for i in range(synergyCount):
                        d = data.readline().strip()
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')            
                        synergies.append(Synergy(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]),
                                                 int(d[6])))
                    assert len(synergies) == synergyCount
                elif 'SItems' in content:
                    for i in range(synergyCount):
                        d = content if '[{' in header else data.readline().strip() # for some reason, these do not start on a new line
                        content = '' # blank this out
                        start = d.index('{') + 1
                        end = d.index('}')
                        for triplet in d[start:end].split(','):
                            t = triplet.strip()
                            assert t[0] == '<' and t[-1] == '>'
                            i = t[1:-1].split(',')
                            synergies[int(i[0]) - 1].AddElement([int(i[0]), int(i[1]), int(i[2])])


def executeC(instance, limit, maxiter, target, sep, mod = True):
    h0 = hr.AllRandN(0, 1, 0, 5)
    h1 = hr.SwapRandom(1, 1, 0, 5)
    h2 = hr.SwapQuarter(2, 1, 0, 5)
    h3 = hr.SwapThird(3, 1, 0, 5)
    h4 = hr.SwapHalf(4, 1, 0, 5)
    h5 = hr.ShakeArea(5, 1, 0, 5)
    h6 = hr.Swap1(6, 2, 0, 1)                                         
    h7 = hr.DrawHightBgtAndFill(7, 2, 0, 1)
    h8 = hr.DrawRandFill(8, 1, 0, 1)                                       
    h9 = hr.MoreProj(9, 4, 0, 1)
    h10 = hr.SetPrjMinFill(10, 4, 0, 1)                                
    h11 = hr.UseBudget(11, 4, 0, 1)
    h12 = hr.SetPrjRndFill(12, 4, 0, 1)
    h13 = hr.QuitBad(13, 4, 0, 1)
    shake = [h0, h1, h2, h3, h4, h5]       
    local = [h6,h7,h8,h9,h10,h11,h12,h13]
    counter = 0
    iterate = 1
    stop = 1
    heuristics_data = ""
    timestamp = datetime.now()
    a = load(instance)
    b = a.initial_solution()
    b.make_factible()       
    adjustment = Adjustment(b, b, shake, [0.5, 0.5], [], 5, 0, counter, heuristics_data)
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
        iterate += 1
    print('# electre', file = target)        
    adjustment.apply_electre()
    diff = datetime.now() - timestamp
    for sol in adjustment.solutions:
        print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                        
    shake.sort(key = lambda x: x.ID, reverse = False)
    local.sort(key = lambda x: x.ID, reverse = False)
    print('# shake', sep.join([str(h.in_use) for h in shake]), file = target)
    print('# local', sep.join([str(h.in_use) for h in local]), file = target)
    print('# time', 'timestamp', file = target)

