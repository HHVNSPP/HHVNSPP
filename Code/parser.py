from portfolio import Portfolio, Group, Project, Activity, Synergy
from itertools import compress

verbose = False

# instances with synergies, areas, and regions; pure partial assignment
def loadC(filename): 
    weights = None
    projects = []
    synergies = []
    areas = []
    regions = []
    with open(filename) as f:
        b = float(f.readline().split()[-1]) # total budget
        weights = [ float(v) for v in (f.readline()).split(' ')[1:] ]
        n = len(weights)
        for line in f:
            line = line.split()
            element = line.pop(0)
            if element == 'A': # an area
                line.pop(0) # the area label
                areas.append(Group(float(line.pop(0)), float(line.pop(0))))
            elif element == 'R': # a region
                line.pop(0) # the region label
                regions.append(Group(float(line.pop(0)), float(line.pop(0))))                
            elif element == 'P': # a project
                line.pop(0) # the project label
                minB = float(line.pop(0))
                maxB = float(line.pop(0))
                a = int(line.pop(0)) - 1
                r = int(line.pop(0)) - 1
                # the contributions for the n objectives            
                obj = [ float(line.pop(0)) for i in range(n) ]
                gr = [ areas[a], regions[r] ]
                p = Project(obj, maxB, minB, gr)
                projects.append(p)
                for g in gr:
                    g.include(p)
            elif element == 'S': # a synergy (unless ignored)
                line.pop(0) # the synergy label
                technical = int(line.pop(0)) == 1 # false or true
                value = float(line.pop(0))
                low = float(line.pop(0)) # lower activation threshold
                high = float(line.pop(0)) # higher activation threshold
                syn = Synergy(value, low, high) 
                for j in line: # participants
                    syn.include(projects[int(j) - 1])
                synergies.append(syn)
    partial = [ True for w in weights ] # all objectives undergo partial impacts
    partition = [ areas, regions ]
    print(f'{len(weights)} objectives and {len(projects)} projects parsed')
    return Portfolio(b, weights, partial, projects, partition, s = synergies) 

def loadB(filename): # instances with areas, regions; no partial assignment
    budget = None
    w = None
    projects = []
    with open(filename) as f:
        projectCount = int(f.readline())
        budget = float(f.readline())
        A = { 1: Group(0.30 * budget, 0.40 * budget),
              2: Group(0.25 * budget, 0.35 * budget),
              3: Group(0.20 * budget, 0.30 * budget) }
        R = { 1: Group(0.40 * budget, 0.60 * budget),
              2: Group(0.40 * budget, 0.60 * budget) }         
        w = [ int(i) for i in (f.readline()).split() ]
        k = len(w)
        for pID in range(projectCount):
            d = f.readline().split()
            req = float(d.pop(0))
            a = int(d.pop(0))
            r = int(d.pop(0))
            obj = [ float(d.pop(0)) for i in range(k) ]
            gr = [ A[a], R[r] ]
            pr = Project(obj, req, groups = gr)
            for g in gr:
                g.include(pr)
            projects.append(pr)
    partial = [ False for obj in w ] # no objective undergo partial impacts
    partitions = [ list(A.values()), list(R.values()) ] # areas and regions
    return Portfolio(budget, w, partial, projects, partitions)

# instances with areas, tasks, partial and non-partial objectives
def loadA(filename): 
    total = 0
    budget = None
    areas = []
    areaCount = 0
    projects = []
    projectCount = 0
    activityCount = None
    synergyCount = 0
    syn = []
    with open(filename) as data:
        while True:
            line = data.readline()
            if len(line) == 0: # no more data
                break
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
                elif "Areas" in header:
                    if verbose:
                        print('Parsing the area data')                    
                    assert areaCount != 0
                    A = dict()
                    for i in range(areaCount):
                        d = data.readline().strip()
                        d = d.replace('];', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))                        
                        A[i] = Group(minB, maxB)
                    assert len(A) == areaCount
                elif 'Projects' in header:
                    if verbose:
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
                        obj = [ None, float(d.pop(0)) ]
                        total += obj[-1]
                        p = Project(obj, maxB, minB, [ A[a] ])
                        A[a].include(p) # include into the area                        
                        projects.append(p)
                    assert len(projects) == projectCount
                elif 'Activities' in header:
                    if verbose:
                        print('Parsing the activity data')                                        
                    # each project has the same number of activities                    
                    for i in range(projectCount * activityCount): 
                        d = data.readline().strip()
                        d = d.replace('};', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        pID = int(d.pop(0)) - 1
                        pr = projects[pID]
                        d.pop(0) # activity IDs are not used
                        # the first one is a counter with unit impact   
                        obj = [ None, float(d.pop(0)) ]
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))
                        pr.tasks.append(Activity(pr, obj, maxB, minB))
                elif 'Synergies' in header:
                    count = dict()
                    for i in range(synergyCount):
                         d = data.readline().strip()[1:-2]
                         if d[-1] == '>':
                             d = d[:-1]
                         f = d.split(',')
                         label = int(f.pop(0)) - 1 # synergy ID
                         assert f.pop(0).strip() == '0' # we only have technical synergies
                         value = float(f.pop(0))
                         kind = int(f.pop(0)) # UNSURE WHAT THIS IS FOR
                         low = int(f.pop(0))
                         high = int(f.pop(0))
                         count[label] = int(f.pop(0))
                         syn.append(Synergy(value, low, high))
                    for line in data:
                        if '{' in line:
                            start = line.index('{') + 1
                            end = line.index('}')
                            d = line[start:end].replace(',', ' ')
                            d = d.replace('<', '')
                            for triplet in d.split('>'):
                                f = triplet.split()
                                if len(f) == 3:
                                    s = int(f.pop(0)) - 1
                                    p = int(f.pop(0)) - 1
                                    t = int(f.pop(0)) - 1
                                    syn[s].include(projects[p].tasks[t])
                    for s in range(synergyCount):
                        assert len(syn[s].elements) == count[s]
                else:
                    print(f'Ignoring line <{header} = {content}>')
    count = 2
    fraction = 1 / count 
    w = [ fraction ] * count # equally important objectives
    partial = [ False, True ] # no and yes (partial impact)
    if verbose:
        print(f'Including {len(areas)} areas')
    print(f'Funding all {len(projects)} projects yields benefit {total} for {filename}')
    return Portfolio(budget, w, partial, projects, [ list(A.values()) ], syn)
