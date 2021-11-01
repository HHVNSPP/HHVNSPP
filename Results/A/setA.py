# parse the result files to construct the illustration
import os

# valuations of solutions provided by the authors of Instance Set A
known = [ (67, 352), (75, 411), (68, 378), (74, 448), (79, 459),
          (74, 404), (76, 416), (68, 397), (74, 472), (76, 460),
          (76, 386), (78, 482), (79, 426), (81, 469), (80, 388) ]

panels = dict()

minCount = float('inf')
maxCount = -minCount
minBenefit = minCount
maxBenefit = -minBenefit

for filename in os.listdir('Replicas/'):
    if filename.startswith('r') and filename.endswith('.txt'):
        labels = filename.split('_')
        rl = labels[0][1:]
        if 's' not in rl:
            replica = int(rl)
        else:
            continue # we do not analyze the ones with synergies since we have no baseline for them
        label = labels[1]
        instance = int(labels[-1][:-4])
        if replica == 1: # print the gnuplot commands only for the first one
            (x, y) = known[instance - 1]
            minCount = min(x, minCount)
            maxCount = max(x, maxCount)
            minBenefit = min(y, minBenefit)
            maxBenefit = min(y, maxBenefit)
            panel = f'set title "A {instance}" font ",30"\n'
            panel += f'x={x}\n'
            panel += f'y={y}\n'
            panel += f'set arrow {instance} from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"\n'
            # draw only the first three replicas (to avoid clutter)
            panel += f'plot "Parsed/A{instance}_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \\\n'
            panel += f'     "Parsed/A{instance}_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \\\n'
            panel += f'     "Parsed/A{instance}_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"\n'
            panel += f'show arrow {instance}\n'
            panel += f'unset arrow {instance}\n'
            panels[instance] = panel
        if replica < 4: # make the TXT files that gnuplot will read
            with open('Replicas/' + filename) as source:
                with open(f'Parsed/A{instance}_r{replica}.txt', 'w') as target:
                    for line in source:
                        if 'electre' in line:
                            values = line.split(';')[2][2:-3].split()
                            count = int(values.pop(0)[:-1]) # skip the . at the end
                            benefit = float(values.pop(0))
                            print(f'{count} {benefit}', file = target)
                            minCount = min(minCount, count)
                            minBenefit = min(minBenefit, benefit)
                            maxCount = max(maxCount, count)
                            maxBenefit = max(maxBenefit, benefit)

from math import floor, ceil
countLow = floor(0.9 * minCount / 10) * 10
countHigh = ceil(1.2 * maxCount / 10) * 10
benefitLow = floor(0.9 * minBenefit / 100) * 100
benefitHigh = ceil(1.2 * maxBenefit / 100) * 100
                            
with open('setA.plot', 'w') as target:
    print('''set term postscript eps font ",20" size 12, 6 color
set output "setA.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Total benefit"
set key outside Right
set pointsize 1
set key off''', file = target)
    print(f'set xrange [{countLow-5}:{countHigh+5}]', file = target)
    print(f'set xtics {countLow}, 10', file = target)
    print(f'set yrange [{benefitLow-50}:{benefitHigh+50}]', file = target)
    print(f'set ytics {benefitLow}, 100', file = target)
    for instance in range(1, 16):
        print(panels.get(instance, ''), file = target)
    print('unset multiplot', file = target)
