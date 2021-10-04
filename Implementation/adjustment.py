import numpy as np
from electre import electre
from collections import defaultdict
from tools import pick, verbose, score, localSearch, FILL

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

    def __init__(self, seed, lim = 50):
        assert seed is not None
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
        s = [f'usage;{k.__name__}={v}' for (k, v) in self.usage.items()]
        print('\n'.join(s), file = target)

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
        contender.adjust()
        if verbose:
            print(f'Filling with <{fh.__name__}>')                
        fh(contender)
        assert contender is not None
        self.usage[sh] += 1
        self.usage[fh] += 1
        fixed = False
        enters = False
        if verbose:
            print(f'Comparing against a pool of {len(self.pool)} pool')
        (prune, better, worse, equal, nondom) = score(contender, self.pool)
        self.pool -= prune
        if worse == 0:
            self.pool.add(contender) # it was not dominated
            if better > 0:
                self.stall = 0 # reset the stall counter            
                if verbose:
                    print('Improvement')
            else: # no improvement
                self.stall += 1                
                if verbose:
                    print('Stalled')
        adj = 10 * better - 10 * worse + 5 * nondom - equal
        self.sr[sh] += adj # apply the adjustments
        self.fr[fh] += adj
    
    def step(self):
        assert self.pool is not None
        seed = self.pool.copy()
        (sol, use) = localSearch(seed)
        self.usage.update(use)
        for s in sol:
            self.improve(s)
        
        
        
        
        
        
        
        
        
