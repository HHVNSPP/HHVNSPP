import numpy as np
from time import time
from electre import electre
from random import shuffle, choice
from collections import defaultdict

BETTER = -1
WORSE = 1
EQUAL = 0
NONDOM = 2

verbose = True

# Pareto dominance

def notDominated(defendant, opponent):
    equal = True
    n = len(defendant)
    assert n == len(opponent)
    matches = 0
    improves = False
    for i in range(n):
        if defendant[i] != opponent[i]:
            equal = False
        if defendant[i] >= opponent[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant[i] > opponent[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return equal, improves and matches == n # defendant is not dominated by opponent

def compare(one, another):
    se = one.evaluate()
    ae = another.evaluate()
    eq, dom = notDominated(se, ae)
    if eq:
        return EQUAL
    elif dom:
        return BETTER
    eq, dom = notDominated(ae, se)
    if dom:
        return WORSE
    return NONDOM

# maximal choices

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
            comp = compare(a, b)
            if comp == BETTER: # a dominates b
                dominated.add(b) # b needs to be pruned
                continue
            elif comp == WORSE: # b dominates a
                dominated.add(a)
                break
    remaining = included - dominated
    return remaining

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

def adjust(alt, s, big = 10, small = 1):
    comp = compare(alt, s)
    if comp == BETTER: # the newly made one dominates the original
        return big
    else:
        if comp == WORSE:
            return -big
        elif comp == EQUAL: 
            return -small
        else: # neither dominates the other, they're not equal
            return 0

class Adjustment():

    def __init__(self, seed, lim):
        assert seed is not None
        self.start = time()
        self.limit = lim
        self.pool = { seed }
        self.usage = defaultdict(int) # counters
        self.stall = 0 # executions with no improvement
        self.sr = { h : 0 for h in SHAKE } # shake ranks
        self.fr = { h : 0 for h in FILL } # shake-stage fill ranks

    def postprocess(self, weights, target):
        sol = list(self.pool)
        eval = np.matrix([ s.evaluate() for s in sol ])
        score = electre(weights, eval)
        for i in range(len(score)):
            print(f'electre;{score[i]};{eval[i, :]}', file = target)
        us = [f'usage;{k.__name__}={v}' for (k, v) in self.usage.items()]
        print('\n'.join(us), file = target)

    def __str__(self):
        return f'{self.stall}\n' + '\n'.join([ str(sol) for sol in self.pool ])

    def __repr__(self):
        return str(self)

    def evaluate(self):
        return np.matrix([s.evaluate() for s in self.pool])
        
    def output(self, target):
        diff = time() - self.start        
        print(f'w;{i};{diff}', file = target)
        print(self.evaluate(), file = target)
        
    def improve(self, maxiter = 20):
        # the improvement ranks persist throughout the process
        sh = pick(self.sr) # pick a shake heuristic
        fh = pick(self.fr) # pick a fill heuristic
        shaken = set()
        for s in self.pool:
            ss = sh(s)
            ss.adjust() # make it feasible
            fh(ss)
            assert ss is not None
            a = adjust(ss, s)
            self.sr[sh] += a
            self.fr[fh] += a
            if a > 0:
                self.stall = 0
            else:
                self.stall += 1
            self.usage[sh] += 1
            self.usage[fh] += 1
            shaken.add(ss)
        self.pool = prune(self.pool | shaken) # keep only the non-dominated ones
        return self.stall < maxiter and time() - self.start < self.limit # true if ok to continue

    def search(self, maxiter = 20):
        hr = { h : 0 for h in LOCAL } # reset each local search
        fr = { h : 0 for h in FILL }
        lstall = 0
        assert len(self.pool) > 0
        while lstall < maxiter and time() - self.start < self.limit:
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
            local = set()
            for sol in self.pool:
                assert sol is not None
                ls = sh(sol) # create an alternative solution
                ls.adjust() # make it feasible
                assert ls.feasible()            
                fh(ls) # fill it
                if not ls.feasible():
                    print(fh.__name__, 'produced an infeasible solution')
                assert ls.feasible()
                self.usage[fh] += 1
                self.usage[sh] += 1
                a = adjust(ls, sol)
                if a > 0:
                    lstall = 0
                else:
                    lstall += 1
                hr[sh] += a
                fr[fh] += a
                local.add(ls)
            self.pool = prune(self.pool | local) # keep only the non-dominated ones
        
    def step(self):
        if self.search(): # do a search
            return self.improve() # time for a shake
        return False # out of time while searching
