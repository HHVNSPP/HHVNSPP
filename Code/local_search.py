from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
import copy
from project import RProject
import random
import portfolio as prf

class LocalSearch():
    def __init__(self, portfolio_base, c, heuristics=None):
        if heuristics is None:
            self.heuristics = []
        else:
            self.heuristics=heuristics
        self.portfolio_base=portfolio_base
        self.c=c
      
    
    def sort_heur(self):
        self.heuristics.sort(key=lambda x: x.rank, reverse=True)
    
    def shuffle_heur(self):
        random.shuffle(self.heuristics)

    def check_heur(self): #Check heuristics rank       
        for i in self.heuristics:
            if i.rank==1 or i.rank==0:
                return True
        return False
    
    
    def setHto_1(self):
        for i in self.heuristics:
            i.rank=1

    def add2nondom(self,portfs,reference): 
        delete=[]
        add=True
        for i in range(len(portfs)):        
            comparison=portfs[i].compare(reference)
            if comparison==1 :   
                delete.append(i)
            if comparison==-1 or comparison==2:
                add=False
        for i in sorted(delete, reverse=True): del portfs[i]     
        if add: portfs.append(reference)
                                                       
    def apply(self):  
        num_non_impr=0
        result=[]          
        portf= copy.deepcopy(self.portfolio_base)
        while num_non_impr<self.c and self.check_heur():
        
            self.shuffle_heur()
            heur=self.heuristics[0]
            for i in self.heuristics:
                if i.rank==1:
                    heur=i
                    break
                elif i.rank>heur.rank:
                    heur=i
              
            portf=heur.apply(self.portfolio_base)  
                                     
            comparison=self.portfolio_base.compare(portf)
                portf.Print()
            
            if comparison==1:
                self.portfolio_base=portf                    
                self.add2nondom(result,portf)
                self.setHto_1()                    
                num_non_impr=0
            elif comparison==0:
                self.add2nondom(result,portf)
                heur.rank=0
                num_non_impr=num_non_impr+1
            else:
                heur.rank=-1
                num_non_impr=num_non_impr+1 
               
        self.setHto_1()
        if len(result)==0:
            return [self.portfolio_base]
        else:
            return result           
                    
      
               
        
 
        
         
     