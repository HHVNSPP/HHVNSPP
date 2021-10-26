import os
import numpy as np
from math import log, floor, ceil
from collections import defaultdict

def candlestick(d):
    if d is None:
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
set boxwidth 0.6 relative
set style fill solid border -1
set logscale x
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"''')

sets = [ (4, 20, 3),
         (9, 20, 3),
         (9, 30, 3),
         (9, 100, 5) ]
replicas = 3

uses = dict()
present = { 'shake': set(), 'search': set() }

for panel in sets:
    uses[panel] = defaultdict(list)
    k, n, instances = panel
    maxiter = 0
    for i in range(instances):
        # replicas of instances in rows, objectives + budget in columns
        filename = f'k{k}n{n}i{i + 1}.txt'
        for r in range(replicas):
            iteration = 0
            objectives = defaultdict(list)
            budget = defaultdict(list)
            combine = None
            with open(f'r{r + 1}_{filename}') as output:
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
                            budget[iteration].append(float(line[-1]))
                            line = line[-2]
                            line = line.replace('[', '')
                            line = line.replace(']', '')
                            line = line.split()
                            values = [ int(f[:-1]) if f[-1] == '.' else float(f) for f in line ]
                            assert k == len(values)
                            objectives[iteration].append(values)
                        elif 'budget' in line:
                            if '[' in line and ']' not in line:
                                combine = line
                                continue
                            line = line.split(';')[1:]
                            values = [ float(f) for f in line ]
                            budget[iteration] += values
                        elif 'usage' in line:
                            line = line.split(';')[1:]
                            stage = line.pop(0)
                            line = line[0].strip().split('=')
                            heur = line.pop(0)
                            count = int(line.pop(0))
                            uses[panel][(stage, heur)].append(count) # combine all replicas of the same instance type
                            present[stage].add(heur)
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
            for obj in range(k + 1): # budget will be objective k + 1 in these files
                with open(f'parsed/r{r + 1}_B{k}_{n}_i{i + 1}_{obj + 1}.txt', 'w') as target:
                    for iteration in objectives:
                        data = [ s[obj] for s in objectives[iteration] ] if obj < k else budget[iteration]
                        values = candlestick(data)
                        print(f'{iteration} {values}', file = target)
    print(f'set output "B{k}_{n}.eps"')
    rows = replicas * instances
    print(f'set multiplot layout {rows}, {k + 1}')
    print(f'set xrange [0.5:1.5 * {maxiter}]')
    for i in range(instances):
        for r in range(replicas):
            print(f'set title "Instance {i + 1}, replica {r + 1}')
            for obj in range(k + 1):
                name = 'Budget' if obj == k else f'Objective {obj + 1}'
                print(f'set ylabel "{name}"')                
                wb = f'u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c{obj} whiskerbars, \\'
                mb = f'"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c{obj}'
                print(f'plot "parsed/r{r + 1}_B{k}_{n}_i{i + 1}_{obj + 1}.txt" {wb}\n{mb}')
    print('unset multiplot')

heuristics = dict()
counter = dict()
for stage in present:
    heuristics[stage] = sorted(list(present[stage]))
    counter[stage] = [ c + 1 for c in range(len(heuristics[stage])) ]

for panel in sets:
    k, n, c = panel
    for stage in present:
        with open(f'parsed/h_B{k}_{n}_{stage}.txt', 'w') as target:
            for (heur, c) in zip(heuristics[stage], counter[stage]):
                data = uses[panel].get((stage, heur), None)
                lst = candlestick(data)
                print(f'{c} {lst}', file = target)

wb = { 'shake': 'using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \\',
       'search': 'using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \\' }
mb = '"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"'
                
with open('heur.plot', 'w') as target:
    print('''set term postscript eps font ",20" size 16, 16 color
    set boxwidth 0.6 relative
    set style fill solid border -1
    set output "heur.eps"
    set key off
    set ylabel "Number of uses"''', file = target)
    print(f'set multiplot layout {len(sets)}, 2', file = target)
    for panel in uses:
        k, n, c = panel
        for stage in present:
            print(f'set xrange [0.1:{len(heuristics[stage])+0.9}]', file = target)
            lst = ','.join([ f'"{h}" {c}' for (h, c) in zip(heuristics[stage], counter[stage]) ])
            print(f'set xtics ({lst}) rotate by 90 right offset 0,-1', file = target)
            print(f'set title "{n} projects, {k} objectives: {stage}"', file = target)
            print(f'plot "parsed/h_B{k}_{n}_{stage}.txt" {wb[stage]}\n{mb}', file = target)
