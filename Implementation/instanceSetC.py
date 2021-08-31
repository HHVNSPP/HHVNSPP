# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:45:00 2020
@author: Madys
"""

import numpy as np
import heuristic as hr
import local_search as ls
from portfolioA import PortfolioA
from adjustment import Adjustment
from project import ProjectA
from datetime import datetime

class Synergy():
    def __init__(self, nombre, tipo, cant, valor, mina, maxa,  elements=None, active=False):
        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo
        self.mina = mina
        self.maxa = maxa
        self.cant = cant
        self.active = active
        if elements == None:
            self.elements = []
        else:
            self.elements = elements

    def AddElement(self, elem):
        self.elements.append(elem)

def load(filename):
    with open(filename) as f:
        cantpr = int(f.readline())
        pres = float(f.readline())
        pesos = [int(i) for i in (f.readline()).split(" ")]
        elemtomax = len(pesos)
        num_syn = int(f.readline())
        synergies=[]
        for i in range(num_syn):
            line = f.readline()
            line = line.split(" ")
            synergies.append(Synergy(int(line[0]),int(line[1]),int(line[2]), int(line[3]),int(line[4]), int(line[5]), []))
            line = f.readline()
            line = line.split(" ")
            for j in line:
                synergies[i].AddElement(int(j))                
        projects = []
        real_impact = np.zeros(elemtomax)
        for i in range(cantpr):
            proj = f.readline()
            proj = proj.split()
            tomax = []
            for x in range(elemtomax):
                tomax.append(float(proj[4 + x]))
            projects.append(ProjectA(i, float(proj[0]), float(proj[1]), int(proj[2]) - 1, int(proj[3]) - 1, tomax,real_impact, 0,False))
        area_limits = [[0.25*pres,0.45*pres],[0.3*pres,0.45*pres],[0.3*pres,0.45*pres]]
        region_limits = [[0.4*pres,0.6*pres],[0.4*pres,0.6*pres]]
        return PortfolioA(pres, cantpr,pesos, 3, 2,  projects,area_limits, region_limits,0,[])

def executeC(instance, limit, maxiter, target, sep, mod = True):
    h1 = hr.SwapRandom(1, 1, 0, 5)
    h2 = hr.SwapQuarter(2, 1, 0, 5)
    h3 = hr.SwapThird(3, 1, 0, 5)
    h4 = hr.SwapHalf(4, 1, 0, 5)      
    h13 = hr.ShakeArea(13, 1, 0, 5)
    h20 = hr.ShakeRegion(20, 1, 0, 5)
    h21 = hr.AllRandN(21, 1, 0, 5)
    h5 = hr.Swap1(5, 2, 0, 1)
    h6 = hr.DrawHightBgt(6, 2, 0, 1)
    h7 = hr.MUseBudget(7, 2, 0, 1)
    h8 = hr.MMoreProj(8, 2, 0, 1)
    h9 = hr.DrawRandom(9, 2, 0, 1)
    h10 = hr.SetPrjMinFill(10, 2, 0, 1)
    h11 = hr.DrawRandomPutLessBgt(11, 1, 0, 1)
    h12 = hr.SetPrjRndFill(12, 2, 0, 1)
    shake = [h1, h2, h3, h4, h13, h20,h21]
    local = [h5, h6, h7, h8, h9, h11, h12]
    counter = 0
    iterate = 1
    stop = 1
    heuristics_data = ""
    timestamp = datetime.now()
    a = load(instance)
    b = a.initial_solution()
    b.make_factible()
    adjustment = Adjustment(b, b, shake, a.weights, [], 4, 0, counter, heuristics_data)
    while adjustment.nim > adjustment.nima:
        if datetime.now() - timestamp > limit:
            break # out of time
        if stop >= maxiter:
            break # out of permitted iterations
        lsearch = ls.LocalSearch(adjustment.shaked, 20, local, mod)
        lista = lsearch.execute()
        adjustment.execute(lista)
        if stop == iterate:    
            diff = datetime.now() - timestamp
            for sol in adjustment.solutions:            
                print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                                    
            stop *= 2                       
        iterate += 1
    print('# electre', file = target)        
    adjustment.electre()
    for sol in adjustment.solutions:
        print(timestamp, sep, iterate, sep, mod, sep, diff, sep, sol.info(), file = target)                                        
    shake.sort(key = lambda x: x.ID, reverse = False)
    local.sort(key = lambda x: x.ID, reverse = False)
    print('# shake', sep.join([str(h.in_use) for h in shake]), file = target)
    print('# local', sep.join([str(h.in_use) for h in local]), file = target)
    print('# time', 'timestamp', file = target)

