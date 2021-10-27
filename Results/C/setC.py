print('set term postscript eps size 6, 6 color\nset output "setC.eps"')
powers = [ p for p in range(6, 10) ]
print(f'set multiplot layout {len(powers)}, 1')
print('''set xlabel "Runtime (seconds)"
set ylabel "Front size"
set key outside Right
set pointsize 1.2''')

# TODO: parse the data into box-whiskers plots

for p in powers:
    n = 2**p
    print(f'set title "{n} projects"')
    print(f'plot "C{n}s.txt" with linespoints  t " with syn" pt 7 dt 2 lw 3 lc rgb "#00aa00", \\')
    print(f'"C{n}.txt" with linespoints t " w/out syn" pt 7 lt -1 lw 2 lc rgb "#990000"')
print('unset multiplot')
