from random import shuffle, choice, random, sample

VERBOSE = False

class Activity():

    def __init__(self, p, imp, maximum, minimum = 0):
        self.potential = imp
        self.minimumBudget = minimum
        self.maximumBudget = maximum
        self.diff = self.maximumBudget - self.minimumBudget
        self.parent = p

    def __str__(self):
        return f'\nA[{self.minimumBudget}, {self.maximumBudget}] = {self.potential}'

    def __repr__(self):
        return str(self)

    def activate(self, assignment, level, incr, available = None):
        amount = self.minimumBudget # level 0, default
        if level == 1:
            amount = self.maximumBudget
        elif level == None: 
            amount = self.random(assignment.get(a, 0)) if incr else self.random()
        if available is not None and available < amount: 
            amount = available # if bounded by availability
        assignment[self] = amount
        return amount         

    def disactivate(self, assignment):
        if self in assignment:
            del assignment[self]
    
    def impact(self, lvl, fr = 0.3):
        rate = self.potential
        if lvl < self.maximumBudget: # TO BE DONE: revision pending for partial impact
            rate = (fr / self.diff) * (lvl - self.minimumBudget) + (1 - fr) * self.potential
        return [rate * p for p in self.parent.potential]

    def random(self, curr = None):
        if self.diff > 0:
            low = self.minimumBudget if curr is None else curr
            return random(low, self.maximumBudget)
        return self.maximumBudget # no partial assignment possible

class Project():
    
    def __init__(self, imp, requested, minimum = None):
        self.potential = imp
        self.requestedBudget = requested
        if minimum is not None:
            assert minimum <= requested
        self.minimumBudget = minimum if minimum is not None else self.requestedBudget
        self.activities = [ ]

    def __str__(self):
        return f'\nP[{self.minimumBudget}, {self.requestedBudget}] ({len(self.activities)})'

    def __repr__(self):
        return str(self)
    
    def activate(self, assignment, level = 0, incr = False, available = None):
        for a in self.activities:
            assigned = a.activate(assignment, level, incr, available)
            if available is not None:
                available -= assigned
            
    def disactivate(self, assignment):
        for a in self.activities:
            a.disactivate(assignment)
    
    def update(self):
        if len(self.activities) == 0:
            # one activity = the whole project (in case there were none)        
            self.activities = [ Activity(self, 1, requested, minimum) ]
        else: # sort in decreasing order of impact
            self.activities.sort(key = lambda a: a.potential, reverse = True)
        if VERBOSE:
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

    def include(self, m):
        self.members.add(m)
        
    def OK(self, a):
        t = sum([a.get(m, 0) for m in self.members])
        if VERBOSE:
            print(f'Goal: {self.lower} <= {t:.0f} <= {self.upper}')
        return [ self.lower is None or t >= self.lower, self.upper is None or t <= self.upper ]

class Portfolio():

    def __init__(self, b, w, p, g = None, s = None):
        self.budget = b
        self.weights = w
        self.numberOfObjectives = len(w)
        self.projects = p
        self.order = None
        self.groups = g
        self.synergies = s
        for pr in self.projects:
            pr.update() # sort the activities

    def __str__(self):
        return f'\nPF w/ {len(self.projects)} P & B = {self.budget}'

    def __repr__(self):
        return str(self)
    
    def choice(self):
        return choice(self.projects)

    def sample(self, count):
        if count == 0: # pick a group at random and use that
            return choice(choice(self.groups)).members # an area or a region
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

