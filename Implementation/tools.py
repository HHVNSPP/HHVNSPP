import numpy as np
from time import time
from math import log, ceil
from electre import electre
from solution import Solution
from collections import defaultdict
from random import shuffle, choice, randint

verbose = True
details = False

def display(d, title):
    if max(d.values()) > 1:
        nonunit = list()
        for k in d:
            v = d[k]
            if v > 1:
                nonunit.append(f'{k.__name__} = {v}')
        lst = '\n'.join(nonunit)
        print(f'{title}:\n{lst}')

def roulette(rank):
    candidates = list(rank.keys())
    total = sum(rank.values())
    if details and total > len(rank):
        print('Roulette wheel:', ' '.join([ str(v) for v in rank.values() ]))
    if total == 0: # all ranks are zero
        return choice(candidates)
    cutoff = randint(0, total) 
    shuffle(candidates)
    acc = 0
    for c in candidates:
        acc += rank[c]
        if acc >= cutoff:
            return c

BETTER = -1
WORSE = 1
EQUAL = 0
NONDOM = 2

# Pareto dominance for maximization
def dominated(s1, s2): 
    ev1 = s1.evaluate()
    ev2 = s2.evaluate()
    if ev1 == ev2:
        return set(), True # equal
    eq12 = []
    eq21 = []
    imp12 = []
    imp21 = []
    for (o1, o2) in zip(ev1, ev2): 
        # at least as good
        eq12.append(o1 >= o2)
        eq21.append(o2 >= o1) 
        # better
        imp12.append(o1 > o2)
        imp21.append(o2 > o1)
    b1 = any(imp12) # s1 is better at something
    b2 = any(imp21) # s2 is better at something
    if b1 and b2: # neither dominates the other
        return set(), False
    if b1 and all(eq12):
        return { s2 }, False # s2 was dominated by s1
    if b2 and all(eq21):
        return { s1 }, False  # s1 was dominated by s2
    # one should never reach this point
    quit()

def compare(original, proposal):
    d, e = dominated(original, proposal)
    if e:
        return EQUAL
    elif len(d) == 0:
        return NONDOM
    return WORSE if original in d else BETTER

def prune(included):
    dom = set()
    for a in included:
        if a not in dom:
            for b in included:
                if a != b:
                    if b not in dom:
                        d, e = dominated(a, b)
                        if not e: # not the same
                            dom |= d
    remaining = included - dom
    return remaining

# Shake heuristics

def swapRandom(original):
    shaken = original.swap()
    if details:
        print(f'Shake swapRandom\n{original.included()}\n{shaken.included()}')
    return shaken

def swapQuarter(original):
    shaken = original.swap(count = 1/4)
    if details:
        print(f'Shake swapQuarter\n{original.included()}\n{shaken.included()}')
    return shaken    

def swapThird(original):
    shaken = original.swap(count = 1/3)
    if details:
        print(f'Shake swapThird\n{original.included()}\n{shaken.included()}')
    return shaken

def swapHalf(original):
    shaken = original.swap(count = 1/2)
    if details:
        print(f'Shake swapHalf\n{original.included()}\n{shaken.included()}')
    return shaken

def swapGroup(original):
    shaken = original.swap(count = 0)
    if details:
        print(f'Shake swapGroup\n{original.included()}\n{shaken.included()}')
    return shaken

SHAKE = [ swapRandom, swapQuarter, swapThird, swapHalf, swapGroup ]

# Local search heuristics

