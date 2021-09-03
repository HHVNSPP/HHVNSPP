from random import shuffle

def SwapOne(sol):
    return sol.swap(count = 1)

def InclRnd(sol):
    return sol.add()

def ExclRnd(sol):
    return sol.fill(random = False)

def inclLow(sol):  
    return sol.fitExtreme(high = False)
    
def omcHigh(sol):
    return sol.fitExteme()

def DrawHigh(sol):
    return sol.dropExtreme().fill()

def ProjMin(sol):
    return sol.randmin()

## GROUP LEVEL

def incrGroup(sol):
    return sol.modGroup(decr = False)
    
def decrGroup(sol):  
    return sol.modGroup()

def alterGroup(sol):
    return sol.alterGroup().fill()
    
LOCAL = [swapOne, addRnd, drawRnd,
         incrRnd, fundRnd,
         inclMax, lowRand, exclRnd, exclHigh,
         incrGroup, decrGroup, alterGroup]

class LocalSearch():
    def __init__(self, s, init = 1):
        self.heuristics = dict()
        for h in LOCAL:
            self.heuristics[h] = init
        self.initial = init
        self.seed = s # initial solution
        self.current = None # current solution

        self.heuristics.sort(key = lambda x: x.rank(self.byDom), reverse = True)

    def check(self):
        for i in self.heuristics:
            if self.rank_by_dom is None:
                if i.get_rank()==1 or i.get_rank()==0:
                    return True
            elif i.get_rank(self.rank_by_dom) > 0:
                return True
            else: return False
    
    def reset(self):
        for h in self.heuristics:
            self.heuristics[h] = self.initial

    # update the set of non-dominated solutions        
    def update(self, alt, reference, heur = None):
        prune = set()
        add = True
        for i in range(len(alt)):        
            comparison = alt[i].compare(reference)
            if comparison == 1:   
                prune.add(i)
            elif comparison == -1 or comparison == 2:
                add = False
        if self.rank_by_dom != None:
            if len(prune) > 0:
                strength = len(prune)
            else:
                strength = 0
            if heur == reference.getheur():
                heur.set_rank(strength, True)
        alt -= prune
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
