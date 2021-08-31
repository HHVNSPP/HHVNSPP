import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from project import ProjectAct
from activity import Activity
from portfolio import PortfolioSyn
from synergy import Synergy
from datetime import datetime

def load(filename, ignoreSynergies = False):
    # TO BE DONE: what area limits are we using for Instance Set A?
    with open(filename) as data:
        budget = None
        areas = None
        areaCount = 0
        projects = []
        projectCount = 0
        activityCount = None
        synergies = None
        synergyCount = 0
        while True:
            line = data.readline()
            if len(line) == 0: # no more data
                print('Done parsing')
                assert budget is not None
                assert projects is not None
                if ignoreSynergies: # blank these out if requested
                    print('Ignoring synergies')
                    synergyCount = 0
                    synergies = []
                # two equally important objectives
                return PortfolioSyn(budget, projects, [1, 1], areaLimits = al, syn = synergies)
            if '=' in line:
                f = (line.strip()).split('=')
                header = f[0]
                content = (f[1].split(';'))[0]
                if 'budget' in header:
                    budget = float(content)
                    al = {'LowerBound': [0.3 * budget, 0.25 * budget, 0.2 * budget],
                          'UpperBound': [0.4 * budget, 0.35 * budget, 0.3 * budget]}
                elif 'nareas' in header:
                    areaCount = int(content)
                elif 'nprojects' in header:
                    projectCount = int(content)
                elif 'nactivities' in header:
                    activityCount = int(content)
                elif 'nsynergies' in header:
                    synergyCount = int(content)                
                elif "Areas" in header:
                    print('Parsing the area data')                    
                    assert areaCount != 0
                    areas = []
                    for i in range(areaCount):
                        d = data.readline().strip()
                        d = d.replace('];', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        areas.append([float(d[0]), float(d[1]), 0]) # min_bdg, max_bgt, real_bgt
                    assert len(areas) == areaCount
                elif 'Projects' in header:
                    print('Parsing the project data')
                    assert projectCount != 0
                    for pID in range(projectCount):
                        d = data.readline().strip()
                        d = d.replace('];', '') # the last one ends this way
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))
                        a = int(d.pop(0)) - 1
                        projects.append(ProjectAct(pID, None, minB, maxB, area = a))
                    assert len(projects) == projectCount
                elif 'Activities' in header:
                    print('Parsing the activity data')                                        
                    assert activityCount is not None 
                    for i in range(projectCount * activityCount): # each project has the same number of activities
                        d = data.readline().strip()
                        d = d.replace('};', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        pID = int(d.pop(0)) - 1
                        pr = projects[pID]
                        # activity IDs are not used
                        d.pop(0)
                        assert pr.activities is not None
                        impact = float(d.pop(0))
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))                        
                        pr.activities.append(Activity(pID, pr, impact, minB, maxB))
                    for pID in range(projectCount):
                        pr = projects[pID]
                        pr.update()
                        assert activityCount == len(pr.activities)
                elif 'Synergies' in header:
                    print('Parsing the synergy setup')
                    assert synergyCount != 0
                    synergies = []
                    for i in range(synergyCount):
                        d = data.readline().strip()
                        d = d.replace('];', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas                        
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')            
                        synergies.append(Synergy(int(d[0]), int(d[1]), int(float(d[2])), int(d[3]), int(d[4]), int(d[5]), int(d[6])))
                    assert len(synergies) == synergyCount
                elif 'SItems' in header:
                    print('Parsing the synergy details')                    
                    for i in range(synergyCount):
                        d = content if '[{' in content else data.readline().strip() # for some reason, these do not start on a new line
                        content = '' # blank this out
                        start = d.index('{') + 1
                        end = d.index('}')
                        triplets = d[start:end].split('>,<')
                        for triplet in triplets:
                            t = triplet.replace('>', '').replace('<', '').strip()
                            i = t.split(',')
                            synergies[int(i[0]) - 1].include([int(i[0]), int(i[1]), int(i[2])])
                else:
                    print(f'Ignoring line <{content}>')        

def executeA(instance, limit, maxiter, target, sep, mod = True, skipSyn = True): # we have no baseline for the synergy-included instances to compare to
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
    local = [h6, h7, h8, h9, h10, h11, h12, h13]
    counter = 0
    iterate = 1
    stop = 1
    heuristics_data = ''
    timestamp = datetime.now()
    a = load(instance, skipSyn)
    b = a.initialize()
    b.makeFeasible()       
    adjustment = Adjustment(b, b, shake, [0.5, 0.5], [], 5, 0, counter, heuristics_data)
    while adjustment.nim > adjustment.nima: # TO BE DONE: better names
        if datetime.now() - timestamp > limit:
            break # out of time
        if stop >= maxiter:
            break # out of permitted iterations
        lsearch = ls.LocalSearch(adjustment.shaked, 20, local, mod)
        adjustment.execute(lsearch.execute())
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
