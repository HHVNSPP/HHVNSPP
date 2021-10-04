from collections import defaultdict
from random import shuffle, choice
from fill import FILL

BETTER = -1
WORSE = 1
EQUAL = 0
NONDOM = 2

verbose = False

def pick(options, high = True):
    assert len(options) > 0
    best = [ choice(list(options.keys())) ]
    score = options[best[0]]
    for o in options:
        s = options[o]
        if (high and s > score) or (not high and s < score):
            score = s
            best = [o]
        elif s == score:
            best.append(o)
    return choice(best) # random tie-break

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

def prune(included):
    dominated = set()
    for a in included:
        for b in included:
            if a == b:
                continue
            if a in dominated:
                continue
            if b in dominated:
                continue
            comp = a.compare(b)
            if comp == BETTER: # a dominates b
                dominated.add(b) # b needs to be pruned
                if verbose:
                    print(a, 'dominates', b)
                    print(a.evaluate())
                    print(b.evaluate())
            elif comp == WORSE: # b dominates a
                dominated.add(a)
                if verbose:
                    print(a, 'is dominated by', b)
                    print(a.evaluate())
                    print(b.evaluate())                
    remaining = included - dominated
    if verbose:
        print(f'{len(included)} -> {len(remaining)}')
    return remaining

def score(contender, pool):
    prune = set()
    better = 0
    worse = 0
    equal = 0
    nondom = 0
    for s in pool:
        comp = contender.compare(s)
        if comp == WORSE: # the one created by the heuristics was worse
            worse += 1
        elif comp == EQUAL: # it was the same impact in every objective
            equal += 1
        elif comp == NONDOM: # it was not dominated but not equal either
            nondom += 1
        elif comp == BETTER: # it improved
            prune.add(s) # the original one must be removed now
            better += 1
    return (prune, better, worse, equal, nondom)

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

def lowRnd(sol):
    return sol.rand(level = 0)

def highRnd(sol):
    return sol.rand(level = 1)

def fundRnd(sol):
    return sol.rand(level = -1)

## GROUP LEVEL LOCAL SEARCH HEURISTICS

def incrGroup(sol):
    return sol.modGroup(decr = False)
    
def decrGroup(sol):  
    return sol.modGroup()

def alterGroup(sol):
    return sol.alterGroup()

LOCAL = [ swapOne, inclRnd, exclRnd, 
          inclLow, inclHigh, exclLow, exclHigh,
          lowRnd, highRnd, fundRnd,
          incrGroup, decrGroup, alterGroup ]

### LOCAL SEARCH

def localSearch(pool, limit = 30):
    assert pool is not None
    assert len(pool) > 0
    assert None not in pool
    counters = defaultdict(int) # usage counters
    if verbose:
        print('Executing local search')
    hr = { h : 0 for h in LOCAL }
    fr = { h : 0 for h in FILL }
    stall = 0
    assert len(pool) > 0
    while stall < limit:
        shuffle(LOCAL) # shuffle for random tie-breaks
        sh = LOCAL[0] # random default
        br = hr[sh]
        for h in LOCAL: # pick a local-search heuristic
            r = hr[h]
            if r > br:
                sh = h
                br = r
        shuffle(FILL)
        fh = FILL[0] # random default
        br = fr[fh]
        for f in FILL: # pick a fill heuristic
            r = fr[f]
            if r > br:
                fh = f
                br = r
        if verbose:
            print(sh.__name__, fh.__name__)
        alts = set()
        for s in pool:
            assert s is not None
            alt = sh(s) # create an alternative solution
            if not alt.feasible():
                print(sh.__name__, 'produced an infeasible solution')
            assert alt is not None and alt.feasible()            
            fh(alt) # fill it
            if not alt.feasible():
                print(fh.__name__, 'produced an infeasible solution')
            assert alt.feasible()
            counters[fh] += 1
            counters[sh] += 1
            comp = alt.compare(s)
            if comp == BETTER: # the newly made one dominates the original
                alts.add(alt) # queue for inclusion
                score = update(pool, alt) # check how many it dominates
                stall = 0 # improvement obtained                        
                hr[sh] += score # reward the heuristics
                fr[fh] += score
            elif comp == EQUAL: 
                stall += 1 # no improvement, but not worse
                hr[sh] -= 1 # punish the heuristics slightly
                fr[fh] -= 1                                
            else: # it was WORSE
                stall += 1
                hr[sh] /= 2 # punish the heuristics heavily
                fr[fh] /= 2                
        pool = prune(pool | alts) # keep only the non-dominated ones
    return (pool, counters)
