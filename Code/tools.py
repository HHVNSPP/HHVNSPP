import numpy as np
from time import time
from sys import stderr
from kmeans import select # for sparsifying
from electre import electre # for ranking
from solution import Solution
from collections import defaultdict
from random import shuffle, choice, randint, sample

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

def pick(options, uses):
    used = [ uses[h] for h in options ]
    h = None
    if min(used) > 0: # all options have been used
        h = roulette(options) # use the ranks
    else: # everyone gets one chance
        candidates = list()
        for h in options:
            if uses[h] == 0:
                candidates.append(h)
        h = choice(candidates)
        assert h is not None
    uses[h] += 1
    return h

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

def liftIncr(sol):
    if details: # this one adds more funds
        print(f'Fill liftIncr\n{sol.allocation()}')
    sol.fill(level = MAXIMUM, active = True, sort = False)
    if details:
        print(sol.allocation())

def liftRnd(sol):
    if details: # this one adds more funds
        print(f'Fill liftRnd\n{sol.allocation()}')
    sol.fill(level = MAXIMUM, active = True, sort = False)
    if details:
        print(sol.allocation())
    
FILL = [ incrMin, incrMax, incrRnd,
         rndMin, rndMax, rndRnd, 
         liftIncr, liftRnd ]

def score(alt, orig, big = 4, intermediate = 2, small = 1):
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
    
    def __init__(self, pf, t, sec = 1, goal = 5, it = 64):
        self.portfolio = pf # the problem instance to optimize
        n = len(self.portfolio.projects) # number of projects
        k = len(self.portfolio.weights) # number of objectives
        self.limit = sec * n * k # maximum permitted runtime
        if verbose:
            print(f'Running for no more than {self.limit} seconds')
        self.goal = 5 # goal for the front size
        self.maxitershake = it # maximum permitted shake iterations
        self.maxitersearch = 10 # maximum permitted search iterations
        f = len(FILL) # how many fill heuristics are there
        self.maxshake = 2 * len(SHAKE) + f # permitted stall while shaking
        self.maxsearch = len(LOCAL) + f # permitted stall while searching
        self.shakestall = 0 # stall counter for shake
        self.searchstall = 0 # stall counter for search
        self.target = t # output file
        self.shakeusage = defaultdict(int) # counters
        self.shakerank = { h : 1 for h in SHAKE } # initial unit shake ranks
        self.shakefillrank = { h : 1 for h in FILL } # initial unit fill ranks        
        self.searchusage = defaultdict(int) # counters
        self.searchrank = { h : 1 for h in LOCAL } # initial unit search ranks
        self.searchfillrank = { h : 1 for h in FILL } # initial unit fill ranks
        self.shaker = None # last used shake heuristic
        self.filler = None # last used fill heuristic
        self.front = None # the storage for the front (none as of yet)
        self.start = time() # start time
        self.search(set([ Solution(self.portfolio) for s in range(self.goal) ]))
        self.output() # print-out of the initial population

    def postprocess(self, i):
        if details:
            self.check()
        t = time() - self.start
        if verbose:
            pl = 's' if i > 0 else ''
            print(f'{t:.0f} / {self.limit} seconds', file = stderr)            
            print(f'{i} / {self.maxitershake} shakes', file = stderr)            
            print(f'{self.shakestall} / {self.maxshake} shake stall', file = stderr)
            print(f'{len(self.front)} / {self.goal} front size', file = stderr)            
        print(f'final;{t:.3f}/{self.limit};{i}/{self.maxitershake};{self.shakestall}/{self.maxshake}', file = self.target)
        sol = list(self.front)
        if details:
            for s in sol:
                print(s.included(), s.evaluate())
        evaluation = np.matrix([ s.evaluate() for s in sol ])
        ranking = electre(self.portfolio.weights, evaluation)
        for i in range(len(ranking)):
            assert(sol[i].feasible()) # make sure nothing is broken
            print(f'electre;{ranking[i]};{evaluation[i, :]}', file = self.target)
        us = [ f'usage;shake;{k.__name__}={v}' for (k, v) in self.shakeusage.items() ]
        print('\n'.join(us), file = self.target)
        us = [ f'usage;search;{k.__name__}={v}' for (k, v) in self.searchusage.items() ]
        print('\n'.join(us), file = self.target)

    def __str__(self):
        return f'{self.shakestall}\n' + '\n'.join([ str(sol) for sol in self.front ])

    def __repr__(self):
        return str(self)

    def evaluate(self):
        return np.matrix([s.evaluate() for s in self.front])
        
    def output(self):
        diff = time() - self.start        
        print(diff, file = self.target)
        print(self.evaluate(), file = self.target)

    def subset(self):
        k = len(self.front)
        if k <= self.goal:
            return self.front # use all if not many
        # downsample if more than needed
        return sample(list(self.front), self.goal)
        
    def shake(self):
        self.shaker = pick(self.shakerank, self.shakeusage)
        self.filler = pick(self.shakefillrank, self.shakeusage)
        shaken = set()
        repetitions = max(1, self.goal - (len(self.front) if self.front is not None else 0))
        for s in self.subset(): # shake some of the front for diversity
            for r in range(repetitions): # repeat when the front is small
                result = self.shaker(s) # shake the solution
                if details:
                    print(r, result.included(), result.allocation())
                result.fix() # make it feasible
                self.filler(result) # fill it
                shaken.add(result) # record it
        k = len(shaken) # how many are there
        if details:
            pl = 's' if k > 1 else ''
            print(f'Shaking with {self.shaker.__name__} yielded {k} alternative{pl}')
            for s in shaken:
                print(s.included())
        missing = self.goal - k # check if there are too few
        if missing > 0: # if so, generate new random solutions 
            shaken |= set([ Solution(self.portfolio) for s in range(missing) ])
            print(f'#added;{missing}', file = self.target)            
        return shaken

    def check(self): # ensure none of the solutions form a Pareto front
        for a in self.front:
            for b in self.front:
                d, e = dominated(a, b)
                assert len(d) == 0 # none should dominate the other

    def assess(self, local, searcher, helper): # combine and prune
        assert len(local) > 0
        curr = self.front if self.front is not None else set()
        result = prune(local | curr)
        if result == self.front:
            self.searchstall += 1
            # losing rank
            self.searchrank[searcher] = max(1, self.searchrank[searcher] // 2)
            self.searchfillrank[helper] = max(1, self.searchfillrank[helper] // 2)            
            if details:
                print(f'The front is stable; stall counter {self.searchstall}/{self.maxsearch}')
            return False # no change
        else:
            k = len(result)
            if k >= 2 * self.goal: # there are too many now
                (self.front, c) = select(result, self.goal)
                print(f'#clust;{c};{len(result)}', file = self.target)
            else:
                self.front = result # no need to cut it down yet
            if details:
                self.check() # used when debugging to make sure none are dominated
            self.searchstall = 0 # reset the counter since the front changed
            # compare against ORIGINAL front 
            adj = round(sum([ score(s, curr) for s in local] )/ len(local))
            if adj > 0: # these heuristics gain rank
                self.searchrank[searcher] += adj
                self.searchfillrank[helper] += adj
                if details:
                    display(self.searchrank, 'Search ranks')
                    display(self.searchfillrank, 'Fill ranks')
            if details:
                print(f'Altered the Pareto front')
                for s in result:
                    print('F', s.included(), ' '.join([ f'{v:.0f}' for v in s.evaluate() ]))
            return True # alteration

    def update(self, altered):
        if self.shaker is None:
            # no shake rank changes when there was no shaking
            return
        if altered > 0:
            self.shakestall = 0 # reset shaking                
            self.shakerank[self.shaker] += altered # gain rank
            self.shakefillrank[self.filler] += altered # gain rank
            if details: 
                display(self.shakerank, 'Shake ranks')
                f = len(self.front)
                pl = 's' if f > 1 else ''
                if self.shaker is not None:
                    print(f'After {self.shaker.__name__}, the front has {f} non-dominated solution{pl}')
                else:
                    print(f'Initialized a front with {f} non-dominated solution{pl}')                
        else: # no front changes occured
            self.shakestall += 1 # stalled, lower ranks
            self.shakerank[self.shaker] = max(1, self.shakerank[self.shaker] // 2)
            self.shakefillrank[self.filler] = max(1, self.shakefillrank[self.filler] // 2)
            if details:
                print(f'Using {self.shaker.__name__} resulted in no front alterations')
 
    def search(self, shaken):
        self.searchstall = 0 # search stall counter resets each stage
        ok = True # whether the time limit is respected
        altered = 0 # how many times the front changes
        for i in range(self.maxitersearch): # permitted iterations
            if time() - self.start > self.limit: 
                if verbose:
                    print('#search;runtime', file = self.target)
                ok = False # no time left
                break
            local = set() # gather the variants here
            searcher = pick(self.searchrank, self.searchusage) # pick a search heuristic
            helper = pick(self.searchfillrank, self.searchusage) # a fill one, too
            if details:
                print(f'Using {searcher.__name__} to search and {helper.__name__} to fill')
            present = len(self.front) if self.front is not None else 0
            repetitions = max(self.goal - present, 1)
            for sol in shaken:
                for r in range(repetitions):                
                    neighbor = searcher(sol) # create an alternative solution
                    neighbor.fix() #  ensure feasibility
                    helper(neighbor) # fill it
                    local.add(neighbor) # record it
            altered += self.assess(local, searcher, helper)
            if self.searchstall == self.maxsearch: # stalled
                print('#search;stall', file = self.target)                
                break
        if self.searchstall < self.maxsearch:
            print('#search;maxiter', file = self.target)
        self.update(altered)
        return ok
        
    def step(self, printout):
        self.search(self.shake())
        if printout: # if output is requested
            self.output()
        progress = self.shakestall < self.maxshake
        if not progress:
            print(f'#shake;stall', file = self.target)
        fast = time() - self.start < self.limit
        return progress and fast # true to continue

    def run(self):
        o = 1
        for i in range(self.maxitershake):
            out = (i + 1) == o
            if out: # output on iterations that are powers of two
                # progress indication print-out
                print(f'Iteration {i + 1} of {self.maxitershake}', file = stderr)
                print(f'w;{i + 1}', file = self.target)
                o *= 2
                if details:
                    k = len(self.front)
                    pl = 's' if k > 1 else ''
                    print(f'Iteration {i+1} starts with {k} non-dominated solution{pl}')
            if not self.step(out):
                self.postprocess(i)
                return
