class Project():
    def __init__(self, ID, i, requested, minimum = None, act = []):
        self.ID = ID
        self.potentialImpact = i
        self.requestedBudget = requested
        self.minimumBudget = minimum
        self.activities = act

    def update(self):
        if len(self.activities) > 0:
            # activities are always processed in a decreasing order of impact
            self.activities.sort(key = lambda a: a.potentialImpact, reverse = True) 

        
