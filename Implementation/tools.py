from collections import defaultdict
from random import shuffle, choice
from fill import FILL

EQUAL = 2
BETTER = -1
WORSE = 1
UNDEFINED = 0

verbose = False

def pick(options, high = True):
    assert len(options) > 0
    best = [choice(list(options.keys()))]
    score = options[best[0]]
    for o in options:
        s = options[o]
        if (high and s > score) or (not high and s < score):
            score = s
            best = [o]
        elif s == score:
            best.append(o)
    return choice(best)

# Fill (budget-exhausting) heuristics

def fillMin(sol):
    sol.fill(level = 0)

def fillMax(sol):
    sol.fill(level = 1)

def fillRnd(sol):
    sol.fill()
     
def fillIncr(sol):
    sol.fill(level = -1)
     
def fillLift(sol):
    sol.fill(level = 2)

FILL = [ fillMin, fillMax, fillRnd, fillIncr, fillLift ]

# local search

def update(sol, ref):
    return sum([ ref.compare(s) == BETTER for s in sol ])

def prune(original, added):
    for a in added:
        ok = True
        pruned = set()
        for s in original:
            comp = a.compare(s)
            if comp == BETTER: # a dominates s   
                pruned.add(s) # s needs to be pruned
            elif comp == WORSE: # s dominates a
                ok = False # a cannot enter
        if ok: # add the one that was not dominated by any
            original.add(a)
        original -= pruned
    return original 

# LOCAL SEARCH HEURISTICS

def swapOne(sol):
    return sol.swap(count = 1)

def inclRnd(sol):
    return sol.add()

def exclRnd(sol):
    return sol.remove()

def inclLow(sol):  
    return sol.fitExtreme(high = False)
    
def inclHigh(sol):
    return sol.fitExtreme()

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
    return sol.alterGroup()

LOCAL = [ swapOne, inclRnd, exclRnd, 
          inclLow, inclHigh, exclLow, exclHigh,
          incrGroup, decrGroup, alterGroup ]

### LOCAL SEARCH

def localSearch(pool, init = -10, limit = 10, byDom = True):
    counters = defaultdict(int) # usage counters
    if verbose:
        print('Executing local search')
    hr = { h : init for h in LOCAL }
    fr = { h : init for h in FILL }
    stall = 0
    assert len(pool) > 0
    while stall < limit:
        shuffle(LOCAL)
        shuffle(FILL)
        sh = LOCAL[0] # random default
        br = 0
        for h in LOCAL: # pick a local-search heuristic
            r = hr[h]
            if not byDom and r == 1:
                sh = h
                break
            elif r > br:
                sh = h
                br = r
        fh = FILL[0] # random default
        br = 0
        for f in FILL: # pick a fill heuristic
            r = fr[f]
            if not byDom and r == 1:
                fh = f
                break
            elif r > br:
                fh = f
                br = r
        if verbose:
            print(sh.__name__, fh.__name__)
        alts = set()
        for s in pool:
            alt = sh(s) # create an alternative solution 
            assert alt is not None
            fh(alt) # fill it
            assert alt.feasible()
            counters[fh] += 1
            counters[sh] += 1
            comp = alt.compare(s)
            if comp == BETTER: # the newly made one dominates the original
                alts.add(alt) # queue for inclusion
                r = update(pool, alt) # check how many it dominates
                stall = 0 # improvement obtained                        
                if byDom: # update the dominance ranks of thr two
                    hr[sh] = r 
                    fr[fh] = r
            elif comp == EQUAL: 
                stall += 1 # no improvement, but not worse
            else: # it was WORSE
                stall += 1                 
                if not byDom:
                    hr[sh] = -1 # punish the search heuristic
                    fr[fh] = -1 # punish the fill heuristic
        pool = prune(pool, alts) # keep only the non-dominated ones
    return (pool, counters)
