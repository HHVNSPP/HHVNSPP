from random import shuffle
from heuristic import MIN_RANK

class LocalSearch():
    def __init__(self, i, h = [], r = False):
        self.heuristics = h
        self.initial = i # initial solution
        self.current = None # current solution
        self.byDom = r

    def sort_heur(self):
        self.heuristics.sort(key = lambda x: x.rank(self.byDom), reverse = True)

    def check(self):
        for i in self.heuristics:
            if self.rank_by_dom is None:
                if i.get_rank()==1 or i.get_rank()==0:
                    return True
            elif i.get_rank(self.rank_by_dom) > 0:
                return True
            else: return False
    
    def reset(self, value = 1):
        for i in self.heuristics:
            i.set_rank(value)

    # update the set of non-dominated solutions        
    def update(self, alt, reference, heur = None):
        delete = []
        add = True
        for i in range(len(alt)):        
            comparison = alt[i].compare(reference)
            if comparison == 1:   
                delete.append(i)
            elif comparison == -1 or comparison == 2:
                add = False
        if self.rank_by_dom != None:
            if len(delete) > 0:
                hstrength = len(delete)
            else:
                hstrength = 0
            if heur == reference.getheur():
                heur.set_rank(hstrength,True)
        for i in sorted(delete, reverse = True):
            del alt[i]     
        if add:
            alt.append(reference)

    def execute(self):
        num_non_impr = 0
        result = []          
        while num_non_impr<self.c and self.check():
            shuffle(self.heuristics)
            selected = self.heuristics
            for h in self.heuristics:
                if self.rank_by_dom is None and h.rank == 1:
                    selected = h
                    break
                elif h.rank(self.rank_by_dom) > heur.rank(self.rank_by_dom):
                    selected = h
            alt = selected.execute(self.initial) # create an alternative solution
            comparison = self.initial.compare(alt)
            if comparison == 1:
                self.solution = self.initial # keep the initial solution
                self.update(result, alt, heur)
                if self.rank_by_dom is None:
                    self.reset()
                num_non_impr=0
            elif comparison == 0:
                self.update(result, alt, heur)
                if self.rank_by_dom is None:
                    heur.rank(0)
                num_non_impr=num_non_impr+1
            else:
                if self.rank_by_dom is None:
                    heur.rank(-1)
                num_non_impr=num_non_impr+1 
        if self.rank_by_dom is None:
            self.reset()
        if len(result) == 0:
            return [self.initial]
        else:
            return result           
