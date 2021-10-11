import numpy as np
from time import time
from math import log, ceil
from electre import electre
from solution import Solution
from collections import defaultdict
from random import shuffle, choice, randint

verbose = True
details = False

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

def swapRandom(sol):
    return sol.swap()

def swapQuarter(sol):
    return sol.swap(count = 1/4)

def swapThird(sol):
    return sol.swap(count = 1/3)

def swapHalf(sol):
    return sol.swap(count = 1/2)

def swapGroup(sol):
    return sol.swap(count = 0)

def swapAll(sol):
    return sol.swap(count = -1)

SHAKE = [ swapRandom, swapQuarter, swapThird, swapHalf, swapAll, swapGroup ]

# Local search heuristics

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

## Group-level local search heuristics

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

# Fill (budget-exhausting) heuristics

from solution import MINIMUM, MAXIMUM, RANDOM

def fillIncrMin(sol):
    sol.fill(level = MINIMUM, active = False, sort = True)
    
def fillIncrMax(sol):
    sol.fill(level = MAXIMUM, active = False, sort = True)
    
def fillIncrRnd(sol):
    sol.fill(level = RANDOM, active = False, sort = True)

def fillRndMin(sol):
    sol.fill(level = MINIMUM, active = False, sort = False)

def fillRndMax(sol):
    sol.fill(level = MAXIMUM, active = False, sort = False)

def fillRndRnd(sol):
    sol.fill(level = RANDOM, active = False, sort = False)
    
def fillLift(sol):
    sol.fill(level = MAXIMUM, active = True, sort = False)

FILL = [ fillIncrMin, fillIncrMax, fillIncrRnd, \
         fillRndMin, fillRndMax, fillRndRnd, fillLift ]

def score(alt, orig, big = 1, intermediate = 0.2, small = 0.1):
    a = 0
    for s in orig:
        comp = compare(alt, s)
        if comp == BETTER: # the newly made one dominates the original
            a += big 
        elif comp == WORSE: # the new one is worse than the original
            a -= big
        elif comp == EQUAL: # they are the same quality
            a +=  small
        else:
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
        self.repetitions = max(3, seed // k)
        print(f'Executing {self.repetitions} variants per solution')                
        self.maxiter = 2 * seed
        if verbose:
            print(f'Executing at most {self.maxiter} iterations')        
        self.stall = 0 # executions with no improvement
        # shake stall
        self.maxshake = len(SHAKE) + self.maxiter // 2
        # search stall maximum        
        self.maxsearch = max([ len(LOCAL), len(FILL) ]) + self.maxiter // 8 
        if verbose:
            print(f'Stall limit is {self.maxshake} for shake and {self.maxsearch} for search')                
        self.target = t
        self.usage = defaultdict(int) # counters
        self.rank = { h : 1 for h in SHAKE } # initial unit shake ranks
        self.chosen = None # last used shake heuristic
        # larger fronts are easier to get with multiple objectives
        # more objectives -> less initial solutions        
        if verbose:
            print(f'Creating {seed} initial solutions')
            # improve the initial front with local search
        self.front = None
        self.start = time() # start the timer now
        self.search(set( [Solution(self.portfolio) for s in range(seed) ]))

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
        if min(used) > 0:
            h = roulette(options) # pick a heuristic
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
        self.chosen = self.pick(self.rank)
        self.usage[self.chosen] += 1        
        shaken = set()
        for s in self.front:
            for r in range(self.repetitions):
                shaken.add(self.chosen(s)) 
        k = len(shaken)
        assert k > 0
        pl = 's' if k > 1 else ''
        print(f'Shaking with {self.chosen.__name__} yielded {k} alternative{pl}')
        if details:
            for s in shaken:
                print(s.included())
        return shaken # note that these may be INFEASIBLE

    def search(self, shaken):
        if self.chosen is None:
            print(f'Executing local search on the initial solutions')
        # ranks that reset each local search        
        lsr = { h : 1 for h in LOCAL } 
        fr = { h : 1 for h in FILL }
        lstall = 0 # stall counter resets, too
        ok = True # whether the time limit is respected
        altered = 0 # how many times the front changes
        while lstall < self.maxsearch: # while not stalled
            if time() - self.start > self.limit: 
                if verbose:
                    print('Out of time while searching')
                ok = False # no time left
                break
            local = set() # gather the variants here
            lsh = self.pick(lsr) # pick a search heuristic
            fh = self.pick(fr) # a fill one, too
            print(f'Using {lsh.__name__} to search and {fh.__name__} to fill')
            for sol in shaken:
                for r in range(self.repetitions):                
                    ls = lsh(sol) # create an alternative solution
                    ls.fix() #  ensure feasibility
                    fh(ls) # fill it
                    local.add(ls) # record it
            k = len(local) # check how many there are
            stalled = True
            if k > 0: # examine them
                # compare against current front
                if self.front is not None: # not the first search
                    adj = sum([ score(s, self.front) for s in local] ) // len(local)
                    if adj > 0: # gain rank
                        if self.chosen is not None:
                            self.rank[self.chosen] += adj
                        lsr[lsh] += adj
                        fr[fh] += adj
                    else: # lose rank
                        if self.chosen is not None:
                            self.rank[self.chosen] = max(self.rank[self.chosen] - adj, 1)
                        lsr[lsh] = max(lsr[lsh] + adj, 1)
                        fr[fh] = max(fr[fh] + adj, 1)
                # combine and prune
                curr = self.front if self.front is not None else set()
                result = prune(local | curr)
                if result == self.front:
                    lstall += 1
                    print(f'The Pareto front did not change; stall counter {lstall}/{self.maxsearch}')
                else:
                    lstall //= 2 # lower the counter
                    altered += 1 # the front has changed
                    print(f'Altered the Pareto front')
                self.front = result # update the front
        if altered > 0:
            self.stall = 0 # reset shaking
            f = len(self.front)
            pl = 's' if f > 1 else ''
            if self.chosen is not None:
                print(f'After shaking with {self.chosen.__name__}, the front has {f} non-dominated solution{pl}')
            else:
                print(f'The initial solutions gave rise to a front with {f} non-dominated solution{pl}')                
            if details:
                for s in self.front:
                    print(s.included(), ' '.join([ f'{v:.0f}' for v in s.evaluate() ]))
        else:
            print(f'Shaking with {self.chosen.__name__} resulted in no alterations of the front')
            self.stall += 1
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
