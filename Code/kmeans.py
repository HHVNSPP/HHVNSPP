from random import sample
from collections import defaultdict

# a custom distance that uses normalized differences
def distance(x, y):
    d = 0
    for (v1, v2) in zip(x, y):
        low = min(v1, v2)
        high = max(v1, v2)
        prop = 0
        if high > 0:
            prop = (high - low) / high
        d += prop
    return d
        
def least(element, centers, values):
    low = None
    nearest = None
    for center in centers:
        x = values[element]
        y = values[center]
        d = distance(x, y)
        if low is None or d < low:
            low = d
            nearest = center
    return nearest

def clustering(values, centers):
    clusters = defaultdict(list)
    for element in values:
        nearest = least(element, centers, values)
        clusters[nearest].append(element)
    return [ clusters[c] for c in clusters ]

def average(cluster, values): 
    n = len(cluster)
    assert n > 0
    if n == 1:
        return cluster
    d = len(values[cluster[0]])
    return [ sum([ values[e][i] for e in cluster ]) / n for i in range(d) ] 

def closest(x, candidates, values):
    low = float('inf')
    chosen = None
    for y in candidates:
        d = distance(values[y], values[x])
        if d < low:
            chosen = y
    return chosen

# create the desired amount of clusters and return the members closest
# to the center of each cluster as cluster representatives
def select(options, count, maxiter = 10):
    if len(options) <= count:
        return options # no need to cluster
    centers = sample(options, count)
    values = { o : o.evaluate() for o in options }
    pick = None
    for i in range(maxiter): # iterate
        clusters = clustering(values, centers)
        averages = [ average(c, values) for c in clusters ]
        centers = [ closest(ce, cl, values) for (ce, cl) in zip(centers, clusters) ]
        if pick is not None:
            if set(centers) == pick:
                print(f'Clustering took {i} iterations to converge')
                return pick # convergence
        pick = set(centers)
    print(f'Clustering did not converge')        
    return pick
