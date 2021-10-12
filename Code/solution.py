import operator
from math import ceil, log, fabs
from random import random, choice, shuffle, sample

MINIMUM = 0
MAXIMUM = 1
RANDOM = 2

# comparing floating-point numbers for equality
# is in general a poor choice; in this scenario,
# we are not interested in tiny changes
def differ(one, another, precision):
    return fabs(one - another) > precision

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
        former = p.assigned(self.assignment)         
        incr = p.maxBudget - former
        if incr > 0 and self.fits(incr):
            if all([ g.assigned(self.assignment) + incr < g.upper for g in p.groups ]):
                if former > 0: # reset funds if any
                    self.disactivate(p)
                self.activate(p, level = level) > former
                    
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
                
    def modify(self, level = MINIMUM, high = True):
        other = self.clone()
        group  = choice(self.portfolio.groups)
        act = self.actives() & group.members
        if len(act) == 0:
            return self # cannot be done
        leaving = choice(list(act)) # this leaves
        amount = leaving.assigned(self.assignment) # how much it had
        other = self.clone()
        other.disactivate(leaving) # unfund
        inact = group.members - act # presently unfunded
        target = None
        for peer in inact:
            if (high and peer.maxBudget > amount) or \
               (not high and peer.minBudget < amount): 
                target = peer
                break
        if target is not None:
            other.activate(target, level)
        return other

    def exchange(self, level = MINIMUM):
        p = choice(self.portfolio.partitions) # areas or regions
        chosen = sample(p, 2) # two groups of the same kind
        losing = chosen[0].members
        act = self.actives() # actives overall
        candidates = act & losing # actives on the losing side
        if len(candidates) == 0:
            return self # cannot be done
        other = self.clone()
        other.disactivate(choice(list(candidates))) # removed
        gaining = chosen[1].members
        candidates = gaining - act # inactives on the gaining side
        if len(candidates) > 0:
            other.activate(choice(list(candidates)), level = level)
        return other
    
    def extreme(self, high = True, active = True):
        candidates = self.inactives() if not active else self.actives()
        if len(candidates) == 0:
            return (None, None) # nothing can be done
        # for the unfunded, we look at the budget; for the funded, we look at the funds assigned
        prices = None
        if active:
            prices = { p: p.assigned(self.assignment) for p in candidates }
        else: # inactive, we use the minimum or the maximum budget
            prices = { p: p.maxBudget if high else p.minBudget for p in candidates }             
        most = max(prices.items(), key = operator.itemgetter(1))[0]
        return (most, prices.get(most, None))

    def dropExtreme(self, high = True):
        (most, price) = self.extreme(high = high)
        if most is None:
            return self # nothing can be done
        alt = self.clone()
        alt.disactivate(most)
        return alt

    def alter(self, level):
        cand = self.actives(aslist = True)
        margin = self.remaining()        
        for target in cand:
            current = target.assigned(self.assignment)
            goal = 0
            if level == MAXIMUM:
                goal = target.maxBudget
            elif level == MINIMUM:
                goal = target.minBudget
            if level == RANDOM or differ(current, goal, 0.1):
                if goal < margin + current: # will be possible to assign
                    alt = self.clone() 
                    alt.disactivate(target) # reset funding
                    alt.activate(target, level = level) # assign funds
                    return alt
        return self # discard the clone, no changes were made

    def fitExtreme(self, high = True, level = MINIMUM):
        other = self.clone()
        (most, price) = self.extreme(high = high, active = False)
        if most is None:
            return self # nothing can be done
        while not other.fits(price):
            cand = self.actives(aslist = True)
            if len(cand) == 0:
                return self # modification unsuccessfull
            other.disactivate(choice(cand))
        other.activate(most, level = level) # it fits now
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
        
    def add(self, level = MINIMUM):
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
    
    def swap(self, count = None, level = MINIMUM):
        selection = None
        if count is None:
            selection = self.portfolio.random()
        else:
            selection = set(self.portfolio.sample(count))
        other = self.clone() # another solution
        exiting = selection & self.actives()
        entering = list(selection - exiting)
        for p in exiting: # liberate funds (these are always the same)
            other.disactivate(p) # unfund 
        shuffle(entering) # fund in random order
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
    