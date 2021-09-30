from portfolio import Portfolio, Group, Project, Activity, Synergy

verbose = False

def loadC(filename):
    with open(filename) as f:
        numberOfProjects = int(f.readline())
        b = float(f.readline())
        gr = {'a1': Group(0.25 * b, 0.45 * b),
              'a2': Group(0.3 * b, 0.45 * b),
              'a3': Group(0.3 * b, 0.45 * b), 
              'r1': Group(0.4 * b, 0.6 * b),
              'r2': Group(0.4 * b, 0.6 * b)}
        weights = [ int(i) for i in (f.readline()).split(" ") ]
        binary = [ False for w in weights ] 
        n = len(weights)
        numberOfSynergies = int(f.readline())
        synergies = []
        for i in range(numberOfSynergies):
            line = f.readline()
            line = line.split()
            synergies.append(Synergy(int(line[0]), int(line[1]), int(line[2]),
                                     int(line[3]), int(line[4]), int(line[5]), []))
            line = f.readline()
            line = line.split()
            for j in line:
                synergies[i].include(int(j))                
        projects = []
        for pID in range(numberOfProjects):
            p = f.readline().split()
            minB = float(p.pop(0))
            maxB = float(p.pop(0))
            area = int(p.pop(0)) 
            region = int(p.pop(0)) 
            obj = [float(p.pop(0)) for i in range(n)] # the contributions for the n objectives
            p = Project(obj, maxB, minB)
            projects.append(p)
            gr[f'a{area}'].include(p)
            gr[f'r{region}'].include(p)
            areas = []
            regions = []
            for g in gr:
                if 'a' in g:
                    if verbose:
                        print(f'Including an area with {len(gr[g].members)} projects')
                    areas.append(gr[g])
                else:
                    assert 'r' in g
                    if verbose:
                        print(f'Including a region area with {len(gr[g].members)} projects')                    
                    regions.append(gr[g])                    
    return Portfolio(b, weights, binary, projects, [areas, regions], s = synergies) 

def loadB(filename):
    with open(filename) as f:
        projectCount = int(f.readline())
        budget = float(f.readline())
        areas = { 1: Group(0.3 * budget, 0.4 * budget),
                  2: Group(0.25 * budget, 0.35 * budget),
                  3: Group(0.2 * budget, 0.3 * budget) }
        regions = { 1: Group(0.4 * budget, 0.6 * budget),
                    2: Group(0.4 * budget, 0.6 * budget) } 
        w = [ int(i) for i in (f.readline()).split() ]
        b = [ False for w in weights ] 
        n = len(weights)        
        k = len(w)
        projects = []
        for pID in range(projectCount):
            d = f.readline().split()
            print(d)
            req = float(d.pop(0))
            a = int(d.pop(0))
            r = int(d.pop(0))
            pr = Project([float(d.pop(0)) for i in range(k)], req)
            areas[a].include(pr)
            regions[r].include(pr)
            projects.append(pr)
        gr = [ list(areas.values()), list(regions.values()) ]
        return Portfolio(budget, w, b, projects, gr)

def loadA(filename, ignoreSynergies = True): # in our experiments, we ignore these synergies
    with open(filename) as data:
        budget = None
        areas = []
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
                w = [ 0.5, 0.5 ] # two equally important objectives
                b = [ True, False ] # the first is a binary one (yes/no)
                if verbose:
                    print(f'Including {len(areas)} areas')
                return Portfolio(budget, w, b, projects, g = [[areas[a] for a in areas]], s = synergies)
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
                    areas = dict()
                    for i in range(areaCount):
                        d = data.readline().strip()
                        d = d.replace('];', '') # the last one ends thus
                        if d[-1] == ',':
                            d = d[:-1] # trim trailing commas
                        assert d[0] == '<' and d[-1] == '>'
                        d = d[1:-1].split(',')
                        minB = float(d.pop(0))
                        maxB = float(d.pop(0))                        
                        areas[i] = Group(minB, maxB, set())
                    assert len(areas) == areaCount
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
                        p = Project([1, float(d.pop(0))], maxB, minB)
                        areas[a].include(p) # include into the area                        
                        projects.append(p)
                    assert len(projects) == projectCount
                elif 'Activities' in header:
                    if verbose:
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
                        pr.activities.append(Activity(pr, impact, maxB, minB))
                    for pID in range(projectCount):
                        pr = projects[pID]
                        pr.update()
                        assert activityCount == len(pr.activities)
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
                    
