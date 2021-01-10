# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:02:17 2020

@author: Madys
"""
from portfolio import Portfolio
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
import copy
from project import RProject
import pickle
import random


class MPortfolio(Portfolio):
    def __init__(self, budget, num_projects, weights, num_areas, num_regions, projects, area_limits, region_limits, num_synergies, synergies,
                 kind="MPortfolio"):
        self.budget = budget
        self.num_projects = num_projects
        self.num_areas = num_areas
        self.num_regions = num_regions
        self.weights = weights
        self.area_limits=area_limits
        self.region_limits=region_limits
        self.num_synergies = num_synergies
        self.projects = projects      
        self.synergies = synergies

    def initial_solution(self):
#        print("initial") ## The region and area limits are supposed to be  given by DM
        tmp_bgt=self.budget  

        temp_area = [0] * self.num_areas
        temp_region = [0] * self.num_regions
        total_impact=[0]* len(self.weights)
        random.shuffle(self.projects)
        for i in self.projects:     
            i.random_budget()
            if i.request_budget<=tmp_bgt and temp_area[i.area]<=self.area_limits[i.area][1] and temp_region[i.region]<=self.region_limits[i.region][1]:

                i.active=True
                for j in range(len(total_impact)):
                    total_impact[j]=total_impact[j]+i.real_impact[j]                               
                temp_area[i.area]=temp_area[i.area]+i.request_budget
                temp_region[i.region]=temp_region[i.region]+i.request_budget
                tmp_bgt=tmp_bgt-i.request_budget
    
        return MSolution(self.budget, self.weights, self.num_projects, self.num_areas,self.num_regions,self.area_limits, self.region_limits, self.projects,
                         self.budget-tmp_bgt, temp_area, temp_region, total_impact,self.num_synergies,self.synergies )


class MSolution(Portfolio):
    def __init__(self, budget, weights, n_projects, num_areas, num_regions,  area_limits, region_limits, projects, total_budget,
                 area_bgt, region_bgt, total_impact, n_synergies, synergies):
        self.budget = budget
        self.nprojects = n_projects
        self.weights=weights
        self.num_areas = num_areas
        self.num_regions=num_regions
        self.area_limits=area_limits
        self.region_limits=region_limits
        self.nsynergies = n_synergies
        self.projects = projects
        self.synergies = synergies
        self.total_bgt = total_budget
        self.area_bgt = area_bgt
        self.region_bgt=region_bgt
        self.total_impact = total_impact

    
    def make_factible(self):

        while self.is_factible() == False:
            
            for i in range(self.num_areas):

                if self.area_limits[i][0] > self.area_bgt[i]:

                    self.increase_area(i)                 
                    self.update()

                elif self.area_limits[i][1] < self.area_bgt[i]:

                    self.decrease_area(i)
                    self.update()
          
            for i in range(self.num_regions):

                if self.region_limits[i][0] > self.region_bgt[i]:                   
                    self.increase_region(i)                 
                    self.update()
                elif self.region_limits[i][1] < self.region_bgt[i]:
                    self.decrease_region(i)
                    self.update()


            if self.total_bgt > self.budget:
                self.decrease_bgt()                 
                self.update()   
    
    def print(self):
       
        a=str(self.budget)+ " " +str(self.total_bgt)
        for i in self.total_impact:
            a=a+" "+str(i)
        print (a)
        
            
        
    
    def is_factible(self):
        for i in range(self.num_areas):
            if self.area_limits[i][0] > self.area_bgt[i]:
                return False
            if self.area_limits[i][1] < self.area_bgt[i]:
                return False
        for i in range(self.num_regions):
            if self.region_limits[i][0] > self.region_bgt[i]:
                return False
            if self.region_limits[i][1] < self.region_bgt[i]:
                return False
        if self.total_bgt > self.budget:
            return False
        return True

    def __solution():
        return {}
    
    def info(self):
        count=0
        for i in self.synergies:
            if i.active:
                count+=1
      
        proy_en_cart=0
        self.projects.sort(key=lambda x: x.ID, reverse=False)
        for i in self.projects:
          #  active = active +str(i.active) + ";" + str (i.request_budget) + ";"
            if i.active:
                proy_en_cart+=1
        impact = ""
        for i in self.total_impact:
            impact = impact + str(round(i)) + ";"
        info = str(round(self.total_bgt)) + ";" +str(round(self.budget))+ ";"+ str(self.points) + ";" + str(self.nsynergies)+";"+ str(proy_en_cart) +";" + str(count)+ ";"+ impact + "\n"
        return info

    def increase_area(self, area):

        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area:
                if self.projects[i].active:                                 
                         if self.projects[i].request_budget==self.projects[i].max_budget:
                            continue
                         else:
                            self.projects[i].set_budget(self.projects[i].max_budget)  
                            return
                else:
                    self.projects[i].active = True
                    return
                
    def increase_region(self, region):
        
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].region == region:
                if self.projects[i].active:                               
                        if self.projects[i].request_budget==self.projects[i].max_budget:
                            continue
                        else:
                           self.projects[i].set_budget(self.projects[i].max_budget)         
                           return
                else:
                    self.projects[i].random_budget()
                    self.projects[i].active = True
                    
                    return
        
    def decrease_area(self, area):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].area == area:
                if self.projects[i].active:                                      
                        if self.projects[i].request_budget==self.projects[i].min_budget:
                            self.projects[i].random_budget()
                            self.projects[i].active = False
                            return                          
                        else:
                            self.projects[i].set_budget(self.projects[i].min_budget)
                            return
                    
    def decrease_region(self, region):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].region == region:
                if self.projects[i].active:                                  
                    if self.projects[i].request_budget==self.projects[i].min_budget:
                        self.projects[i].random_budget()
                        self.projects[i].active = False
                        return                          
                    else:
                        self.projects[i].set_budget(self.projects[i].min_budget)
                        return

    def decrease_bgt(self):
        li = list(range(len(self.projects)))
        random.shuffle(li)
        for i in li:
            if self.projects[i].active:              
                self.projects[i].active = False
                return

    def update(self):  # Update total budget asigned to portfolio, also area and region budget
        area_bgt = [0] * self.num_areas
        region_bgt = [0] * self.num_regions
        total_bgt = 0
        total_impact = [0]*len(self.weights)
        for project in self.projects:
            if project.active:
                area_bgt[project.area] = area_bgt[project.area] + project.request_budget
                region_bgt[project.region] = region_bgt[project.region] + project.request_budget
                total_bgt = total_bgt + project.request_budget
                for i in range(len(total_impact)):
                    total_impact [i]= total_impact[i] + project.real_impact[i]+125
        self.area_bgt = area_bgt
        self.region_bgt = region_bgt
        self.total_impact = total_impact
        self.total_bgt = total_bgt
        if self.nsynergies>0:
            for synergy in self.synergies: 
                counter=0
                for p in synergy.elements:
                    for i in self.projects:
                        if i.ID==p and i.active:
                            counter+=1
                if counter >=synergy.mina and counter <=synergy.maxa:
                    self.total_bgt=self.total_bgt-(synergy.valor*(counter-synergy.mina+1))
                    synergy.active=True
                else:
                    synergy.active=False

    def amINotDominated(self, to_compare):
        for i in range(len(self.weights)):
            if to_compare.total_impact[i] > self.total_impact[i]:
                return False
        return True

    def isItNotDominated(self, to_compare):
        for i in range(len(self.weights)):
            if self.total_impact[i] > to_compare.total_impact[i]:
                return False
        return True

    def areWeEqual(self, to_compare):
        for i in range(len(self.weights)):
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
