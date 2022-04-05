from random import shuffle, choice, random, sample
from math import ceil, fabs
from gurobipy import GRB
import gurobipy as gp
from solution import Solution

verbose = False

def same(x, y, epsilon = 0.0001):
    return fabs(x - y) < epsilon

def zero(x):
    return same(x, 0)

def geq(x, y):
    if same(x, y):
        return True
    else:
        return x > y

def leq(x, y):
    if same(x, y):
        return True
    else:
        return x < y

def gt(x, y):
    if same(x, y):
        return False
    else:
        return x > y

def lt(x, y):
    if same(x, y):
        return False
    else:
        return x < y

class Activity(): # these are the tasks 

    def __init__(self, project, imp, maximum, minimum = 0):
        self.parent = project
        self.relativeImportance = imp
        self.minBudget = minimum
        self.maxBudget = maximum
        self.diff = self.maxBudget - self.minBudget
        assert self.diff >= 0

    def __str__(self):
        return f'A[{self.minBudget:.0f}, {self.maxBudget:.0f}] = {self.relativeImportance}'

    def funding(self, assignment):
        # force all to decimal (some are integers)        
        amount = 1.0 * assignment.get(self, 0) 
        return f'{amount:.0f}' # ignore fractional differences when comparing

    def bounds(self, a):
        amount = a.get(self, 0)
        if amount > 0:
            b = f'{self.minBudget:.0f} <= {amount:.0f} <= {self.maxBudget:.0f}'
            print(f'A {amount > 0}: {b}')
    
    def feasible(self, a):
        if self not in a:
            return True # inactive tasks are always feasible
        amount = a[self]
        if lt(self.maxBudget, amount):
            if verbose:
                print(f'activity has too much: {amount} > {self.maxBudget}')
            return False
        if lt(amount, self.minBudget):
            if verbose:
                print(f'activity has too little: {amount} < {self.minBudget}')            
            return False
        return True # both limits are respected
    
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

    # cf. Fig. 1 in https://doi.org/10.1109/TSMCA.2010.2041228        
    def impact(self, active, amount, i, alpha = 0.5): # for objective at index i
        span = self.maxBudget - self.minBudget
        excess = amount - self.minBudget
        scaled = (1 - alpha) * (excess / span)
        total = alpha + scaled
        return active * self.parent.socialImpact[i] * self.relativeImportance[i] * total

    def contribution(self, amount, i): # for objective at index i
        return self.parent.socialImpact[i] * self.relativeImportance[i]
    
    def deactivate(self, assignment):
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
        self.socialImpact = imp
        self.maxBudget = requested
        if minimum is not None:
            assert minimum <= requested
        self.diff = 0 if minimum is None else requested - minimum
        self.minBudget = minimum if minimum is not None else self.maxBudget
        assert self.minBudget <= self.maxBudget
        self.tasks = list()
        self.groups = groups

    def __str__(self):
        pot = '|'.join([ str(p) for p in self.socialImpact ])
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
            b = f'{self.minBudget:.0f} <= {t:.0f} <= {self.maxBudget:.0f}'
            print(f'P {t > 0}: {b}')
            for act in self.tasks:
                act.bounds(a)
    
    def feasible(self, a):
        t = self.assigned(a)
        if not zero(t):
            if lt(t, self.minBudget):
                if verbose:
                    print(f'project has too little: {t} < {self.minBudget}')
                    for act in self.tasks:
                        print(a.get(act, None))
                    quit()
                return False
            if gt(t, self.maxBudget):
                if verbose:
                    print(f'project has too much: {t} > {self.maxBudget}')                                        
                return False
            # check also tasks
            ca = [ act.feasible(a) for act in self.tasks ]
            if not all(ca) and verbose:
                print('activities not ok', ca)
            return all(ca)
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

    def deactivate(self, assignment):
        for a in self.tasks:
            a.deactivate(assignment)
            
    def impact(self, assignment, alpha = 0.5):
        k = len(self.socialImpact)
        pi = [ 0 ] * k
        amount = self.assigned(assignment)        
        if lt(amount, self.minBudget):
            assert zero(amount)
            for t in self.tasks: # make sure there are no funds
                assert assignment.get(t, 0) == 0
            return pi # unfunded, no impact, all zeroes
        for task in self.tasks: # accumulate over tasks
            for i in range(k):
                if task in assignment: # only if it was assigned funds
                    a = assignment[task]
                    assert geq(a, task.minBudget) # make sure it is enough
                    assert leq(a, task.maxBudget) # make sure it is not too much
                    if self.socialImpact[i] is not None: 
                        # linear objectives: compute numerical impact
                        if task.minBudget < task.maxBudget: # one that scales
                            pi[i] += task.impact(1, a, i) # only active tasks
                        else:
                            # inefficient for compatibility
                            pi[i] += task.contribution(a, i) # all or nothing 
                    else: # for counters, just count
                        pi[i] = max(pi[i], 1) 
        return pi
                
    def update(self):
        if len(self.tasks) == 0:
            # one activity = the whole project (in case there were none)
            imp = [ 1 for p in self.socialImpact ] # full impact 
            self.tasks = [ Activity(self, imp, self.maxBudget, self.minBudget) ]
        else: # sort in decreasing order of impact
            self.tasks.sort(key = lambda a: a.relativeImportance, reverse = True)
            self.maxBudget = sum([ a.maxBudget for a in self.tasks ])

