import numpy as np
from sklearn.preprocessing import normalize

DEBUG = False
VERBOSE = True

def electre(weights, sol):
    if sol.shape[0] < 2:
        return [ 1 ] # there is only one, it gets a constant rank
    w = np.diag(np.array(weights))
    M = normalize(sol, axis = 0, norm = 'l1')
    (alt, atr) = M.shape 
    n = atr # attributes (the objective function evaluations)    
    m = alt # alternatives (the solutions to rank)
    if DEBUG:
        print('normalized data', M)
    C = np.zeros((m, m)) # concordance
    count = m * m - m
    for i in range(m):          
        for k in range(m):            
            s = 0
            if i != k:
                for j in range(n):
                    v = w[j][j] 
                    if M[i][j] > M[k][j]:                                     
                        s += v
                    elif M[i][j] == M[k][j]: 
                        s += v / 2               
                C[i][k] = s                     
    t = np.sum(C) / count # threshold by the off-diagonal mean
    C[C < t] = 0    
    C[C >= t] = 1 # keep the ones _above_
    if DEBUG:
        print('concordance', C)
    W = M @ w # apply the weights
    if DEBUG:
        print('weighted data', W)
    Dv = np.zeros((m, m)) # discordance
    s = np.max(W) - np.min(W) # span to normalize
    if s == 0: # all are the same
        return [ 1 ] * sol.shape[0] # all get the same rank
    for i in range(m):
        for k in range(m):  
            diff = 0             
            if i != k:
                for j in range(n):
                    if W[i][j] < W[k][j]:
                        diff = max(diff, W[k][j] - W[i][j])
                Dv[i][k] = diff / s
    t = np.sum(Dv) / count # threshold by the off-diagonal mean
    if DEBUG:
        print(f'discordance before thresholding by {t}', Dv)
    D = np.zeros((m, m)) # discordance
    D[Dv >= t] = 0
    D[Dv < t] = 1
    if DEBUG:
        print('discordance', D)
    dom = C # like C, but filtered
    dom[C != D] = 0 # the non-matching ones are zeroed out
    if DEBUG:
        print('dominance', dom)
    rowSums = np.sum(dom, axis = 0)
    colSums = np.sum(dom, axis = 1)
    # differences between column sums and row sums
    # for maximization, the more negative, the better
    return [ rowSums[i] - colSums[i] for i in range(m) ] 

