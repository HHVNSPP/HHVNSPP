from random import shuffle, choice, random, sample
from math import ceil

class Activity():

    def __init__(self, project, imp, maximum, minimum = 0):
        self.parent = project
        self.pot = imp
        self.minBudget = minimum
        self.maxBudget = maximum
        self.diff = self.maxBudget - self.minBudget
        assert self.diff >= 0

    def __str__(self):
        return f'A[{self.minBudget:.0f}, {self.maxBudget:.0f}] = {self.pot}'

    def funding(self, assignment):
        # force all to decimal (some are integers)        
        amount = 1.0 * assignment.get(self, 0) 
        return f'{amount:.0f}' # ignore fractional differences when comparing

    def bounds(self, a):
        amount = a.get(self, 0)
        if amount > 0:
            print(f'A {amount > 0}: {self.minBudget:.0f} <= {amount:.0f} <= {self.maxBudget:.0f}')
    
    def feasible(self, a):
        amount = a.get(self, 0)
        active = amount > 0
        if active: # if funded, check the levels
            return amount >= self.minBudget and amount <= self.maxBudget
        return True # this is inactive
    
    def __repr__(self):
        return str(self)

    def randomize(self, low = None, high = None, integer = False):
        if low is None:
            low = self.minBudget
        if high is None:
            high = self.maxBudget
        span = high - low
        lvl = random() * span + low
        return round(lvl) if integer else lvl
        
    def impact(self, assignment, partial, fraction = 0.3):
        lvl = assignment.get(self, 0)
        if lvl == 0: # no funds, no impact
            return [0 for p in self.pot]
        i = []
        lacking = lvl < self.maxBudget
        if lacking: # partial assigment
            multiple = fraction / self.diff
            excess = lvl - self.minBudget
            base = multiple * excess
        for (pot, part) in zip(self.pot, partial):
            rate = pot # all-or-nothing as default
            if part and lacking:
                rate = base + (1 - fraction) * pot
            i.append(rate) 
        return i

    def disactivate(self, assignment):
        if self in assignment:
            del assignment[self]

    def activate(self, assignment, amount = 0, level = 0):
        current = assignment.get(self, 0)
        if level == 0: # lowest possible funding was requested
            amount = self.minBudget
        elif level == 1: # highest possible funding was requested
            amount = self.maxBudget  
        elif level == 2: # random funding was requested
            amount = self.randomize(current, current + amount)
        amount = min(amount, self.maxBudget)
        amount = max(amount, self.minBudget)
        assignment[self] = amount
        return amount
    
class Project():
    
    def __init__(self, imp, requested, minimum = None, groups = []):
        self.pot = imp
        self.maxBudget = requested
        if minimum is not None:
            assert minimum <= requested
        self.minBudget = minimum if minimum is not None else self.maxBudget
        assert self.minBudget <= self.maxBudget
        self.tasks = list()
        self.groups = groups

    def __str__(self):
        pot = '|'.join([ str(p) for p in self.pot ])
        k = len(self.tasks)
        act = f'({k})' if k > 0 else ''
        r = f'={self.minBudget:.2f}'
        if  self.minBudget < self.maxBudget:        
            r = f'=[{self.minBudget:.2f}, {self.maxBudget:.2f}]'
        return 'P' + r + act + pot

    def assigned(self, assignment):
        return sum([ assignment.get(act, 0) for act in self.tasks ])

    def bounds(self, a):
        if not self.feasible(a):
            t = self.assigned(a)
            print(f'P {t > 0}:  {self.minBudget:.0f} <= {t:.0f} <= {self.maxBudget:.0f}')
            for act in self.tasks:
                act.bounds(a)
    
    def feasible(self, a):
        t = self.assigned(a)
        inactive = t == 0
        if not inactive: # check levels if funded
            if t < self.minBudget or t > self.maxBudget:
                return False
            # check also tasks
            return all ([ act.feasible(a) for act in self.tasks ])
        return True # not active, hence feasible at zero
        
    def underfunded(self, a):
        return self.assigned(a) < self.minBudget

    def overfunded(self, a):
        return self.assigned(a) > self.maxBudget
    
    def funding(self, assignment):
        lvls = [ a.funding(assignment) for a in self.tasks ]
        return '|'.join(lvls)

    def __repr__(self):
        return str(self)
    
    def activate(self, assignment, amount, level = 0):
        current = self.assigned(assignment)
        if amount + current < self.minBudget:
            return 0 # nothing can be done 
        available = amount
        while available > 0:
            ok = False
            for a in self.tasks:
                allocated = a.activate(assignment, available, level)
                if allocated > 0:
                    ok = True
                    available -= allocated
            if not ok: # none of the tasks took any more money
                break
        assigned =  amount - available
        return assigned

    def disactivate(self, assignment):
        for a in self.tasks:
            a.disactivate(assignment)
            
    def impact(self, assignment, partial, fraction = 0.3):
        k = len(self.pot)
        pi = [0] * k
        for a in self.tasks:
            imp = a.impact(assignment, partial, fraction)
            for pos in range(k):
                if partial[pos]:
                    pi[pos] += imp[pos] * self.pot[pos]
                else:
                    pi[pos] = max(pi[pos], 1 * imp[pos])
        return pi
                
    def update(self):
        if len(self.tasks) == 0:
            # one activity = the whole project (in case there were none)
            imp = [ 1 for p in self.pot ] # full impact 
            self.tasks = [ Activity(self, imp, self.maxBudget, self.minBudget) ]
        else: # sort in decreasing order of impact
            self.tasks.sort(key = lambda a: a.pot, reverse = True)
            self.maxBudget = sum([ a.maxBudget for a in self.tasks ])