class Synergy(): # we only implement technical synergies; feel free to add more options

    def __init__(self, value, lower, upper):
        self.value = value
        self.lowerThreshold = lower
        self.upperThreshold = upper
        self.elements = set()

    def include(self, elem):
        self.elements.add(elem)

    def active(self, activated):
        count = len(activated & self.elements) # shared
        return count >= self.lowerThreshold and count <= self.upperThreshold

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
        ok = 'OK' if self.feasible(a) else 'NO'
        print(f'G {ok}: {self.lower:.0f} <= {self.assigned(a):.0f} <= {self.upper:.0f}')
        
    def feasible(self, a):
        t = self.assigned(a)
        p = [ p.feasible(a) for p in self.members ]
        bot = self.lower is None or geq(t, self.lower)
        top = self.upper is None or geq(self.upper, t)
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

    def __init__(self, total, w, i, p, part = [], s = []):
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
        if len(self.groups) == 0: # no partitions, no groups: make one for compatibility
            self.groups = [ self.projects ]
            self.partitions = [ self.groups ]
        self.synergies = s
        self.hypothetical() # print out info on hypothetical objective values 

    def included(self, active):
        return ''.join([ str(1 * (p in active)) for p in self.projects ])

    def funding(self, assignment):
        return '#'.join([ p.funding(assignment) for p in self.projects ])    
        
    def __str__(self):
        s = f'PF w/ {len(self.projects)} P & B = {self.budget}\n'
        s += '\n'.join(' '.join([ str(g) for g in p ]) for p in self.partitions)
        return s
    
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
        if not leq(assigned, self.budget):
            return False # too much has been spent
        gc = [ g.feasible(a) for g in self.groups ] 
        if verbose:
            print('groups', gc)       
        gOK = all(gc)
        pc = [ p.feasible(a) for p in self.projects ]
        if verbose:
            print('projects', pc)
        pOK = all(pc)
        return gOK and pOK
    
    def permutation(self):
        if self.order is None: # create if non-existant
            self.order = [ i for i in range(len(self.projects)) ] 
        shuffle(self.order) # reorder
        return self.order

    def evaluate(self, solution):
        v = [0] * self.dim
        funded = set()
        added = 0
        act = solution.actives()
        for s in self.synergies:
            if s.active(act):
                added += s.value
        for project in act:
            ei = project.impact(solution.assignment, self.impact)
            for i in range(self.dim):
                v[i] += ei[i]
        if len(self.synergies) > 0:
            for i in range(self.dim): # partial objectives gain synergies
                if self.impact[i]: # this objective is affected
                    v[i] += added
        return v

    def hypothetical(self):
        low = dict() 
        high = dict()
        vl = [0] * self.dim
        vh = [0] * self.dim        
        for p in self.projects:
            for t in p.tasks:
                low[t] = t.minBudget
                high[t] = t.maxBudget
        for p in self.projects:        
            il = p.impact(low, self.impact)
            ih = p.impact(high, self.impact)
            for i in range(self.dim):
                vl[i] += il[i]
                vh[i] += ih[i]
        tl = sum(low.values())
        th = sum(high.values())        
        print(f'# funding everything at the lowest level costs {tl:.0f} ->', vl)
        print(f'# funding everything at the highest level costs {th:.0f} ->', vh)
    
    def ideal(self, alpha = 0.5): # this computation IGNORES synergies
        global verbose                    
        print('GUROBI output starts')
        m = gp.Model("MIP model")
        tasks = list() # all tasks
        for p in self.projects:
            tasks += p.tasks
        assert len(tasks) == len(set(tasks)) # ensure unique tasks
        # funding-level variables
        ta = m.addVars(self.projects, tasks) # task-level fund assignment amounts
        pa = m.addVars(self.projects) # project-level fund assignment amounts
        # indicator varibles
        pi = m.addVars(self.projects, vtype = GRB.BINARY) # project-level funded yes/no
        ti = m.addVars(self.projects, tasks, vtype = GRB.BINARY) # task-level fund yes/no
        # respect the total budget
        m.addConstr(gp.quicksum(ta[p, t] \
                                for p in self.projects for t in tasks) <= self.budget) 
        for g in self.groups: # groups = areas and/or regions
            # lower limit of each area/region            
            m.addConstr(g.lower <= gp.quicksum(ta[p, t] for p in g.members for t in tasks))
            # upper limit of each area/region                        
            m.addConstr(g.upper >= gp.quicksum(ta[p, t] for p in g.members for t in tasks))
        for p in self.projects: # consistency between ALL tasks and projects
            m.addConstr(pa[p] >= 0) # no negative funding is allowed
            # project-to-task consistency:
            # a project is funded only when at least one task is funded          
            m.addConstr(pi[p] <= gp.quicksum(ti[p, t] for t in tasks))
            # the total funding for the tasks matched the project funding
            m.addConstr(pa[p] == gp.quicksum(ta[p, t] for t in tasks))            
            # task-to-project consistency:
            # the number of tasks funded does not exceed the tasks in the project            
            m.addConstr(gp.quicksum(ti[p, t] for t in tasks) <= pi[p] * len(p.tasks))
            # minimum budget for project
            m.addConstr(pa[p] >= pi[p] * p.minBudget)
            # maximum budget for project            
            m.addConstr(pa[p] <= pi[p] * p.maxBudget)
            # project assignment is equal to the sum of tasks                
            m.addConstr(pa[p] == gp.quicksum(ta[p, t] for t in tasks))
            for t in tasks: # constraints for each task
                m.addConstr(ta[p, t] >= 0) # no negative funding
                # a task can be funded only if the project is funded
                m.addConstr(ti[p, t] <= pi[p])
                # minimum budget for task
                m.addConstr(ta[p, t] >= ti[p, t] * t.minBudget)
                # maximum budget for task
                m.addConstr(ta[p, t] <= ti[p, t] * t.maxBudget) 
                # task can be active only if project is active                   
                m.addConstr(ti[p, t] <= pi[p])
                if t not in p.tasks: # for tasks of OTHER projects
                    m.addConstr(ta[p, t] == 0) # no funds can be allocated
                    m.addConstr(ti[p, t] == 0) # task cannot be activated (some tasks have zero minimums)
        # objectives: first the project count, then the ones in the instance,
        # all treated as partially affected
        obj = list()
        for i in range(self.dim):
            if self.impact[i]: # affected by partial funding
                obj.append(gp.quicksum(gp.quicksum(t.impact(ti[p, t],
                                                            ta[p, t], i) \
                                                   for t in p.tasks) for p in self.projects))
            else: # these are counters
                obj.append(gp.quicksum(pi[p] for p in self.projects)) # count the projects
        pos = 0
        for o in obj: # single-objective ideal points
            m.setObjective(o, GRB.MAXIMIZE) # optimize number of projects included
            m.update() 
            m.presolve()            
            m.optimize()
            if m.status != GRB.OPTIMAL:
                print(f'ERROR: gurobi exited with status {m.status}')
            else:
                value = m.getObjective().getValue()
                print(f'IDEAL POINT: {value}')
                print('COUNT:', sum(pi[p].X for p in self.projects))
                spent = sum(ta[p, t].X for p in self.projects for t in tasks)
                print(f'SPENDING: {spent:.0f} / {self.budget:.0f}')
                # verify the solution
                a = dict()
                c = 0
                for p in self.projects:
                    total = pa[p].X # amount assigned by gurobi
                    assert geq(p.maxBudget, total) # not too much
                    active = pi[p].X
                    if not active:
                        assert zero(total) # nothing if inactive
                    else: # active
                        assert geq(total, p.minBudget) # not too little
                        assert leq(total, p.maxBudget) # not too much
                    assert not active or total > 0 # marked as none unless there is some
                    c += 1 if total > 0 else 0 # count those ones that have funds
                    found = 0 # count funded tasks
                    accumulated = 0 # count fund assignment
                    for t in tasks: # check ALL tasks
                        amount = ta[p, t].X # check assigned funds
                        if ti[p, t].X > 0: # the task is active
                            a[t] = amount # assign the funds in the verification solution
                            if verbose:
                                print(p, t, amount, total) 
                            # a funded task must match its project      
                            assert t in p.tasks 
                            # note that at least one task
                            # (in project 57 of instance 10 of Set A)
                            # has minimum budget zero(!)
                            assert pi[p].X > 0 # the project must be active
                            # the upper limit is respected
                            assert geq(t.maxBudget, amount)
                            # the lower limit is respected      
                            assert geq(amount, t.minBudget) 
                            found += 1
                            accumulated += amount
                        else:
                            assert zero(amount)
                    assert same(total, accumulated)
                    if found == 0:
                        assert not active
                comp = Solution(self, a)
                if not comp.feasible():
                    # we need to see the debug if something turned out infeasible in the verification                    
                    verbose = True 
                assert comp.feasible()                
                e = self.evaluate(comp)
                print('VERIFICATION:', e)
                assert same(value, e[pos])
                pos += 1
                r = ''.join(f'{int(pi[p].X)}' for p in self.projects)
                print('SELECTION:', r)
                if verbose: # repeat in debug mode
                    print('SELECTION:', comp)                
                assert str(comp) == r
            m.reset()
        print('GUROBI output ends')            
