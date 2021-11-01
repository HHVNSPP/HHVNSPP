set term postscript eps size 24, 12 color
set output "setC64.eps"
set logscale x
set boxwidth 0.06 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
set multiplot layout 3, 6
set xrange [0.6:121.78999999999998]
set yrange [35:70]
set title "64 projects, instance 1, replica 1"
plot "Parsed/r1s_C64_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C64_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r1s_C64_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C64_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 1, replica 2"
plot "Parsed/r2s_C64_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C64_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r2s_C64_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C64_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 1, replica 3"
plot "Parsed/r3s_C64_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C64_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r3s_C64_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C64_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set xrange [0.6:121.78999999999998]
set yrange [35:70]
set title "64 projects, instance 2, replica 1"
plot "Parsed/r1s_C64_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C64_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r1s_C64_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C64_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 2, replica 2"
plot "Parsed/r2s_C64_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C64_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r2s_C64_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C64_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 2, replica 3"
plot "Parsed/r3s_C64_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C64_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r3s_C64_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C64_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set xrange [0.6:121.78999999999998]
set yrange [35:70]
set title "64 projects, instance 3, replica 1"
plot "Parsed/r1s_C64_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C64_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r1s_C64_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C64_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 3, replica 2"
plot "Parsed/r2s_C64_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C64_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r2s_C64_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C64_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [35:70]
set title "64 projects, instance 3, replica 3"
plot "Parsed/r3s_C64_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C64_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [870:1050]
set ylabel "Budget"
plot "Parsed/r3s_C64_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C64_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
unset multiplot
