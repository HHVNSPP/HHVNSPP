from random import shuffle
from numpy.random import uniform

MIN_RANK = -10

class BaseHeuristic():
    
    def __init__(self, ID, kind, rank):
        self.ID = ID
        self.kind = kind # 1 = General, 2 = Shuffle
        self.uses = 0
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
        
    def execute(self, sol):
        self.active += 1

class Swap1(BaseHeuristic): 
    def __init__(self, ID, kind,active, rank):
        super().__init__(ID, kind,active, rank)

    def execute(self, sol): # randomly include or exclude a project
        super.execute(self)
        return sol.swap()
        
class SwapRandom(BaseHeuristic):    
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        a=[True,False]    
        for i in portf.projects:
           i.active=random.choice(a)
        return s.feasible()
     
###############################################
       
class SwapQuarter(BaseHeuristic):  
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        cant=int(len(portf.projects)/4)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        return s.feasible()

###############################################
       
class SwapThird(BaseHeuristic):    #quita o pone 2 proyectos, aleatorio
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        cant=int(len(portf.projects)/3)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        return s.feasible()
            
class ShakeArea(BaseHeuristic):    
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        num=random.choice(range(portf.num_areas))     
        for i in portf.projects:        
            if i.area==num:                    
                    i.active=not i.active
        return s.feasible()
        
###############################################
            
class ShakeRegion(BaseHeuristic):    
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        num=random.choice(range(portf.num_regions))
        for i in portf.projects:        
            if i.region==num:                    
                    i.active=not i.active
        return s.feasible()
            
class SwapHalf(BaseHeuristic):    #quita o pone 2 proyectos, aleatorio
    def __init__(self, ID, kind, rank):
        super().__init__(ID, kind, rank)
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        cant=int(len(portf.projects)/2)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        return s.feasible()
      
class AddRandom(BaseHeuristic):   
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        nonactives=[]
        for i in portf.projects:
            if i.active==False:              
                nonactives.append(i.ID)                      
        if (len(nonactives)>0):           
            portf.projects[random.choice(nonactives)].active=True
        return s.feasible()
    
class AddLowBgt(BaseHeuristic):  #Añade el de menos presupuesto 
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        lower=portf.budget
        temp=0
        for i in portf.projects:
            if i.active==False:
                if i.request_budget<lower:
                    lower=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=True 
        return s.feasible()
        
class AddMaxBgt(BaseHeuristic):  
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
        portf = super().execute(sol)
        m=0
        temp=0
        for i in portf.projects:
            if i.active==False:
                if i.request_budget>m:
                    m=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=True  
        return s.feasible()

################################################# 
class DrawRandom(BaseHeuristic):   
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        actives=[]
        count=0
        for i in portf.projects:
            if i.active:  
                actives.append(count)
                count=count+1
            else:                
                count=count+1       
        if (len(actives)>0):           
            portf.projects[random.choice(actives)].active=False
        portf.update() 
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf) 
        return s.feasible()


class UseBudgetAT(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt                                                            
        for prj in portf.projects:
            if diff <= 0:  
                break
            else:
                if not prj.active:
                    if prj.request_budget<=diff:                                                    
                        diff -= prj.request_budget
                        prj.active=True
                        portf.update()  
                                                                           
        return s.feasible()
    
 ################################################
class DrawHightBgt(BaseHeuristic):   #Saca el de mayor presupuesto
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        maxim=0
        temp=0
        for i in portf.projects:
            if i.active:
                if i.request_budget>maxim:
                    maxim=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=False 
        portf.update()    
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf)           
        return s.feasible()
            
class DrawRandomPutLessBgt(BaseHeuristic):   #Draw one ramdom and put one with less budget req
    def __init__(self, ID, kind,rank):  
        super().__init__(ID,kind,rank)
       
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        for i in portf.projects:
            if i.active: 
                actives.append(i.ID)             
            else: 
                nonactives.append(i.ID)                 
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives)             
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].request_budget<portf.projects[selected].request_budget):                 
                    portf.projects[i].active=True
                    break
        return s.feasible()
               
class SwapArea(BaseHeuristic):   #Draw one ramdom and put one from other area
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       

    def execute(self, sol):
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].area!=portf.projects[selected].area):                 
                    portf.projects[i].active=True
                    break
        return s.feasible()

###########################################################
        
class IncreseBgtArea(BaseHeuristic):   #Draw one ramdom and put one with more budget in same area
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank) 
        
    def execute(self, sol):
        self.active+=1
#        print(self.ID)
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].area==portf.projects[selected].area):
                    if portf.projects[i].request_budget>portf.projects[selected].request_budget:
                        portf.projects[i].active=True
                        break
        return s.feasible()


class DecreaseBgtArea(BaseHeuristic):     #Draw one ramdom and put one with less budget in same area
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].area==portf.projects[selected].area):
                    if portf.projects[i].request_budget<portf.projects[selected].request_budget:
                        portf.projects[i].active=True
                        break
        return s.feasible

  
class SwapRegion(BaseHeuristic):   #Draw one ramdom and put one in other region
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].region!=portf.projects[selected].region):                 
                    portf.projects[i].active=True
                    return s.feasible()
        portf.update()
        h=UseBudgetAT(20, 2, 0, 1)   
        h.execute(portf) 
        return s.feasible()


class IncreseBgtRegion(BaseHeuristic):   #Draw one ramdom and put one with more budget in same region
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    def execute(self, sol):
        super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].region==portf.projects[selected].region):
                    if portf.projects[i].request_budget>portf.projects[selected].request_budget:
                        portf.projects[i].active=True
                        break
            return s.feasible()

