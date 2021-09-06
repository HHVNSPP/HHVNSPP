from random import random, choice

VERBOSE = False

# PARETO DOMINANCE

def equal(first, second):
    k = len(first)
    if VERBOSE:
        assert k == len(second)
    for i in range(k):
        if first[i] != second[i]:
            return False
    return True

def notDominated(defendant, opponent):
    n = len(defendant)
    if VERBOSE:
        assert n == len(opponent)
    matches = 0
    improves = False
    for i in range(n):
        if defendant[i] >= opponent[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant[i] > opponent[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return improves and matches == n # defendant is not dominated by opponent

EQUAL = 2
BETTER = -1
WORSE = 1
UNDEFINED = 0

### CREATION OF AN INITIAL SOLUTION

def initial(pf): # build a random solution for a portfolio
    a = dict() # fund assignment 
    if len(pf.groups) == 1: # no areas or regions (instance set B)
        for p in pf.projects:
            if random() < 0.5: # each project has a 50-50 chance of activation
                p.activate(a, p.minimumBudget)
    else:
        for i in pf.permutation(): # iterate over the projects in random order
            p = pf.projects[i]
            lvl = p.minimumBudget # funds minimum
            ok = True
            if VERBOSE:
                print(f'Considering {len(pf.groups)} types of groups')
            for gt in pf.groups: # check if the bounds are not yet violated
                if VERBOSE:
                    print(f'Considering a group type with {len(gt)} groups')
                    for g in gt:
                        if VERBOSE:
                            print(f'Considering a group of {len(g.members)} members')
                            if p in g.members:
                                if not g.OK(a):
                                    ok = False
                                    break
            if ok and lvl >= pf.budget: # funds remaining
                p.activate(a, lvl)
    if VERBOSE:
        print('Initial solution created')
    created = Solution(pf, a)
    created.feasible() # make it feasible
    return created

class Solution():

    def __init__(self, p, a):
        self.portfolio = p
        self.assignment = a

    def __str__(self):
        return f'\nFA {self.portfolio} w/ {sum(self.assignment.values())} to {len(self.assignment)}' 

    def __repr__(self):
        return str(self)
    
    def disactivate(self, p):
        if p is not None:
            p.disactivate(self.assignment)
        
    def activate(self, p, level = 0, enforce = True):
        if p is not None:
            amount = p.minimumBudget if level == 0 else p.maximumBudget
            if not enforce or sum(self.assignment.values()) + amount <= self.portfolio.budget:
                p.activate(self.assignment, amount)

    def fill(self, level = None):
        if level is None: # random
            for i in self.portfolio.permutation():
                self.activate(self.portfolio.projects[i])
        elif level < 1: # from cheapest to the most expensive
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
        if sum(na.values()) + p.minimumBudget <= self.portfolio.budget:
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
        selection = set(self.portfolio.sample(count)) if count is not None else self.portfolio.random()
        other = Solution(self.portfolio, na)
        for p in selection:
            present = False
            for a in p.activities:
                if a in self.assignment: 
                    present = True
                    break
            if not present: # presently inactive
                if sum(na.values()) + p.minimumBudget <= self.portfolio.budget:                
                    other.activate(p) 
            else: # presently active
                other.disactivate(p) 
        return other # note that these may be infeasible
    
    def choice(self): # return a random project
        return self.portfolio.choice()
        
    def evaluate(self):
        n = self.portfolio.numberOfObjectives
        v = [0] * n
        for (element, funding) in self.assignment.items():
            ei = element.impact(funding)
            for i in range(n):
                v[i] += ei[i]
        if VERBOSE:
            print(f'Evaluated an assignment comprising of {len(self.assignment)} targets as {v}')
        return v

    def compare(self, another):
        se = self.evaluate()
        ae = another.evaluate()
        if equal(se, ae):
            return EQUAL
        elif notDominated(se, ae):
            return BETTER
        elif notDominated(ae, se):
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
            for gl in self.portfolio.groups:
                for g in gl:
                    print(g)
                    bounds = g.OK(self.assignment)
                    if not bounds[LOWER]:
                        self.increase(g)
                    elif not bounds[UPPER]:
                        self.decrease(g)

    def increase(self, gr):
        if VERBOSE:
            print('Increasing')
        p = self.pick(gr.members, active = False)
        if p is not None:
            self.activate(p)

    def decrease(self, gr):
        if VERBOSE:
            print('Decreasing')        
        p = self.pick(gr.members)        
        if  p is not None:
            self.disactivate(p)

    def makeFeasible(self, amount):
        for p in self.portfolio.projects:
            for act in p.activities:
                if value < act.minimumBudget:
                    if act.assignedBudget < act.maximumBudget: # not fully funded
                        act.funding(uniform(act.assignedBudget, act.maximumBudget))
                        level = act.assignedBudget # what actually got assigned
                        amount -= level # that is no longer available
                        self.assignedBudget += level # it has been assigned to this project
       
    def update(self):
        for act in self.activities:
            self.assignedBudget += act.assignedBudget
        # TO BE DONE: revision pending, is the below functionality the intended one?
        if self.requestedBudget < self.minimumBudget: # if the funding is not yet sufficient
            self.makeFeasible(self.assignedBudget) # reallocate the funds in a feasible way at activity level

