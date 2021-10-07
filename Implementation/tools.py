import numpy as np
from time import time
from electre import electre
from solution import Solution
from collections import defaultdict
from random import shuffle, choice, randint

def roulette(rank):
    candidates = list(rank.keys())
    total = sum([ max(rank[c], 1) for c in candidates ])
    if total == 0: # all ranks are zero
        return choice(candidates)
    cutoff = randint(0, total) 
    shuffle(candidates)
    acc = 0
    for c in candidates:
        acc += max(rank[c], 1)
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
                if b not in dom:
                    if a == b:
                        continue
                    d, e = dominated(a, b)
                    if not e:
                        dom |= d
    remaining = included - dom
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

def score(alt, orig, big = 10, small = 1):
    comp = compare(alt, orig)
    if comp == BETTER: # the newly made one dominates the original
        return big 
    elif comp == WORSE: # the new one is worse than the original
        return -big
    elif comp == EQUAL: # they are the same quality
        return -small
    return small

class Adjustment():

    def __init__(self, pf, lim, t, seed = 50):
        self.target = t
        self.portfolio = pf
        self.start = time()
        self.limit = lim
        self.front = prune(set( [Solution(pf) for s in range(seed) ]))
        self.usage = defaultdict(int) # counters
        self.stall = 0 # executions with no improvement
        self.sr = { h : 1 for h in SHAKE } # shake ranks
        self.fr = { h : 1 for h in FILL } # shake-stage fill ranks

    def postprocess(self):
        sol = list(self.front)
        evaluation = np.matrix([ s.evaluate() for s in sol ])
        ranking = electre(self.portfolio.weights, evaluation)
        for i in range(len(ranking)):
            assert(sol[i].feasible()) # make sure nothing is broken
            print(f'electre;{ranking[i]};{evaluation[i, :]}', file = self.target)
        us = [f'usage;{k.__name__}={v}' for (k, v) in self.usage.items()]
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
        
    def improve(self, maxiter = 50):
        # the improvement ranks persist throughout the process
        sh = roulette(self.sr) # pick a shake heuristic
        fh = roulette(self.fr) # pick a fill heuristic
        shaken = set()
        print(f'front size {len(self.front)}')
        for s in self.front:
            ss = sh(s)
            ss.fix()
            fh(ss)
            assert ss.feasible()
            a = score(ss, s)
            self.sr[sh] += a
            self.fr[fh] += a
            if a >= 0:
                shaken.add(ss) # not dominated
            self.usage[sh] += 1
            self.usage[fh] += 1
        k = len(shaken)
        if k > 0:
            pl = 's' if k > 1 else ''
            print(f'{sh.__name__} shook up {k} variant{pl}')        
            # keep only the non-dominated ones
            self.front = prune(self.front | shaken) 
            self.stall = 0
        else:
            self.stall += 1
        progress = self.stall < maxiter
        fast = time() - self.start < self.limit
        return progress and fast # true if ok to continue

    def search(self, maxiter = 50, verbose = False):
        hr = { h : 1 for h in LOCAL } # reset each local search
        fr = { h : 1 for h in FILL }
        lstall = 0
        while lstall < maxiter:
            if time() - self.start > self.limit:
                print('out of time while searching')
                return False
            sh = roulette(hr)
            fh = roulette(fr)
            local = set()
            for sol in self.front:
                ls = sh(sol) # create an alternative solution
                ls.fix() #  make feasible
                fh(ls) # fill it
                self.usage[fh] += 1
                self.usage[sh] += 1
                assert ls.feasible()
                a = score(ls, sol)
                if a >= 0: # not dominated
                    local.add(ls)
                hr[sh] += a
                fr[fh] += a
            k = len(local)
            if k > 0:
                if verbose:
                    pl = 's' if k > 1 else ''
                    print(f'{sh.__name__} produced {k} neighbor{pl}')
                # keep only the non-dominated ones
                self.front = prune(self.front | local)
                lstall = 0
            else:
                lstall += 1
        return True # still time to keep going
        
    def step(self, printout):
        ok = self.search() # do a search
        if ok: # still have time
            ok = self.improve() # do a shake
        if printout: # if output is requested
            self.output()
        return ok
