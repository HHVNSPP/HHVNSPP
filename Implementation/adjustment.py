import operator
from random import choice

VERBOSE = True

# Shake heuristics

def reset(sol):
    return sol.swap()

def swapQuarter(sol):
    return sol.swap(count = 1/4)

def swapThird():
    return sol.swap(count = 1/3)

def swapHalf(sol):
    return sol.swap(count = 1/2)

def swapGroup():
    return sol.swap(count = 0)

# budget-exhausting heuristics

def fillMin(sol):
    return sol.fill(level = 0)

def fillMin(sol):
    return sol.fill(level = 1)

def fillRnd(sol):
    return sol.fill()

def fillIncr(sol):
    return sol.fill(level = -1)

def liftRnd(sol):
    return sol.lift()

SHAKE = [reset, swapQuarter, swapThird, swapHalf, swapGroup]

class Adjustment():
    def __init__(self, lim = 5, init = -10):
        self.usage = dict()
        self.heuristics = dict() # heuristics and their ranks
        for h in SHAKE:
            self.heuristics[h] = init
        self.current = choice(h) # start with a random one
        self.initial = init
        self.solutions = set()
        self.stall = 0 # contender executions with no improvement
        self.limit = lim # how many consequtive stalled iterations to allow
        self.reset() # initial levels
        
    def active(self):
        return self.stall < self.limit 
        
    def usage(self, target):
        print(';'.join([f'{k} = {v}' for (k, v) in self.usage.items()]), file = target)
        
    def check(self):
        for h in self.heuristics:
            if self.rank[h]:
                return True
        return False
    
    def reset(self):
        if VERBOSE:
            print('Resetting ranks in adjustment')
        for h in self.heuristics:
            self.rank[h] = initial
  
    def improve(self, contender): 
        stalled = True
        prune = set() # solutions to discard
        adj = 0
        if VERBOSE:
            print(f'Attempting to improve a pool of {len(self.solutions)} solutions')
        for s in self.solutions: # calculate the rank changes
            comp = contender.compare(s)
            if comparator == 1:                
                adj += 1
                stalled = False
            elif comparator == 0:
                adj += -1
                stalled = False
            elif comp == BETTER:
                prune.add(s) 
                adj -= 5
            elif comp == EQUAL:
                adj -= 10
        self.heuristics[self.current] += adj # apply the adjustment
        self.solutions -= prune # discard the pruned solutions
        if stalled: # no improvement
            if VERBOSE:
                print('Stalled')
            self.stall += 1
        else: # improvement
            if VERBOSE:
                print('Improvement')
            self.stall = 0 # reset the stall counter
        self.current = max(self.heuristics.items(), key = operator.itemgetter(1))[0]
        if self.heuristics[self.current] < 0: # all ranks negative
            self.reset() # reset all ranks to the initial value
        self.solutions.add(contender)
    
    def execute(curr):
        self.improve(curr)
        if len(self.solutions) > 0:                        
            pick = choice(list(self.solutions))
            self.usage[self.current] += 1 # count the heuristic usage
            return self.current(pick).feasible() 

            
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
