from random import shuffle, choice

def initial(pf): # build a random solution for a portfolio
    a = dict() # fund assignment 
    if len(pf.groups) == 1: # no areas or regions (instance set B)
        for p in pf.projects:
            if random() < 0.5: # each project has a 50-50 chance of activation
                a[p] = p.requestedBudget # fully funded
    else:
        for i in pf.permutation(): # iterate over the projects in random order
            p = pf.projects[i]
            lvl = p.requestedBudget # funds requested
            ok = True
            for g in pr.groups: # check if the bounds are not yet violated
                if p in g:
                    if not g.OK():
                        ok = False
                        break
            if ok and lvl >= b: # funds remaining
                p.allocate(lvl, a)
    return Solution(pf, a)


class Activity():

    def __init__(self, imp, maximum, minimum = 0):
        self.impact = imp
        self.minimumBudget = minimum
        self.maximumBudget = maximum
        self.difference = self.maximumBudget - self.minimumBudget 

    def effect(self, level, fraction = 0.3):
        if level == self.maximumBudget:
            return self.impact                
        else:
            # TO BE DONE: REVISION PENDING, how is the currenty impact of a partially funded activity computed?
            return ((fraction / self.difference) * (level - self.minimumBudget) + (1 - fraction)) * self.impact

class Project():
    
    def __init__(self, i, requested, minimum = None, act = None):
        self.potentialImpact = i
        self.requestedBudget = requested
        self.minimumBudget = minimum
        # one activity = the whole project (in case there were none)        
        self.activities = act if act is not None else Activity(1, requested, minimum)

    def match(self, a):
        return a in self.activities

    def activate(self, assignment):
        for a in self.activities:
            assignment[a] = 0

    def disactivate(self, assignment):
        for a in self.activities:
            del assignment[a]
    
    def update(self):
        self.activities.sort(key = lambda a: a.potentialImpact, reverse = True)

    def impact(self, assignment):
        if any([a in assignment for a in self.activities]): # at least one activity is funded
            return sum([self.impact * a.effect() for a in self.activities])
        return 0 # no funds, no impact
    
    def allocate(self, amount, assignment):
        for a in self.activities:
            lvl = a.maximumBudget # attempt to fund the activity fully
            if amount >= lvl: # do so if possible
                assignment[a] = lvl
                amount -= lvl
            else:
                # assign it the minimum funding if that is feasible otherwise random partial                
                lvl = act.minimumBudget
                lvb = lvl if (lvl > 0 and lvl <= amount) else a.random(amount)
                if lvl > 0: 
                    assignment[a] = lvl
                    amount -= level

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

    def __init__(self, m, l, u):
        self.members = m
        self.lower = l # upper bound for total funding
        self.upper = u # lower bound for total funding
        self.total = 0

    def include(self, m):
        self.members.add(m)
        
    def update(self, assignment): 
        self.total = 0        
        for m in self.members:
            if m in assignment:
                self.total += assignment[m].assigned
            
    def lowerOK(self):
        return self.lower is None or self.total >= self.lower

    def upperOK(self):
        return self.upper is None or self.upper <= self.total

    def OK(self):
        return self.lowerOK() and self.upperOK()

class Portfolio():

    def __init__(self, b, w, p, g = None, s = None):
        self.budget = b
        self.weights = w
        self.numberOfObjectives = len(w)
        self.projects = p
        self.order = None
        self.groups = g
        self.synergies = s

    def choice(self):
        return choice(self.projects)
        
    def lowerOK(self):
        for g in self.groups:
            if not g.lowerOK():
                return False
        return True

    def upperOK(self):
        for g in self.groups:
            if not g.upperOK():
                return False
        return True

    def OK():
        for g in self.groups:
            if not g.OK():
                return False
        return True
        
    def permutation(self):
        if self.order is None: # create if non-existant
            k = 0
            for p in self.projects:
                assert p.ID == k # they are supposed to be numbered 0, 1, 2, ...
            k += 1 # count them
            self.order = [i for i in range(k)] # make a list of the IDs [0, k - 1]            
        shuffle(self.order) # reorder
        return self.order

