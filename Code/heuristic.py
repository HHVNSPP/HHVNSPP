#------------------------------------------------------
# Cambios introducidos a la clase BaseHeuristic para incluir el rank por dominancia
# y los metodos para modificar (set) y devolver (get) el rank
# se modifica o devuelve el rank si se no se le pasa valor al parametro rank_by_dom,
# de lo contrario se modifica o devuelve el rank_dom
#Pase la copia del portfolio para  el metodo apply de BaseHeuristic y ahi le pase la referencia de la heuristica al portfolio que se modifica
#-----------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:59:55 2019

@author: Madys
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:08:09 2019
@author: Madys
"""
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from project import RProject
import pickle
from random import shuffle
import random
import copy
import portfolio as prf
from numpy.random import uniform

MIN_RANK = -10
@dataclass
class BaseHeuristic(ABC):
    
    # Constructor
    def __init__(self, ID, kind,in_use,rank):
        super().__init__()
        self.ID = ID
        self.kind=kind
        self.in_use=in_use
        self.rank=rank
        #---------------- linea adicionada por fernando 27/07/2021
        self.rank_dom = MIN_RANK
        #--------------------------------------------------------
#    kind description:
#        1: General 
#        2:Shuffle 

    #--------metodos adicionados por fernando 27 de julio del 2021
    def set_rank(self,rank,rank_by_dom=None):
        if rank_by_dom is None:
            self.rank = rank
        else:
            self.rank_dom = rank

    def get_rank(self, rank_by_dom=None):
        if rank_by_dom is None:
            return self.rank
        return self.rank_dom
    #--------------------------------------------------------------

    # Class members region
    def set_ID(self, ID):
        self.ID = ID

    def set_kind(self, impact):
        self.impact = impact

    def set_in_use(self, active):
        self.active = active
        
    def apply(self, portfolio):
        portf = copy.deepcopy(portfolio)
        portf.setheur(self)
        return portf

############################################
class Swap1(BaseHeuristic):      #quita o pone un proyecto, aleatorio
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        portf = super().apply(portfolio)
        self.in_use+=1
        p= random.choice(list(range(len(portf.projects))))
        portf.projects[p].active=not portf.projects[p].active
        portf.update()
        portf.make_factible()
        return portf
   
###############################################
        
class SwapRandom(BaseHeuristic):    
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        a=[True,False]    
        for i in portf.projects:
           i.active=random.choice(a)
        portf.update()
        portf.make_factible()
        return portf
     
###############################################
       
class SwapQuarter(BaseHeuristic):  
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        cant=int(len(portf.projects)/4)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        portf.update()
        portf.make_factible()
        return portf    

###############################################
       
class SwapThird(BaseHeuristic):    #quita o pone 2 proyectos, aleatorio
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        cant=int(len(portf.projects)/3)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        portf.update()
        portf.make_factible()
        return portf
###############################################
            
class ShakeArea(BaseHeuristic):    
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        num=random.choice(range(portf.num_areas))     
        for i in portf.projects:        
            if i.area==num:                    
                    i.active=not i.active
        portf.update()                
        portf.make_factible()
        return portf
        
###############################################
            
class ShakeRegion(BaseHeuristic):    
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        num=random.choice(range(portf.num_regions))
        for i in portf.projects:        
            if i.region==num:                    
                    i.active=not i.active
        portf.update()                
        portf.make_factible()
        return portf
###############################################
            
class SwapHalf(BaseHeuristic):    #quita o pone 2 proyectos, aleatorio
    def __init__(self, ID, kind,in_use, rank):
        super().__init__(ID, kind,in_use, rank)
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        cant=int(len(portf.projects)/2)
        li= list(range(len(portf.projects)))
        random.shuffle(li)
        l2=li[:cant]
        for i in l2:
           portf.projects[i].active=not portf.projects[i].active
        portf.update()
        portf.make_factible()
        return portf     
################################################
      
class AddRandom(BaseHeuristic):   
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        nonactives=[]
        for i in portf.projects:
            if i.active==False:              
                nonactives.append(i.ID)                      
        if (len(nonactives)>0):           
            portf.projects[random.choice(nonactives)].active=True
        portf.update()
        portf.make_factible()
        return portf
    
################################################
class AddLowBgt(BaseHeuristic):  #Añade el de menos presupuesto 
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        lower=portf.budget
        temp=0
        for i in portf.projects:
            if i.active==False:
                if i.request_budget<lower:
                    lower=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=True 
        portf.update()                
        portf.make_factible()
        return portf      

################################################
class AddMaxBgt(BaseHeuristic):  
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        m=0
        temp=0
        for i in portf.projects:
            if i.active==False:
                if i.request_budget>m:
                    m=i.request_budget
                    temp=i.ID
        portf.projects[temp].active=True  
        portf.update()             
        portf.make_factible()
        return portf  

################################################# 
class DrawRandom(BaseHeuristic):   
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
        h.apply(portf) 
        portf.make_factible()
        return portf 
#########################    
class UseBudgetAT(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
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
                                                                           
        portf.make_factible()
        return portf 
    
 ################################################
class DrawHightBgt(BaseHeuristic):   #Saca el de mayor presupuesto
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
        h.apply(portf)           
        portf.make_factible()
        return portf  
###################################################
            
class DrawRandomPutLessBgt(BaseHeuristic):   #Draw one ramdom and put one with less budget req
    def __init__(self, ID, kind,in_use,rank):  
        super().__init__(ID,kind,in_use,rank)
       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
                    portf.update()
                    portf.make_factible()
                    return portf
        portf.update()
        portf.make_factible()
        return portf 
               
                    ###############
######################## Area ###########################

class SwapArea(BaseHeuristic):   #Draw one ramdom and put one from other area
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
                    portf.update()
                    portf.make_factible()
                    return portf
        portf.update()
        portf.make_factible()
        return portf

###########################################################
        
class IncreseBgtArea(BaseHeuristic):   #Draw one ramdom and put one with more budget in same area
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank) 
        
    def apply(self, portfolio):
        self.in_use+=1
#        print(self.ID)
        portf = super().apply(portfolio)
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
                        portf.update()
                        portf.make_factible()
                        return portf
        portf.update()
        portf.make_factible()
        return portf 


###########################################################
class DecreaseBgtArea(BaseHeuristic):     #Draw one ramdom and put one with less budget in same area
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
                        portf.update()
                        portf.make_factible()
                        return portf
        portf.update()
        portf.make_factible()
        return portf   

                           #############
############################## Region ############################
  
class SwapRegion(BaseHeuristic):   #Draw one ramdom and put one in other region
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
                    portf.update()
                    portf.make_factible()
                    return portf
        portf.update()
        h=UseBudgetAT(20, 2, 0, 1)   
        h.apply(portf) 
        portf.make_factible()
        return portf 

###################################################################   
class IncreseBgtRegion(BaseHeuristic):   #Draw one ramdom and put one with more budget in same region
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
                        portf.update()
                        portf.make_factible()
                        return portf
        portf.update()
        portf.make_factible()
        return portf 

###########################################################
class DecreaseBgtRegion(BaseHeuristic):     #Draw one ramdom and put one with less budget in same area
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
#        print(self.ID)
        portf = super().apply(portfolio)
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
                        portf.update()
                        portf.make_factible()
                        return portf
        portf.update()
        portf.make_factible()
        return portf
    
#########****************NPORTFOLIO*****************##############

class MoreProj(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        change=False
        portf = super().apply(portfolio)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
                if not prj.active and diff > prj.min_budget:                   
                    prj.active = True
                    change=True
                    prj.set_budget(prj.min_budget)
                    diff -= prj.min_budget                       
                    portf.update()
        if change:
            h=UseBudget(21, 4, 0, 1)   
            h.apply(portf)            
        portf.make_factible()
        
        return portf

###########################################################
        
class QuitBad(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        bad=0
        portf = super().apply(portfolio)
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
        h.apply(portf)            
        portf.make_factible()        
        return portf



######################################################################     
class UseBudget(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
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
        portf.make_factible()
        return portf    
    
    
######################################################################
class SetPrjMinFill(BaseHeuristic): #Selects a project, fill activities random till min bdg, don't change status
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
        selected=random.choice(portf.projects) 
        selected.set_budget(selected.min_budget)  
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.apply(portf)   
        portf.make_factible()
        return portf
    
#######################################################################
        
class SetPrjRndFill(BaseHeuristic): 
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
        selected=random.choice(portf.projects) 
        selected.set_budget(int(uniform(selected.min_budget, selected.max_budget)))
        portf.update()
        h=MoreProj(17, 4, 0, 1)        
        portf=h.apply(portf)  
        portf.make_factible()
        return portf

####################################    
class ProjMin(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
        selected=random.choice(portf.projects) 
        selected.set_budget=selected.min_budget                
        portf.update()
        portf.make_factible()              
        return portf


    
########***********Shake***********########
class AllRandN(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
        for x in portf.projects:
            x.set_budget( uniform(x.min_budget, x.max_budget))                   
        portf.update()  
        portf.make_factible()            
        return portf
 
 
    
    
    
    
########***********MLOCAL***********########


#class MMoreProj(BaseHeuristic): mal
#    def __init__(self, ID, kind,in_use,rank):
#        super().__init__(ID,kind,in_use,rank)       
#    
#    def apply(self, portfolio):
#        print(self.ID)
#        self.in_use+=1
#        portf= copy.deepcopy(portfolio)
#        diff = portf.budget - portf.total_bgt
#        if diff > 0:
#            for prj in portf.projects:
#                if not prj.active and diff > prj.min_budget:
#                    if portf.areas[prj.area_limits][1] - portf.areas[prj.area_limits][2] >= prj.min_budget and portf.region_limits[prj.area][1] - portf.region_limits[prj.area][2] >= prj.min_budget:
#                        prj.active = True
#                        prj.set_budget(prj.min_budget)
#                        diff -= prj.min_budget                        
#                        portf.update()                        
#        portf.make_factible()
#        return portf

######################################################################  
class MTrySetMax(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
#        print(self.ID)
        portf = super().apply(self,portfolio)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
                if prj.active and diff >= prj.min_budget:                   
                    if prj.min_budget<=diff:                        
                        prj.set_budget
                        (diff)
                        if prj.max_budget<=diff:
                           diff-=prj.max_budget
                        else:
                           diff=0                                                                                
        portf.update()                   
        portf.make_factible()
        return portf
       
#######################################################################
        
class MSetPrjRnd(BaseHeuristic): #Selects a project, fill activities random g
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
#        print(self.ID)
        portf = super().apply(self,portfolio)
        selected=random.choice(portf.projects) 
        selected.random_budget()           
        portf.update()
        portf.make_factible()
        return portf

#######################################################################
class MMoreProj(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        change=False
        portf = super().apply(portfolio)
        diff = portf.budget - portf.total_bgt
        if diff > 0:
            for prj in portf.projects:
                if not prj.active and diff > prj.min_budget:                   
                    prj.active = True
                    change=True
                    prj.set_budget(prj.min_budget)
                    diff -= prj.min_budget                       
                    portf.update()
        if change:
            h=UseBudget(21, 4, 0, 1)   
            h.apply(portf)            
        portf.make_factible()
        
        return portf

######################################################################     
class MUseBudget(BaseHeuristic):
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
        self.in_use+=1
        portf = super().apply(portfolio)
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
        portf.make_factible()
        return portf    
    
#####################################
class MChange5perc(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)          

    def apply(self, portfolio):
        self.in_use+=1
#        print(self.ID)
        portf = super().apply(portfolio)
        for i in portf.projects:
            if (random.choice([True,False])):              
                i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20)) 
            else:
                i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))
       
        portf.update()  
        portf.make_factible()            
        return portf
    
#####################################
class MMore5perc(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        i=random.choice(portf.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/20))            
        portf.update()  
        portf.make_factible()            
        return portf

#####################################
class MLess5perc(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)           
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        i=random.choice(portf.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/20))                
        portf.update()  
        portf.make_factible()            
        return portf   
#####################################
        
    
    
    
    
class MMore10perc(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)       
    
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        i=random.choice(portf.projects)                        
        i.set_budget(i.request_budget+((i.max_budget-i.min_budget)/10))
        portf.update()  
        portf.make_factible()            
        return portf

#####################################
class MLess10perc(BaseHeuristic):    
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)           
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
        i=random.choice(portf.projects)         
        i.set_budget(i.request_budget-((i.max_budget-i.min_budget)/10))                    
        portf.update()  
        portf.make_factible()            
        return portf     
##########################################
class DrawHightBgtAndFill(BaseHeuristic):   #Saca el de mayor presupuesto y llena
    def __init__(self, ID, kind,in_use,rank):
        super().__init__(ID,kind,in_use,rank)
        
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
        portf = super().apply(portfolio)
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
        portf=h.apply(portf)        
        portf.update()              
        portf.make_factible()
        return portf 
############################################
class DrawRandFill(BaseHeuristic):   #Draw one ramdom and put one with less budget req
    def __init__(self, ID, kind,in_use,rank):  
        super().__init__(ID,kind,in_use,rank)
       
    def apply(self, portfolio):
#        print(self.ID)
        self.in_use+=1
          
        portf = super().apply(portfolio)
        li = list(range(len(portf.projects))) 
        random.shuffle(li)
        for i in li:
            if portf.projects[i].active: 
                portf.projects[i].active=True
                portf.update()
                break                  
        h=MoreProj(17, 4, 0, 1)        
        portf=h.apply(portf)           
        portf.make_factible()
        return portf 
  