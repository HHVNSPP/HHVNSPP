def notDominated(defendant, opponent, n):
    matches = 0
    improves = False
    for i in range(n):
        if defendant.impact[i] >= opponent.impact[i]:
            matches += 1 # defendant is better or equal to opponent
            if defendant.impact[i] > opponent.impact[i] :
                improves = True # defendant improves upon the opponent in this aspect
    return improves and matches == n # defendant is not dominated by opponent

EQUAL = 2
BETTER = -1
WORSE = 1
UNDEFINED = 0

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
            return EQUAL
        elif notDominated(self, another):
            return BETTER
        elif notDominated(another, self):
            return WORSE
        return UNDEFINED
        
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
            
### HEURISTICS

from random import shuffle
from numpy.random import uniform

MIN_RANK = -10

def __init__(self, kind, rank):
    self.kind = kind # 1 = General, 2 = Shuffle
    self.rank = rank
    self.dRank = MIN_RANK
    
def set_rank(self,rank,rank_by_dom=None):
    if rank_by_dom is None:
        self.rank = rank
    else:
        self.rank_dom = rank
        
def get_rank(self, rank_by_dom=None):
    if rank_by_dom is None:
        return self.rank
    return self.rank_dom
    
def Swap1(sol):
    return sol.swap()
        
def SwapRandom(sol):
        a=[True,False]    
        for i in sol.portfolio.projects:
           i.active=random.choice(a)
        return s.feasible()
     

def SwapQuarter(sol):  
        cant=int(len(sol.portfolio.projects)/4)
        li= list(range(len(sol.portfolio.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           sol.portfolio.projects[i].active=not sol.portfolio.projects[i].active
        return s.feasible()

def SwapThird():    #quita o pone 2 proyectos, aleatorio
    cant=int(len(sol.portfolio.projects)/3)
    li= list(range(len(sol.portfolio.projects)))
    random.shuffle(li)
    l2=li[:cant]
    for i in l2:
        sol.portfolio.projects[i].active=not sol.portfolio.projects[i].active
    return s.feasible()
            
def ShakeArea():    
        num=random.choice(range(portf.num_areas))     
        for i in sol.portfolio.projects:        
            if i.area==num:                    
                    i.active=not i.active
        return s.feasible()
        
def ShakeRegion(sol):    
        num=random.choice(range(portf.num_regions))
        for i in sol.portfolio.projects:        
            if i.region==num:                    
                    i.active=not i.active
        return s.feasible()
            
def SwapHalf(sol):    #quita o pone 2 proyectos, aleatorio
        cant=int(len(sol.portfolio.projects)/2)
        li= list(range(len(sol.portfolio.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           sol.portfolio.projects[i].active=not sol.portfolio.projects[i].active
        return s.feasible()
      
def AddRandom(sol):   
        nonactives=[]
        for i in sol.portfolio.projects:
            if i.active==False:              
                nonactives.append(i.ID)                      
        if (len(nonactives)>0):           
            sol.portfolio.projects[random.choice(nonactives)].active=True
        return s.feasible()
    
def AddLowBgt(sol):  #Añade el de menos presupuesto 
        lower=portf.budget
        temp=0
        for i in sol.portfolio.projects:
            if i.active==False:
                if i.request_budget<lower:
                    lower=i.request_budget
                    temp=i.ID
        sol.portfolio.projects[temp].active=True 
        return s.feasible()
        
def AddMaxBgt(sol):  
        m=0
        temp=0
        for i in sol.portfolio.projects:
            if i.active==False:
                if i.request_budget>m:
                    m=i.request_budget
                    temp=i.ID
        sol.portfolio.projects[temp].active=True  
        return s.feasible()


def DrawRandom(sol):   
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active:  
                actives.append(count)
                count=count+1
            else:                
                count=count+1       
        if (len(actives)>0):           
            sol.portfolio.projects[random.choice(actives)].active=False
        portf.update() 
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf) 
        return s.feasible()


def UseBudgetAT(sol):
        diff = portf.budget - portf.total_bgt                                                            
        for prj in sol.portfolio.projects:
            if diff <= 0:  
                break
            else:
                if not prj.active:
                    if prj.request_budget<=diff:                                                    
                        diff -= prj.request_budget
                        prj.active=True
                        portf.update()  
                                                                           
        return s.feasible()
    
def DrawHightBgt(sol):   #Saca el de mayor presupuesto
        maxim=0
        temp=0
        for i in sol.portfolio.projects:
            if i.active:
                if i.request_budget>maxim:
                    maxim=i.request_budget
                    temp=i.ID
        sol.portfolio.projects[temp].active=False 
        portf.update()    
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf)           
        return s.feasible()
            
def DrawRandomPutLessBgt(sol):   #Draw one ramdom and put one with less budget req
        nonactives=[]
        actives=[]
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(i.ID)             
            else: 
                nonactives.append(i.ID)                 
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives)             
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].request_budget<sol.portfolio.projects[selected].request_budget):                 
                    sol.portfolio.projects[i].active=True
                    break
        return s.feasible()
               
def SwapArea(sol):   #Draw one ramdom and put one from other area
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].area!=sol.portfolio.projects[selected].area):                 
                    sol.portfolio.projects[i].active=True
                    break
        return s.feasible()

