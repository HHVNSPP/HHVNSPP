# parse the result files to construct the illustration
import os

minCount = float('inf')
maxCount = -minCount
minBenefit = minCount
maxBenefit = -minCount


# ideal solutions optimizing each objective separately
known = dict()
for filename in os.listdir('Ideal/'):
    if filename.startswith('EXR_') and filename.endswith('.txt'):
        labels = filename.split('_')
        instance = int(labels[-1][:-4])
        with open(f'Ideal/{filename}') as source:
            source.readline() # [INSTANCE=P100R5A2S5_01.txt]
            source.readline() # [OBJECTIVE VALUES]
            num = int(source.readline().strip().split('=')[-1][:-2]) # NUM. PROJECTS=80.0
            imp = float(source.readline().strip().split('=')[-1]) # IMPACT=2653.4322294150666
            maxCount = max(num, maxCount)
            maxBenefit = max(imp, maxBenefit)
            known[instance] = (num, imp)
            print(f'Instance {instance}: ideally {num} / {imp:.2f}')

panels = dict()

folder = 'Replicas/OneSecondLimit/'

for filename in os.listdir(folder):
    if filename.startswith('r') and filename.endswith('.txt'):
        labels = filename.split('_')
        rl = labels[0][1:]
        if 's' not in rl:
            replica = int(rl)
        else:
            continue # we do not analyze the ones with synergies since we have no baseline for them
        label = labels[1]
        instance = int(labels[-1][:-4])
        print(f'Parsing replica {replica} for instance {instance}')
        if replica == 1: # print the gnuplot commands only for the first one
            (x, y) = known[instance]
            minCount = min(x, minCount)
            maxCount = max(x, maxCount)
            minBenefit = min(y, minBenefit)
            maxBenefit = max(y, maxBenefit)
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
benefitLow = floor(0.7 * minBenefit / 100) * 100
benefitHigh = ceil(1.1 * maxBenefit / 100) * 100
                            
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
    print(f'set yrange [{benefitLow-100}:{benefitHigh+100}]', file = target)
    print(f'set ytics {benefitLow}, 1000', file = target)
    for instance in range(1, 16):
        print(panels.get(instance, ''), file = target)
    print('unset multiplot', file = target)

print('Parsing completed')
