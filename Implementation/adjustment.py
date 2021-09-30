import numpy as np
from electre import electre
from search import localSearch
from collections import defaultdict
from tools import pick, verbose, BETTER, EQUAL

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

# budget-exhausting heuristics

def fillMin(sol):
    return sol.fill(level = 0)

def fillMax(sol):
    return sol.fill(level = 1)

def fillRnd(sol):
    return sol.fill()

def fillIncr(sol):
    return sol.fill(level = -1)

def liftRnd(sol):
    return sol.lift()

SHAKE = [ reset, swapQuarter, swapThird, swapHalf, swapGroup ]

class Adjustment():

    def __init__(self, seed, lim = 5, init = -10):
        self.pool = { seed }
        self.usage = defaultdict(int) # counters
        self.heuristics = dict() # heuristics and their ranks
        for h in SHAKE:
            self.heuristics[h] = init
        self.initial = init
        self.stall = 0 # executions with no improvement
        self.limit = lim # how many consequtive stalled iterations to allow
        self.reset() # initial levels

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
        
    def check(self):
        for h in self.heuristics:
            if self.heuristics[h]:
                return True
        return False
    
    def reset(self):
        if verbose:
            print('Resetting ranks in adjustment')
        for h in self.heuristics:
            self.heuristics[h] = self.initial
  
    def improve(self, seed):
        if max(self.heuristics.values()) < 0: # all ranks negative
            self.reset() # reset all ranks to the initial value        
        heur = pick(self.heuristics)
        contender = heur(seed) # apply the shake heuristic
        assert contender is not None
        assert contender.feasible()
        self.usage[heur] += 1
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
        self.heuristics[heur] += adj # apply the adjustment
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
            
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
