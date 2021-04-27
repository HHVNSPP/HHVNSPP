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
from project import RProject
from project import NProject

from portfolio import NPortfolio
import os
import numpy as np
import copy
from datetime import datetime,datetime, date, time, timedelta


class RProgram():
    def __init__(self, addresses=[]):
        self.addresses = addresses

    def load_from_Rfile(self, filename):
        print("Loading....")
        f = open(filename)
        cantpr = int(f.readline())
        pres = float(f.readline())
        pesos = f.readline()
        pesos = pesos.split()
        pesos1 = []
        for i in pesos:
            i = int(i)
            pesos1.append(i)
        elemtomax = len(pesos1)
        projects = []
        for i in range(cantpr):
            proj = f.readline()
            proj = proj.split()
            tomax = []
            for x in range(elemtomax):
                tomax.append(float(proj[3 + x]))
            projects.append(RProject(i, float(proj[0]), int(proj[1]) - 1, int(proj[2]) - 1, tomax, False))

        a = prf.RPortfolio(pres, elemtomax, 3, 2, pesos1, projects, "RPortfolio")
        f.close()
        return a

    def apply(self):

        for  runing_time in [160 ,200   
                             ]:
            for address in self.addresses:
                for i in range(1):
                    h1 = hr.SwapRandom(1, 1, 0, 5)
                    h2 = hr.SwapQuarter(2, 1, 0, 5)
                    h3 = hr.SwapThird(3, 1, 0, 5)
                    h4 = hr.SwapHalf(4, 1, 0, 5)      
                    h13 = hr.ShakeArea(13, 1, 0, 5)
                    h20 = hr.ShakeRegion(20, 1, 0, 5)
                    ############
                    h5 = hr.Swap1(5, 2, 0, 1)
                    h6 = hr.DrawHightBgt(6, 2, 0, 1)
                    h7 = hr.AddRandom(7, 2, 0, 1)
                    h8 = hr.AddLowBgt(8, 2, 0, 1)
                    h9 = hr.DrawRandom(9, 2, 0, 1)
                    h10 = hr.DrawHightBgt(10, 2, 0, 1)
                    h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
                    h12 = hr.AddMaxBgt(12, 2, 0, 1)
            
                    ######### Area####### 
                    h14 = hr.SwapArea(14, 3, 0, 1)
                    h15 = hr.IncreseBgtArea(15, 3, 0, 1)
                    h16 = hr.DecreaseBgtArea(16, 3, 0, 1)
            
                    ##### Region #######
                    h17 = hr.SwapRegion(17, 4, 0, 1)
                    h18 = hr.IncreseBgtRegion(18, 4, 0, 1)
                    h19 = hr.DecreaseBgtRegion(19, 4, 1, 1)
                    h21=hr.UseBudgetAT(20, 2, 0, 1)   
    
                    ######################################
            
                    shake = [h1, h2, h3, h4, h13, h20]
                    local = [h5, h6, h7, h8, h9, h10, h11, h12, h14, h15, h16, h17, h18, h21]
            
                    ################
                    counter=0
                    heuristics_data=""
                    starttime = datetime.now()
                    a = self.load_from_Rfile(address)
                    b = a.initial_solution()
                    #            b.print()
                    b.make_factible()
                    adjustment = Adjustment(b, b, shake, a.weights, [], 5, 0,counter,heuristics_data)
                    #                print("Into the while" + str(i))
                    #            while adjustment.nim>0 and adjustment.check_rank():
                   
                    while adjustment.nim > adjustment.nima and datetime.now()-starttime<timedelta (minutes=runing_time):              
                        lsearch = ls.LocalSearch(adjustment.shaked, 40, local)
                        lista = lsearch.apply()
                        adjustment.apply(lista)
                        # print(datetime.now())
                    adjustment.apply_electre()
                    endtime = datetime.now() - starttime
                 
                    file = open("b_" + address+".csv", "a+")
                    for sol in adjustment.solutions:
                        file.write("{0};{1};{2}".format(starttime, round(endtime.total_seconds()), sol.info()))                
                    
                    file.close()
                    to_save=""
                    shake.sort(key=lambda x: x.ID, reverse=False)
                    local.sort(key=lambda x: x.ID, reverse=False)
                    for h in shake:
                        to_save= to_save+"; " + str(h.in_use) 
                    for h in local:                 
                        to_save= to_save+ "; "+  str(h.in_use)
                    file1 = open("har_" + address+ ".csv", "a+") 
                    file1.write(str(starttime)+ to_save + "; adj:"+ str (adjustment.nim) + ";" + "ls:" +str(lsearch.c)+ "; "+ str( runing_time)+" min"+ "\n" )
                    file1.close()

a=RProgram(["o100_1.txt","o100_2.txt","o100_3.txt","o100_4.txt","o100_5.txt"])

# "o1.txt","o1obj4.txt","o1obj9.txt","o2.txt","o2obj4.txt","o2obj9.txt","o3.txt","o3obj4.txt","o3obj9.txt","o100_1.txt","o100_2.txt"
#            ,"o100_3.txt","o100_4.txt","o100_5.txt"
a.apply()