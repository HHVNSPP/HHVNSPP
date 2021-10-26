import os
import numpy as np
from math import log, floor, ceil
from collections import defaultdict

def candlestick(d):
    if d is None:
        return '0 0 0 0 0'
    data = np.array(d)    
    low = float(min(data))
    q1 = np.quantile(data, 0.25)
    med = np.quantile(data, 0.5)
    q3 = np.quantile(data, 0.75)
    high = float(max(data))
    return f'{low} {q1} {med} {q3} {high}'

print('''set term postscript eps font ",43" size 32, 16 color
set key off
set boxwidth 0.6 relative
set style fill solid border -1
set logscale x
set xrange [0.6:70]
set xtics ("0" 1, "1" 2, "2" 4, "3" 8, "4" 16, "5" 32, "6" 64)
set xlabel "Iteration (power of 2)"
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

sets = { 'a': (4, 20, 3),
         'b': (9, 20, 3),
         'c': (9, 30, 3),
         'd': (9, 100, 5) }
replicas = 3

uses = dict()
present = { 'shake': set(), 'search': set() }

for panel in sets:
    uses[panel] = defaultdict(list)
    k, n, c = sets[panel]
    for i in range(c):
        print(f'set output "B{k}_{n}.eps"')
        # replicas of instances in rows, objectives + budget in columns
        rows = replicas * c
        print(f'set multiplot layout {rows}, {k + 1}')    
        filename = f'k{k}n{n}i{i}.txt'
        for r in range(replicas):
            iteration = 0
            objectives = defaultdict(list)
            budget = defaultdict(list)
            with open('r{r}_{filename}') as output:
                for line in output:
                    if '#' not in line:
                        if 'w;' in line:
                            data[iteration] = objectives
                            iteration = int(line.split(';')[-1])
                            objectives = defaultdict(list)
                        elif 'end;' in line:
                            data[iteration] = objectives            
                            iteration = int(line.split(';')[3].split('/')[0])
                            objectives = defaultdict(list)
                        elif '[' in line:
                            line = line.replace('[', '')
                            line = line.replace(']', '')
                            values = [ int(f[:-1]) if f[-1] == '.' else float(f) for f in line.split() ]
                            assert k == len(values)
                            objectives[iteration].append(values)                        
                        elif 'budget' in line:
                            line = line.split(';')[1:]
                            values = [ float(f) for f in line ]
                            budget[iteration].append(values)
                        elif 'usage' in line:
                            line = line.split(';')[1:]
                            stage = line.pop(0)
                            heur = line.pop(0)
                            count = int(line.pop(0))
                            uses[panel][(stage, heur)].append(count) # combine all replicas of the same instance type
                            present[stage].add(heur)
            for obj in range(k + 1): # budget will be objective k in these files
                with open(f'r{r + 1}_B{k}_{n}_{obj}.txt') as target:
                    for iteration in objectives:
                        data = [ s[obj] for s in ( objectives[iteration] if obj < k else budget[iteration] ) ] 
                        values = candlesticks(data)
                        print(f'{iteration} {values}', file = target)
        for obj in range(k + 1):
            name = 'Budget' if obj == k else f'Objective {k + 1}'
            for r in range(replicas):
                print(f'set ylabel "{name} for replica {r + 1}"')
                wb = f'u 1:3:2:5:6 with candlesticks lt -1 lw 2 lc rgb c{obj} whiskerbars, \\'
                mb = f'"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c{obj}'
                print(f'plot "r{r}_B{k}_{n}_{obj}.txt" {wb}\n{mb}')
        print('unset multiplot')

heuristics = dict()
counter = dict()        
for stage in present:
    heuristics[stage] = list(present[stage]).sort() # alphabetical
    counter[stage] = [ c + 1 for c in range(len(heuristics)) ]

for panel in sets:
    k, n, c = sets[panel]
    for stage in present:
        with open(f'h_B{k}_{n}_{stage}.txt') as target:
            for (heur, c) in zip(heuristics[stage], counter[stage]):
                data = uses[panel].get((stage, heur), None)
                lst = candlesticks(data)
                print(f'{c + 1} {lst}', file = target)
        
print('''set term postscript eps font ",8" size 3, 4 color
set boxwidth 0.6 relative
set style fill solid border -1
set key off
xlabel "Heuristic"
set ylabel "Number of uses"
set ytics 0, 1000''')
print(f'set multiplot layout {len(sets)}, 2')
print(f'set output "heur.eps"')

wb = 'using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00# whiskerbars, \\'
mb = '"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"'

for stage in present:
    lst = ','.join([ f'"{h}", {c}' for (h, c) in zip(heuristics, counter) ])
    print(f'set xtics ({lst})')
    for panel in uses:
        k, n, c = sets[panel]
        print(f'set title "B {n} projects, {k} objectives: {stage}"')
        print(f'plot "h_B{k}_{n}_{stage}.txt" {wb}\n{mb}')

