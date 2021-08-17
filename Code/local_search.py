from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
import copy
from project import RProject
import random
import portfolio as prf
from heuristic import MIN_RANK
class LocalSearch():
    def __init__(self, portfolio_base, c, heuristics=None,rank_by_dom=None):
        if heuristics is None:
            self.heuristics = []
        else:
            self.heuristics=heuristics
        self.portfolio_base=portfolio_base
        self.c=c
        self.rank_by_dom=rank_by_dom
    #---------------linea modificada por fernando 27/0/2021: adicionado parametro self.rank_by_dom
    def sort_heur(self):
        #--------- linea modificada por fernando 27/07/2021------
        self.heuristics.sort(key=lambda x: x.get_rank(self.rank_by_dom), reverse=True)
        #--------------------------------------------------------
    def shuffle_heur(self):
        random.shuffle(self.heuristics)

    #---------------metodo modificada por fernando 27/0/2021: adicionado parametro rank_by_dom
    def check_heur(self): #Check heuristics rank
        for i in self.heuristics:
            if self.rank_by_dom is None:
                if i.get_rank()==1 or i.get_rank()==0:
                    return True
            elif i.get_rank(self.rank_by_dom) > 0:
                return True
            else: return False


    
    def setHto_1(self):
        for i in self.heuristics:
            # --------- linea modificada por fernando 27/07/2021------
            i.set_rank(1)
            # --------------------------------------------------------

    #---------------metodo modificado por fernando 27/07/2021
    def add2nondom(self,portfs,reference,heur=None):
        delete=[]
        add=True
        for i in range(len(portfs)):        
            comparison=portfs[i].compare(reference)
            if comparison==1 :   
                delete.append(i)
            elif comparison==-1 or comparison==2:
                add=False
        if self.rank_by_dom != None:
            if len(delete) > 0:
                hstrength = len(delete)
            else:
                hstrength = 0
            if heur == reference.getheur():
                heur.set_rank(hstrength,True)

        for i in sorted(delete, reverse=True): del portfs[i]     
        if add: portfs.append(reference)

    #--------------- metodo modificado por fernando 27/07/2021
    def apply(self):
        num_non_impr=0
        result=[]          
        portf= copy.deepcopy(self.portfolio_base)
        while num_non_impr<self.c and self.check_heur():
        
            self.shuffle_heur()
            heur=self.heuristics[0]
            for i in self.heuristics:
                #---------------linea modificada por fernando 21/07/2021
                if self.rank_by_dom is None and i.get_rank()==1:
                    heur=i
                    break
                # ---------------linea modificada por fernando 21/07/2021
                elif i.get_rank(self.rank_by_dom)>heur.get_rank(self.rank_by_dom):
                    heur=i
                    
            portf=heur.apply(self.portfolio_base)                                    
            comparison=self.portfolio_base.compare(portf)
            # portf.Print()
            
            if comparison==1:
                self.portfolio_base=portf                    
                self.add2nondom(result,portf,heur)
                if self.rank_by_dom is None:
                    self.setHto_1()
                num_non_impr=0
            elif comparison==0:
                self.add2nondom(result,portf,heur)
                if self.rank_by_dom is None:
                    heur.set_rank(0)
                num_non_impr=num_non_impr+1
            else:
                if self.rank_by_dom is None:
                    heur.set_rank(-1)
                num_non_impr=num_non_impr+1 
        if self.rank_by_dom is None:
            self.setHto_1()
        if len(result)==0:
            return [self.portfolio_base]
        else:
            return result           
                    
      
               
        
 
        
         
     