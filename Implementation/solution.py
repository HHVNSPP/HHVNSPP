from random import random, choice, shuffle, sample
from tools import pick

### CREATION OF AN INITIAL SOLUTION

def initial(pf, attempts = 30): # build a random solution for a portfolio
    ok = None
    for attempt in range(attempts):
        ok = True
        a = dict() # fund assignment 
        shuffle(pf.groups) # randomize order
        for g in pf.groups:
            for p in g.permutation(): # random order
                if g.lowerOK(a):
                    break # assign no more to this subgroup
                if pf.budget - sum(a.values()) >= p.minimumBudget: # if there are funds
                    p.activate(a, p.minimumBudget, level = 0) # try funding
                    if not g.upperOK(a): # cancel if infeasible
                        p.disactivate(a)
            if not g.feasible(a):
                ok = False
                break # infeasible, try again from the start
    if ok:
        created = Solution(pf, a)
        assert created.feasible()
        return created
    print('ERROR: Unable to create a feasible initial solution for', pf)
    return None 

class Solution():

    def adjust(self, attempts = 50): # ensure feasibility
        ok = False
        for attempt in range(attempts):
            ok = True
            shuffle(self.portfolio.groups) # randomize order
            for g in self.portfolio.groups:
                for p in g.permutation(): # random order
                    if not g.lowerOK(self.assignment):
                        self.decrease(g)
                    if not g.upperOK(self.assignment): 
                        self.increase(g)
                if not g.feasible(self.assignment):
                    ok = False
                    break # infeasible, try again from the start
            if self.feasible():
                return
        print('ERROR: Unable turn a solution feasible', self)

    def __hash__(self): # these must be able to go into dictionaries
        return hash(self.portfolio.funding(self.assignment))
        
    def __eq__(self, other): # we do not want duplicate solutions
        return self.assignment == other.assignment
        
    def __init__(self, p, a):
        self.portfolio = p
        self.assignment = a

    def __str__(self):
        incl = self.portfolio.included(self.actives())
        return f'S {incl} w/ {self.allocation():.2f} to {len(self.assignment)}' 

    def __repr__(self):
        return str(self)
    
    def disactivate(self, a):
        if a is not None:
            a.disactivate(self.assignment)
        
    def activate(self, p, level = 0):
        if p is not None:
            amount = min(p.minimumBudget if level == 0 else p.maximumBudget,
                         self.portfolio.budget - self.allocation())
            if amount > 0:
                p.activate(self.assignment, amount)

    def allocation(self):
        return sum(self.assignment.values())
    
    def fill(self, level = None, active = False):
        if level is None: # random
            for i in self.portfolio.permutation():
                self.activate(self.portfolio.projects[i])
        elif level < 1: # from cheapest to the most expensive
            cand = self.inactives() if not active else self.actives() 
            opt = [ (p, p.minimumBudget) for p in cand ]
            opt.sort(key = lambda a: a[1])
            if len(opt) > 1:
                assert opt[0][1] < opt[-1][1] # increasing order
            for (p, b) in opt:
                self.activate(p)

    def select(self, cand, active = True):
        opt = cand & (self.actives() if active else self.inactives())
        chosen = None
        if len(opt) > 0:
            chosen = choice(list(opt))
        return chosen
                
    def alterGroup(self, level = 0):
        if len(self.portfolio.groups) > 1:
            na = self.assignment.copy()
            other = Solution(self.portfolio, na)            
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
        other = Solution(self.portfolio, self.assignment.copy())                    
        for first in entering:
            for second in exiting:
                above = self.allocation() > second.minimumBudget
                if (decr and above) or (not decr and not above):
                    other.disactivate(first)
                    other.activate(second)
                    return other
        return self # was not possible to perform
    
    def extreme(self, high = True, active = True):
        prices = {p:  p.minimumBudget for p in (self.inactives() if not active else self.actives())}
        if len(prices) == 0: # no candidates
            return (None, None)
        most = pick(prices, high)
        return (most, prices.get(most, None))

    def dropExtreme(self, high = True):
        (most, price) = self.extreme(high = high)
        if most is None:
            return self # nothing can be done
        alt = Solution(self.portfolio, self.assignment.copy())
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
        alt = Solution(self.portfolio, self.assignment.copy())
        alt.disactivate(target) # reset funding
        alt.activate(target, level = 2) # set a random level
        return alt

    def fitExtreme(self, high = True):
        other = Solution(self.portfolio, self.assignment.copy())        
        (most, price) = self.extreme(high = high, active = False)
        if most is None:
            return self # nothing can be done
        while self.portfolio.budget < other.allocation() + price:
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
        other = Solution(self.portfolio, self.assignment.copy())
        cand = self.inactives(aslist = True)
        if len(cand) == 0:
            return self # nothing can be done
        p = choice(cand)
        if other.allocation() + p.minimumBudget <= self.portfolio.budget:
            other.activate(p, level = level)
        return other

    def remove(self):
        other = Solution(self.portfolio, self.assignment.copy())
        cand = self.actives(aslist = True)
        if len(cand) == 0:
            return self # nothing can be done
        p = choice(cand)
        other.disactivate(p)
        return other
    
    def swap(self, count = None, level = 0):
        selection = set(self.portfolio.sample(count)) if count is not None else self.portfolio.random()
        other = Solution(self.portfolio, self.assignment.copy())
        for p in selection:
            present = False
            for a in p.activities:
                if a in self.assignment: 
                    present = True
                    break
            if not present: # presently inactive
                other.activate(p, level) 
            else: # presently active
                other.disactivate(p) 
        return other 
    
    def choice(self): # return a random project
        return self.portfolio.choice()
        
    def evaluate(self):
        n = self.portfolio.numberOfObjectives
        partial = self.portfolio.impact
        v = [0] * n
        funded = set()
        for (element, funding) in self.assignment.items():
            funded.add(element.parent)
        for project in funded:
            ei = project.impact(self.assignment, partial)
            assert len(ei) == n
            for i in range(n):
                v[i] += ei[i]
        return v
        
    def feasible(self):
        return self.portfolio.feasible(self.assignment)
    
    def increase(self, gr):
        p = self.select(gr.members, active = False)
        if p is not None:
            self.activate(p, level)

    def decrease(self, gr):
        p = self.select(gr.members)        
        if p is not None:
            self.disactivate(p)

