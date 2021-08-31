class Activity():

    def __init__(self, ID, project, potentialImpact, minimumBudget, maximumBudget):
        self.ID = ID
        self.project = project
        self.potentialImpact = potentialImpact
        self.minimumBudget = minimumBudget
        self.maximumBudget = maximumBudget
        self.difference = self.maximumBudget - self.minimumBudget

    def impact(self, level):
        if level == self.maximumBudget:
            # TO BE DONE: revision pending, is this how the impact of a fully funded activity is supposed to be computed?
            return self.project.potentialImpact * self.potentialImpact                
        else:
            multiplier = fraction / self.difference
            # TO BE DONE: REVISION PENDING, how is the currenty impact of a partially funded activity computed?
            return (multiplier * (level - self.minimumBudget) + (1 - fraction)) * self.project.potentialImpact * self.potentialImpact
        
