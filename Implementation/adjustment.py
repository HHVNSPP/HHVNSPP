import numpy as np
from electre import electre
from collections import defaultdict
from tools import pick, verbose, BETTER, EQUAL, localSearch, FILL

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

SHAKE = [ reset, swapQuarter, swapThird, swapHalf, swapGroup ]

class Adjustment():

    def __init__(self, seed, lim = 10):
        self.pool = { seed }
        self.usage = defaultdict(int) # counters
        self.stall = 0 # executions with no improvement
        self.limit = lim # how many consequtive stalled iterations to allow
        self.sr = { h : 1 for h in SHAKE } 
        self.fr = { h : 1 for h in FILL }

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
        if verbose:
            print(f'Stalled for {self.stall} iterations of the permitted {self.limit}')
        return self.stall < self.limit 
        
    def improve(self, seed):
        assert seed is not None
        if len(self.sr) > 0 and max(self.sr.values()) < 0:
            self.sr = { h : 1 for h in SHAKE } # reset
        if len(self.fr) > 0 and max(self.fr.values()) < 0:
            self.fr = { h : 1 for h in FILL } # reset
        sh = pick(self.sr) # pick a shake heuristic
        fh = pick(self.fr) # pick a fill heuristic
        if verbose:
            print(f'Shaking with <{sh.__name__}>')                        
        contender = sh(seed)
        assert contender is not None
        if verbose:
            print(f'Filling with <{fh.__name__}>')                
        fh(contender)
        assert contender is not None
        self.usage[sh] += 1
        self.usage[fh] += 1
        stalled = True
        prune = set() # pool to discard
        adj = 0
        if verbose:
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
        self.sr[sh] += adj # apply the adjustment
        self.fr[fh] += adj # apply the adjustment
        if stalled: # no improvement
            if verbose:
                print('Stalled')
            self.stall += 1
        else: # improvement
            if verbose:
                print('Improvement')
            self.stall = 0 # reset the stall counter
        self.pool -= prune
        self.pool.add(contender)
    
    def step(self):
        seed = self.pool.copy()
        (sol, use) = localSearch(seed)
        self.usage.update(use)
        for s in sol:
            self.improve(s)
            
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
