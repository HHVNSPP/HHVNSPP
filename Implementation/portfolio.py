from random import shuffle, choice, random, sample

class Activity():

    def __init__(self, project, imp, maximum, minimum = 0):
        self.parent = project
        self.potential = imp
        self.minimumBudget = minimum
        self.maximumBudget = maximum
        self.diff = self.maximumBudget - self.minimumBudget
        assert self.diff >= 0

    def __str__(self):
        return f'A[{self.minimumBudget:.0}, {self.maximumBudget:.0}] = {self.potential}'

    def funding(self, assignment):
        amount = 1.0 * assignment.get(self, 0) # force all to decimal (some are integers)
        return f'{amount:.0}' # ignore fractional differences

    def feasible(self, a):
        amount = a.get(self, 0)
        return amount >= self.minimumBudget and amount <= self.maximumBudget
    
    def __repr__(self):
        return str(self)

    def randomize(self):
        return self.minimumBudget + random() * (self.maximumBudget - self.minimumBudget)
        
    def impact(self, assignment, partial, fraction = 0.3):
        lvl = assignment.get(self, 0)
        if lvl == 0: # no funds, no impact
            return [0 for p in self.potential]
        assert lvl >= self.minimumBudget
        assert lvl <= self.maximumBudget
        i = []
        for (pot, part) in zip(self.potential, partial):
            rate = pot
            if part and lvl < self.maximumBudget:
                multiple = (fraction / self.diff)
                excess = lvl - self.minimumBudget
                base = (1 - fraction) * pot
                rate = multiple * excess + base
            i.append(rate) 
        return i

    def disactivate(self, assignment):
        if self in assignment:
            del assignment[self]

    def activate(self, assignment, amount, level = 0):
        if amount < self.minimumBudget:
            return 0 # nothing can be assigned
        if level == 0:
            lvl = self.minimumBudget
        elif level == 1:
            lvl = min(amount, self.maximumBudget) # as much as we afford
        elif level == 2:
            lvl = self.randomize(amount)
        assert lvl >= self.minimumBudget
        assert lvl <= self.maximumBudget
        assignment[self] = lvl
        return lvl
    
class Project():
    
    def __init__(self, imp, requested, minimum = None):
        self.potential = imp
        self.maximumBudget = requested
        if minimum is not None:
            assert minimum <= requested
        self.minimumBudget = minimum if minimum is not None else self.maximumBudget
        assert self.minimumBudget <= self.maximumBudget
        self.activities = list()

    def __str__(self):
        pot = '|'.join([ str(p) for p in self.potential ])
        k = len(self.activities)
        act = f'({k})' if k > 0 else ''
        r = f'={self.minimumBudget}'
        if  self.minimumBudget < self.maximumBudget:        
            r = f'=[{self.minimumBudget}, {self.maximumBudget}]'
        return 'P' + r + act + pot

    def assigned(self, a):
        return sum([ a.get(act, 0) for act in self.activities ])

    def feasible(self, a):
        t = self.assigned(a)
        if t < self.minimumBudget or t > self.maximumBudget:
            return False
        return all ([ act.feasible(a) for act in self.activities ])

    def funding(self, assignment):
        return ''.join([ a.funding(assignment) for a in self.activities ])        

    def __repr__(self):
        return str(self)
    
    def activate(self, assignment, amount, level = 0):
        spent = 0
        for a in self.activities:
            spent += a.activate(assignment, amount - spent, level)
        return spent

    def disactivate(self, assignment):
        for a in self.activities:
            a.disactivate(assignment)
            
    def impact(self, assignment, partial, fraction = 0.3):
        k = len(self.potential)
        assert len(partial) == k
        pi = [0] * k
        for a in self.activities:
            imp = a.impact(assignment, partial, fraction)
            for pos in range(k):
                if partial[pos]:
                    pi[pos] += imp[pos] * self.potential[pos]
                else:
                    pi[pos] = max(pi[pos], 1 * (imp[pos] > 0))
        return pi
                
    def update(self):
        if len(self.activities) == 0:
            # one activity = the whole project (in case there were none)
            imp = [ 1 for p in self.potential ] # full impact since it is a singleton task
            self.activities = [ Activity(self, imp, self.maximumBudget, self.minimumBudget) ]
        else: # sort in decreasing order of impact
            self.activities.sort(key = lambda a: a.potential, reverse = True)
            self.maximumBudget = sum([ a.maximumBudget for a in self.activities ])

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
        return sum([m.assigned(a) for m in self.members])
    
    def lowerOK(self, a):
        return self.lower is None or self.assigned(a) >= self.lower

    def upperOK(self, a):
        return self.upper is None or self.assigned(a) <= self.upper
        
    def feasible(self, a):
        t = self.assigned(a)
        p = [ p.feasible(a) for p in self.members ]
        return [ self.lower is None or t >= self.lower, self.upper is None or t <= self.upper, all(p) ]

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
        self.impact = i # false if all-or-nothing, true if partial assignment affects it
        self.numberOfObjectives = len(w)
        assert len(self.impact) == self.numberOfObjectives
        self.projects = p
        for pr in self.projects:
            pr.update() # sort the activities if several, create singleton if none
            assert len(pr.potential) == self.numberOfObjectives
            for act in pr.activities:
                assert len(pr.potential) == self.numberOfObjectives                
        self.order = None
        self.partitions = part
        self.groups = list()
        for p in self.partitions:
            for g in p:
                self.groups.append(g)
                for pr in g.members:
                    assert pr in self.projects
        self.synergies = s

    def included(self, active):
        return ''.join([ str(1 * (p in active)) for p in self.projects ])

    def funding(self, assignment):
        return ''.join([ p.funding(assignment) for p in self.projects ])    
        
    def __str__(self):
        return f'PF w/ {len(self.projects)} P & B = {self.budget}'

    def __repr__(self):
        return str(self)
    
    def choice(self):
        return choice(self.projects)

    def sample(self, count):
        if count == 0: # pick a group at random and use that
            partition = choice(self.partitions) # an area or a region
            group = choice(partition)
            return group.members # the member or that subgroup
        elif count < 1: # expressed as a fraction
            count *= len(self.projects)
            count = round(count) # round to an integer
        return sample(self.projects, count)
    
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

    def feasible(self, a):
        assigned = sum(a.values())
        if self.budget < assigned:
            return False
        return all([ g.feasible(a) for g in self.groups ])
    
    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = [ i for i in range(len(self.projects)) ] 
        shuffle(self.order) # reorder
        return self.order
