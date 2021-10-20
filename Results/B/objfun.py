import os
import numpy as np
from math import log, floor, ceil
from collections import defaultdict

def candlestick(data):
    return f'{float(min(data))} {np.quantile(data, 0.25)} {np.quantile(data, 0.5)} {np.quantile(data, 0.75)} {float(max(data))}'

print('''set term postscript eps font ",43" size 32, 16 color
set key off
set boxwidth 0.6 relative
set style fill solid border -1
set logscale x
set xrange [0.6:70]
set xtics ("0" 1, "1" 2, "2" 4, "3" 8, "4" 16, "5" 32, "6" 64)
set xlabel "Iteration (power of 2)"
set ylabel "Value"
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

for panel in sets:
    k, n, c = sets[panel]
    print(f'set output "objfun{panel}.eps"')
    print(f'set multiplot layout {len(instances)}, {k + 1}')    
    for i in range(c):
        filename = f'k{k}n{n}i{i}.dat'
        replicas = []
        for r in '123':
            data = defaultdict()
            iteration = 0
            objectives = defaultdict(list)
            for line in replica:
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
                        values = [ int(f[:-1]) if f[-1] = '.' else float(f) for f in line.split() ]
                        objectives[iteration].append(values)
                        assert k == len(values)
            data[iteration] = objectives
            replicas.append(data)
        print(f'set title "Instance {i + 1}: n = {n} and k = {k}" font ",44"\nplot ', end = '')
        for obj in range(k):
            name = 'Budget' i
            print('set ylabel {name}')

WORK IN PROGRESS
        
set title 'B 20-4 1 Budget' font ",24"
set yrange [460000000:490000000]
plot 'sol_b20_4obj1.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [0:300000]
set title 'B 20-4 1 Objective 1' font ",24"
plot 'sol_b20_4obj1.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-4 1 Objective 2' font ",24"
plot 'sol_b20_4obj1.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set yrange [100000:400000]
set title 'B 20-4 1 Objective 3' font ",24"
plot 'sol_b20_4obj1.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 20-4 1 Objective 4' font ",24"
plot 'sol_b20_4obj1.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4

set title 'B 20-4 2 Budget' font ",24"
set yrange [460000000:490000000]
plot 'sol_b20_4obj2.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [0:300000]
set title 'B 20-4 2 Objective 1' font ",24"
plot 'sol_b20_4obj2.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-4 2 Objective 2' font ",24"
plot 'sol_b20_4obj2.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set yrange [100000:400000]
set title 'B 20-4 2 Objective 3' font ",24"
plot 'sol_b20_4obj2.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 20-4 2 Objective 4' font ",24"
plot 'sol_b20_4obj2.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4

set title 'B 20-4 3 Budget' font ",24"
set yrange [460000000:490000000]
plot 'sol_b20_4obj3.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [0:300000]
set title 'B 20-4 3 Objective 1' font ",24"
plot 'sol_b20_4obj3.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-4 3 Objective 2' font ",24"
plot 'sol_b20_4obj3.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set yrange [100000:400000]
set title 'B 20-4 3 Objective 3' font ",24"
plot 'sol_b20_4obj1.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 20-4 3 Objective 4' font ",24"
plot 'sol_b20_4obj1.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4

    print('unset multiplot')

unset multiplot
set term postscript eps font ",26" size 32, 12 color
set output "objfunb.eps"
set xrange [0.6:600]
set xtics ("0" 1, "1" 2, "2" 4, "3" 8, "4" 16, "5" 32, "6" 64, "7" 128, "8" 256)

set multiplot layout 3, 10

set title 'B 20-9 1 Budget' font ",24"
set yrange [400000000:550000000]
plot 'sol_b20_9obj1.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-20000:200000]
set title 'B 20-9 1 Objective 1' font ",24"
plot 'sol_b20_9obj1.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-9 1 Objective 2' font ",24"
plot 'sol_b20_9obj1.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 20-9 1 Objective 3' font ",24"
plot 'sol_b20_9obj1.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-20000:300000]
set title 'B 20-9 1 Objective 4' font ",24"
plot 'sol_b20_9obj1.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 20-9 1 Objective 5' font ",24"
plot 'sol_b20_9obj1.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 20-9 1 Objective 6' font ",24"
plot 'sol_b20_9obj1.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [-20000:400000]
set title 'B 20-9 1 Objective 7' font ",24"
plot 'sol_b20_9obj1.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 20-9 1 Objective 8' font ",24"
plot 'sol_b20_9obj1.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 20-9 1 Objective 9' font ",24"
plot 'sol_b20_9obj1.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 20-9 2 Budget' font ",24"
set yrange [400000000:550000000]
plot 'sol_b20_9obj2.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-20000:200000]
set title 'B 20-9 2 Objective 1' font ",24"
plot 'sol_b20_9obj2.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-9 2 Objective 2' font ",24"
plot 'sol_b20_9obj2.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 20-9 2 Objective 3' font ",24"
plot 'sol_b20_9obj2.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-20000:300000]
set title 'B 20-9 2 Objective 4' font ",24"
plot 'sol_b20_9obj2.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 20-9 2 Objective 5' font ",24"
plot 'sol_b20_9obj2.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 20-9 2 Objective 6' font ",24"
plot 'sol_b20_9obj2.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [-20000:400000]
set title 'B 20-9 2 Objective 7' font ",24"
plot 'sol_b20_9obj2.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 20-9 2 Objective 8' font ",24"
plot 'sol_b20_9obj2.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 20-9 2 Objective 9' font ",24"
plot 'sol_b20_9obj2.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9


set title 'B 20-9 3 Budget' font ",24"
set yrange [400000000:550000000]
plot 'sol_b20_9obj3.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-20000:200000]
set title 'B 20-9 3 Objective 1' font ",24"
plot 'sol_b20_9obj3.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 20-9 3 Objective 2' font ",24"
plot 'sol_b20_9obj3.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 20-9 3 Objective 3' font ",24"
plot 'sol_b20_9obj3.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-20000:300000]
set title 'B 20-9 3 Objective 4' font ",24"
plot 'sol_b20_9obj3.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 20-9 3 Objective 5' font ",24"
plot 'sol_b20_9obj3.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 20-9 3 Objective 6' font ",24"
plot 'sol_b20_9obj3.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [-20000:400000]
set title 'B 20-9 3 Objective 7' font ",24"
plot 'sol_b20_9obj3.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 20-9 3 Objective 8' font ",24"
plot 'sol_b20_9obj3.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 20-9 3 Objective 9' font ",24"
plot 'sol_b20_9obj3.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

unset multiplot

set output "objfunc.eps"
set xrange [0.6:300]
set xtics ("0" 1, "1" 2, "2" 4, "3" 8, "4" 16, "5" 32, "6" 64, "7" 128)

set multiplot layout 3, 10

set title 'B 30-9 1 Budget' font ",24"
set yrange [600000000:800000000]
plot 'sol_b30_9obj1.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-50000:300000]
set title 'B 30-9 1 Objective 1' font ",24"
plot 'sol_b30_9obj1.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 30-9 1 Objective 2' font ",24"
plot 'sol_b30_9obj1.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 30-9 1 Objective 3' font ",24"
plot 'sol_b30_9obj1.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-50000:500000]
set title 'B 30-9 1 Objective 4' font ",24"
plot 'sol_b30_9obj1.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 30-9 1 Objective 5' font ",24"
plot 'sol_b30_9obj1.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 30-9 1 Objective 6' font ",24"
plot 'sol_b30_9obj1.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [0:600000]
set title 'B 30-9 1 Objective 7' font ",24"
plot 'sol_b30_9obj1.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 30-9 1 Objective 8' font ",24"
plot 'sol_b30_9obj1.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 30-9 1 Objective 9' font ",24"
plot 'sol_b30_9obj1.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 30-9 2 Budget' font ",24"
set yrange [600000000:800000000]
plot 'sol_b30_9obj2.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-50000:300000]
set title 'B 30-9 2 Objective 1' font ",24"
plot 'sol_b30_9obj2.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 30-9 2 Objective 2' font ",24"
plot 'sol_b30_9obj2.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 30-9 2 Objective 3' font ",24"
plot 'sol_b30_9obj2.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-50000:500000]
set title 'B 30-9 2 Objective 4' font ",24"
plot 'sol_b30_9obj2.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 30-9 2 Objective 5' font ",24"
plot 'sol_b30_9obj2.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 30-9 2 Objective 6' font ",24"
plot 'sol_b30_9obj2.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [0:600000]
set title 'B 30-9 2 Objective 7' font ",24"
plot 'sol_b30_9obj2.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 30-9 2 Objective 8' font ",24"
plot 'sol_b30_9obj2.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 30-9 2 Objective 9' font ",24"
plot 'sol_b30_9obj2.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9


set title 'B 30-9 3 Budget' font ",24"
set yrange [600000000:800000000]
plot 'sol_b30_9obj3.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [-50000:300000]
set title 'B 30-9 3 Objective 1' font ",24"
plot 'sol_b30_9obj3.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 30-9 3 Objective 2' font ",24"
plot 'sol_b30_9obj3.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 30-9 3 Objective 3' font ",24"
plot 'sol_b30_9obj3.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set yrange [-50000:500000]
set title 'B 30-9 3 Objective 4' font ",24"
plot 'sol_b30_9obj3.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 30-9 3 Objective 5' font ",24"
plot 'sol_b30_9obj3.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 30-9 3 Objective 6' font ",24"
plot 'sol_b30_9obj3.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set yrange [0:600000]
set title 'B 30-9 3 Objective 7' font ",24"
plot 'sol_b30_9obj3.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 30-9 3 Objective 8' font ",24"
plot 'sol_b30_9obj3.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 30-9 3 Objective 9' font ",24"
plot 'sol_b30_9obj3.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

unset multiplot
set term postscript eps font ",26" size 32, 16 color
set output "objfund.eps"

set xrange [0.6:500]
set xtics ("0" 1, "1" 2, "2" 4, "3" 8, "4" 16, "5" 32, "6" 64, "7" 128, "8" 256)

set multiplot layout 5, 10

set title 'B 100-9 1 Budget' font ",24"
set yrange [180000:260000]
plot 'sol_b100_9obj1.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [100000:1300000]
set title 'B 100-9 1 Objective 1' font ",24"
plot 'sol_b100_9obj1.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 100-9 1 Objective 2' font ",24"
plot 'sol_b100_9obj1.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 100-9 1 Objective 3' font ",24"
plot 'sol_b100_9obj1.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 100-9 1 Objective 4' font ",24"
plot 'sol_b100_9obj1.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 100-9 1 Objective 5' font ",24"
plot 'sol_b100_9obj1.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 100-9 1 Objective 6' font ",24"
plot 'sol_b100_9obj1.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set title 'B 100-9 1 Objective 7' font ",24"
plot 'sol_b100_9obj1.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 100-9 1 Objective 8' font ",24"
plot 'sol_b100_9obj1.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 100-9 1 Objective 9' font ",24"
plot 'sol_b100_9obj1.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 100-9 2 Budget' font ",24"
set yrange [180000:260000]
plot 'sol_b100_9obj2.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [100000:1300000]
set title 'B 100-9 2 Objective 1' font ",24"
plot 'sol_b100_9obj2.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 100-9 2 Objective 2' font ",24"
plot 'sol_b100_9obj2.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 100-9 2 Objective 3' font ",24"
plot 'sol_b100_9obj2.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 100-9 2 Objective 4' font ",24"
plot 'sol_b100_9obj2.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 100-9 2 Objective 5' font ",24"
plot 'sol_b100_9obj2.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 100-9 2 Objective 6' font ",24"
plot 'sol_b100_9obj2.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set title 'B 100-9 2 Objective 7' font ",24"
plot 'sol_b100_9obj2.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 100-9 2 Objective 8' font ",24"
plot 'sol_b100_9obj2.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 100-9 2 Objective 9' font ",24"
plot 'sol_b100_9obj2.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 100-9 3 Budget' font ",24"
set yrange [180000:260000]
plot 'sol_b100_9obj3.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [100000:1300000]
set title 'B 100-9 3 Objective 1' font ",24"
plot 'sol_b100_9obj3.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 100-9 3 Objective 2' font ",24"
plot 'sol_b100_9obj3.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 100-9 3 Objective 3' font ",24"
plot 'sol_b100_9obj3.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 100-9 3 Objective 4' font ",24"
plot 'sol_b100_9obj3.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 100-9 3 Objective 5' font ",24"
plot 'sol_b100_9obj3.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 100-9 3 Objective 6' font ",24"
plot 'sol_b100_9obj3.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set title 'B 100-9 3 Objective 7' font ",24"
plot 'sol_b100_9obj3.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 100-9 3 Objective 8' font ",24"
plot 'sol_b100_9obj3.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 100-9 3 Objective 9' font ",24"
plot 'sol_b100_9obj3.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 100-9 4 Budget' font ",24"
set yrange [180000:260000]
plot 'sol_b100_9obj4.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [100000:1300000]
set title 'B 100-9 4 Objective 1' font ",24"
plot 'sol_b100_9obj4.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 100-9 4 Objective 2' font ",24"
plot 'sol_b100_9obj4.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 100-9 4 Objective 3' font ",24"
plot 'sol_b100_9obj4.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 100-9 4 Objective 4' font ",24"
plot 'sol_b100_9obj4.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 100-9 4 Objective 5' font ",24"
plot 'sol_b100_9obj4.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 100-9 4 Objective 6' font ",24"
plot 'sol_b100_9obj4.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set title 'B 100-9 4 Objective 7' font ",24"
plot 'sol_b100_9obj4.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 100-9 4 Objective 8' font ",24"
plot 'sol_b100_9obj4.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 100-9 4 Objective 9' font ",24"
plot 'sol_b100_9obj4.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9

set title 'B 100-9 5 Budget' font ",24"
set yrange [180000:260000]
plot 'sol_b100_9obj5.txt' u 1:8:7:11:10 notitle with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
     '' u 1:9:9:9:9 notitle with candlesticks lt -1 lw 3 lc rgb c0
set yrange [100000:1300000]
set title 'B 100-9 5 Objective 1' font ",24"
plot 'sol_b100_9obj5.txt' u 1:13:12:16:15 notitle with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
     '' u 1:14:14:14:14 notitle with candlesticks lt -1 lw 3 lc rgb c1
set title 'B 100-9 5 Objective 2' font ",24"
plot 'sol_b100_9obj5.txt' u 1:18:17:21:20 notitle with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
     '' u 1:19:19:19:19 notitle with candlesticks lt -1 lw 3 lc rgb c2
set title 'B 100-9 5 Objective 3' font ",24"
plot 'sol_b100_9obj5.txt' u 1:23:22:26:25 notitle with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
     '' u 1:24:24:24:24 notitle with candlesticks lt -1 lw 3 lc rgb c3
set title 'B 100-9 5 Objective 4' font ",24"
plot 'sol_b100_9obj5.txt' u 1:28:27:31:30 notitle with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
     '' u 1:29:29:29:29 notitle with candlesticks lt -1 lw 3 lc rgb c4
set title 'B 100-9 5 Objective 5' font ",24"
plot 'sol_b100_9obj5.txt' u 1:33:32:36:35 notitle with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
     '' u 1:34:34:34:34 notitle with candlesticks lt -1 lw 3 lc rgb c5
set title 'B 100-9 5 Objective 6' font ",24"
plot 'sol_b100_9obj5.txt' u 1:38:37:41:40 notitle with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
     '' u 1:39:39:39:39 notitle with candlesticks lt -1 lw 3 lc rgb c6
set title 'B 100-9 5 Objective 7' font ",24"
plot 'sol_b100_9obj5.txt' u 1:43:42:46:45 notitle with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
     '' u 1:44:44:44:44 notitle with candlesticks lt -1 lw 3 lc rgb c7
set title 'B 100-9 5 Objective 8' font ",24"
plot 'sol_b100_9obj5.txt' u 1:48:47:51:50 notitle with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
     '' u 1:49:49:49:49 notitle with candlesticks lt -1 lw 3 lc rgb c8
set title 'B 100-9 5 Objective 9' font ",24"
plot 'sol_b100_9obj5.txt' u 1:53:20:56:55 notitle with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
     '' u 1:54:54:54:54 notitle with candlesticks lt -1 lw 3 lc rgb c9


unset multiplot