def swapOne(original):
    neighbor = original.swap(count = 1)
    if details:
        print(f'Search swapOne\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclRndMin(original):
    neighbor = original.add(level = MINIMUM)
    if details:
        print(f'Search inclRndMin\n{original.included()}\n{neighbor.included()}')
    return neighbor

def inclRndMax(original):
    neighbor = original.add(level = MAXIMUM)
    if details:
        print(f'Search inclRndMax\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclRndRnd(original):
    neighbor = original.add(level = RANDOM)
    if details:
        print(f'Search inclRndRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor

def exclRnd(original):
    neighbor = original.remove()
    if details:
        print(f'Search exclRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclLowMin(original):  
    neighbor = original.fitExtreme(high = False, level = MINIMUM)
    if details:
        print(f'Search inclLowMin\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclLowMax(original):  
    neighbor = original.fitExtreme(high = False, level = MAXIMUM)
    if details:
        print(f'Search inclLowMax\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclLowRnd(original):  
    neighbor = original.fitExtreme(high = False, level = RANDOM)
    if details:
        print(f'Search inclLowRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclHighMin(original):
    neighbor = original.fitExtreme(high = True, level = MINIMUM)
    if details:
        print(f'Search inclHighMin\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclHighMax(original):
    neighbor = original.fitExtreme(high = True, level = MAXIMUM)
    if details:
        print(f'Search inclHighMax\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inclHighRnd(original):
    neighbor = original.fitExtreme(high = True, level = RANDOM)
    if details:
        print(f'Search inclHighRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def exclHigh(original):
    neighbor = original.dropExtreme()
    if details: # the change is best seen in the assignment
        print(f'Search exclHigh\n{original.allocation()}\n{neighbor.allocation()}')
    return neighbor    

def exclLow(original):
    neighbor = original.dropExtreme(high = False)
    if details:
        print(f'Search exclLow\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def fundAtMin(original):
    neighbor = original.alter(MINIMUM)
    if details: # it is the amount that may change, not the activation
        print(f'Search fundAtMin\n{original.evaluate()}\n{neighbor.evaluate()}')
    return neighbor    

def fundAtMax(original):
    neighbor = original.alter(MAXIMUM)
    if details: # it is the amount that may change, not the activation
        print(f'Search fundAtMax\n{original.evaluate()}\n{neighbor.evaluate()}')
    return neighbor    

def fundAtRnd(original):
    neighbor = original.alter(RANDOM)
    if details: # it is the amount that may change, not the activation
        print(f'Search fundAtRnd\n{original.evaluate()}\n{neighbor.evaluate()}')
    return neighbor    

## Group-level local search heuristics

def inflGrMin(original):
    neighbor = original.modify(high = True, level = MINIMUM)
    if details:
        print(f'Search inflGrMin\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inflGrMax(original):
    neighbor = original.modify(high = True, level = MAXIMUM)
    if details:
        print(f'Search inflGrMax\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def inflGrRnd(original):
    neighbor = original.modify(high = True, level = RANDOM)
    if details:
        print(f'Search inflGrRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def deflGrMin(original):  
    neighbor = original.modify(high = False, level = MINIMUM)
    if details:
        print(f'Search deflGrMin\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def deflGrMax(original):  
    neighbor = original.modify(high = False, level = MAXIMUM)
    if details:
        print(f'Search deflGrMax\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def deflGrRnd(original):  
    neighbor = original.modify(high = False, level = RANDOM)
    if details:
        print(f'Search deflGrRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

def exchGrMin(original):
    neighbor = original.exchange(level = MINIMUM)
    if details:
        print(f'Search exchGrMin\n{original.included()}\n{neighbor.included()}')
    return neighbor

def exchGrMax(original):
    neighbor = original.exchange(level = MAXIMUM)
    if details:
        print(f'Search exchGrMax\n{original.included()}\n{neighbor.included()}')
    return neighbor

def exchGrRnd(original):
    neighbor = original.exchange(level = RANDOM)
    if details:
        print(f'Search exchGrRnd\n{original.included()}\n{neighbor.included()}')
    return neighbor    

LOCAL = [ swapOne,
          inclRndMin, inclRndMax, inclRndRnd,
          inclLowMin, inclLowMax, inclLowRnd,
          inclHighMin, inclHighMax, inclHighRnd,
          fundAtMin, fundAtMax, fundAtRnd,
          exclRnd, exclLow, exclHigh,
          inflGrMin, inflGrMax, inflGrRnd,
          deflGrMin, deflGrMax, deflGrRnd,
          exchGrMin, exchGrMax, exchGrRnd ]

# Fill (budget-exhausting) heuristics

from solution import MINIMUM, MAXIMUM, RANDOM

def incrMin(sol):
    if details:
        print(f'Fill incrMin\n{sol.included()}')
    sol.fill(level = MINIMUM, active = False, sort = True)
    if details:
        print(sol.included())
     
def incrMax(sol):
    if details:
        print(f'Fill incrMax\n{sol.included()}')
    sol.fill(level = MAXIMUM, active = False, sort = True)
    if details:
        print(sol.included())
    
def incrRnd(sol):
    if details:
        print(f'Fill incrRnd\n{sol.included()}')
    sol.fill(level = RANDOM, active = False, sort = True)
    if details:
        print(sol.included())    

def rndMin(sol):
    if details:
        print(f'Fill rndMin\n{sol.included()}')
    sol.fill(level = MINIMUM, active = False, sort = False)
    if details:
        print(sol.included())    

def rndMax(sol):
    if details:
        print(f'Fill rndMax\n{sol.included()}')
    sol.fill(level = MAXIMUM, active = False, sort = False)
    if details:
        print(sol.included())

def rndRnd(sol):
    if details:
        print(f'Fill rndRnd\n{sol.included()}')
    sol.fill(level = RANDOM, active = False, sort = False)
    if details:
        print(sol.included())
    
FILL = [ incrMin, incrMax, incrRnd, \
         rndMin, rndMax, rndRnd ]

def score(alt, orig, big = 2, intermediate = 0.5, small = 0.1):
    a = 0
    for s in orig:
        comp = compare(alt, s)
        if comp == BETTER: # the newly made one dominates the original
            a += big 
        elif comp == EQUAL: # they are the same quality
            a += small
        elif comp != WORSE:
            a += intermediate # neither dominates
    return round(a)

class Adjustment():

    def __init__(self, pf, t, sec = 2):
        self.portfolio = pf
        n = len(self.portfolio.projects)
        k = len(self.portfolio.weights)
        seed = 2**(6 - ceil(log(k, 2))) 
        self.limit = sec * n # seconds per project
        if verbose:
            print(f'Running for no more than {self.limit} seconds')
        self.goal = 5 # how many solutions we would like to have in the front at minimum
        self.maxiter = 2 * seed
        if verbose:
            print(f'Executing at most {self.maxiter} iterations')        
        self.stall = 0 # executions with no improvement
        # shake stall
        self.maxshake = 3 * len(SHAKE)
        # search stall maximum
        self.maxsearch = len(LOCAL) + len(FILL)
        if verbose:
            print(f'Stall limit is {self.maxshake} for shake and {self.maxsearch} for search')                
        self.target = t
        self.usage = defaultdict(int) # counters
        self.shakerank = { h : 1 for h in SHAKE } # initial unit shake ranks
        self.searchrank = { h : 1 for h in LOCAL } # initial unit search ranks
        self.fillrank = { h : 1 for h in FILL } # initial unit fill ranks
        self.shaker = None # last used shake heuristic
        self.filler = None # last used fill heuristic
        # larger fronts are easier to get with multiple objectives
        # more objectives -> less initial solutions        
        if verbose:
            print(f'Creating {seed} initial solutions')
            # improve the initial front with local search
        self.front = None
        self.start = time() # start the timer now
        self.search(set([ Solution(self.portfolio) for s in range(seed) ]))

    def postprocess(self, i):
        if verbose:
            pl = 's' if i > 0 else ''
            print(f'Terminated after {i+1} iteration{pl}') 
        t = time() - self.start
        print(f'final;{t};{i};{self.stall}', file = self.target)
        sol = list(self.front)
        if verbose:
            print(f'Final front size {len(sol)}')
            print(f'Took {t:.0f} seconds of the {self.limit} permitted')
            if details:
                for s in sol:
                    print(s.included(), s.evaluate())
        evaluation = np.matrix([ s.evaluate() for s in sol ])
        ranking = electre(self.portfolio.weights, evaluation)
        for i in range(len(ranking)):
            assert(sol[i].feasible()) # make sure nothing is broken
            print(f'electre;{ranking[i]};{evaluation[i, :]}', file = self.target)
        us = [ f'usage;{k.__name__}={v}' for (k, v) in self.usage.items() ]
        print('\n'.join(us), file = self.target)

    def __str__(self):
        return f'{self.stall}\n' + '\n'.join([ str(sol) for sol in self.front ])

    def __repr__(self):
        return str(self)

    def evaluate(self):
        return np.matrix([s.evaluate() for s in self.front])
        
    def output(self):
        diff = time() - self.start        
        print(diff, file = self.target)
        print(self.evaluate(), file = self.target)

    def pick(self, options):
        used = [ self.usage[h] for h in options ]
        h = None
        if min(used) > 0: # all options have been used
            h = roulette(options) # use the ranks
        else: # everyone gets one chance
            candidates = list()
            for h in options:
                if self.usage[h] == 0:
                    candidates.append(h)
            h = choice(candidates)
        assert h is not None
        self.usage[h] += 1
        return h
            
    def shake(self):
        self.shaker = self.pick(self.shakerank)
        self.filler = self.pick(self.fillrank)
        shaken = set()
        repetitions = max(2, self.goal - (len(self.front) if self.front is not None else 0))
        for s in self.front:
            for r in range(repetitions):
                result = self.shaker(s) # shake it
                if details:
                    print(r, result.included(), result.allocation())
                result.fix() # make feasible
                self.filler(result)
                shaken.add(result)
        k = len(shaken)
        pl = 's' if k > 1 else ''
        if details:
            print(f'Shaking with {self.shaker.__name__} yielded {k} alternative{pl}')
            for s in shaken:
                print(s.included())
        missing = 2 * self.goal - k
        if missing > 0: # too few, add new random solutions
            shaken |= set([ Solution(self.portfolio) for s in range(missing) ])
            if details:
                pl = 's' if missing > 1 else ''            
                print(f'Adding {missing} new solution{pl}')            
        return shaken # note that these may be INFEASIBLE

    def search(self, shaken):
        if details and self.shaker is None:
            print(f'Executing local search on the initial solutions')
        lstall = 0 # search stall counter resets each stage
        ok = True # whether the time limit is respected
        altered = 0 # how many times the front changes
        while lstall < self.maxsearch: # while not stalled
            if time() - self.start > self.limit: 
                if verbose:
                    print('Out of time while searching')
                ok = False # no time left
                break
            local = set() # gather the variants here
            searcher = self.pick(self.searchrank) # pick a search heuristic
            helper = self.pick(self.fillrank) # a fill one, too
            if details:
                print(f'Using {searcher.__name__} to search and {helper.__name__} to fill')
            repetitions = max(2, self.goal - (len(self.front) if self.front is not None else 0))
            for sol in shaken:
                for r in range(repetitions):                
                    neighbor = searcher(sol) # create an alternative solution
                    neighbor.fix() #  ensure feasibility
                    helper(neighbor) # fill it
                    local.add(neighbor) # record it
            k = len(local) # check how many there are
            stalled = True
            if k > 0: # examine them
                # combine and prune
                curr = self.front if self.front is not None else set()
                result = prune(local | curr)
                if result == self.front:
                    lstall += 1
                    if details:
                        print(f'The Pareto front did not change; stall counter {lstall}/{self.maxsearch}')
                    # losing rank
                    self.searchrank[searcher] = max(1, self.searchrank[searcher] // 2)
                    self.fillrank[helper] = max(1, self.fillrank[helper] // 2)
                else:
                    self.front = result # update the front                    
                    # compare against ORIGINAL front
                    adj = round(sum([ score(s, curr) for s in local] )/ len(local))
                    if adj > 0: # these heuristics gain rank
                        self.searchrank[searcher] += adj
                        self.fillrank[helper] += adj
                    display(self.searchrank, 'Search ranks')
                    display(self.fillrank, 'Fill ranks')
                    lstall = 0 # reset the counter
                    altered += 1 # the front has changed
                    if details:
                        print(f'Altered the Pareto front')
                        for s in result:
                            print('F', s.included(), ' '.join([ f'{v:.0f}' for v in s.evaluate() ]))
                        for s in curr:
                            print('C', s.included(), ' '.join([ f'{v:.0f}' for v in s.evaluate() ]))
                        for s in local:
                            print('L', s.included(), ' '.join([ f'{v:.0f}' for v in s.evaluate() ]))
        if altered > 0:
            if self.shaker is not None:
                self.shakerank[self.shaker] += altered # gain rank
                display(self.shakerank, 'Shake ranks')
                self.stall = 0 # reset shaking
            if details:
                f = len(self.front)
                pl = 's' if f > 1 else ''
                if self.shaker is not None:
                    print(f'After shaking with {self.shaker.__name__}, the front has {f} non-dominated solution{pl}')
                else:
                    print(f'The initial solutions gave rise to a front with {f} non-dominated solution{pl}')                
        elif self.shaker is not None:
            if details:
                print(f'Shaking with {self.shaker.__name__} resulted in no alterations of the front')
            self.stall += 1
            self.shakerank[self.shaker] = max(1, self.shakerank[self.shaker] // 2)
        return ok
        
    def step(self, printout):
        self.search(self.shake())
        if printout: # if output is requested
            self.output()
        progress = self.stall < self.maxshake
        if not progress:
            print(f'Shaking has stalled')
        fast = time() - self.start < self.limit
        return progress and fast # true to continue

    def run(self):
        o = 1
        for i in range(self.maxiter):
            k = len(self.front)
            pl = 's' if k > 1 else ''
            if details:
                print(f'Iteration {i+1} with {k} non-dominated solution{pl}')
            out = i == o
            if out: # output on iterations that are powers of two
                print(f'w;{i}', file = self.target)
                if details:
                    print(f'Iteration {i} of {self.maxiter}')
                o *= 2
            if not self.step(out):
                self.postprocess(i)
                return
