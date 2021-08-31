class Funding:
    def __init__(self, t, amount = 0):
        self.target = t
        self.impact = 0        
        self.assigned = 0
        self.fullyFunded = False
        self.active = False
        if amount > 0:
            self.assign(amount)
        if self.target.activities is not None:
            self.activities = dict()

    def assign(self, amount, fraction = 0.3):
        if self.target.potentialImpact > 0: # targets with no impact do not get any funds assigned to them
            if amount <= self.target.minimumBudget: # insufficient funds
                # TO BE DONE: should insufficient assignments sometimes be accepted?
                self.assigned = 0 # nothing assigned
                self.impact = 0 # no impact
                self.active = False
                return
            self.allocate(min(assigned, target.maximumBudget)) # assign only the requested amount

    def allocate(self, amount)
            self.fullyFunded = amount == target.maximumBudget
            self.active = True
            self.impact = self.target.impact(self.assigned)
            if self.target.activities is not None: # instance set A includes activities
                for act in self.target.activities: # in order of decreasing impact
                    level = act.maximumBudget # attempt to fund the activity fully
                    if amount >= level: # do so if possible
                        self.activities[act] = Funding(act, level)
                        amount -= level # reduce the remaining funds to assign
                    else: # attempt to fund the activity partially
                        level = act.minimumBudget 
                        if amount >= level: # assign it the minimum funding if that is feasible
                            self.activities[act] = Funding(act, level)
                            amount -= level # reduce the remaining funds to assign
            
    def randomize(self):
        high = self.target.maximumBudget
        low = self.target.minimumBudget + self.target.difference / 2
        self.assign(uniform(low, high))            


        
                        
        