def IncreseBgtArea(sol):   #Draw one ramdom and put one with more budget in same area
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].area==sol.portfolio.projects[selected].area):
                    if sol.portfolio.projects[i].request_budget>sol.portfolio.projects[selected].request_budget:
                        sol.portfolio.projects[i].active=True
                        break
        return s.feasible()


def DecreaseBgtArea(sol):     #Draw one ramdom and put one with less budget in same area
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].area==sol.portfolio.projects[selected].area):
                    if sol.portfolio.projects[i].request_budget<sol.portfolio.projects[selected].request_budget:
                        sol.portfolio.projects[i].active=True
                        break
        return s.feasible

  
def SwapRegion(sol):   #Draw one ramdom and put one in other region
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].region!=sol.portfolio.projects[selected].region):                 
                    sol.portfolio.projects[i].active=True
                    return s.feasible()
        portf.update()
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf) 
        return s.feasible()


def IncreseBgtRegion(sol):   #Draw one ramdom and put one with more budget in same region
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].region==sol.portfolio.projects[selected].region):
                    if sol.portfolio.projects[i].request_budget>sol.portfolio.projects[selected].request_budget:
                        sol.portfolio.projects[i].active=True
                        break
            return s.feasible()


def DecreaseBgtRegion(sol):     #Draw one ramdom and put one with less budget in same area
        nonactives=[]
        actives=[]
        count=0
        for i in sol.portfolio.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            sol.portfolio.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (sol.portfolio.projects[i].region==sol.portfolio.projects[selected].region):
                    if sol.portfolio.projects[i].request_budget<sol.portfolio.projects[selected].request_budget:
                        sol.portfolio.projects[i].active=True
                        break
        return s.feasible()
    

def MoreProj(sol):
        change=False
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in sol.portfolio.projects:
                if not prj.uses and diff > prj.min_budget:                   
                    prj.uses = True
                    change=True
                    prj.set_budget(prj.min_budget)
                    diff -= prj.min_budget                       
                    portf.update()
        if change:
            h=UseBudget(21, 4, 0, 1)   
            h.execute(portf)            
        return s.feasible()

        
def QuitBad(sol):
        bad=0
        portf = super().execute(sol)
        temp=portf.total_impact[0]
        for i in range(len(sol.portfolio.projects)):
                if sol.portfolio.projects[i].active:
                    if sol.portfolio.projects[i].real_impact==0 or sol.portfolio.projects[i].request_budget==0:
                        sol.portfolio.projects[i].active=False                   
                    elif sol.portfolio.projects[i].real_impact/sol.portfolio.projects[i].request_budget<temp:
                        bad=i
                  
        sol.portfolio.projects[bad].active=False
        portf.update()
        h=MoreProj(21, 4, 0, 1)   
        h.execute(portf)            
        return s.feasible()

def UseBudget(sol):
        diff = portf.budget - portf.total_bgt                                                            
        for prj in sol.portfolio.projects:
            if diff <= 0:  
                break
            else:
                 if prj.active:
                    if prj.request_budget<prj.max_budget:  
                        if diff>=prj.max_budget-prj.request_budget:                              
                            diff -= prj.max_budget-prj.request_budget
                            prj.set_budget(prj.max_budget)  
                            portf.update()
                        elif diff+prj.request_budget>=prj.min_budget:
                            prj.set_budget(diff+prj.request_budget) 
                            break                                              
        return s.feasible()
    
