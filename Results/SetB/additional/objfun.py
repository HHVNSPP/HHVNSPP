import os
import numpy as np
from math import log, floor, ceil
from collections import defaultdict

def candlestick(data):
    return f'{float(min(data))},{np.quantile(data, 0.25)},{np.quantile(data, 0.5)},{np.quantile(data, 0.75)},{float(max(data))}'

for filename in os.listdir('.'):
    if (not filename.startswith('h_')) and filename.endswith(".csv"):
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
                it = int(i)
                if ceil(log(it, 2)) != floor(log(it, 2)):
                    continue # not a power of two
                d = iterations[i]
                t = [int(v[0]) for v in d] # time in seconds
                b = [float(v[1]) for v in d] # budget
                obj = defaultdict(list)
                for p in range(3, len(d[0]) - 1): # skip the ELECTRE score and the final \n
                    obj[p - 2] = [float(v[p]) for v in d]
                o = list(obj.keys())
                o.sort()
                objs = ','.join([str(candlestick(np.array(obj[p]))) for p in o])
                print(f'{it},{candlestick(np.array(t))},{candlestick(np.array(b))},{objs}', file = target)            
            
