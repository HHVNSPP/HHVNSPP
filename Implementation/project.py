class Project():
    def __init__(self, ID, impact, requestedBudget):
        self.ID = ID
        self.potentialImpact = impact
        self.requestedBudget = requestedBudget
        self.activities = None

class ProjectAR(Project):
    def __init__(self, ID, impact, requestedBudget, area = None, region = None):
        super().__init__(ID, impact, requestedBudget)
        self.area = area
        self.region = region
        
class ProjectAct(ProjectAR):
    def __init__(self, ID, impact, minimumBudget, maximumBudget, area = None, region = None):
        super().__init__(ID, impact, maximumBudget, area, region)
        self.minimumBudget = minimumBudget
        self.activities = []        

    def update(self):
        # activities are always processed in a decreasing order of impact
        self.activities.sort(key = lambda a: a.potentialImpact, reverse = True) 

        