def SetPrjMinFill(sol): #Selects a project, fill activities random till min bdg, don't change status
        selected=random.choice(sol.portfolio.projects) 
        selected.set_budget(selected.min_budget)  
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)   
        return s.feasible()
    
def SetPrjRndFill(sol): 
        selected=random.choice(sol.portfolio.projects) 
        selected.set_budget(int(uniform(selected.min_budget, selected.max_budget)))
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)  
        return s.feasible()

def ProjMin(sol):    
    def __init__(self, ID, kind,rank):
        selected=random.choice(sol.portfolio.projects) 
        selected.set_budget=selected.min_budget                
        return s.feasible()

def AllRandN(sol):    
        for x in sol.portfolio.projects:
            x.set_budget( uniform(x.min_budget, x.max_budget))                   
        return s.feasible()
 
def MTrySetMax(sol):
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in sol.portfolio.projects:
                if prj.uses and diff >= prj.min_budget:                   
                    if prj.min_budget<=diff:                        
                        prj.set_budget
                        (diff)
                        if prj.max_budget<=diff:
                           diff-=prj.max_budget
                        else:
                           diff=0                                                                                
        return s.feasible()
        
def MSetPrjRnd(sol): #Selects a project, fill activities random g
        selected=random.choice(sol.portfolio.projects) 
        selected.random_budget()
        return s.feasible()


def MMoreProj(sol):
        change=False
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in sol.portfolio.projects:
                if not prj.uses and diff > prj.min_budget:                   
                    prj.uses = True
                    change=True
                    prj.set_budget(prj.min_budget)
                    diff -= prj.min_budget                       
                    portf.update()
        if change:
            h=UseBudget(21, 4, 0, 1)   
            h.execute(portf)            
        return s.feasible()

def MUseBudget(sol):
        diff = portf.budget - portf.total_bgt                                                            
        for prj in sol.portfolio.projects:
            if diff <= 0:  
                break
            else:
                 if prj.active:
                    if prj.request_budget<prj.max_budget:  
                        if diff>=prj.max_budget-prj.request_budget:                              
                            diff -= prj.max_budget-prj.request_budget
                            prj.set_budget(prj.max_budget)  
                            portf.update()
                        elif diff+prj.request_budget>=prj.min_budget:
                            prj.set_budget(diff+prj.request_budget) 
                            portf.update()
                            break                                              
        portf.make_feasible()
        return portf    
    
def MChange5perc(sol):    
        for i in sol.portfolio.projects:
            if (random.choice([True,False])):              
                i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20)) 
            else:
                i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))
       
        portf.update()  
        portf.make_feasible()            
        return portf
    
def MMore5perc(sol):    
        i=random.choice(sol.portfolio.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20))            
        portf.update()  
        portf.make_feasible()            
        return portf


def MLess5perc(sol):    
        i=random.choice(sol.portfolio.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))                
        portf.update()  
        portf.make_feasible()            
        return portf   
    
def MMore10perc(sol):    
        i=random.choice(sol.portfolio.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/10))
        portf.update()  
        portf.make_feasible()            
        return portf

def MLess10perc(sol):    
        i=random.choice(sol.portfolio.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/10))                    
        portf.update()  
        portf.make_feasible()            
        return portf     

def DrawHightBgtAndFill(sol):   #Saca el de mayor presupuesto y llena
        maxim=0
        temp=0
        for i in sol.portfolio.projects:
            if i.active:
                if i.request_budget>maxim:
                    maxim=i.request_budget
                    temp=i.ID
        sol.portfolio.projects[temp].active=False 
        portf.update()
        h=MoreProj(17, 4, 0, 1)         
        portf=h.execute(portf)        
        return s.feasible()

def DrawRandFill(sol):   #Draw one ramdom and put one with less budget req
        for i in sol.portfolio.permutation():
            p = sol.portfolio.projects[i]
            if p.active: 
                sol.portfolio.projects[i].active=True
                portf.update()
                break                  
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)           
        return s.feasible()
  



    
    
            