###########################################################
class DecreaseBgtRegion(BaseHeuristic):     #Draw one ramdom and put one with less budget in same area
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
#        print(self.ID)
        portf = super().execute(sol)
        nonactives=[]
        actives=[]
        count=0
        for i in portf.projects:
            if i.active: 
                actives.append(count)
                count=count+1
            else: 
                nonactives.append(count)
                count=count+1       
        if (len(nonactives)>0 and len(actives)>0):
            selected=random.choice(actives) 
            portf.projects[selected].active=False                  
            random.shuffle(nonactives)
            for i in nonactives:               
                if (portf.projects[i].region==portf.projects[selected].region):
                    if portf.projects[i].request_budget<portf.projects[selected].request_budget:
                        portf.projects[i].active=True
                        break
        return s.feasible()
    

class MoreProj(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        change=False
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
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

###########################################################
        
class QuitBad(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        bad=0
        portf = super().execute(sol)
        temp=portf.total_impact[0]
        for i in range(len(portf.projects)):
                if portf.projects[i].active:
                    if portf.projects[i].real_impact==0 or portf.projects[i].request_budget==0:
                        portf.projects[i].active=False                   
                    elif portf.projects[i].real_impact/portf.projects[i].request_budget<temp:
                        bad=i
                  
        portf.projects[bad].active=False
        portf.update()
        h=MoreProj(21, 4, 0, 1)   
        h.execute(portf)            
        return s.feasible()

class UseBudget(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt                                                            
        for prj in portf.projects:
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
    
    
######################################################################
class SetPrjMinFill(BaseHeuristic): #Selects a project, fill activities random till min bdg, don't change status
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        selected=random.choice(portf.projects) 
        selected.set_budget(selected.min_budget)  
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)   
        return s.feasible()
    
#######################################################################
        
class SetPrjRndFill(BaseHeuristic): 
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        selected=random.choice(portf.projects) 
        selected.set_budget(int(uniform(selected.min_budget, selected.max_budget)))
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)  
        return s.feasible()

class ProjMin(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(sol):
        self.active+=1
        portf = super().execute(sol)
        selected=random.choice(portf.projects) 
        selected.set_budget=selected.min_budget                
        return s.feasible()

class AllRandN(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.active+=1
        portf = super().execute(sol)
        for x in portf.projects:
            x.set_budget( uniform(x.min_budget, x.max_budget))                   
        return s.feasible()
 
class MTrySetMax(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        portf = super().execute(self,sol)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
                if prj.uses and diff >= prj.min_budget:                   
                    if prj.min_budget<=diff:                        
                        prj.set_budget
                        (diff)
                        if prj.max_budget<=diff:
                           diff-=prj.max_budget
                        else:
                           diff=0                                                                                
        return s.feasible()
        
class MSetPrjRnd(BaseHeuristic): #Selects a project, fill activities random g
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        portf = super().execute(self,sol)
        selected=random.choice(portf.projects) 
        selected.random_budget()
        return s.feasible()


class MMoreProj(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        change=False
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
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

class MUseBudget(BaseHeuristic):
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        portf = super().execute(sol)
        diff = portf.budget - portf.total_bgt                                                            
        for prj in portf.projects:
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
    
#####################################
class MChange5perc(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)          

    def execute(self, sol):
        self.active+=1
#        print(self.ID)
        portf = super().execute(sol)
        for i in portf.projects:
            if (random.choice([True,False])):              
                i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20)) 
            else:
                i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))
       
        portf.update()  
        portf.make_feasible()            
        return portf
    
#####################################
class MMore5perc(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        i=random.choice(portf.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20))            
        portf.update()  
        portf.make_feasible()            
        return portf

#####################################
class MLess5perc(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)           
    def execute(self, sol):
#        print(self.ID)
        self.active+=1
        portf = super().execute(sol)
        i=random.choice(portf.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))                
        portf.update()  
        portf.make_feasible()            
        return portf   
#####################################
        
    
    
    
    
class MMore10perc(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)       
    
    def execute(self, sol):
        self.uses += 1
        portf = super().execute(sol)
        i=random.choice(portf.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/10))
        portf.update()  
        portf.make_feasible()            
        return portf

class MLess10perc(BaseHeuristic):    
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)           
    def execute(self, sol):
        self.uses += 1
        portf = super().execute(sol)
        i=random.choice(portf.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/10))                    
        portf.update()  
        portf.make_feasible()            
        return portf     

class DrawHightBgtAndFill(BaseHeuristic):   #Saca el de mayor presupuesto y llena
    def __init__(self, ID, kind,rank):
        super().__init__(ID,kind,rank)
        
    def execute(self, sol):
        self.uses += 1
        portf = super().execute(sol)
        maxim=0
        temp=0
        for i in portf.projects:
            if i.active:
                if i.request_budget>maxim:
                    maxim=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=False 
        portf.update()
        h=MoreProj(17, 4, 0, 1)         
        portf=h.execute(portf)        
        return s.feasible()

class DrawRandFill(BaseHeuristic):   #Draw one ramdom and put one with less budget req
    def __init__(self, ID, kind,rank):  
        super().__init__(ID,kind,rank)
       
    def execute(self, sol):
        self.uses += 1
        portf = super().execute(sol)
        li = list(range(len(portf.projects))) 
        random.shuffle(li)
        for i in li:
            if portf.projects[i].active: 
                portf.projects[i].active=True
                portf.update()
                break                  
        h=MoreProj(17, 4, 0, 1)        
        portf=h.execute(portf)           
        return s.feasible()
  
