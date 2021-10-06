from portfolio import Portfolio, Group, Project, Activity, Synergy

verbose = False

def loadC(filename):
    weights = None
    projects = []
    synergies = []
    areas = []
    regions = []
    with open(filename) as f:
        numberOfProjects = int(f.readline())
        b = float(f.readline())
        A = { 1: Group(0.25 * b, 0.45 * b),
              2: Group(0.30 * b, 0.45 * b),
              3: Group(0.30 * b, 0.45 * b) }
        R = { 1: Group(0.40 * b, 0.60 * b),
              2: Group(0.40 * b, 0.60 * b) } 
        weights = [ int(i) for i in (f.readline()).split(" ") ]
        n = len(weights)
        numberOfSynergies = int(f.readline())
        for i in range(numberOfSynergies):
            line = f.readline()
            line = line.split()
            synergies.append(Synergy(int(line[0]), int(line[1]), int(line[2]),
                                     int(line[3]), int(line[4]), int(line[5]), []))
            line = f.readline()
            line = line.split()
            for j in line:
                synergies[i].include(int(j))                
        for pID in range(numberOfProjects):
            p = f.readline().split()
            minB = float(p.pop(0))
            maxB = float(p.pop(0))
            a = int(p.pop(0)) 
            r = int(p.pop(0)) 
            obj = [float(p.pop(0)) for i in range(n)] # the contributions for the n objectives
            p = Project(obj, maxB, minB)
            projects.append(p)
            A[a].include(p)
            R[r].include(p)
    partial = [ True for w in weights ] # all objectives undergo partial impacts
    return Portfolio(b, weights, partial, projects, [ list(A.values()), list(R.values()) ], s = synergies) 

def loadB(filename):
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
            imp = [ float(d.pop(0)) for i in range(k) ] # all are yes/no objectives
            pr = Project(imp, req)
            A[a].include(pr)
            R[r].include(pr)
            projects.append(pr)
    partial = [ False for obj in w ] # no objective undergo partial impacts
    partitions = [ list(A.values()), list(R.values()) ] # areas and regions
    return Portfolio(budget, w, partial, projects, partitions)

def loadA(filename, ignoreSynergies = True): # in our experiments, we ignore these synergies
    budget = None
    areas = []
    areaCount = 0
    projects = []
    projectCount = 0
    activityCount = None
    synergies = None
    synergyCount = 0
    with open(filename) as data:
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
                w = [ 0.5, 0.5 ] # two equally important objectives
                if verbose:
                    print(f'Including {len(areas)} areas')
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
                        impact = [1, float(d.pop(0))]
                        p = Project(impact, maxB, minB)
                        A[a].include(p) # include into the area                        
                        projects.append(p)
                    assert len(projects) == projectCount
                elif 'Activities' in header:
                    if verbose:
                        print('Parsing the activity data')                                        
                    assert activityCount is not None
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
                        # activity IDs are not used
                        d.pop(0)
                        assert pr.activities is not None
                        impact = [ 1, float(d.pop(0)) ] # first objective binary, second linear
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))
                        pr.activities.append(Activity(pr, impact, maxB, minB))
                elif 'Synergies' in header:
                    if verbose:
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
                        synergies.append(Synergy(int(d[0]), int(d[1]),
                                                 int(float(d[2])), int(d[3]),
                                                 int(d[4]), int(d[5]), int(d[6])))
                    assert len(synergies) == synergyCount
                elif 'SItems' in header:
                    if verbose:
                        print('Parsing the synergy details')                    
                    for i in range(synergyCount):
                        d = content if '[{' in content else data.readline().strip() 
                        content = '' # blank this out
                        start = d.index('{') + 1
                        end = d.index('}')
                        triplets = d[start:end].split('>,<')
                        for triplet in triplets:
                            t = triplet.replace('>', '').replace('<', '').strip()
                            i = t.split(',')
                            synergies[int(i[0]) - 1].include([int(i[0]), int(i[1]), int(i[2])])
                else:
                    print(f'Ignoring line <{header} = {content}>')
    partial = [ False, True ] # no and yes
    return Portfolio(budget, w, partial, projects, [ list(A.values()) ], s = synergies)                    
