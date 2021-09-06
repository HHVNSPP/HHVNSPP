from random import shuffle

VERBOSE = False

def update(sol, ref):
    prune = set()
    ok = True
    for s in sol:
        comp = ref.compare(s)
        if comp == BETTER: # ref dominates s   
            prune.add(s) # s needs to be pruned
        elif comp == WORSE: # s dominates ref
            ok = False # ref cannot enter
        ref -= prune # remove the dominated ones
    if ok: # add the one that was not dominated by any
        sol.add(ref)
    return len(prune) # how many did ref dominate

def check(heur, byDom = True):
    for h in heur:
        r = heur[h]
        if byDom:
            if r == 0 or r == 1:
                return True
        elif r > 0:
            return True    
    return False

# LOCAL SEARCH HEURISTICS

def swapOne(sol):
    return sol.swap(count = 1)

def inclRnd(sol):
    return sol.add()

def exclRnd(sol):
    return sol.fill(random = False)

def inclLow(sol):  
    return sol.fitExtreme(high = False)
    
def inclHigh(sol):
    return sol.fitExteme()

def exclHigh(sol):
    return sol.dropExtreme()

def exclLow(sol):
    return sol.dropExtreme(high = False)

def lowRand(sol):
    return sol.randmin()

## GROUP LEVEL LOCAL SEARCH HEURISTICS

def incrGroup(sol):
    return sol.modGroup(decr = False)
    
def decrGroup(sol):  
    return sol.modGroup()

def alterGroup(sol):
    return sol.alterGroup().fill()

LOCAL = [swapOne, inclRnd, exclRnd, 
         inclLow, inclHigh, exclLow, exclHigh,
         incrGroup, decrGroup, alterGroup]

# fill heuristics

def fillMin(sol):
    return sol.fill(level = 0)

def fillMax(sol):
    return sol.fill(level = 1)

def fillRnd(sol):
    return sol.fill()

def fillIncr(sol):
    return sol.fill(level = -1)

def fillLift(sol):
    return sol.fill(level = 2)

FILL = [fillMin, fillMax, fillRnd, fillIncr, fillLift]

### LOCAL SEARCH

def localSearch(pool, counters, init = -10, limit = 10, byDom = True):
    if VERBOSE:
        print('Executing local search')
    hr = { h : init for h in LOCAL}
    fr = { h : init for h in LOCAL}
    shuffle(LOCAL)
    stall = 0
    assert len(pool) > 0
    while stall < limit and check(hr, fr):
        sh = None
        br = 0
        for h in LOCAL: # pick a local-search heuristic
            r = heur[h]
            if not byDom and r == 1:
                sh = h
                break
            elif r > br:
                sh = h
                br = r
        fh = None
        br = 0
        for f in FILL: # pick a fill heuristic
            r = fill[f]
            if not byDom and r == 1:
                fh = f
                break
            elif r > br:
                fh = f
                br = r
        for s in pool:
            alt = fh(sh(s)) # create an alternative solution and fill it
            counters[fh] += 1
            counters[sh] += 1
            comp = alt.compare(s)
            if comp == BETTER: # alt dominates s
                r = update(pool, alt)
                stall = 0 # improvement obtained                        
                if byDom: # update the dominance ranks of thr two
                    heur[sh] = r 
                    fill[fh] = r
            elif comp == EQUAL: 
                stall += 1 # no improvement, but not worse
            else: # it was WORSE
                stall += 1                 
                if not byDom:
                    heur[sh] = -1 # punish the search heuristic
                    fill[fh] = -1 # punish the fill heuristic
    return pool    
