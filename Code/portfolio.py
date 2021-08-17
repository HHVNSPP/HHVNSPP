#-----------------------------------------
# cambios introducidos  a la clase Portfolio para incluir referencia a la heuristica que crea la solucion
# decidi modificar esta clase pues no existe una clase general para la solucion, de esta manera los cambios son minimos
# tambien pase los metodos relativos a la comparacion de dominancia a la clase base, asi todas las soluciones los heredan.
#------------------------------------------
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
import copy
from project import RProject
import pickle
import random


@dataclass
class Portfolio(ABC):
    # Constructor
    # ----------------parametros adicionados por fernando 27 de julio del 2021, los pesos y indica la heuristica que creo la solucion
    def __init__(self, weights=None, num_obj=None):
    #-------------------------------------------------------------------------------------------------------------------
        super().__init__()
        self.total_impact = []
        # ----------------linea adicionada por fernando 27 de julio del 2021
        # Indica la heuristica que lo creo (si es una solucion), si aplica, de lo contrario es None
        self.createdby = None
        self.num_obj=num_obj
        # ------------------------------------------------------------------

    #--------metodos adicionados por fernando 27 de julio del 2021
    def setheur(self, heur):
        self.createdby = heur

    def getheur(self): # get  reference to the heuristic that created the solution
        return self.createdby
    #---------------------------------------------------------
    #------------metodos modificados por fernando 27/07/2021
    #-----------la implementacion de no dominancia estaba mal, ahora ya esta corregida
    def amINotDominated(self, to_compare):
        greater_equal = 0
        greater = False
        for i in range(self.num_obj):
            if self.total_impact[i] >= to_compare.total_impact[i] :
                greater_equal += 1
                if self.total_impact[i] > to_compare.total_impact[i] :
                    greater = True
        return greater == True and greater_equal == self.num_obj

    def isItNotDominated(self, to_compare):
        greater_equal = 0
        greater = False
        for i in range(self.num_obj):
            if to_compare.total_impact[i] >= self.total_impact[i] :
                greater_equal += 1
                if to_compare.total_impact[i] > self.total_impact[i] :
                    greater = True
        return greater == True and greater_equal == self.num_obj

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

class RPortfolio(Portfolio):
    def __init__(self, budget, num_obj, num_areas, num_reg, weights=None, projects=None, kind="RPortfolio"):
        super().__init__()
        self.budget = budget
        self.kind = kind
        self.num_obj = num_obj
        if weights == None:
            self.weights = []
        else:
            self.weights = weights
        if projects == None:
            self.projects = []
        else:
            self.projects = projects
        self.num_areas = num_areas
        self.num_reg = num_reg
        if len(weights) == num_obj:
            self.weights = copy.deepcopy(weights)
        else:
            print("Number of objectives different from number of weights")

        try:
            if len(projects) > 0:
                self.projects = copy.deepcopy(projects)
            else:
                self.projects = projects
        except MemoryError:
            print("Severe error: an exception has occurred on deep copying file")


    def add_project(self, project):
        self.projects.append(project)


    def load(self, filename):
        print("Loading....")
        prj_file = open(filename, 'rb')
        prj_header = pickle.load(prj_file)
        for i in prj_header.keys():
            print(i, prj_header[i])
        prj_file.close()

    ### Solution has values of impact(beneficts) normalized and multiplied by weights
    def initial_solution(self):  ## The region and area limits are supposed to be  given by DM
        #        benef=[]
        area_bgt = [0] * self.num_areas
        region_bgt = [0] * self.num_reg
        total_impact = [0] * self.num_obj
        total_bgt = 0

        lim_inf_area = [0.3 * self.budget, 0.25 * self.budget, 0.2 * self.budget]
        lim_sup_area = [0.4 * self.budget, 0.35 * self.budget, 0.3 * self.budget]
        lim_inf_region = [0.4 * self.budget, 0.4 * self.budget]
        lim_sup_region = [0.6 * self.budget, 0.6 * self.budget]

        for i in self.projects:
            i.active = random.choice([True, False])
            #            for index in range(self.num_obj):
            #                i.impact[index]=float(self.weights[index])/100*(i.impact[index]-benef[index][0])/(benef[index][1]-benef[index][0])
            if i.active:
                area_bgt[i.area - 1] = area_bgt[i.area - 1] + i.request_budget
                region_bgt[i.region - 1] = region_bgt[i.region - 1] + i.request_budget
                total_bgt = total_bgt + i.request_budget
                for index1 in range(self.num_obj-1):
                    total_impact[index1] = total_impact[index1] + i.impact[index1]
                    total_impact[self.num_obj-1]=total_impact[index1]
        return RSolution(self.budget, "RPortfolio", self.num_obj, self.num_areas, self.num_reg, self.projects,
                         lim_inf_area, lim_sup_area, lim_inf_region, lim_sup_region, area_bgt, region_bgt, total_bgt,
                         total_impact)

  
    
    
