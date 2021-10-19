# parse the result files to construct the illustration
import os

# valuations of solutions provided by the authors of Instance Set A
known = [ (67, 352), (75, 411), (68, 378), (74, 448), (79, 459),
          (74, 404), (76, 416), (68, 397), (74, 472), (76, 460),
          (76, 386), (78, 482), (79, 426), (81, 469), (80, 388) ]

panels = dict()

for filename in os.listdir('.'):
    if filename.startswith('r') and filename.endswith('.dat'):
        labels = filename.split('_')
        replica = int(labels[0][1:])
        label = labels[1]
        instance = int(labels[-1][:-4])
        if replica == 1: # print the gnuplot commands only for the first one
            (x, y) = known[instance - 1]
            panel = f'set title "A {instance}" font ",30"\n'
            panel += f'x={x}\n'
            panel += f'y={y}\n'
            panel += f'set arrow {instance} from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"\n'
            # draw only the first three replicas (to avoid clutter)
            panel += f'plot "A{instance}_r1.csv" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \\\n'
            panel += f'     "A{instance}_r2.csv" using 1:2 with points pt 5 lc rgb "#ff0000", \\\n'
            panel += f'     "A{instance}_r3.csv" using 1:2 with points pt 7 lc rgb "#00ff00"\n'
            panel += f'show arrow {instance}\n'
            panel += f'unset arrow {instance}\n'
            panels[instance] = panel
        if replica < 4: # make the CSV files that gnuplot will read
            with open(filename) as source:
                with open(f'A{instance}_r{replica}.csv', 'w') as target:
                    for line in source:
                        if 'electre' in line:
                            values = line.split(';')[-1][2:-3]
                            print(' '.join(values.replace('. ', '').split()), file = target)

with open('biobj.plot', 'w') as target:
    print('''set term postscript eps font ",20" size 12, 6 color
set output "biobj.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Total benefit"
set key outside Right
set pointsize 1
set key off
set xrange [35:85]
set xtics 40, 10
set yrange [50:550]
set ytics 100, 100''', file = target)
    for instance in range(1, 16):
        print(panels.get(instance, ''), file = target)
    print('unset multiplot', file = target)
