from random import random

# a custom distance that uses normalized differences
def distance(vec1, vec2):
    d = 0
    for (v1, v2) in zip(vec1, vec2):
        low = min(v1, v2)
        high = max(v1, v2)
        prop = (high - low) / high
        d += prop
    return d
        
def least(element, centers):
    dist, pos = min((distance(e, c), i) for (i, c) in enumerate(centers))
    return pos

def clustering(elements, centers):
    clusters = [ list() for c in centers ]
    for e in elements:
        clusters[least(e, centers)].append(e)
    return clusters

def average(cluster): # a k-means type of assignment
    n = len(cluster)
    assert n > 0
    if n == 1:
        return cluster[0]
    d = len(cluster[0])
    return [ sum([ e[i] for e in cluster ]) / n for i in range(d) ] 

def update(centers, clustes):
    changes = 0
    for (i, center) in enumerate(centers):
        substitute = average(cluster)
        if substitute != center:
            centers[i] = substitute
            changes += 1
    return changes > 0

def closest(location, options):
    low = float('inf')
    chosen = None
    for o in options:
        d = distance(o, location)
        if d < low:
            chosen = o
    return chosen

# create the desired amount of clusters and return the members closest
# to the center of each cluster as cluster representatives
def representatives(count, candidates, maxiter = 30):
    centers = sample(candidates, count)
    clusters = None
    for i in range(maxiter): # iterate
        clusters = clustering(candidates, centers)
        if not update(centers, clusters):
            break # reached convergence
    return [ closest(ce, cl) for zip(centers, clusters) ]


