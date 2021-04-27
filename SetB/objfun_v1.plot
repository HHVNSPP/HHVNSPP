set term postscript eps size 12, 6 color
set output "objfuna.eps"
set title 'B 20-4'
set multiplot layout 3, 1
set xlabel "runtime (seconds)"
set ylabel "objective function"
set datafile separator ","
set key outside Right
set pointsize 1.2
last=4600
set yrange [100000:400000]
set ytics 100000,100000
set xrange [-100:(last + 100)]
set title 'B 20-4 1'
dx=75
l1=-1
l2=-1
l3=-1
l4=-1
val(l, i, x, last) = ((sprintf("obj_%d", i)  eq l) ? x : (last > 0 ? last : 1/0))
plot '2plt_b_20obj4_1.csv' u ($1 <= last ? $1 : 1/0):(l1=val(strcol(2), 1, $3, l1)) every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     '' u ($1 <= last ? $1 + 1 * dx : 1/0):(l2=val(strcol(2), 2, $3, l2)) every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lw 3 lc rgb '#0000bb', \
     '' u ($1 <= last ? $1 + 2 * dx : 1/0):(l3=val(strcol(2), 3, $3, l3)) every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lw 3 lc rgb '#cc0000', \
     '' u ($1 <= last ? $1 + 3 * dx : 1/0):(l4=val(strcol(2), 4, $4, l4)) every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lw 3 lc rgb '#00dddd'
set title 'B 20-4 2'
plot '2plt_b_20obj4_2.csv' u ($1 <= last ? $1 : 1/0):(l1=val(strcol(2), 1, $3, l1)) every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     '' u ($1 <= last ? $1 + 1 * dx : 1/0):(l2=val(strcol(2), 2, $3, l2)) every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lw 3 lc rgb '#0000bb', \
     '' u ($1 <= last ? $1 + 2 * dx : 1/0):(l3=val(strcol(2), 3, $3, l3)) every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lw 3 lc rgb '#cc0000', \
     '' u ($1 <= last ? $1 + 3 * dx : 1/0):(l4=val(strcol(2), 4, $4, l4)) every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lw 3 lc rgb '#00dddd'
set title 'B 20-4 3'
plot '2plt_b_20obj4_3.csv' u ($1 <= last ? $1 : 1/0):(l1=val(strcol(2), 1, $3, l1)) every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     '' u ($1 <= last ? $1 + 1 * dx : 1/0):(l2=val(strcol(2), 2, $3, l2)) every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lw 3 lc rgb '#0000bb', \
     '' u ($1 <= last ? $1 + 2 * dx : 1/0):(l3=val(strcol(2), 3, $3, l3)) every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lw 3 lc rgb '#cc0000', \
     '' u ($1 <= last ? $1 + 3 * dx : 1/0):(l4=val(strcol(2), 4, $4, l4)) every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lw 3 lc rgb '#00dddd'
