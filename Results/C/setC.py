print('set term postscript eps size 18, 12 color\nset output "setC.eps"')
powers = [ p for p in range(6, 10) ]
print('''set logscale x
set boxwidth 0.5 relative
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
set key outside Right''')

import os
import numpy as np
from math import log, floor, ceil
from collections import defaultdict

def candlestick(d):
    if d is None or len(d) == 0:
        return '0 0 0 0 0'
    data = np.array(d)
    low = min(data)
    q1 = np.quantile(data, 0.25)
    med = np.quantile(data, 0.5)
    q3 = np.quantile(data, 0.75)
    high = max(data)
    return f'{low} {q1} {med} {q3} {high}'

instances = 3
replicas = 3
print(f'set multiplot layout {len(powers)}, 2 * {instances}')
for p in powers:
    n = 2**p
    for i in range(instances):
        for syn in [ ('s', ''), ('', 'out')]: # with, without
            for r in range(replicas):
                filename = f'Replicas/r{r}With{syn[1]}_C{n}_{i + 1}.txt'
                iteration = 0
                budget = defaultdict(list)
                size = defaultdict(list)
                combine = None
                with open(filename) as output:
                    for line in output:
                        if '#' not in line:
                            if combine is not None:
                                line = combine.strip() + ' ' + line
                                combine = None
                            if 'w;' == line[:2]:
                                iteration = int(line.split(';')[-1])
                                maxiter = max(maxiter, iteration)
                            elif 'end;' == line[:4]:
                                iteration = int(line.split(';')[3].split('/')[0])
                                maxiter = max(maxiter, iteration)                            
                            elif 'electre' in line: # final front
                                if '[' in line and ']' not in line:
                                    combine = line
                                    continue
                                line = line.split(';')
                                size[iteration].append(float(line[-1]))
                                budget[iteration].append(float(line[-2]))
                            elif 'budget' in line:
                                if '[' in line and ']' not in line:
                                    combine = line
                                    continue
                                line = line.split(';')[1:]
                                values = [ float(f) for f in line ]
                                budget[iteration] += values
                            elif 'size' in line:
                                if '[' in line and ']' not in line:
                                    combine = line
                                    continue
                                line = line.split(';')[1:]
                                values = [ int(f) for f in line ]
                                size[iteration] += values
            filename = f'Parsed/r{r}{syn[0]}_C{n}_{i + 1}.txt'                            
            with open(filename, 'w') as target:
                for iteration in size:
                    b = budget[iteration]
                    s = size[iteration]
                    print(f'{iteration} {candlesticks(b)} {candlesticks(s)}', file = target)
            if syn[0] == 's':
                print(f'set title "{n} projects, instance {i + 1}"')
                print('set ylabel "Front size"')
                print(f'plot "{filename}" u 1:3:2:6:5 t "with syn" with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \\')
                print('"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0')
                print('set ylabel "Budget"')                
                print(f'plot "{filename}" u 1:3:2:6:5 t "with syn" with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \\')
                print('"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0')
            else:


print('unset multiplot')
