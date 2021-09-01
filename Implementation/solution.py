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

    def __init__(self, portfolio, assignment, g = None, h = None):
        self.portfolio = p
        self.assignment = a
        self.heuristic = h
        self.groups = g        
        self.update()

    def swap(self): 
        p = self.portfolio.choice() # pick a random project
        na = dict()
        for a in self.assignment:
            if p.active and not p.match(a):
                na = self.assignment[a] # copy the other assignments as such 
        if not p.active:
            p.activate(na) # activate the project with a zero funding
        return Solution(self.portfolio, na) # create another solution with this assignment
        
    def update(self):
        for g in self.groups:
            g.update(self.assignment)

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
            return 2
        elif notDominated(self, another):
            return -1
        elif notDominated(another, self):
            return 1
        return 0
        
    def OK(self):
        for g in self.groups():
            if not g.OK():
                return False
        return True
    
    def feasible(self):
        self.update() # initial update
        while not self.OK():
            for g in self.groups:
                if not g.lowOK():
                    self.increase(g)
                elif not g.highOK():
                    self.decrease(g)
            self.update() 

    def increase(self, g):
        for i in self.permutation():
            p = self.projects[i]
            if p in g and p not in self.assignment:
                self.assignment[p] = 0 # activate with zero funds
                return

    def decrease(self, area):
        for i in self.permutation():
            p = self.projects[i]            
            if p in g and p in self.assignment:
                del self.assignment[p] # discard present funding
                return
            



    
    
            
