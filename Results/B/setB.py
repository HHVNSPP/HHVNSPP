import os
import numpy as np
from collections import defaultdict
from math import log, floor, ceil, sqrt

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

print('''set term postscript eps font ",12" size 32, 24 color
set key off
set logscale x
set boxwidth 0.5 relative
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"''')
palette = 'c0="#dddddd"\nc1="#ff4500"\nc2="#009999"\nc3="#a020f0"\nc4="#1e90ff"\nc5="#006400"\nc6="#4b0082"\nc7="#a0522d"\nc8="#ff0000"\nc9="#0000dd"\nc10="#33dd00"'
print(palette)

sets = [ (4, 20, 3),
         (9, 20, 3),
         (9, 30, 3),
         (9, 100, 5) ]
replicas = 3

objlow = dict()
objhigh = dict()
for panel in sets:
    k, n, instances = panel
    maxiter = 0
    for i in range(instances):
        objlow[i] = dict()
        objhigh[i] = defaultdict(int)
        filename = f'k{k}n{n}i{i + 1}.txt'
        for r in range(replicas):
            iteration = 0
            objectives = defaultdict(list)
            budget = defaultdict(list)
            size = defaultdict(list)
            combine = None
            with open(f'r{r + 1}-original-{filename}') as output:
                for line in output:
                    if 'included;' in line:
                        continue # not parsed
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
                            if len(line) != 5:
                                print('# ignoring old format', line)
                                continue
                            size[iteration].append(float(line[-1]))
                            budget[iteration].append(float(line[-2]))
                            l = line[-3]
                            l = l.replace('[', '')
                            l = l.replace(']', '')
                            l = l.split()
                            values = [ int(f[:-1]) if f[-1] == '.' else float(f) for f in l ]
                            assert k == len(values)
                            objectives[iteration].append(values)
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
                        elif '[' in line:
                            if ']' not in line:
                                combine = line
                                continue
                            line = line.replace('[', '')
                            line = line.replace(']', '')
                            line = line.split()
                            values = [ int(f[:-1]) if f[-1] == '.' else float(f) for f in line ]
                            assert k == len(values)
                            objectives[iteration].append(values)                            
            for obj in range(k + 2): # budget will be objective k + 1 and portfolio size k + 2 in these files
                with open(f'Parsed/r{r + 1}_B{k}_{n}_i{i + 1}_{obj + 1}.txt', 'w') as target:
                    for iteration in objectives:
                        data = None
                        if obj < k:
                            data = [ s[obj] for s in objectives[iteration] ]
                        elif obj == k:
                            data = budget[iteration]
                        elif obj == k + 1:
                            data = size[iteration]
                        values = candlestick(data)
                        if obj not in objlow[i]:
                            objlow[i][obj] = float('inf')
                        objlow[i][obj] = min(objlow[i][obj], min(data))
                        objhigh[i][obj] = max(objhigh[i][obj], max(data))                        
                        print(f'{iteration} {values}', file = target)
    print(f'set output "B{k}_{n}.eps"')
    rows = replicas * instances
    # replicas of instances in rows, objectives + budget + size in columns
    print(f'set multiplot layout {rows}, {k + 2}')
    print(f'set xrange [0.5 : 1.5 * {maxiter}]')
    l = int(ceil(sqrt(k + 2)))
    w = l
    h = l
    while w * h > k + 2:
        if w * h % 2 == 0 and w > 2:
            w -= 1
            if w * h < k + 2:
                w += 1
                break
        elif h > 1:
            h -= 1
            if w * h < k + 2:
                h += 1
                break            
        else:
            break
    for i in range(instances):
        for r in range(replicas):
            print(f'set title "Instance {i + 1}, replica {r + 1}')
            with open(f'B{k}_{n}_{i + 1}_{r + 1}.plot', 'w') as individual:
                print(f'set term postscript eps font ",12" size {2 * w}, {2 * h} color', file = individual)
                print(f'set output "B{k}_{n}_{i + 1}_{r + 1}.eps"', file = individual)
                print(f'set xrange [0.5 : 1.5 * {maxiter}]', file = individual)    
                print('set key off\nset logscale x\nset boxwidth 0.5 relative\nset style fill solid border -1', file = individual)
                print(f'set xtics 1, 2\nset xlabel "Iteration"\nset multiplot layout {h}, {w}', file = individual)
                print(palette, file = individual)
                for obj in range(k + 2):
                    name = 'Budget' if obj == k else 'Portfolio size' if obj == k + 1 else f'Objective {obj + 1}'
                    wb = f'u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c{obj} whiskerbars, \\'
                    mb = f'"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c{obj}'
                    print(f'set ylabel "{name}"')
                    print(f'set yrange [{0.7 * objlow[i][obj]}:{1.1 * objhigh[i][obj]}]')                
                    print(f'plot "Parsed/r{r + 1}_B{k}_{n}_i{i + 1}_{obj + 1}.txt" {wb}\n{mb}')
                    print(f'set ylabel "{name}"', file = individual)                    
                    print(f'set yrange [{0.7 * objlow[i][obj]}:{1.1 * objhigh[i][obj]}]', file = individual)                
                    print(f'plot "Parsed/r{r + 1}_B{k}_{n}_i{i + 1}_{obj + 1}.txt" {wb}\n{mb}', file = individual)
    print('unset multiplot')

