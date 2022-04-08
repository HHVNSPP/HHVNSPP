# parse the result files to construct the illustration
import os

# ideal solutions optimizing each objective separately
count = dict()
benefit = dict()
maxCount = minCount = 100 # these instances all have 100 projects
minBenefit = float('inf')
maxBenefit = 0

with open('log_A.txt') as source:
    for line in source:
        if 'Instance' in line:
            which = line.split('/')[-1][:-5]
            count[which] = None
            benefit[which] = None
        elif 'IDEAL POINT' in line:
            value = float(line.split()[-1])
            if count[which] is None:
                value = int(round(value))
                count[which] = value
            else:
                benefit[which] = value
        elif 'Funding all' in line:
            value = float(line.split()[6])
            minBenefit = min(minBenefit, value)
            maxBenefit = max(maxBenefit, value)
            
print(f'Maximum project count for funding everything: {maxCount}')
print(f'Maximum benefit for funding everything: {maxBenefit}')
            
panels = dict()
folder = './'
for filename in os.listdir(folder):
    if filename.startswith('r') and filename.endswith('.txt'):
        if '-reduced-' not in filename:
            # we do not include the ones with synergies
            # in this analysis since they are not used in Gurobi
            continue
        fields = filename.split('-')
        replica = int(fields[0][1:])
        labels = fields[-1].split('_')
        instance = int(labels[1][:-4])
        label = f'{labels[0]}_{instance:02d}'
        print(f'Parsing replica {replica} for instance {instance}')
        if replica == 1: # print the gnuplot commands only for the first one
            x = count[label]
            y = benefit[label]            
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
            with open(folder + filename) as source:
                with open(f'Parsed/A{instance}_r{replica}.txt', 'w') as target:
                    for line in source:
                        if 'electre' in line:
                            values = line.split(';')[2][2:-3].split()
                            c = int(values.pop(0)[:-1]) # skip the . at the end
                            b = float(values.pop(0))
                            minCount = min(minCount, c)
                            maxCount = max(maxCount, c)
                            minBenefit = min(minBenefit, b)
                            maxBenefit = max(maxBenefit, b)
                            print(f'{c} {b}', file = target)

from math import floor, ceil
countLow = floor(0.9 * minCount / 10) * 10
countHigh = ceil(1.2 * maxCount / 10) * 10
benefitLow = floor(0.7 * minBenefit / 100) * 100
benefitHigh = ceil(1.1 * maxBenefit / 100) * 100
                            
with open('setA.plot', 'w') as target:
    print('''set term postscript eps font ",20" size 12, 6 color
set output "setA.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Total benefit"
set key outside Right
set pointsize 0.7
set key off''', file = target)
    print(f'set xrange [{countLow-5}:{countHigh+5}]', file = target)
    print(f'set xtics {countLow}, 20', file = target)
    print(f'set yrange [{benefitLow-100}:{benefitHigh+100}]', file = target)
    print(f'set ytics {benefitLow}, 200', file = target)
    for instance in range(1, 16):
        print(panels.get(instance, ''), file = target)
    print('unset multiplot', file = target)

print('Parsing completed')
