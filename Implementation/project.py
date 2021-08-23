from abc import ABC, abstractmethod
from dataclasses import dataclass
import copy
import random
from numpy.random import uniform


@dataclass
class Project(ABC):
    # Constructor
    def __init__(self, ID, request_budget, impact, active):
        super().__init__()
        self.ID = ID

        self.request_budget = request_budget
        self.impact = impact
        self.active = active

    # Class members region
    def set_budget(self, budget):
        assert float(budget) or budget > 0, "Severe error: Budget can't be a negative number!"
        self.request_budget = budget

    def set_impact(self, impact):
        self.impact = impact

    def add_impact(self, impact):
        self.impact.append(impact)

    def set_active(self, active):
        self.active = active

    def set_ID(self, ID):
        self.ID = ID

    # Class properties region
    @property
    def get_ID(self):
        return self.ID

    @property
    def get_budget(self):
        return self.request_budget

    @property
    def get_impact(self):
        return self.impact

    @property
    def get_active(self):
        return self.active

class ProjectB(Project):
    def __init__(self, ID, request_budget, area, region, impact, active):
        super().__init__(ID, request_budget, impact, active)
        self.area = area
        self.region = region

class ProjectA(Project):
    def __init__(self, ID, min_budget, max_budget, area, region, impact, real_impact, request_budget, active):
        super().__init__(ID, request_budget, impact, active)
        self.area = area
        self.region = region
        self.min_budget = min_budget
        self.max_budget = max_budget
        self.real_impact = real_impact
     
    def random_budget(self):
        self.request_budget = random.randint(self.min_budget,self.max_budget)
        m = 0.3 / (self.max_budget - self.min_budget)  # esto sale de asumir que el mínimo implica disminuir benef al 70%
        for i in range(len(self.impact)):
            self.real_impact[i] = round((m * (self.request_budget - self.min_budget) + 0.7 )* self.impact[i])
    
    def set_budget(self, to_asign):
        if to_asign <= self.min_budget:
            self.request_budget = self.min_budget
            m = 0.3 / (self.max_budget - self.min_budget)  # esto sale de asumir que el mínimo implica disminuir benef al 70%
            for i in range(len(self.impact)):
                self.real_impact[i] = round((m * (self.request_budget - self.min_budget) + 0.7) * self.impact[i])
        elif to_asign >= self.max_budget:
            self.request_budget = self.max_budget
            self.real_impact=self.impact

        else:
            self.request_budget = to_asign
            m = 0.3 / (self.max_budget - self.min_budget)  # esto sale de asumir que el mínimo implica disminuir benef al 70%
            for i in range(len(self.impact)):
                self.real_impact[i] = round((m * (self.request_budget - self.min_budget) + 0.7) * self.impact[i])

class ProjectC(Project):
    def __init__(self, ID, min_budget, max_budget, area, impact, activities, real_impact, request_budget, active):
        super().__init__(ID, request_budget, impact, active)
        self.min_budget = min_budget
        self.area = area
        self.activities = activities
        self.real_impact = real_impact
        self.max_budget = max_budget
        # self.profit = 0  #Se usa para ordenar los proyectos de acuerdo al beneficio
    
    def make_factible(self,value):
        real_impact = 0
        request_budget = 0
        value=value
        for i in self.activities:
            if value<self.min_budget:
                if i.asigned_budget<i.rmax:   
                    val=random.randint(int(i.asigned_budget),int(i.rmax))
                    value=value+val-i.asigned_budget
                    i.set_budget(val,self.impact)                   
            real_impact = real_impact + i.real_impact
            request_budget = request_budget + i.asigned_budget
        self.real_impact = real_impact
        self.request_budget = request_budget
       
        
    
    
    def update(self):
        real_impact = 0
        request_budget = 0
        for i in self.activities:
            real_impact = real_impact + i.real_impact
            request_budget = request_budget + i.asigned_budget
        if request_budget<self.min_budget:
            self.make_factible(request_budget)
        
        else:
            self.real_impact = real_impact
            self.request_budget = request_budget
            if self.real_impact==0 or self.request_budget==0:
                self.profit=0
            else:
                self.profit = round(self.real_impact / self.request_budget * 1e6, 2)

      
    def save(self):  # abstract method
        data = dict(
            ID=self.ID,
            budget=self.request_budget,
            area=self.area,
            impact=self.impact,
            active=self.active
        )
        return data

    def print(self):
        print("{0} {1} {2} {3} {4} {5} {6} {7}".format(
            self.ID,
            self.min_budget,
            self.request_budget,
            self.area,
            self.impact,
            self.real_impact,
            self.active,
            self.profit)
        )
#        for act in self.activities:
#            print("[{0} -> {1} {2} {3}]".format(act.num, act.profit, act.rmin, act.imp))

    def set_budget(self, budget):
         
        real_impact = 0
        request_budget = 0
        if budget>=self.min_budget:           
            for i in self.activities:
                if budget>=i.rmax and i.imp>0:               
                    i.set_budget(i.rmax,self.impact)
                    real_impact = real_impact + i.real_impact
                    request_budget = request_budget + i.asigned_budget
                    budget-=i.rmax
                elif budget>=i.rmin and i.imp>0:
                    i.set_budget(budget,self.impact)
                    real_impact = real_impact + i.real_impact
                    request_budget = request_budget + i.asigned_budget
                    self.real_impact = real_impact
                    self.request_budget = request_budget
                    # self.profit = round(self.real_impact / self.request_budget * 1e6, 2)
                    return
            self.real_impact = real_impact
            self.request_budget = request_budget
         
          
    def initial_sol(self):
        self.activities.sort(key=lambda x: x.imp, reverse=True)
        tmp_prj_budget = uniform(self.min_budget + ((self.max_budget - self.min_budget) / 2),
                                 self.max_budget)       
        self.set_budget(tmp_prj_budget)

class Activity():
    def __init__(self, num, imp, rmin, rmax, asigned_budget, real_impact):
        self.num = num
        self.imp = imp
        self.rmin = rmin
        self.rmax = rmax
        self.asigned_budget = asigned_budget
        self.real_impact = real_impact
        self.profit = self.setProfit()
   
    def setProfit(self):
        if self.rmin==0:

            return round(self.imp*1e6,2)
        else:
            return round((self.imp / self.rmin) * 1e6, 2)
        
    def set_budget(self, asigned_budget, project_impact):
        if self.imp==0:
            self.asigned_budget=0
            self.real_impact=0
        else:
       
            if asigned_budget <= self.rmin:
                self.asigned_budget = 0
                self.real_impact = 0
            elif asigned_budget >= self.rmax:
                self.asigned_budget = self.rmax
                self.real_impact = project_impact * self.imp
    
            else:
                self.asigned_budget = asigned_budget
                m = 0.2 / (self.rmax - self.rmin)  # esto sale de asumir que el mínimo implica disminuir benef al 70%
                self.real_impact = (m * (self.asigned_budget - self.rmin) + 0.8) * project_impact * self.imp
