import os
import numpy as np
from collections import defaultdict

def candlestick(d):
    if d is None:
        return '0 0 0 0 0'
    data = np.array(d)
    return f'{np.quantile(data, 0.25)} {float(min(data))} {float(max(data))} {np.quantile(data, 0.75)}  {np.quantile(data, 0.5)}'

group = ['b20_4', 'b20_9', 'b30_9', 'b100_9']
uses = dict()
n = None
for gr in group:
    uses[gr] = defaultdict(list)

for filename in os.listdir('.'):
    if filename.startswith('h_') and filename.endswith(".csv"):
        gr = None
        for g in group:
            if g in filename:
                gr = g
                break
        if gr is None:
            print(filename)
            exit()
        with open(filename) as data:
            for line in data:
                f = (line.strip()).split(';')
                f.pop(0) # timestamp not used
                if n is None:
                    n = len(f)
                else:
                    assert len(f) == n
                for i in range(n):
                    uses[gr][i].append(int(f.pop(0)))

for g in group:
    with open(f'heur_{g}.txt', 'w') as target:
        for i in range(n):
            print(i + 1, candlestick(uses[g].get(i, None)), file = target)

            
