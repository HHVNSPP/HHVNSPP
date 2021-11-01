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
powers = [ p for p in range(6, 10) ]
maxiter = 0
for p in powers:
    n = 2**p
    with open(f'setC{n}.plot', 'w') as target:
        print(f'set term postscript eps size 24, 12 color\nset output "setC{n}.eps"', file = target)
        print('''set logscale x\nset boxwidth 0.06 absolute\nset style fill solid border -1
set xtics 1, 2\nset xlabel "Iteration"''', file = target)
        print(f'set multiplot layout {instances}, {2 * replicas}', file = target)
        for i in range(instances):
            for syn in [ 's', '' ]: # with, without
                suffix = '' if syn == 's' else 'out'
                for r in range(replicas):
                    filename = f'Replicas/With{suffix}Synergies/r{r + 1}{syn}_C{n}_{i + 1}.txt'
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
                                    iteration = int(line.split(';')[2].split('/')[0]) + 1
                                    maxiter = max(maxiter, iteration)                            
                                elif 'electre' in line: # final front
                                    if '[' in line and ']' not in line:
                                        combine = line
                                        continue
                                    line = line.split(';')
                                    if iteration not in size: # not the same as the last recorded
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
                    filename = f'Parsed/r{r + 1}{syn}_C{n}_{i + 1}.txt'                            
                    with open(filename, 'w') as parsed:
                        for iteration in size:
                            b = budget[iteration]
                            s = size[iteration]
                            print(f'{iteration} {candlestick(b)} {candlestick(s)}', file = parsed)
            print(f'set xrange [0.6:{1.9 * (maxiter + 0.1)}]', file = target)
            for r in range(replicas): # two plots per replica
                for kind in [ 'Front size', 'Budget' ]:
                    red = 99
                    blue = 33
                    med = 4
                    if kind == 'Front size':
                        if n == 64: # manually adjusted for maximum aesthetic
                            print('set yrange [35:70]', file = target)
                        elif n == 128:
                            print('set yrange [90:140]', file = target)
                        elif n == 256:
                            print('set yrange [170:270]', file = target)
                        elif n == 512:
                            print('set yrange [450:530]', file = target)                            
                        red = 33
                        blue = 99
                        print(f'set title "{n} projects, instance {i + 1}, replica {r + 1}"', file = target)
                        med = 9
                    else:
                        if n == 64:
                            print('set yrange [870:1050]', file = target)
                        elif n == 128:
                            print('set yrange [1700:2050]', file = target)
                        elif n == 256:
                            print('set yrange [3650:3920]', file = target)                            
                        elif n == 512:
                            print('set yrange [7200:7900]', file = target)
                        print(f'set ylabel "{kind}"', file = target)
                    cols = f'{med - 1}:{med - 2}:{med + 2}:{med + 1}'
                    for syn in [ 's', '' ]:
                        cont = ''
                        filename = f'Parsed/r{r + 1}{syn}_C{n}_{i + 1}.txt'
                        mult = 1.2
                        if syn == 's':
                            mult = 0.7
                            c = f'lc rgb "#{red}66{blue}"'
                            print(f'plot "{filename}" u ({mult} * ($1 + 0.1)):{cols} t "with" with candlesticks lt -1 lw 1 {c} whiskerbars, \\', \
                                  file = target)
                            cont = ',\\'
                        else:
                            c = f'lc rgb "#{red}00{blue}"'                                
                            print(f'     "{filename}" u ({mult} * ($1 + 0.1)):{cols} t "without" with candlesticks lt -1 lw 1 {c} whiskerbars, \\',
                                  file = target)
                        print(f'     "" u ({mult} * ($1 + 0.1)):{med}:{med}:{med}:{med} notitle with candlesticks lt -1 lw 2 {c} {cont}',
                              file = target) # median bar
        print('unset multiplot', file = target)
