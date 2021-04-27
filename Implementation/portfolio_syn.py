from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
import copy
from project import RProject
import pickle
import random


@dataclass
class Portfolio(ABC):
    # Constructor
    def __init__(self):
        super().__init__()


class Synergy():
    def __init__(self, nombre, tecn, valor, tipo, mina, maxa, cant, active=False):
        self.nombre = nombre
        self.tecn = tecn
        self.valor = valor
        self.tipo = tipo
        self.mina = mina
        self.maxa = maxa
        self.cant = cant
        self.elements = []
        self.active=active

    def AddElement(self, elem):
        self.elements.append(elem)




class NPortfolio(Portfolio):
    def __init__(self, budget, num_projects, num_areas, num_activities, num_synergies, projects, areas, synergies,
                 kind="RPortfolio"):
        self.budget = budget
        self.num_projects = num_projects
        self.num_areas = num_areas
        self.num_activities = num_activities
        self.num_synergies = num_synergies
        self.projects = projects
        self.areas = areas
        self.synergies = synergies

   

    def initial_solution(self):
## The region and area limits are supposed to be  given by DM
        temp_bgt=self.budget
        temp_area=[0]*self.num_areas
        final_imp = 0
        final_bgt = 0
        act_proj = 0
        
        area_bgt = [0] * self.num_areas
        for i in self.projects:            
            i.initial_sol()
       
        for i in self.projects:            
            if i.request_budget<=temp_bgt and temp_area[i.area]<=self.areas[i.area][1]:
                i.active=True
                final_imp=final_imp+i.real_impact
                final_bgt=final_bgt+i.request_budget
                temp_area[i.area]=temp_area[i.area]+i.request_budget
      
        return NSolution(self.budget, self.num_projects, self.num_areas, self.num_activities, self.num_synergies,
                         self.areas, self.projects, self.synergies, final_bgt, area_bgt, [final_imp, act_proj])




    def test_sol(self,address):
## The region and area limits are supposed to be  given by DM
        temp_bgt=self.budget
        temp_area=[0]*self.num_areas
        final_imp = 0
        final_bgt = 0
        act_proj = 0        
        area_bgt = [0] * self.num_areas
        for i in self.projects:            
            i.initial_sol()
       
        for i in self.projects:            
            if i.request_budget<=temp_bgt and temp_area[i.area]<=self.areas[i.area][1]:
                i.active=True
                final_imp=final_imp+i.real_impact
                final_bgt=final_bgt+i.request_budget
                temp_area[i.area]=temp_area[i.area]+i.request_budget
      
        return NSolution(self.budget, self.num_projects, self.num_areas, self.num_activities, self.num_synergies,
                         self.areas, self.projects, self.synergies, final_bgt, area_bgt, [final_imp, act_proj])
class NSolution(Portfolio):
    def __init__(self, budget, n_projects, n_areas, n_activities, n_synergies, areas, projects, synergies, total_budget,
                 area_bgt, total_impact):
        self.budget = budget
        self.nprojects = n_projects
        self.num_areas = n_areas
        self.nactivities = n_activities
        self.nsynergies = n_synergies
        self.areas = areas
        self.projects = projects
        self.synergies = synergies
        self.total_bgt = total_budget
        self.area_bgt = area_bgt
        self.total_impact = total_impact
        self.num_obj = 2  
    
    def make_factible(self):
        while self.is_factible() == False:
          
            for i in range(self.num_areas):
                if self.areas[i][0] > self.area_bgt[i]:
                    self.increase_area(i)                                
                    self.update()
                  
                elif self.areas[i][1] < self.area_bgt[i]:                 
                    self.decrease_area(i)                  
                    self.update()                   
            if self.total_bgt > self.budget:              
                self.decrease_bgt()           
                self.update()
                

    def is_factible(self):
       
        for i in range(self.num_areas):
            if self.areas[i][0] > self.area_bgt[i]:
                return False
            if self.areas[i][1] < self.area_bgt[i]:
                return False
        if self.total_bgt > self.budget:           
            return False
      
        return True


    def __solution():
        return {}
    
    def info(self):
             
        active = str(self.budget)+ ";"  
        self.projects.sort(key=lambda x: x.ID, reverse=False)
        for i in self.projects:
            active = active +str(i.active) + ";" + str (round(i.request_budget,1)) + ";" + str (round(i.real_impact,1))+ ";" 
        impact = ""
        sin=""
        for syn in self.synergies:
            if syn.active:
                sin=sin+"T"
            else:
                sin=sin+"F"
          
            
        for i in self.total_impact:
            impact = impact + str(round(i,1)) + ";"
        info = str(round(self.total_bgt,1)) + ";" + str(self.points) + ";" + impact +sin+";"+ active + "\n"
        return info

    def increase_area(self, area):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area:
                if self.projects[i].active:              
                    if self.projects[i].request_budget<self.projects[i].max_budget:
                        self.projects[i].set_budget(int(random.uniform(self.projects[i].request_budget, self.projects[i].max_budget)))
                        return
                else:
                    self.projects[i].active = True
                    return
        return

    def decrease_area(self, area):
        # print("decrese area")
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area:
                if self.projects[i].active:
                    if self.projects[i].request_budget>self.projects[i].min_budget:                               
                        self.projects[i].set_budget(self.projects[i].min_budget)
                        return    
                    else:
                        self.projects[i].active = False
                        return

    def decrease_bgt(self):      
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:              
            if self.projects[i].active:
                if self.projects[i].request_budget>self.projects[i].min_budget:
                    self.projects[i].set_budget(self.projects[i].min_budget)            
                    return
                else:
                                      
                    self.projects[i].active=False
                    return
                
    def update(self):  # Update total budget asigned to portfolio, also area and region budget                 # Update total impact per objectives
        area_bgt = [0] * self.num_areas
        total_bgt = 0
        total_impact = 0
        act = 0
        
        for project in self.projects:
            if project.real_impact==0 or project.request_budget==0:
                project.active=False
            if project.active:
                act = act + 1
                area_bgt[project.area] = area_bgt[project.area] + project.request_budget
                total_bgt = total_bgt + project.request_budget
                total_impact = total_impact + project.real_impact
        for i in self.synergies:
            act_syn=0
            for elem in i.elements:
                for proj in self.projects:                 
                    if proj.active and str(proj.ID+1)==str(elem[1]):
                        for a in proj.activities:
                            if str(a.num)==str(elem[2]):
                                act_syn+=1
                               
            if act_syn>=  i.mina and act_syn<=i.maxa:
                i.active==True  
                print("T")
                if i.tipo==1:
                    total_impact+=i.valor
                elif i.tipo==2:
                    total_bgt+=i.valor
                elif i.tipo==3:
                    total_bgt-=i.valor
            else: i.active==False
            print("F")
        self.area_bgt = area_bgt
        self.total_impact = [total_impact, act]
        self.total_bgt = total_bgt


    def amINotDominated(self, to_compare):
        for i in range(self.num_obj):
            if to_compare.total_impact[i] > self.total_impact[i]:
                return False
        return True

    def isItNotDominated(self, to_compare):
        for i in range(self.num_obj):
            if self.total_impact[i] > to_compare.total_impact[i]:
                return False
        return True

    def areWeEqual(self, to_compare):
        for i in range(self.num_obj):
            if (self.total_impact[i] != to_compare.total_impact[i]):
                return False
        return True

    def compare(self, to_compare):
        if self.areWeEqual(to_compare):
            return 2
        if self.amINotDominated(to_compare):
            return -1
        if self.isItNotDominated(to_compare):
            return 1
        else:
            return 0

