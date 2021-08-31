from Electre import Electre
from random import choice

class Adjustment():
    def __init__(self, to_shake, shook, heuristics, weights, solutions, nim, nima, counter, heuristic_data):  
        self.heuristics = heuristics
        self.to_shake = to_shake
        self.shook = shook
        self.weights = weights
        self.solutions = solutions
        self.nim = nim # TO BE DONE: revision needed, these variable names are not clear enough
        self.nima = nima  # TO BE DONE: revision needed, these variable names are not clear enough
        self.counter = counter
        self.heuristic_data = heuristic_data
     
    def check_rank(self):
        for i in self.heuristics:
            if i.rank > 0:
                return True
        return False
    
    def reset(self, level = 5):
        for i in self.heuristics:
            i.rank = level
  
    def delete_d(self,local_s):
        if len(local_s) > 1:
            it = 0            
            while it < len(local_s):
                to_del = []  
                is_bad = False
                for i in range(len(local_s)):
                    if i > it:
                        comparator = local_s[it].compare(local_s[i])
                        if comparator == 1:                
                            to_del.append(i)                
                        elif comparator == -1:
                            is_bad = True                          
                        elif comparator == 2:
                            is_bad = True
                if is_bad:
                    to_del.append(it)
                else:
                    it += 1
                to_del = set(to_del)
                for i in sorted(to_del, reverse = True):
                    del local_s[i] 
            return local_s
        return local_s
    
    def sort_heur(self):
        self.heuristics.sort(key=lambda x: x.rank, reverse=True)                

    def check_improvement(self,local_s): 
        nd_locals = self.delete_d(local_s)  
        if len(nd_locals) > 0:
            non_improvement = True
            to_delete = []
            for i in range(len(nd_locals)):
                comparator = self.to_shake.compare(nd_locals[i])
                if comparator == 1:                
                    self.heuristics[0].rank=self.heuristics[0].rank+1
                    non_improvement=False
                elif comparator == 0:
                    non_improvement=False
                    self.heuristics[0].rank=self.heuristics[0].rank-1
                elif comparator == -1:
                    to_delete.append(i) 
                    self.heuristics[0].rank=self.heuristics[0].rank-5
                elif comparator == 2:
                    self.heuristics[0].rank=self.heuristics[0].rank-10 
            to_delete = set(to_delete)
            for i in sorted(to_delete, reverse=True):
                del nd_locals[i] 
            self.nd_locals = to_delete 
            if non_improvement: 
                self.nima += 1
            else:
                self.nima = 0
            self.sort_heur() 
            if self.heuristics[0].rank<0:
                self.reset()
        return nd_locals     
    
    def execute(self, local_s):
        sol = self.check_improvement(local_s)      
        self.solutions += sol
        self.solutions = self.delete_d(self.solutions)     
        if len(self.solutions) > 0:            
            self.to_shake = self.solutions[choice(list(range(len(self.solutions))))]
        self.shook = self.heuristics[0].execute(self.to_shake)
    
    def electre(self):
        e = Electre(self.weights, [sol.total_impact for sol in self.solutions])
        for i in range(len(self.solutions)):
            self.solutions[i].points = e.sol[i]        
        self.solutions.sort(key=lambda x: x.points, reverse = True)
        
   
        
            
                 
        
        
        
        
        
        
        
        
        
        
        
