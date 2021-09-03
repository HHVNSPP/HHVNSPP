from random import shuffle, choice, random
from solution import Solution, initial

VERBOSE = True

class Activity():

    def __init__(self, p, imp, maximum, minimum = 0):
        self.impact = imp
        self.minimumBudget = minimum
        self.maximumBudget = maximum
        self.difference = self.maximumBudget - self.minimumBudget
        self.parent = p

    def effect(self, level, fraction = 0.3):
        if level == self.maximumBudget:
            return self.impact                
        else:
            # TO BE DONE: REVISION PENDING, how is the currenty impact of a partially funded activity computed?
            return ((fraction / self.difference) * (level - self.minimumBudget) + (1 - fraction)) * self.impact

class Project():
    
    def __init__(self, imp, requested, minimum = None):
        self.potential = imp
        self.requestedBudget = requested
        self.minimumBudget = minimum
        # one activity = the whole project (in case there were none)        
        self.activities = []

    def activate(self, assignment, amount, l = 0):
        for a in self.activities:
            lvl = min(amount, a.maximumBudget if l == 1 else a.minimumBudget if l == 0 else a.random())
            assignment[a] = lvl
            amount -= lvl
                    
    def disactivate(self, assignment):
        for a in self.activities:
            if a in assignment:
                del assignment[a]
    
    def update(self):
        if len(self.activities) == 0:
            self.activities = [ Activity(1, requested, minimum) ]
        else:
            self.activities.sort(key = lambda a: a.impact, reverse = True)

    def impact(self, assignment):
        if any([a in assignment for a in self.activities]): # at least one activity is funded
            return sum([self.potential * a.effect() for a in self.activities])
        return 0 # no funds, no impact
    
class Synergy():

    def __init__(self, nombre, technical, value, kind, lowerThreshold, upperThreshold, elementCount, active = False):
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

    def __init__(self, l, u, m = []):
        self.members = m
        self.lower = l # upper bound for total funding
        self.upper = u # lower bound for total funding

    def include(self, m):
        self.members.add(m)

    def total(self, assignment):
        return sum([assignment.get(m, 0) for m in self.members])
        
    def lowerOK(self, a):
        return self.lower is None or self.total(a) >= self.lower

    def upperOK(self, a):
        return self.upper is None or self.upper >= self.total(a)

    def OK(self, a):
        t = self.total(a)
        both = (self.lower is None or t >= self.lower) and (self.upper is None or t <= self.upper)
        return both

class Portfolio():

    def __init__(self, b, w, p, g = None, s = None):
        self.budget = b
        self.weights = w
        self.numberOfObjectives = len(w)
        self.projects = p
        self.order = None
        self.groups = g
        self.synergies = s
        if VERBOSE:
            print(f'A portfolio with {len(p)} and a budget of {b} has been created.')

    def choice(self):
        return choice(self.projects)

    def sample(self, count):
        if count == 0: # pick a group at random and use that
            return choice(choice(self.groups)) # an area or a region
        elif count < 1: # expressed as a fraction
            count *= len(self.projects)
            count = round(count) # round to an integer
        return sample(self.projects, count)
    
    def random(self):
        chosen = set()
        for p in self.projects:
            if random() < 0.5:
                chosen.add(p)
        return p
    
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

    def OK(a):
        for g in self.groups:
            if not g.OK(a):
                return False
        return True
    
    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = [ i for i in range(len(self.projects)) ] 
        shuffle(self.order) # reorder
        return self.order

