# Generator for the Instance Set C

from random import choice, random, sample
from sys import argv

replicas = int(argv[1]) # replicas of instances
k = int(argv[2]) # number of objectives
n = int(argv[3]) # number of projects
s = int(argv[4]) # number of technical synergies to create
a = int(argv[5]) # number of areas
r = int(argv[6]) # number of regions
b = float(argv[7]) # total budget in terms of total project cost

# call for example as
#
#     python3 generator.py 3 4 20 5 0.8 3 2
#
# to generate
# three instances
# with four objectives
# twenty projects
# five synergies
# three areas
# two regions
# and a total budget being 80% of the total minimum project cost

# limits (min, max) for amounts
budgetLow = ( 5, 10 ) # project minimum [5, 15]
budgetSpan = ( 5, 45 ) # project difference between min and max [5, 50]
synSize = ( 2, 8 ) # number of participants in a synergy [2, 10]
synValue = ( 1, 9 ) # synergy value [1, 10]
synActMin = ( 0.1, 0.4 ) # synergy activation low
synActMax = ( 0.3, 0.7 ) # synergy activation high
levels = [ 0, 0.2, 0.5, 0.8, 1.0 ] # possible impact levels

def uniform(data, decimals = 2):
   (low, span) = data
   value = low + span * random()
   if decimals > 0:
      return round(value, decimals)
   return round(value)

areas = [ v + 1 for v in range(a) ] # 1, 2, etc.
regions = [ v + 1 for v in range(r) ] # 1, 2, etc.

for replica in range(replicas): 
   # generate the project data
   projects = []
   total = 0
   for i in range(n): 
      low = uniform(budgetLow)
      total += low
      high = low + uniform(budgetSpan)
      area = choice(areas)
      reg = choice(regions)
      obj = ' '.join( f'{v:.1f}' for v in [ choice(levels) for o in range(k) ] )
      projects.append([ low, high, area, reg, obj ])
   # compute the budget
   budget = round(b * total, 2)
   # generate random weights for the objectives 
   w = [ 0.1 + random() for o in range(k) ] # minimum weight 10 %
   t = sum(w) # must sum to one
   w = [ round(v / t, 2) for v in w ]
   d = 1 - sum(w)
   w[0] += d # make the rounded ones sum to one
   # generate the synergy data
   synergies = []
   pid = [ i + 1 for i in range(n) ] # project numbers for sampling
   for i in range(s):
      size = min(n, uniform(synSize, decimals = 0)) # member count
      low = max(1, round(uniform(synActMin) * size)) # lower threshold
      high = max(low, min(size, round(uniform(synActMax) * size))) # upper threshold
      value = uniform(synValue) # value created by the synergy
      part = ' '.join([ str(p) for p in sample(pid, size) ]) # which projects take part
      synergies.append([ size, low, high, value, part ])
   # output the instance
   with open(f'C{n}_{replica+1}.txt', 'w') as target:
      print(f'B {budget:.2f}', file = target)
      print('W', ' '.join([ f'{v:.2f}' for v in w ]), file = target)
      small = (0.5 / (2 * a), 1.5 / (2 * a))
      large = (0.8 / a, 1.2 / a)
      c = 0
      for a in areas:
         low = budget * uniform(small, 2)
         high = max(1.2 * low, min(budget, budget * uniform(large, 2)))
         print(f'A {c + 1} {low:.2f} {high:.2f}', file = target)
         c += 1
      small = (0.5 / (2 * r), 1.5 / (2 * r))
      large = (0.8 / r, 1.2 / r)
      c = 0
      for r in regions:
         low = budget * uniform(small, 2)
         high = max(1.2 * low, min(budget, budget * uniform(large, 2)))
         print(f'R {c + 1} {low:.2f} {high:.2f}', file = target)
         c += 1
      for i in range(n):
         t = ' '.join([ f'{v:.2f}' if isinstance(v, float) else str(v) for v in projects[i] ])
         print(f'P {i + 1} {t}', file = target)
      for i in range(s):
         t = ' '.join([ f'{v:.2f}' if isinstance(v, float) else str(v) for v in synergies[i] ])
         print(f'S {i + 1} {t}', file = target)         
