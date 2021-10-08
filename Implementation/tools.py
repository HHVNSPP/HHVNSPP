import numpy as np
from time import time
from math import log, ceil
from electre import electre
from solution import Solution
from collections import defaultdict
from random import shuffle, choice, randint

def roulette(rank):
    candidates = list(rank.keys())
    total = sum(rank.values())
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

def swapTenth(sol):
    return sol.swap(count = 1/10)

def swapQuarter(sol):
    return sol.swap(count = 1/4)

def swapThird(sol):
    return sol.swap(count = 1/3)

def swapHalf(sol):
    return sol.swap(count = 1/2)

def swapGroup(sol):
    return sol.swap(count = 0)

SHAKE = [ reset, swapTenth, swapQuarter, swapThird, swapHalf, swapGroup ]

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

def score(alt, orig, big = 10, intermediate = 5, small = 1):
    comp = compare(alt, orig)
    if comp == BETTER: # the newly made one dominates the original
        return big 
    elif comp == WORSE: # the new one is worse than the original
        return -big
    elif comp == EQUAL: # they are the same quality
        return small
    return intermediate # neither dominates

verbose = True

class Adjustment():

    def __init__(self, pf, lim, mi, t):
        self.portfolio = pf
        self.limit = lim
        self.maxiter = mi
        self.maxsearch = self.maxiter // 2 # half for search
        self.target = t
        n = 2**(7 - ceil(log(len(pf.weights), 2))) # more objectives -> less initial solutions
        if verbose:
            print(f'Creating {n} initial solutions')
        # larger fronts are easier to get with multiple objectives
        self.front = prune(set( [Solution(pf) for s in range(n) ]))
        if verbose:
            print(f'Initial front size {len(self.front)}')        
        self.usage = defaultdict(int) # counters
        self.stall = 0 # executions with no improvement
        self.sr = { h : 1 for h in SHAKE } # shake ranks
        self.fr = { h : 1 for h in FILL } # shake-stage fill ranks
        self.start = time() # start the timer now
        self.search() # improve the initial front with local search

    def postprocess(self):
        t = time() - self.start
        stalled = self.stall
        print(f'final;{t};{self.stall};{stalled}', file = self.target)
        sol = list(self.front)
        if verbose:
            print(f'Final front size {len(sol)}')
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
        
    def shake(self):
        # the shake ranks persist throughout the process
        sh = roulette(self.sr) # pick a shake heuristic
        fh = roulette(self.fr) # pick a fill heuristic
        shaken = set()
        for s in self.front:
            ss = sh(s)
            ss.fix()
            fh(ss)
            assert ss.feasible()
            a = score(ss, s)
            if a > 0:
                self.sr[sh] += a
                self.fr[fh] += a
                shaken.add(ss) # not worse
            else: # negative score
                self.sr[sh] = max(self.sr[sh] - a, 1)
                self.fr[fh] = max(self.fr[fh] - a, 1)
            self.usage[sh] += 1
            self.usage[fh] += 1
        k = len(shaken)
        if k > 0:
            if verbose:
                pl = 's' if k > 1 else ''
                print(f'Shaking with {sh.__name__} created {k} variant{pl}')
            # keep only the non-dominated ones
            old = self.front.copy()
            self.front = prune(self.front | shaken)
            if old == self.front: # no change
                self.stall += 1
            else: # the front has changed
                self.stall = 0

    def search(self):
        # ranks that reset each local search        
        lsr = { h : 1 for h in LOCAL } 
        lfr = { h : 1 for h in FILL }
        lstall = 0
        ok = True
        altered = 0
        while lstall < self.maxsearch: 
            if time() - self.start > self.limit:
                if verbose:
                    print('Out of time while searching')
                ok = False
                break
            local = set()
            sh = roulette(lsr) # pick a search heuristic
            fh = roulette(lfr) # a fill one, too
            for sol in self.front:
                ls = sh(sol) # create an alternative solution
                ls.fix() #  ensure feasibility
                fh(ls) # fill it
                assert ls.feasible() 
                a = score(ls, sol) # score it
                if a > 0: # it is not worse
                    local.add(ls)
                    lsr[sh] += a
                    lfr[fh] += a
                else: # negative score
                    lsr[sh] = max(lsr[sh] - a, 1)
                    lfr[fh] = max(lfr[fh] - a, 1)                    
                self.usage[fh] += 1
                self.usage[sh] += 1
            k = len(local)
            if k > 0:
                old = self.front.copy()
                self.front = prune(self.front | local)
                if old == self.front: # no change
                    lstall += 1
                else: # the front has changed
                    lstall //= 2 # lower the counter
                    altered += 1
        if verbose and altered > 0:
            pl = 's' if altered > 1 else ''
            print(f'Search altered the front {altered} time{pl}')
        return ok
        
    def step(self, printout):
        self.shake()
        self.search() 
        if printout: # if output is requested
            self.output()
        progress = self.stall < self.maxiter
        fast = time() - self.start < self.limit
        return progress and fast # true to continue

    def run(self):
        o = 1
        for i in range(self.maxiter):
            out = i == o
            if out: # output on iterations that are powers of two
                print(f'w;{i}', file = self.target)
                if verbose:
                    print(f'Iteration {i} of {self.maxiter}')
                o *= 2
                if not self.step(out):
                    if verbose:
                        pl = 's' if i > 0 else ''
                        print(f'Terminated after {i+1} iteration{pl}') 
                    break # out of time or stalled
        self.postprocess()
