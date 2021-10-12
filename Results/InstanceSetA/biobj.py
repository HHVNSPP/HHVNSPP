# parse the result files to construct the illustration
import os

print('''set term postscript eps font ",20" size 12, 6 color
set output "biobj.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Benefit"
set datafile separator ","
set key outside Right
set pointsize 1.2
set key off
#set xrange [59:86]
set xtics 60, 5
#set yrange [260:540]
set ytics 300, 100''')

# valuations of solutions provided by the authors of Instance Set A
known = [ (67, 352), (75, 411), (68, 378), (74, 448), (79, 459),
          (74, 404), (76, 416), (68, 397), (74, 472), (76, 460),
          (76, 386), (78, 482), (79, 426), (81, 469), (80, 388) ]

counter = 0
for filename in os.listdir('.'):
    if filename.startswith('r') and filename.endswith('.dat'):
        labels = filename.split('_')
        replica = int(labels.pop(0)[1:])
        instance = labels.pop(0)
        print(f'Processing replica {replica} of instance {instance}')
        if replica == 1: # print the gnuplot commands only for the first one
            print(f'set title "A {counter + 1} ({instance})" font ",30"')
            (x, y) = known[counter]
            print(f'x={x}')
            print(f'x={y}')
            print('set arrow 1 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#ff0000"')
            # draw only the first three replicas (to avoid clutter)
            print('plot "100a_{counter}_1.csv" using 1:2 with points pt 7 lc rgb "#009999", y with lines lt -1 lw 3 lc rgb "#ff0000", \\')
            print('"100a_{counter}_2.csv" using 1:2 with points pt 5 lc rgb "#990099", \\')
            print('"100a_{counter}_3.csv" using 1:2 with points pt 3 lc rgb "#999900"')
            print('show arrow 1')
            print('unset arrow 1')
        if replica < 4: # make the CSV files that gnuplot will read
            with open(filename) as source:
                with open('100a_{counter}_{replica}.csv', 'w') as target:
                    for line in source:
                        if 'electre' in line:
                            fields = line.split(';')[-1][2:-2]
                            print(fields, file = target)
print('unset multiplot')
