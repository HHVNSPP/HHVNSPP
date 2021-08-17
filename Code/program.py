# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:03:00 2019

@author: Madys
"""

import portfolio as prf
import project as prj
import random
import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from project import RProject
from project import NProject
from project import Activity
from portfolio import NPortfolio
from portfolio import Synergy
import os
import numpy as np
import copy
from datetime import datetime,datetime, date, time, timedelta




class NProgram():
    def __init__(self, addresses,Fer_Update=None):
        self.addresses = addresses
        self.Fer_Update=Fer_Update
    def ReadNF(self, param, address):

        f = open(address)
        for line in f:
            if line.find(param) != -1:
                a = line.lstrip(param)
                b = a.find(";")
                f.close()
                return a[0:b]

    def ReadAreas(self, address, nareas):
        if nareas == 0:
            print("Wrong number of areas")
            return
        f = open(address)
        first = False
        areas = []
        while True:
            aux = f.readline()
            if aux.find("Areas=") != -1:
                first = True
                aux = f.readline()
            if first:
                for char in aux:
                    if char in " <>}];\n":
                        aux = aux.replace(char, '')
                temp = aux.split(",")
                areas.append([float(temp[0]), float(temp[1]), 0])  # min_bdg, max_bgt, real_bgt
                nareas = nareas - 1
            if nareas == 0:
                f.close()
                return areas

    def ReadProjects(self, address, nprojects):
        if nprojects == 0:
            print("Wrong number of areas")
            return
        f = open(address)
        first = False
        projects = []
        count = 0
        while True:
            aux = f.readline()
            if aux.find("Projects=") != -1:
                first = True
                aux = f.readline()
            if first:
                for char in aux:
                    if char in " <>}];\n":
                        aux = aux.replace(char, '')
                temp = aux.split(",")
                projects.append(
                    NProject(count, float(temp[0]), float(temp[1]), int(temp[2]) - 1, float(temp[3]), [], 0, 0, False))
                nprojects = nprojects - 1
                count += 1
            if nprojects == 0:
                f.close()
                return projects

    def ReadActivities(self, address, nprojects, nactivities, projects):
        f = open(address)
        total = nprojects * nactivities
        first = False
        while True:
            if total == 0:
                f.close()
                return
            aux = f.readline()
            if aux.find("Activities=") != -1:
                first = True
                aux = f.readline()
            if first:
                if first:
                    for char in aux:
                        if char in " <>}];\n":
                            aux = aux.replace(char, '')
                            temp = aux.split(",")
                # print(temp[0]+" "+temp[1]+ " "+temp[2]+" "+temp[3]+" "+temp[4])
                projects[int(temp[0]) - 1].activities.append(
                    Activity(int(temp[1]) - 1, float(temp[2]), float(temp[3]), float(temp[4]), 0, 0))
                total = total - 1
            if total == 0:
                f.close()
                return projects

    def ReadSynergies(self, address, nsynergies):
        f = open(address)
        first = False
        synergies = []
        while True:
            if nsynergies == 0:
                f.close()
                return synergies
            aux = f.readline()
            if aux.find("Synergies=") != -1:
                first = True
                aux = f.readline()
            if first:
                for char in aux:
                    if char in " <>}];\n":
                        aux = aux.replace(char, '')
                        temp = aux.split(",")
                synergies.append(Synergy(int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]), int(temp[5]),
                            int(temp[6])))
                nsynergies = nsynergies - 1
            if nsynergies == 0:
                f.close()
                return synergies

    def ReadSItem(self, address, nsynergies, synergies):
        f = open(address)
        first = False
        while True:
            if nsynergies == 0:
                f.close()
                return synergies
            aux = f.readline()
            if aux.find("SItems=") != -1:
                first = True
            if first:
                if first:
                    aux = aux.split(">,<")
                    for i in aux:
                        for char in i:
                            if char in " SItems= [{\n}]<>;":
                                i = i.replace(char, '')
                        i = i.split(",")
                        synergies[int(i[0]) - 1].AddElement([int(i[0]), int(i[1]), int(i[2])])
                    nsynergies = nsynergies - 1
            if nsynergies == 0:
                f.close()
                return synergies

    def loadfromNfile(self, address):
        budget = float(self.ReadNF("budget= ", address))
        nprojects = int(self.ReadNF("nprojects=", address))
        nareas = int(self.ReadNF("nareas= ", address))
        nactivities = int(self.ReadNF("nactivities= ", address))
        nsynergies = int(self.ReadNF("nsynergies= ", address))
        areas = self.ReadAreas(address, nareas)
        projects = self.ReadProjects(address, nprojects)
        self.ReadActivities(address, nprojects, nactivities, projects)
        # for i in projects:
        #     i.reorder()2
        synergies=[]
        # synergies = self.ReadSynergies(address, nsynergies)
        # synergies = self.ReadSItem(address, nsynergies, synergies)
        return (NPortfolio(budget, nprojects, nareas, nactivities,
                           nsynergies, projects, areas, synergies, kind="RPortfolio"))

    def apply(self):
       
       for runing_time in [0.5]:
            for address in self.addresses:
                
                print(address)
                for i in range(1):
                    h0= hr.AllRandN(0, 1, 0, 5)
                    h1 = hr.SwapRandom(1, 1, 0, 5)
                    h2 = hr.SwapQuarter(2, 1, 0, 5)
                    h3 = hr.SwapThird(3, 1, 0, 5)
                    h4 = hr.SwapHalf(4, 1, 0, 5)
                    h5 = hr.ShakeArea(5, 1, 0, 5)
                   
                    ############
                    h6 = hr.Swap1(6, 2, 0, 1)                                         
                    h7 = hr.DrawHightBgtAndFill(7, 2, 0, 1)
                    h8 = hr.DrawRandFill(8, 1, 0, 1)                                       
                    h9 = hr.MoreProj(9, 4, 0, 1)
                    h10=hr.SetPrjMinFill(10, 4, 0, 1)                                
                    h11=hr.UseBudget(11, 4, 0, 1)
                    h12=hr.SetPrjRndFill(12, 4, 0, 1)
                    h13=hr. QuitBad(13, 4, 0, 1)
                
                
                   
                    shake = [h0, h1, h2, h3, h4, h5]       
                    local = [h6,h7,h8,h9,h10,h11,h12,h13]
                    
  
                    counter=0
                    iterate=1 #num iteracion
                    stop=1
                    heuristics_data=""
                    starttime = datetime.now()
                    a = self.loadfromNfile(address)
                    b = a.initial_solution()
                   
                    b.make_factible()       
                    adjustment = Adjustment(b, b, shake, [0.5, 0.5], [], 5, 0, counter, heuristics_data)
                  
                    
                    while adjustment.nim > adjustment.nima and datetime.now()-starttime<timedelta (minutes=runing_time)and stop<2049: 
                        lsearch = ls.LocalSearch(adjustment.shaked, 20, local,self.Fer_Update)
                        lista = lsearch.apply()
                        adjustment.apply(lista)
                        if stop==iterate:    
                            adjustment.apply_electre()
                            endtime = datetime.now() - starttime
                         
                            file = open("sol_" + address+".csv", "a+")
                            for sol in adjustment.solutions:
                                file.write("{0};{1};{2};{3};{4}".format( starttime, stop,str(self.Fer_Update), round(endtime.total_seconds()), sol.info()))                                          
                            file.close()
                            stop=stop*2                       
                        iterate=iterate+1
                    adjustment.apply_electre()
                    endtime = datetime.now() - starttime
                    file = open("sol_" + address+".csv", "a+")
                    for sol in adjustment.solutions:
                        file.write("{0};{1};{2};{3};{4}".format( starttime, iterate,str(self.Fer_Update), round(endtime.total_seconds()), sol.info()))                                          
                    file.close()  
                    to_save=""
                    shake.sort(key=lambda x: x.ID, reverse=False)
                    local.sort(key=lambda x: x.ID, reverse=False)
                    for h in shake:
                        to_save= to_save+"; " + str(h.in_use) 
                    for h in local:                 
                        to_save= to_save+ "; "+  str(h.in_use)
                    file1 = open("h_" + address+ ".csv", "a+") 
                    file1.write(str(starttime)+ to_save+"\n" )
                    file1.close()
                
            
a = NProgram(["P100R5A2S5_1.dat"], True)
a.apply()

