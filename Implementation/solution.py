import operator
from math import ceil, log
from random import random, choice, shuffle, sample

class Solution():

    def __init__(self, pf, a = None):
        self.portfolio = pf
        self.assignment = a
        if a is None: # not a clone, but a fresh fund assignment 
            self.assignment = dict() 
            for i in self.portfolio.permutation():
                p = self.portfolio.projects[i]
                fund = False
                if len(p.groups) > 0:
                    for g in p.groups:
                        if not g.lowerOK(self.assignment):
                            fund = True
                else: # no groups
                    fund = True        
                if fund and self.fits(p.minBudget):
                    self.activate(p, level = 2)
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
                    self.activate(p, level = 0) # minimal funds
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
    
    def disactivate(self, a):
        if a is not None:
            a.disactivate(self.assignment)
        
    def activate(self, p, amount = None, level = 0):
        if p is not None:
            if amount is None:
                amount = p.maxBudget
            amount = min(amount, self.remaining())
            if level == 0:
                amount = min(amount, p.minBudget)
            if amount > 0:
                p.activate(self.assignment, amount)

    def increment(self, p):
        incr = p.maxBudget - p.assigned(self.assignment)         
        if self.fits(incr):
            ok = False
            for g in p.groups:
                current = g.assigned(self.assignment)
                if current + incr > g.upper:
                    ok = False # would violate upper bound
                    break
            if ok:
                self.activate(p, incr)
    
    def fill(self, level = None, active = False):
        if level is None: # random
            for i in self.portfolio.permutation():
                p = self.portfolio.projects[i]
                self.increment(p)
        elif level < 1: # from cheapest to the most expensive
            cand = self.inactives() if not active else self.actives() 
            opt = [ (p, p.minBudget) for p in cand ]
            opt.sort(key = lambda a: a[1])
            for (p, b) in opt:
                self.increment(p)

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
        selection = set(self.portfolio.sample(count)) \
            if count is not None else self.portfolio.random()
        other = self.clone()
        act = self.actives()
        for p in selection:
            if p not in act: # presently inactive
                other.activate(p, level) # fund it
            else: # presently active
                other.disactivate(p) # unfund it
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
    
