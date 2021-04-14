import os
from collections import defaultdict
import numpy as np

def candlestick(data):
    return f'{min(data)} {np.quantile(data, 0.25)} {np.quantile(data, 0.5)} {np.quantile(data, 0.75)} {max(data)}'

for filename in os.listdir('.'):
    if filename.endswith(".csv"):
        solutions = defaultdict(list)
        with open(filename) as data:
            for line in data:
                fields = line.split(';')
                ID = fields[0]
                solutions[ID].append(fields[1:])
        for solution in solutions:
            iterations = defaultdict(list)
            for info in solutions[solution]:
                i = info[0]
                iterations[i].append(info[1:])
        with open(filename.replace('csv', 'txt'), 'w') as target:
            for i in iterations:
                d = iterations[i]
                t = [int(v[0]) for v in d] # time in seconds
                b = [float(v[1]) for v in d] # budget
                obj = defaultdict(list)
                for p in range(3, len(d[0]) - 1): # skip the ELECTRE score and the final \n
                    obj[p - 2] = [float(v[p]) for v in d]
                objs = ' '.join([str(candlestick(np.array(obj[p]))) for p in obj])
                print(i, candlestick(np.array(t)), candlestick(np.array(b)), objs, file = target)

            
            
