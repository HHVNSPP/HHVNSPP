import os
import numpy as np
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

uses = dict()
present = { 'shake': set(), 'search': set() }
maxcount = {'shake': 0, 'search': 0 }

cases = { 'A': [''], 'B': [''], 'C': ['WithSynergies/', 'WithoutSynergies/']}

uses['global'] = defaultdict(list)

for s in 'ABC':
    base = r'../Results/' + s + '/Replicas/'
    for c in cases[s]:
        directory = base + c
        for filename in os.listdir(directory):
            if filename.startswith('r') and filename.endswith('.txt'):
                f = filename.split('_')
                i = f[1].split('.')[0]
                dataset = f'Set {s} instance {i}'
                if 's' in f[0]:
                    dataset = f'{dataset} with synergies'
                else:
                    dataset = f'{dataset} without synergies'
                if dataset not in uses:
                    uses[dataset] = defaultdict(list)
                source = f'{directory}{filename}'
                print(source)
                with open(source) as output:
                    for line in output:
                        if '#' not in line:
                            if 'usage' in line:
                                line = line.split(';')[1:]
                                stage = line.pop(0)
                                line = line[0].strip().split('=')
                                heur = line.pop(0)
                                count = int(line.pop(0))
                                maxcount[stage] = max(count, maxcount[stage])
                                uses[dataset][(stage, heur)].append(count) # combine all replicas of the same instance type
                                uses['global'][(stage, heur)].append(count) # combine all replicas of the same instance type
                                present[stage].add(heur)

heuristics = dict()
counter = dict()
for stage in present:
    heuristics[stage] = sorted(list(present[stage]))
    counter[stage] = [ c + 1 for c in range(len(heuristics[stage])) ]

for stage in present:
    for dataset in uses:
        filename = '_'.join(dataset.split())
        with open(f'Usage/{filename}_{stage}.txt', 'w') as target:
            for (heur, c) in zip(heuristics[stage], counter[stage]):
                data = uses[dataset].get((stage, heur), None)
                lst = candlestick(data)
                print(f'{c} {lst}', file = target)
    with open(f'Usage/global_{stage}.txt', 'w') as target:
            for (heur, c) in zip(heuristics[stage], counter[stage]):
                data = uses['global'].get((stage, heur), None)
                lst = candlestick(data)
                print(f'{c} {lst}', file = target)

wb = { 'shake': 'using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \\',
       'search': 'using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \\' }
mb = '"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"'

with open('usage.plot', 'w') as target:
    print(f'set term postscript eps font ",16" size 12, {4 * len(uses)} color', file = target)
    print('set boxwidth 0.6 relative\nset style fill solid border -1\nset output "usage_details.eps"', file = target)
    print('set key off\nset ylabel "Number of uses"''', file = target)
    print(f'set multiplot layout {len(uses)}, 2', file = target)
    for dataset in uses:
        for stage in present:
            print(f'set xrange [0.1:{len(heuristics[stage])+0.9}]', file = target)
            print(f'set yrange [{-0.1 * maxcount[stage]}:{1.1 * maxcount[stage]}]', file = target)
            lst = ','.join([ f'"{h}" {c}' for (h, c) in zip(heuristics[stage], counter[stage]) ])
            print(f'set xtics ({lst}) rotate by 90 right offset 0,-1', file = target)
            print(f'set title "{dataset}"', file = target)
            filename = '_'.join(dataset.split())            
            print(f'plot "Usage/{filename}_{stage}.txt" {wb[stage]}\n{mb}', file = target)
    print(f'unset multiplot\nset term postscript eps font ",24" size 12, 12 color', file = target)
    print('set boxwidth 0.6 relative\nset style fill solid border -1\nset output "usage.eps"', file = target)
    print('set key off\nset ylabel "Number of uses"''', file = target)
    print(f'set multiplot layout 2, 1', file = target)
    for stage in present:
        print(f'set title "Global heuristic usage in the {stage} stage"', file = target)
        print(f'set xrange [0.1:{len(heuristics[stage])+0.9}]', file = target)
        print(f'set yrange [{-0.1 * maxcount[stage]}:{1.1 * maxcount[stage]}]', file = target)
        lst = ','.join([ f'"{h}" {c}' for (h, c) in zip(heuristics[stage], counter[stage]) ])
        print(f'set xtics ({lst}) rotate by 90 right offset 0,-1', file = target)
        print(f'plot "Usage/global_{stage}.txt" {wb[stage]}\n{mb}', file = target)

