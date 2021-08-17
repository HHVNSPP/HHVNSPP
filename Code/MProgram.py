# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:56:02 2020

@author: Madys
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:45:00 2020

@author: Madys
"""
import portfolio as prf
import project as prj
import random
import heuristic as hr
import local_search as ls
from adjustment import Adjustment
from project import MProject
from project import NProject
from project import Activity
from MPortafolio import MPortfolio
import os
import numpy as np
import copy
from datetime import datetime, datetime, date, time, timedelta


class Synergy():
    def __init__(self, nombre, tipo, cant, valor, mina, maxa,  elements=None, active=False):

        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo
        self.mina = mina
        self.maxa = maxa
        self.cant = cant
        self.active=active
        if elements == None:
            self.elements = []
        else:
            self.elements = elements

    def AddElement(self, elem):
        self.elements.append(elem)

    def print(self):
        print(self.nombre)
        print(self.elements)




class MProgram():
    def __init__(self, addresses=[], Fer_Update=None):
        self.addresses = addresses
        self.Fer_Update=Fer_Update
    def load_from_Mfile(self, filename):
        
        print("Loading... "+filename)
        f = open(filename+'.txt')
        cantpr = int(f.readline())
        pres = float(f.readline())
        pesos = f.readline()
        pesos = pesos.split(" ")
        pesos1 = []
        for i in pesos:
            i = int(i)
            pesos1.append(i)
        elemtomax = len(pesos1)
        num_syn = int(f.readline())
        # num_syn = 0
        synergies=[]
        for i in range(num_syn):
            line= f.readline()
            line=line.split(" ")
            synergies.append(Synergy(int(line[0]),int(line[1]),int(line[2]), int(line[3]),int(line[4]), int(line[5]), []))
            line= f.readline()
            line=line.split(" ")
            for j in line:
                synergies[i].AddElement(int(j))
                
        projects = []
        real_impact=np.zeros(elemtomax)
        for i in range(cantpr):
            proj = f.readline()
            proj = proj.split()
            tomax = []
#            test=""
            for x in range(elemtomax):
                tomax.append(float(proj[4 + x]))

            projects.append(MProject(i, float(proj[0]), float(proj[1]), int(proj[2]) - 1, int(proj[3]) - 1, tomax,real_impact, 0,False))


        area_limits=[[0.25*pres,0.45*pres],[0.3*pres,0.45*pres],[0.3*pres,0.45*pres]]
        region_limits=[[0.4*pres,0.6*pres],[0.4*pres,0.6*pres]]
        a = MPortfolio(pres, cantpr,pesos1, 3, 2,  projects,area_limits, region_limits,0,[])
        f.close()
        return a

    def apply(self):
        
        
        # times=[0.5,1,2,3,5,7.5,10,12.5,15,17.5,20,23,26,30,35,40,45,50]
       
        for runing_time in [0.5]:
            for address in self.addresses:
           
                for i in range(1):
                    h1 = hr.SwapRandom(1, 1, 0, 5)
                    h2 = hr.SwapQuarter(2, 1, 0, 5)
                    h3 = hr.SwapThird(3, 1, 0, 5)
                    h4 = hr.SwapHalf(4, 1, 0, 5)      
                    h13 = hr.ShakeArea(13, 1, 0, 5)
                    h20 = hr.ShakeRegion(20, 1, 0, 5)
                    h21=hr.AllRandN(21, 1, 0, 5)
                    ############
                    h5 = hr.Swap1(5, 2, 0, 1)
                    h6 = hr.DrawHightBgt(6, 2, 0, 1)
                    h7 = hr.MUseBudget(7, 2, 0, 1)
                    h8 = hr.MMoreProj(8, 2, 0, 1)
                    h9 = hr.DrawRandom(9, 2, 0, 1)
                    h10 = hr.SetPrjMinFill(10, 2, 0, 1)
                    h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
                    h12 = hr.SetPrjRndFill(12, 2, 0, 1)
            
        
                    ######################################
            
                    shake = [h1, h2, h3, h4, h13, h20,h21]
                    local = [h5, h6, h7, h8, h9, h11, h12]
            
                    ################
                    counter=0
                    iterate=1 #num iteracion
                    stop=1
                    heuristics_data=""
                    starttime = datetime.now()
                    a = self.load_from_Mfile(address)
                    b = a.initial_solution()
    #                b.print()
                    b.make_factible()
    #                b.print()
                    adjustment = Adjustment(b, b, shake, a.weights, [], 4, 0,counter,heuristics_data)
                    
                    
                    while adjustment.nim > adjustment.nima and datetime.now()-starttime<timedelta (minutes=runing_time)and stop<4100: 
                     #El segundo parámetro es la cantidad de veces sin mejora para búsqueda local, el cuarto es True para ajustes de Fernando, False, como estaba
                        lsearch = ls.LocalSearch(adjustment.shaked, 20, local,self.Fer_Update)
                        lista = lsearch.apply()
                        adjustment.apply(lista)
                        if stop==iterate:    
                            adjustment.apply_electre()
                            endtime = datetime.now() - starttime
                         
                            file = open("sol_" + address+".csv", "a+")
                            for sol in adjustment.solutions:
                                file.write("{0};{1};{2};{3};{4}".format( starttime, stop,str(self.Fer_Update), round(endtime.total_seconds()), sol.info()) )                                         
                            file.close()
                            stop=stop*2                       
                        iterate=iterate+1
                    adjustment.apply_electre()
                    endtime = datetime.now() - starttime
                    file = open("sol_" + address+".csv", "a+")
                    for sol in adjustment.solutions:
                        file.write("{0};{1};{2};{3};{4}".format( starttime, iterate,str(self.Fer_Update), round(endtime.total_seconds()), sol.info())  )                                        
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
a=MProgram(["mns4obj100_1"],True)
# a=MProgram(["m_4obj_64_2.txt","m_4obj_64_2_ns.txt","m_4obj_128_1.txt","m_4obj_128_1_ns.txt","m_4obj_256_1.txt","m_4obj_256_1_ns.txt","m_4obj_512_1.txt","m_4obj_512_1_ns.txt"])
# a=MProgram(["m_4obj_512_3.txt","m_4obj_1024_1.txt","m_4obj_1024_2.txt","m_4obj_1024_3.txt"])
a.apply()