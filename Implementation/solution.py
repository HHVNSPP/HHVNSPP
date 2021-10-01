from random import random, choice, shuffle
from tools import pick, WORSE, EQUAL, BETTER, UNDEFINED, verbose

# PARETO DOMINANCE

def equal(first, second):
    k = len(first)
    if verbose:
        assert k == len(second)
    for i in range(k):
        if first[i] != second[i]:
            return False
    return True

def notDominated(defendant, opponent):
    n = len(defendant)
    if verbose:
        assert n == len(opponent)
    matches = 0
    improves = False
    for i in range(n):
        if defendant[i] >= opponent[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant[i] > opponent[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return improves and matches == n # defendant is not dominated by opponent


### CREATION OF AN INITIAL SOLUTION

def initial(pf, attempts = 10): # build a random solution for a portfolio
    ok = None
    for attempt in range(attempts):
        ok = True
        available = pf.budget
        a = dict() # fund assignment 
        shuffle(pf.groups) # consider the partitions in random order
        for part in pf.groups: 
            shuffle(part) # consider the subgroups in random order
            for g in part:
                spent = 0
                for p in g.permutation(): # random order
                    if spent > g.lower: # feasible
                        break
                    if available - spent >= p.minimumBudget: # if there are funds left
                        if p.minimumBudget + spent < g.upper: # feasible
                            spent += p.activate(a, p.minimumBudget, level = 0)
                if not (spent >= g.lower and spent <= g.upper):
                    ok = False
                    break # infeasible, try again from the start
                available -= spent
        if ok:
            if verbose:
                print('Initial solution created')
            created = Solution(pf, a)
            assert created.feasible()
            return created
    return None # no feasible initial solution found; the instance may be ill-posed

class Solution():

    def __init__(self, p, a):
        self.portfolio = p
        self.assignment = a

    def __str__(self):
        return f'\nFA {self.portfolio} w/ {self.allocation()} to {len(self.assignment)}' 

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
            gr = sample(self.portfolio.groups, 2)
            other.disactivate(self.select(gr.pop(0))) # exclude
            other.activate(self.select(gr.pop(1), active = False)) #include
            return other
        return self # cannot be done

    def modGroup(self, decr = True):
        subgroup = choice(choice(self.portfolio.groups)) # pick an area or a region
        gr = subgroup.members
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
    
    def randmin(self, level = 0):
        other = Solution(self.portfolio, self.assignment.copy())
        cand = self.actives()
        if len(cand) == 0:
            return self # nothing can be done
        p = choice(cand)
        other.activate(p, level)
        return other

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
        b = self.portfolio.binary
        v = [0] * n
        funded = set()
        for (element, funding) in self.assignment.items():
            funded.add(element.parent)
        for project in funded:
            ei = project.impact(self.assignment, b)
            for i in range(n):
                v[i] += ei[i]
        if verbose:
            print(f'Evaluated an assignment comprising of {len(funded)} projects as {v}')
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

