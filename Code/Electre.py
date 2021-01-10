# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:29:10 2019

@author: Madys
"""
import numpy as np
import copy
import pandas as pd



class Electre():
    def __init__(self, pesos, matriz):  
        self.pesos=copy.deepcopy(pesos)     
        self.matriz=copy.deepcopy(matriz)
        self.atributos=len(pesos)
        self.alternativas=len(matriz)
        self.concordancia = np.zeros((self.alternativas,self.alternativas))
        self.discordancia = np.zeros((self.alternativas,self.alternativas))
        self.dominancia = np.zeros((self.alternativas,self.alternativas))
        self.sol=np.zeros(self.alternativas)
        
        if self.normalizar_matriz():
            self.calc_concordancia()
            self.calc_discordancia()
            self.calc_dominancia()  
        else:   
            for i in range(self.alternativas):       
                self.sol[i]=  "3333"                       
    
    def normalizar_matriz(self):
        mini=[]
        maxi=[]
        try:
            for atributo in range(self.atributos):
                mini.append(self.matriz[0][atributo])
                maxi.append(0)     
            for alternativa in self.matriz:
               for atributo in range(self.atributos):
                    if maxi[atributo]<alternativa[atributo]:
                        maxi[atributo]=alternativa[atributo]
                    if mini[atributo]>alternativa[atributo]:
                         mini[atributo]=alternativa[atributo] 
     
            for alternativa in self.matriz:
               for atributo in range(self.atributos):
    #                alternativa[atributo]=(alternativa[atributo]-mini[atributo])/(maxi[atributo]-mini[atributo]) 
                   if maxi[atributo]-mini[atributo]==0:
                       return False
                       alternativa[atributo]=alternativa[atributo]/(maxi[atributo]-mini[atributo])
            return True  
        except IndexError:
            return False
               
    def calc_concordancia(self):       	
        media = 0          		
        for i in range(self.alternativas):          
            for k in range(0, self.alternativas):            
                suma = 0
                if i==k:
                     continue
                else:
                    for j in range(0, self.atributos):                                                    
                        if self.matriz[i][j] > self.matriz[k][j]:                                     
                            suma = suma + self.pesos[j] 
                        elif self.matriz[i][j] == self.matriz[k][j]: 
                            suma=suma+(self.pesos[j]/2)               
                    self.concordancia[i][k] = suma                     
                    media = media + suma
        media = media / (self.alternativas*self.alternativas-self.alternativas)               
        for i in range(0, self.alternativas):
            for j in range(0, self.alternativas):
                if self.concordancia[i][j] >=media:               
                    self.concordancia[i][j] = 1
                else:                          
                    self.concordancia[i][j] = 0
     
    def calc_discordancia(self):
        media = 0
        ponderada=copy.deepcopy(self.matriz)
        for i in ponderada:
            for j in range(len(i)):
                i[j]=i[j]*self.pesos[j]   
        denominador=np.amax(ponderada)-np.amin(ponderada)
        for i in range(0, self.alternativas):
            for k in range(0, self.alternativas):  
                maximo=0             
                if i != k:
                    for j in range(0, self.atributos):
                        if ponderada[i][j] < ponderada[k][j]:
                            if ponderada[k][j]-ponderada[i][j] >maximo:
                                maximo=ponderada[k][j]-ponderada[i][j] 
                      
                    self.discordancia[i][k] = maximo / denominador
                    media = media + self.discordancia[i][k]
        media = media / (self.alternativas*self.alternativas-self.alternativas)  
        for i in range(0, self.alternativas):
            for k in range(0, self.alternativas):
                if i != k:
                    if self.discordancia[i][k] < media:
                        self.discordancia[i][k] = 1
                    else:
                        self.discordancia[i][k] = 0
                else:
                    self.discordancia[i][k] = 0

    def calc_dominancia(self):  	
        for i in range(0, self.alternativas):
            for j in range(0, self.alternativas):
                if self.concordancia[i][j] == self.discordancia[i][j]:
                    self.dominancia[i][j] = self.concordancia[i][j]	
        df = pd.DataFrame(self.dominancia)  
        for i in range(self.alternativas):       
            self.sol[i]=  df.iloc[i,:].sum()-df[i].sum()
       
#el=Electre(pesos,matrix)
#print(el.sol)