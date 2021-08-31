from random import shuffle, random

class Portfolio():
    def __init__(self, b, w, p):
        self.budget = b
        self.weights = w
        self.numberOfObjectives = len(w)
        self.projects = p
        self.order = None
        
    def permutation(self):
        if self.order is None: # create if non-existant
            k = 0
            for p in self.projects:
                assert p.ID == k # they are supposed to be numbered 0, 1, 2, ...
            k += 1 # count them
            self.order = [i for i in range(k)] # make a list of the IDs [0, k - 1]            
        shuffle(self.order) # reorder
        return self.order

class PortfolioAR(Portfolio): # this one adds areas and/or regions
    def __init__(self, b, w, p, areaLimits = None, regionLimits = None):
        super().__init__(b, w, p)
        self.areas = False
        self.regions = False
        if areaLimits is not None:
            self.areas = True
            self.areaLimits = areaLimits
            self.numberOfAreas = len(self.areaLimits['LowerBound'])
        if regionLimits is not None:
            self.regions = True
            self.regionLimits = regionLimits
            self.numberOfRegions = len(self.regionLimits['LowerBound'])

class PortfolioSyn(PortfolioAR): # this one add synergies on top of areas/regions 
    def __init__(self, b, w, p, areaLimits = None, regionLimits = None, syn = None):
        super().__init__(b, w, p, areaLimits, regionLimits)
        if syn is not None:
            self.numberOfSynergies = len(syn)
        self.synergies = syn
