# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:03:09 2019

@author: Madys
"""
from Electre import Electre
from random import choice

class Adjustment():
    def __init__(self,to_shake,shaked, heuristics,weights,solutions, nim, nima, counter, heuristic_data):  
        self.heuristics=heuristics
        self.to_shake=to_shake
        self.shaked=shaked
        self.weights=weights
        self.solutions=solutions
        self.nim=nim 
        self.nima=nima  
        self.counter=counter
        self.heuristic_data=heuristic_data
     
    def check_rank(self):
        for i in self.heuristics:
            if i.rank>0:
                return True
        return False
    
    def setHto_5(self):
        for i in self.heuristics:
            i.rank=5

  
    def delete_d(self,local_s):
        if len(local_s)>1:
            it=0            
            while(it<len(local_s)):
                to_del=[]  
                is_bad=False
                for i in range(len(local_s)):
                    if i>it:
                        comparator=local_s[it].compare(local_s[i])
                        if comparator==1:                
                            to_del.append(i)                
                        elif comparator==-1:
                            is_bad=True                          
                        elif comparator==2:
                            is_bad=True
                if is_bad:
                    to_del.append(it)
                else:
                    it=it+1
                to_del=set(to_del)
                for i in sorted(to_del, reverse=True): del local_s[i] 
            return local_s
        return local_s
    
    def sort_heur(self):
        self.heuristics.sort(key=lambda x: x.rank, reverse=True)                

    def check_improvement(self,local_s): 
        nd_locals=self.delete_d(local_s)  
#        print(len(nd_locals))
        if len(nd_locals)>0:
#            print("adjustmente, check improvent")
#            print(len(nd_locals))
#            for i in nd_locals:
#                i.Print()
            non_improvement=True
            to_delete=[]
            for i in range(len(nd_locals)):
                comparator=self.to_shake.compare(nd_locals[i])
                if comparator==1:                
                    self.heuristics[0].rank=self.heuristics[0].rank+1
                    non_improvement=False
                elif comparator==0:
                    non_improvement=False
                    self.heuristics[0].rank=self.heuristics[0].rank-1
                elif comparator==-1:
                    to_delete.append(i) 
                    self.heuristics[0].rank=self.heuristics[0].rank-5
                elif comparator==2:
                    self.heuristics[0].rank=self.heuristics[0].rank-10 
            to_delete=set(to_delete)
            for i in sorted(to_delete, reverse=True): del nd_locals[i] 
            self.nd_locals=to_delete 
            if non_improvement: 
                self.nima=self.nima+1
            else:
                self.nima=0
#                print(nim)
            
            self.sort_heur() 
            if self.heuristics[0].rank<0:
                self.setHto_5()
#        print("return fro check improvement") 
#        print(len(nd_locals))        
#        for i in nd_locals:
#            i.Print()
        return nd_locals     

    
    def execute(self, local_s):
#        for i in self.heuristics:
#            print(str(i.ID)+ " " +str(i.rank))
#        print("inside adjustment.execute")          
        sol=self.check_improvement(local_s)      
        self.solutions=self.solutions+sol
        self.solutions=self.delete_d(self.solutions)     

        if len(self.solutions)>0:            
            to_select = choice(list(range(len(self.solutions))))
#            print("to select " + str(to_select))
            self.to_shake=self.solutions[to_select]
#        print("into adjustment")   
#        print(self.to_shake)
        self.shaked=self.heuristics[0].execute(self.to_shake)
        
        
#        print(self.nim)
#        print("SOLUTIONS")
#        print(len(self.solutions))
    
    def electre(self):
        array=[]      
        for sol in self.solutions:
            array.append(sol.total_impact)
        e = Electre(self.weights,array)
        for i in range(len(self.solutions)):
            self.solutions[i].points = e.sol[i]        
        self.solutions.sort(key=lambda x: x.points, reverse=True)
        
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
