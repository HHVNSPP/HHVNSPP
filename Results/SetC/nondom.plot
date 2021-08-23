set term postscript eps size 6, 6 color
set output "nondom.eps"
set multiplot layout 4, 1
set xlabel "Runtime (seconds)"
set ylabel "# non-dom (avg)"
set datafile separator ","
set key outside Right
set pointsize 1.2
last=3010
set xrange [-100:(last + 100)]
set yrange [0:300]
set ytics 0, 100
set xtics 0, 300
set title "64 projects"
plot 'Gc_64consinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " with syn" pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     'Gc_64_nosinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " w/out syn" pt 7 lt -1 lw 2 lc rgb '#990000'
set title "128 projects"
plot 'Gc_128consinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " with syn" pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     'Gc_128nosinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " w/out syn" pt 7 lt -1 lw 2 lc rgb '#990000'
set title "256 projects"
plot 'Gc_256consinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " with syn" pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     'Gc_256nosinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " w/out syn" pt 7 lt -1 lw 2 lc rgb '#990000'
set title "512 projects"
plot 'Gc_512consinerg.csv' u ($1 <= last ? $1 : 1/0):2 every ::1 with linespoints  t " with syn" pt 7 dt 2 lw 3 lc rgb '#00aa00', \
     'Gc_512nosinerg.csv' u ($1 <= last ? $1 : 1/0):2  every ::1 with linespoints  t " w/out syn" pt 7 lt -1 lw 2 lc rgb '#990000'
unset multiplot