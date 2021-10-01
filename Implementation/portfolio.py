from tools import verbose
from random import shuffle, choice, random, sample

class Activity():

    def __init__(self, p, imp, maximum, minimum = 0):
        self.potential = imp
        self.minimumBudget = minimum
        self.maximumBudget = maximum
        self.diff = self.maximumBudget - self.minimumBudget
        assert self.diff >= 0
        self.parent = p

    def __str__(self):
        return f'\nA[{self.minimumBudget}, {self.maximumBudget}] = {self.potential}'

    def __repr__(self):
        return str(self)

    def randomize(self):
        return self.minimumBudget + random() * (self.maximumBudget - self.minimumBudget)
        
    def impact(self, assignment, binary, fr = 0.3):
        lvl = assignment.get(self, 0)
        if lvl == 0: # no funds, no impact
            return [0 for p in self.parent.potential]
        assert lvl >= self.minimumBudget
        assert lvl <= self.maximumBudget
        rate = self.potential
        if lvl < self.maximumBudget: 
            rate = (fr / self.diff) * (lvl - self.minimumBudget) + (1 - fr) * self.potential
        i = []
        for (p, b) in zip(self.parent.potential, binary):
            if b:
                i.append(p) # yes or no
            else:
                i.append(rate * p) # partial benefit
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
        self.activities = [ ]

    def __str__(self):
        return f'\nP[{self.minimumBudget}, {self.maximumBudget}] ({len(self.activities)})'

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
            
    def impact(self, assignment, binary, fr = 0.3):
        pi = None
        for a in self.activities:
            if pi is None: # the first is places as is
                pi = a.impact(assignment, binary, fr)
            else:
                ia = a.impact(assignment, binary, fr)
                # binary objectives are yes/no, the others accumulate
                contrib = [ (not b) * 1 * v for (v, b) in zip(ia, binary) ]
                pi = [ p + c for (p, c) in zip(pi, contrib) ]
        return pi
                
    def update(self):
        if len(self.activities) == 0:
            # one activity = the whole project (in case there were none)        
            self.activities = [ Activity(self, 1, self.maximumBudget, self.minimumBudget) ]
        else: # sort in decreasing order of impact
            self.activities.sort(key = lambda a: a.potential, reverse = True)
        self.maximumBudget = sum([ a.maximumBudget for a in self.activities ])
        if verbose:
            print(f'A project with {len(self.activities)} activities is ready:',
                  ''.join([str(a) for a in self.activities]))

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

    def __init__(self, l, u, m = set()):
        self.members = m
        self.lower = l # upper bound for total funding
        self.upper = u # lower bound for total funding
        self.order = None

    def include(self, m):
        self.members.add(m)
        
    def feasible(self, a):
        t = sum([a.get(m, 0) for m in self.members])
        if verbose:
            print(f'Goal: {self.lower} <= {t:.0f} <= {self.upper}')
        return [ self.lower is None or t >= self.lower, self.upper is None or t <= self.upper ]

    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = list(self.members)
        shuffle(self.order) # reorder
        return self.order
    
class Portfolio():

    def __init__(self, total, w, b, p, g = None, s = None):
        self.budget = total
        self.weights = w
        self.binary = b
        self.numberOfObjectives = len(w)
        self.projects = p
        self.order = None
        self.groups = g
        self.synergies = s
        for pr in self.projects:
            pr.update() # sort the activities in each project

    def __str__(self):
        return f'\nPF w/ {len(self.projects)} P & B = {self.budget}'

    def __repr__(self):
        return str(self)
    
    def choice(self):
        return choice(self.projects)

    def sample(self, count):
        if count == 0: # pick a group at random and use that
            partition = choice(self.groups) # an area or a region
            subgroup = choice(partition)
            return subgroup.members # the member or that subgroup
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
        for part in self.groups: # check each partition
            for g in part:
                if not g.feasible(a): # check each subgroup
                    return False
        return True
    
    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = [ i for i in range(len(self.projects)) ] 
        shuffle(self.order) # reorder
        return self.order

