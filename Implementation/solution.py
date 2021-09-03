from random import random, choice

VERBOSE = True

def initial(pf): # build a random solution for a portfolio
    a = dict() # fund assignment 
    if len(pf.groups) == 1: # no areas or regions (instance set B)
        for p in pf.projects:
            if random() < 0.5: # each project has a 50-50 chance of activation
                a[p] = p.minimumBudget # fully funded
    else:
        for i in pf.permutation(): # iterate over the projects in random order
            p = pf.projects[i]
            lvl = p.minimumBudget # funds minimum
            ok = True
            for g in pr.groups: # check if the bounds are not yet violated
                if p in g:
                    if not g.OK():
                        ok = False
                        break
            if ok and lvl >= b: # funds remaining
                p.activate(a, lvl)
    if VERBOSE:
        print('Initial solution created')
    return Solution(pf, a)

def notDominated(defendant, opponent, n):
    matches = 0
    improves = False
    for i in range(n):
        if defendant.impact[i] >= opponent.impact[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant.impact[i] > opponent.impact[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return improves and matches == n # defendant is not dominated by opponent

EQUAL = 2
BETTER = -1
WORSE = 1
UNDEFINED = 0

class Solution():

    def __init__(self, p, a):
        self.portfolio = p
        self.assignment = a

    def disactivate(self, p):
        if p is not None:
            p.disactivate(self.assignment)
        
    def activate(self, p, level = 0, enforce = True):
        if p is not None:
            amount = p.minimumBudget if level == 0 else p.maximumBudget
            if not enforce or sum(self.assignment.values() + amount <= self.portfolio.budget):
                p.activate(self.assignment, amount)

    def fill(self, random = True):
        if random:
            for i in self.portfolio.permutation():
                self.activate(self.portfolio.projects[i])
        else: # from cheapest to the most expensive
            opt = [(p, p.minimumBudget) for p in (self.inactives() if not active else self.actives())]
            opt.sort(key = lambda a: a[1])
            assert opt[0] < opt[-1] # increasing order
            for p in opt:
                self.activate(p)

    def pick(self, cand, active = True):
        opt = cand & (self.active() if active else self.inactive())
        if len(opt) > 0:
            return choice(list(opt))
        return None
                
    def alterGroup(self):
        if len(self.portfolio.groups) > 1:
            na = self.assignment.copy()
            other = Solution(self.portfolio, na)            
            gr = sample(self.portfolio.groups, 2)
            other.disactivate(self.pick(gr.pop(0))) # exclude
            other.activate(self.pick(gr.pop(1), active = False)) #include
            return other
        return sol # cannot be done

    def modGroup(self, decr = True):
        gr = choice(choice(self.portfolio.groups)) # pick an area or a region
        act = self.active()
        exiting = list(act & gr)
        entering = list((self.portfolio.projects - act) & gr)
        na = self.assignment.copy()
        other = Solution(self.portfolio, na)                    
        for first in entering:
            for second in exiting:
                above = self.allocation() > second.minimumBudget
                if (decr and above) or (not decr and not above):
                    na.activate(second)
                    na.disactivate(first)
                    return other
        return self # was not possible to perform
    
    def randmin(self):
        other = Solution(self.portfolio, na)
        p = choice(self.active())
        other.activate(p)
        return other

    def extreme(self, high = True, active = True):
        prices = {p:  p.minimumBudget for p in (self.inactives() if not active else self.actives())}
        most = max(prices.items(), key = operator.itemgetter(1))[0] if high else min(prices.items(), key = operator.itemgetter(1))[0] 
        return (most, prices[most])

    def dropExtreme(self, high = True):
        na = self.assignment.copy()
        (most, price) = self.extreme(high = high)        
        del na[most]
        return Solution(self.portfolio, na)

    def fitExtreme(self, high = True):
        na = self.assignment.copy()
        other = Solution(self.portfolio, na)        
        (most, price) = self.extreme(high = high, active = False)
        while self.portfolio.budget < sum(na.values()) + price:
            cand = self.active()
            if len(cand) == 0:
                return self # modification unsuccessfull
            other.disactivate(choice(self.active()))
        na[most] = price # it fits now
        return other

    def active(self):
        return set(self.assignment.keys())

    def inactive(self):
        return set(self.portfolio.projects) - self.active()
        
    def add(self):
        na = self.assignment.copy()
        other = Solution(self.portfolio, na)
        p = choice(self.inactive())
        if sum(na.values() + p.minimumBudget <= self.portfolio.budget):
            other.activate(p)
        return other

    def remove(self, fill = True):
        na = self.assignment.copy()
        p = choice(self.active)
        other = Solution(self.portfolio, na)
        other.disactivate(p)
        return other.fill()
    
    def swap(self, count = None):
        na = self.assignment.copy()
        selection = { self.portfolio.sample(count) } if count is not None else self.portfolio.random()
        other = Solution(self.portfolio, na)
        for p in selection:
            present = False
            for a in p.activities:
                if a in self.assignment: 
                    present = True
                    break
            if not present: # presently inactive
                if sum(na.values() + p.minimumBudget <= self.portfolio.budget):                
                    other.activate(p) 
            else: # presently active
                other.disactivate(p) 
        return other # note that these may be infeasible
    
    def choice(self): # return a random project
        return self.portfolio.choice()
        
    def evaluate(self):
        obj = [0] * self.portfolio.numberOfObjectives
        for element in self.assignment:
            for o in range(self.portfolio.numberOfObjectives):
                obj[o] += element.impact()
        return obj
        
    def equal(self, another):
        for i in range(self.n):
            if (self.objectiveFunction[i] != another.objectiveFunction[i]):
                return False
        return True

    def compare(self, another):
        if self.equal(another):
            return EQUAL
        elif notDominated(self, another):
            return BETTER
        elif notDominated(another, self):
            return WORSE
        return UNDEFINED
        
    def OK(self):
        for g in self.portfolio.groups:
            for m in g:
                if not m.OK(self.assignment):
                    return False
        return True
    
    def feasible(self):
        while not self.OK():
            for g in self.portfolio.groups:
                for m in g:
                    if not m.lowerOK(self.assignment):
                        self.increase(m)
                    elif not m.upperOK(self.assignment):
                        self.decrease(m)

    def increase(self, gr):
        p = self.pick(gr.members, active = False)
        if p is not None:
            self.activate(p)


    def decrease(self, gr):
        p = self.pick(gr.members)        
        if  p is not None:
            self.disactivate(p)