class RSolution(Portfolio):

    def __init__(self, budget, kind="RPortfolio", num_obj=4, num_areas=3, num_regions=2, projects=[], lim_inf_area=[],
                 lim_sup_area=[], lim_inf_region=[], lim_sup_region=[], area_bgt=[], region_bgt=[], total_bgt=0,
                 total_impact=[], points=0):
        super().__init__()
        self.budget = budget
        self.kind = kind
        self.num_obj = num_obj
        self.num_areas = num_areas
        self.num_regions = num_regions
        self.projects = projects
        self.lim_inf_area = lim_inf_area
        self.lim_sup_area = lim_sup_area
        self.lim_inf_region = lim_inf_region
        self.lim_sup_region = lim_sup_region
        self.area_bgt = area_bgt
        self.region_bgt = region_bgt
        self.total_impact = total_impact
        self.total_bgt = total_bgt
        self.points = points


    def update(self):  # Update total budget asigned to portfolio, also area and region budget
        #          Update total impact per objectives
        area_bgt = [0] * self.num_areas
        region_bgt = [0] * self.num_regions
        total_impact = [0] * self.num_obj
        total_bgt = 0
        for project in self.projects:
            if project.active:
                area_bgt[project.area] = area_bgt[project.area] + project.request_budget
                region_bgt[project.region] = region_bgt[project.region] + project.request_budget
                total_bgt = total_bgt + project.request_budget
                for index in range(self.num_obj-1):
                    total_impact[index] = total_impact[index] + project.impact[index]
                    total_impact[self.num_obj-1]=total_impact[index]
        self.area_bgt = area_bgt
        self.region_bgt = region_bgt
        self.total_impact = total_impact
        self.total_bgt = total_bgt

    def checkareas(self):
        area1 = 0
        area2 = 0
        area3 = 0
        for project in self.projects:
            if project.area == 0:
                area1 = area1 + project.request_budget
            if project.area == 1:
                area2 = area2 + project.request_budget
            if project.area == 2:
                area3 = area3 + project.request_budget
        print(self.lim_inf_area)
        print(str(area1) + " " + str(area2) + " " + str(area3))


    def make_factible(self):

        while self.is_factible() == False:

            for i in range(self.num_areas):
                if self.lim_inf_area[i] > self.area_bgt[i]:
                    self.increase_area(i)
                    self.update()
                elif self.lim_sup_area[i] < self.area_bgt[i]:
                    self.decrease_area(i)
                    self.update()
            for i in range(self.num_regions):
                if self.lim_inf_region[i] > self.region_bgt[i]:
                    self.increase_region(i)
                    self.update()
                elif self.lim_sup_region[i] < self.region_bgt[i]:
                    self.decrease_region(i)
                    self.update()
            if self.total_bgt > self.budget:
                self.decrease_bgt()
                self.update()

    def is_factible(self):
        for i in range(self.num_areas):
            if self.lim_inf_area[i] > self.area_bgt[i]:
                return False
            if self.lim_sup_area[i] < self.area_bgt[i]:
                return False
        for i in range(self.num_regions):
            if self.lim_inf_region[i] > self.region_bgt[i]:
                return False
            if self.lim_sup_region[i] < self.region_bgt[i]:
                return False
        if self.total_bgt > self.budget:
            return False
        return True

    def increase_area(self, area):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area and self.projects[i].active == False:
                self.projects[i].active = True
                return

    def decrease_area(self, area):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area and self.projects[i].active == True:
                self.projects[i].active = False
                return

    def decrease_region(self, region):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].region == region and self.projects[i].active == True:
                self.projects[i].active = False
                return

    def increase_region(self, region):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].region == region and self.projects[i].active == False:
                self.projects[i].active = True
                return

    def decrease_bgt(self):
        nonactives = []
        actives = []
        #        rand=[True,False]
        for i in self.projects:
            if i.active:
                actives.append(i.ID)
            else:
                nonactives.append(i.ID)
        selected = random.choice(actives)
        self.projects[selected].active = False

 

    def info(self):
        active = ""
        # for i in self.projects:
        #     active = active + str(i.active)+ ";"
        impact = ""
        for i in self.total_impact:
            impact = impact + str(i) + ";"
        info = str(self.total_bgt) + ";" + str(self.points) + ";" + impact + active + "\n"
        return info

    def save(self, filename):
        prf_file = open(filename, 'wb')
        prf_data = dict(
            budget=self.budget,
            kind=self.kind,
            area=self.weights,
            weights=self.weights,
            projects=[]
        )
        try:
            for prj in self.projects:
                prf_data["projects"].append(prj.save())
        except AssertionError:
            print("Severe error: Invalid project instance!!!")

        pickle.dump(prf_data, prf_file)
        print("Saving....")
        prf_file.close()

    def load(self, filename):
        print("Loading....")
        prj_file = open(filename, 'rb')
        prj_header = pickle.load(prj_file)
        for i in prj_header.keys():
            print(i, prj_header[i])
        prj_file.close()



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
#        print("initial")## The region and area limits are supposed to be  given by DM
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
        # print("make factible")
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
        for i in self.total_impact:
            impact = impact + str(round(i,1)) + ";"
        info = str(round(self.total_bgt,1)) + ";" + str(self.points) + ";" + impact + active + "\n"
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
        self.area_bgt = area_bgt
        self.total_impact = [total_impact, act]
        self.total_bgt = total_bgt

