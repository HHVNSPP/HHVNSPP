import operator
from math import ceil, log
from random import random, choice, shuffle, sample

MINIMUM = 0
MAXIMUM = 1
RANDOM = 1

class Solution():

    def __init__(self, pf, a = None):
        self.portfolio = pf
        self.assignment = a
        if a is None: # not a clone, but a fresh fund assignment 
            self.assignment = dict() 
            for i in self.portfolio.permutation():
                p = self.portfolio.projects[i]
                fund = [ not g.lowerOK(self.assignment) for g in p.groups ]
                if len(fund) == 0 or any(fund): # if a group lacks funds or there is no group
                    if self.fits(p.minBudget): # if there are funds
                        self.activate(p, level = RANDOM)
            if not self.fix(): # ensure feasability
                print('ERROR: unable to create a feasible initial solution')
                self.bounds() # diagnose

    def included(self):
        return self.portfolio.included(self.actives())
                
    def __str__(self):
        return self.portfolio.funding(self.assignment)

    def __repr__(self):
        return str(self)

    def fix(self): # ensure feasibility
        permitted = len(self.portfolio.projects)
        permitted *= len(self.portfolio.groups) + 1
        for attempt in range(permitted):
            if self.feasible():
                return True
            remove = self.remaining() < 0
            for i in self.portfolio.permutation(): # random order
                p = self.portfolio.projects[i]
                if p.assigned(self.assignment) > 0: # has funds
                    top = [ True ] + [ g.upperOK(self.assignment) for g in p.groups ]
                    if remove or not all(top): # at least one group has excess
                        self.disactivate(p) # unfund
                        remove = self.remaining() < 0                        
                        continue
                bot = [ True ] + [ g.lowerOK(self.assignment) for g in p.groups ]
                if not all(bot): # at least one group needs more
                    self.activate(p, level = MINIMUM) # minimal funds
        self.bounds()
        return False # unable to fix

    def clone(self):
        return Solution(self.portfolio, self.assignment.copy())

    def __hash__(self): # these must be able to go into dictionaries
        return hash(str(self))
        
    def __eq__(self, other): # we do not want duplicate solutions
        return self.assignment == other.assignment
    
    def allocation(self):
        return sum(self.assignment.values())

    def remaining(self):
        return self.portfolio.budget - self.allocation()

    def fits(self, amount):
        return self.remaining() >= amount
    
    def disactivate(self, p):
        p.disactivate(self.assignment)
        
    def activate(self, p, level = MINIMUM, amount = None):
        if amount is None:
            amount = p.maxBudget
        amount = min(amount, self.remaining())
        if level == MINIMUM:
            amount = min(amount, p.minBudget)
        if amount > 0:
            return p.activate(self.assignment, amount, level = level)
        return 0

    def increment(self, p, level):
        current = p.assigned(self.assignment)         
        incr = p.maxBudget - current
        if incr > 0 and self.fits(incr):
            if all([ g.assigned(self.assignment) + incr < g.upper for g in p.groups ]):
                if current > 0:
                    self.disactivate(p) # reset funds
                self.activate(p, level = level) # fund
                    
    def fill(self, level = None, active = False, sort = False):
        cand = self.inactives() if not active else self.actives() 
        if sort:
            opt = [ (p, p.minBudget) for p in cand ]
            opt.sort(key = lambda a: a[1])
            cand = [ p for (p, b) in opt ]
        else:
            cand = list(cand)
            shuffle(cand)
        for p in cand:
            self.increment(p, level = level)

    def select(self, cand, active = True):
        opt = cand & (self.actives() if active else self.inactives())
        chosen = None
        if len(opt) > 0:
            chosen = choice(list(opt))
        return chosen
                
    def alterGroup(self, level = 0):
        if len(self.portfolio.groups) > 1:
            other = self.clone()
            gr = sample(self.portfolio.groups, 2) # any two groups
            other.disactivate(self.select(gr[0].members)) # exclude
            other.activate(self.select(gr[1].members, active = False)) #include
            return other
        return self # cannot be done

    def modGroup(self, decr = True):
        p = choice(choice(self.portfolio.partitions)) # areas or regions
        gr = p.members
        act = self.actives()
        exiting = list(act & gr)
        ia = set(self.portfolio.projects) - act
        entering = list(ia & gr)
        other = self.clone()
        for first in entering:
            for second in exiting:
                above = self.allocation() > second.minBudget
                if (decr and above) or (not decr and not above):
                    other.disactivate(first)
                    other.activate(second)
                    return other
        return self # was not possible to perform
    
    def extreme(self, high = True, active = True):
        prices = {p:  p.minBudget for p in (self.inactives() \
                                            if not active else self.actives())}
        if len(prices) == 0: # no candidates
            return (None, None)
        most = max(prices.items(), key = operator.itemgetter(1))[0]
        return (most, prices.get(most, None))

    def dropExtreme(self, high = True):
        (most, price) = self.extreme(high = high)
        if most is None:
            return self # nothing can be done
        alt = self.clone()
        alt.disactivate(most)
        return alt
    
    def rand(self, level = 0):
        target = None
        if level != -1:
            (target, price) = self.extreme(high = (level == 1))
        else: # random one
            cand = self.actives(aslist = True)
            if len(cand) > 0:
                target = choice(cand)
        if target is None:
            return self # nothing can be done            
        alt = self.clone()
        alt.disactivate(target) # reset funding
        alt.activate(target, level = 2) # set a random level
        return alt

    def fitExtreme(self, high = True):
        other = self.clone()
        (most, price) = self.extreme(high = high, active = False)
        if most is None:
            return self # nothing can be done
        while not other.fits(price):
            cand = self.actives(aslist = True)
            if len(cand) == 0:
                return self # modification unsuccessfull
            other.disactivate(choice(cand))
        other.activate(most, price) # it fits now
        return other

    def actives(self, aslist = False):
        act = [a.parent for a in self.assignment.keys()]
        if aslist:
            return act
        else:
            return set(act)

    def inactives(self, aslist = False):
        if aslist:
            return list(set(self.portfolio.projects) - self.actives())
        else:
            return set(self.portfolio.projects) - self.actives()
        
    def add(self, level = 0):
        other = self.clone()
        cand = self.inactives(aslist = True)
        if len(cand) == 0:
            return self # nothing can be done
        p = choice(cand)
        if other.fits(p.minBudget):
            other.activate(p, level = level)
        return other

    def remove(self):
        other = self.clone()
        cand = self.actives(aslist = True)
        if len(cand) == 0:
            return self # nothing can be done
        p = choice(cand)
        other.disactivate(p)
        return other
    
    def swap(self, count = None, level = 0):
        selection = None
        if count is not None and count < 1: # swap all
            selection = set(self.portfolio.projects)
        else: # swap some
            selection = set(self.portfolio.sample(count)) \
                if count is not None else self.portfolio.random()
        other = self.clone() # another solution
        exiting = selection & self.actives()
        entering = list(selection - exiting)
        shuffle(entering) # in random order
        for p in exiting: # liberate funds
            other.disactivate(p) # unfund 
        for p in entering:
            other.activate(p, level)
        return other 
    
    def choice(self): # return a random project
        return self.portfolio.choice()
        
    def evaluate(self):
        n = self.portfolio.dim
        partial = self.portfolio.impact
        v = [0] * n
        funded = set()
        for (element, funding) in self.assignment.items():
            project = element.parent
            funded.add(project)
        for project in funded:
            ei = project.impact(self.assignment, partial)
            for i in range(n):
                v[i] += ei[i]
        return v

    def bounds(self):
        self.portfolio.bounds(self.assignment)
        quit() # this is diagnostic info
    
    def feasible(self):
        return self.portfolio.feasible(self.assignment)
    
