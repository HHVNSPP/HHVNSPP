from math import sqrt
from random import sample
from collections import defaultdict

# euclidean distance 
def distance(x, y):
    return sqrt(sum([ (v - w)**2 for (v, w) in zip(x, y) ]))
        
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

def normalize(data):
    # normalize each dimension to [0, 1]
    low = None
    high = None
    d = None
    i = float('inf')
    for v in data.values():
        d = len(v)
        if low is None:
            low = [ i ] * d
            high = [ -i ] * d
        for p in range(d):
            w = v[p]
            low[p] = min(w, low[p])
            high[p] = max(w, high[p])
    n = dict()
    span = [ high[p] - low[p] for p in range(d) ]
    for (k, v) in data.items():
        nv = []
        for p in range(d):
            if span[p] > 0:
                nv.append(v[p] - low[p] / span[p])
            else:
                nv.append(1) # this dimension is a constant
        n[k] = nv
    return n

# create the desired amount of clusters and return the members closest
# to the center of each cluster as cluster representatives
def select(options, count, maxiter = 10):
    if len(options) <= count:
        return (options, 0) # no need to cluster
    centers = sample(options, count)
    values = normalize({ o : o.evaluate() for o in options })
    pick = None
    for i in range(maxiter): # iterate
        clusters = clustering(values, centers)
        averages = [ average(c, values) for c in clusters ]
        centers = [ closest(ce, cl, values) for (ce, cl) in zip(centers, clusters) ]
        if pick is not None: # if not the initial round
            if set(centers) == pick:
                return (pick, i) # convergence
        pick = set(centers)
    return (pick, maxiter) # no convergence
