import operator
import numpy as np
from electre import electre
from random import choice, shuffle
from collections import defaultdict
from solution import BETTER, EQUAL, WORSE

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
    sol -= prune # remove the dominated ones
    if ok: # add the one that was not dominated by any
        sol.add(ref)
    return len(prune) # how many did ref dominate

# Shake heuristics

def reset(sol):
    return sol.swap()

def swapQuarter(sol):
    return sol.swap(count = 1/4)

def swapThird(sol):
    return sol.swap(count = 1/3)

def swapHalf(sol):
    return sol.swap(count = 1/2)

def swapGroup(sol):
    return sol.swap(count = 0)

# Fill (budget-exhausting) heuristics

def fillMin(sol):
    return sol.fill(level = 0)

def fillMax(sol):
    return sol.fill(level = 1)

def fillRnd(sol):
    return sol.fill() 

def fillIncrMin(sol):
    return sol.fill(level = 0, sort = True)

def fillIncrMax(sol):
    return sol.fill(level = 1, sort = True)

def fillIncrRnd(sol):
    return sol.fill(level = None, sort = True)

def liftLift(sol):
    return sol.lift(incr = True)

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

def incrGroupMin(sol):
    return sol.modGroup(decr = False, level = 0)

def incrGroupMax(sol):
    return sol.modGroup(decr = False, level = 1)

def incrGroupRnd(sol):
    return sol.modGroup(decr = False, level = None)
    
def decrGroupMin(sol):  
    return sol.modGroup()

def decrGroupMax(sol, level = 0):  
    return sol.modGroup(level = 1)

def decrGroupRnd(sol):  
    return sol.modGroup(level = None)

def alterGroupMin(sol):
    return sol.alterGroup(level = 0)

def alterGroupMax(sol):
    return sol.alterGroup(level = 1)

def alterGroupRnd(sol):
    return sol.alterGroup(level = None)

# fill heuristics

def fillMin(sol):
    return sol.fill(level = 0)

def fillMax(sol):
    return sol.fill(level = 1)

def fillRnd(sol):
    return sol.fill(level = None)

def fillIncrMin(sol):
    return sol.fill(level = 0, incr = True)

def fillIncrMax(sol):
    return sol.fill(level = 1, incr = True)

def fillIncrRnd(sol):
    return sol.fill(level = None, sort = True)

def fillLiftRnd(sol):
    return sol.fill(level = None, incr = True)

def fillLiftMax(sol):
    return sol.fill(level = 1, incr = True)

### HEURISTIC GROUPS PER PHASE

DEFAULT = -10

heur = { 'shake': [ reset, swapQuarter, swapThird, swapHalf, swapGroup ],
         'search':  [ swapOne, inclRnd, exclRnd, 
                      inclLow, inclHigh, exclLow, exclHigh,
                      incrGroupMin, incrGroupMax, incrGroupRnd,
                      decrGroupMin, decrGroupMax, decrGroupRnd,
                      alterGroupMin, alterGroupMax, alterGroupRnd ],
         'fill' : [ fillMin, fillMax, fillRnd,
                    fillIncrMin, fillIncrMax, fillIncrRnd,
                    fillLiftMax, fillLiftRnd ] }

def pick(ranks, phase): # pick the highest-ranking heuristic
    return max(ranks.items(), key = operator.itemgetter(1))[0]

def initialize(incl):
    use = []
    for i in incl:
        shuffle(heur[i])
        use += heur[i]
    return { h : DEFAULT for h in use }

### LOCAL SEARCH ROUTINE

def localSearch(pool, counters, limit = 10):
    if VERBOSE:
        print('Executing local search')
    ranks = initialize(['search', 'fill'])
    stall = 0
    assert len(pool) > 0
    while stall < limit:
        s = choice(list(pool))
        searchWith = pick(ranks, 'fill') 
        alt = searchWith(s)
        if VERBOSE:
            print(f'Searching with <{searchWith.__name__}>')
        assert alt is not None
        fillWith = pick(ranks, 'fill')
        if VERBOSE:
            print(f'Filling with <{fillWith.__name__}>')        
        fillWith(alt)
        assert alt is not None        
        counters[fillWith] += 1
        counters[searchWith] += 1
        comp = alt.compare(s)
        if comp == BETTER: # alt dominates s
            r = update(pool, alt)
            stall = 0 # improvement obtained                        
            ranks[searchWith] = r 
            ranks[fillWith] = r
        else: # it was WORSE or EQUAL
            stall += 1
        if max(ranks.values()) < 0: # all are negative
            break # stop searching
    return pool    


class Adjustment():

    def __init__(self, seed, lim = 10):
        self.pool = { seed }
        self.usage = defaultdict(int) # counters
        self.ranks = initialize(['shake', 'fill'])
        self.stall = 0 # executions with no improvement
        self.limit = lim # how many consequtive stalled iterations to allow

    def postprocess(self, w, target):
        sol = np.matrix([ s.evaluate() for s in self.pool ])
        i = 0
        for score in electre(w, sol):
            print(f'electre;{score};{sol[i, :]}', file = target)
            i += 1
        print('\n'.join([f'usage;{k.__name__}={v}' for (k, v) in self.usage.items()]), file = target)

    def evaluate(self):
        return np.matrix([s.evaluate() for s in self.pool])
        
    def output(self, target):
        print(self.evaluate(), file = target)
        
    def active(self):
        if VERBOSE:
            print(f'Stalled for {self.stall} iterations of the permitted {self.limit}')
        return self.stall < self.limit 
          
    def improve(self, seed):
        if max(self.ranks.values()) < 0: # all are negative
            self.ranks = initialize(['shake', 'fill']) # reset the ranks
        shakeWith = pick(self.ranks, 'shake') # pick a shake heuristic
        fillWith = pick(self.ranks, 'fill') # pick a fill heuristic
        assert seed is not None
        if VERBOSE:
            print(f'Shaking with <{fillWith.__name__}>')                        
        contender = shakeWith(seed)
        assert contender is not None
        if VERBOSE:
            print(f'Filling with <{fillWith.__name__}>')                
        fillWith(contender)
        assert contender is not None
        self.usage[shakeWith] += 1
        self.usage[fillWith] += 1
        contender.feasible()
        stalled = True
        prune = set() # pool to discard
        adj = 0
        if VERBOSE:
            print(f'Comparing against a pool of {len(self.pool)} pool')
        for s in self.pool: # calculate the rank changes
            comp = contender.compare(s)
            if comp == 1:                
                adj += 1
                stalled = False
            elif comp == 0:
                adj += -1
                stalled = False
            elif comp == BETTER:
                prune.add(s) 
                adj -= 5
            elif comp == EQUAL:
                adj -= 10
        self.ranks[shakeWith] += adj # apply the adjustment
        self.ranks[fillWith] += adj # apply the adjustment
        if stalled: # no improvement
            if VERBOSE:
                print('Stalled')
            self.stall += 1
        else: # improvement
            if VERBOSE:
                print('Improvement')
            self.stall = 0 # reset the stall counter
        self.pool -= prune
        self.pool.add(contender)
    
    def step(self):
        seed = self.pool.copy()
        for s in localSearch(seed, self.usage):
            self.improve(s)
            
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