class Synergy():

    def __init__(self, nombre, technical, value, kind,
                 lowerThreshold, upperThreshold, elementCount, active = False):
        self.nombre = nombre
        self.technical = technical
        self.value = value
        self.kind = kind
        self.lowerThreshold = lowerThreshold
        self.upperThreshold = upperThreshold
        self.elementCount = elementCount
        self.elements = []
        self.active = active

    def include(self, elem):
        self.elements.append(elem)

class Group():

    def __init__(self, l, u):
        self.members = set() 
        self.lower = l # upper bound for total funding
        self.upper = u # lower bound for total funding
        self.order = None

    def include(self, m):
        self.members.add(m)

    def assigned(self, a):
        return sum([ m.assigned(a) for m in self.members ])
    
    def lowerOK(self, a):
        return self.lower is None or self.assigned(a) >= self.lower

    def upperOK(self, a):
        return self.upper is None or self.assigned(a) <= self.upper

    def bounds(self, a):
        if not self.feasible(a):
            print('G: {self.lower:.0f} <= {self.assigned(a):.0f} <= {self.upper:.0f}')
        
    def feasible(self, a):
        t = self.assigned(a)
        p = [ p.feasible(a) for p in self.members ]
        bot = self.lower is None or t >= self.lower
        top = self.upper is None or t <= self.upper
        return all([ bot, top ] + p)

    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = list(self.members)
        shuffle(self.order) # reorder
        return self.order

    def __str__(self):
        return f'G[{self.lower}, {self.upper}] ({len(self.members)})'

    def __repr__(self):
        return str(self)

class Portfolio():

    def __init__(self, total, w, i, p, part = None, s = None):
        self.budget = total
        self.weights = w
        self.impact = i # all-or-nothing (F) / linear (T)
        self.dim = len(w)
        self.projects = p
        for pr in self.projects:
            pr.update() # sort if several, create singleton if none
        self.order = None
        self.partitions = part
        self.groups = list()
        for p in self.partitions: # make a list of the groups for ease of access
            self.groups += p
        self.synergies = s

    def included(self, active):
        return ''.join([ str(1 * (p in active)) for p in self.projects ])

    def funding(self, assignment):
        return '#'.join([ p.funding(assignment) for p in self.projects ])    
        
    def __str__(self):
        return f'PF w/ {len(self.projects)} P & B = {self.budget}'

    def __repr__(self):
        return str(self)
    
    def choice(self):
        return choice(self.projects)

    def sample(self, count):
        if count == 0: # pick a group at random and use that
            partition = choice(self.partitions) # an area or a region
            group = choice(partition) # pick a group within that
            return group.members # the members of that subgroup
        if count < 1: # expressed as a fraction
            count *= len(self.projects)
            count = int(ceil(count)) # an integer (rounded up)
        included = list()
        for i in self.permutation()[:count]:
            included.append(self.projects[i])
        assert len(included) == count
        return included
    
    def random(self):
        chosen = set()
        for p in self.projects:
            if random() < 0.5:
                chosen.add(p)
        return chosen
    
    def lowerOK(self, a):
        for g in self.groups:
            if not g.lowerOK(a):
                return False
        return True

    def upperOK(self, a):
        for g in self.groups:
            if not g.upperOK(a):
                return False
        return True

    def bounds(self, a):
        print(f'I: {sum(a.values())} <= {self.budget}')
        for g in self.groups:
            g.bounds(a)
        for p in self.projects:
            p.bounds(a)
    
    def feasible(self, a):
        assigned = sum(a.values())
        if self.budget < assigned:
            return False
        gOK = all([ g.feasible(a) for g in self.groups ])
        pOK = all([ p.feasible(a) for p in self.projects ])
        return gOK and pOK
    
    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = [ i for i in range(len(self.projects)) ] 
        shuffle(self.order) # reorder
        return self.order
