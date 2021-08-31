from portfolio import Portfolio

def notDominated(defendant, opponent, n):
    matches = 0
    improves = False
    for i in range(n):
        if defendant.impact[i] >= opponent.impact[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant.impact[i] > opponent.impact[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return improves and matches == n # defendant is not dominated by opponent

class Solution():

    def update(self):
        self.assignedBudget = 0
        if self.areas:
            self.areaBudget = [0] * self.portfolio.numberOfAreas
        if self.regions:
            self.regionBudget = [0] * self.portfolio.numberOfRegions
        for f in self.assignment:
            lvl = f.assigned
            fa = f.target.area 
            if fa is not None:
                self.areaBudget[fa] += lvl
            fr = f.target.region
            if fr is not None:
                self.regionBudget[fr] += lvl
            self.assignedBudget += lvl
            
    def __init__(self, portfolio, assignment, h = None):
        self.portfolio = p
        self.assignment = a
        self.heuristic = h
        self.areas = False
        self.regions = False
        self.areaBudget = None
        self.regionBudget = None
        self.assignedBudget = 0 
        self.update()

    def evaluate(self):
        self.objectiveFunction = [0] * self.portfolio.numberOfObjectives
        print('WARNING: This must be overriden by inheriting classes or everything will always be zero.')
                        
    def equal(self, another):
        for i in range(self.n):
            if (self.objectiveFunction[i] != another.objectiveFunction[i]):
                return False
        return True

    def compare(self, another):
        if self.equal(another):
            return 2
        elif notDominated(self, another):
            return -1
        elif notDominated(another, self):
            return 1
        return 0
        
    def checkAreas(self):
        if self.areas:
            for a in self.areaBudget:
                if self.areaBudget[a] < self.areaLimits['LowerBound'][a]:
                    return False # too low
                elif self.areaBudget[a] > self.areasLimits['UpperBound'][a]:
                    return False # too high
        return True

    def checkRegions(self):
        if self.regions:
            for r in self.regionBudget:
                if self.regionBudget[r] < self.regionLimits['LowerBound'][r]:
                    return False # too low
                elif self.regionBudget[r] > self.regionLimits['UpperBound'][r]:
                    return False # too high
        return True

    def makeFeasible(self):
        while not (self.checkAreas() and self.checkRegions() and self.assignedBudget > self.budget):
            for a in range(self.numberOfAreas):
                if self.areaLimits['LowerBound'][a] > self.areaBudget[a]:
                    self.increaseArea(a)
                elif self.areaLimits['UpperBound'][a] < self.areaBudget[a]:
                    self.decreaseArea(a)            
            for r in range(self.numberOfRegions):
                if self.regionLimits['LowerBound'][r] > self.regionBudget[r]:
                    self.increaseRegion(r)
                elif self.regionLimits['UpperBound'][r] < self.regionBudget[r]:
                    self.decreaseRegion(r)
            if self.assignedBudget > self.budget:
                self.decreaseBudget()
            self.update() # MUST be done after every change to update the area and the region budget counters

    def increasArea(self, area):
        for i in self.permutation():
            p = self.projects[i]
            if p.area == area and self.assignment[p].active == False:
                self.assignment[p].active = True # activate a random project for the area
                return

    def decreaseArea(self, area):
        for i in self.permutation():
            p = self.projects[i]            
            if p.area == area and self.assignment[p].active == True:
                self.assignment[p].active = False # disactivate a random project for the area
                return

    def increaseRegion(self, region):
        for i in self.permutation():
            p = self.projects[i]            
            if p.region == region and self.assignment[p].active == False:
                self.assignment[p].active = True # activate a random project for the region
                return
            
    def decreaseRegion(self, region):
        for i in self.permutation():
            p = self.projects[i]            
            if p.region == region and self.assignment[p].active == True:
                self.assignment[p].active = False # disactivate a random project for the region
                return

    def decreaseBudget(self): # disactive a random project
        for i in self.permutation():            
            p = self.projects[i]            
            if self.assignment[p].active:
                self.assignment[p].active = False
                return
            
    def randomize(self, limits = False): # a random solution
        assignment = dict()
        if not limits: # limits are not considered (instance set B is like this)
            for p in self.projects:
                if random() < 0.5: # each project has a 50-50 chance of activation
                    assignment[p] = Funding(p, p.requestedBudget) # total assignment for the instance set B
        else: # upper limits are enforced (instance set A does this for areas, C does this for both)
            amount = self.portfolio.budget
            if self.areas:
                self.areaBudget = [0] * self.portfolio.numberOfAreas # reset
            if self.regions:
                self.regionBudget = [0] * self.portfolio.numberOfRegions # reset        
            for i in self.portfolio.permutation(): # iterate over the projects in random order
                p = self.portfolio.projects[i]
                pa = p.area
                pr = p.region
                p.randomize() # random assignment for a project
                aOK = not self.areas or self.areaBudget[pa] <= self.areaLimits['UpperBound'][pa]
                rOK = not self.regions or self.regionBudget[pr] <= self.regionLimits['UpperBound'][pr]
                level = p.requestedBudget
                if level <= amount and aOK and rOK:
                    assignment[p] = Funding(p, level)
                    if self.areas:
                        self.areaBudget[pa] += level # count this into the area total
                    if self.regions:
                        self.regionBudget[pr] += level # count this into the region total
                    amount -=  level # reduce the available funds
        return Solution(self, assignment)



    
