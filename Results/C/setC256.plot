set term postscript eps size 24, 12 color
set output "setC256.eps"
set logscale x
set boxwidth 0.06 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
set multiplot layout 3, 6
set xrange [0.6:121.78999999999998]
set yrange [170:270]
set title "256 projects, instance 1, replica 1"
set ylabel "Front size"
plot "Parsed/r1s_C256_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C256_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r1s_C256_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C256_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 1, replica 2"
set ylabel "Front size"
plot "Parsed/r2s_C256_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C256_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r2s_C256_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C256_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 1, replica 3"
set ylabel "Front size"
plot "Parsed/r3s_C256_1.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C256_1.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r3s_C256_1.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C256_1.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set xrange [0.6:121.78999999999998]
set yrange [170:270]
set title "256 projects, instance 2, replica 1"
set ylabel "Front size"
plot "Parsed/r1s_C256_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C256_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r1s_C256_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C256_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 2, replica 2"
set ylabel "Front size"
plot "Parsed/r2s_C256_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C256_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r2s_C256_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C256_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 2, replica 3"
set ylabel "Front size"
plot "Parsed/r3s_C256_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C256_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r3s_C256_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C256_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set xrange [0.6:121.78999999999998]
set yrange [170:270]
set title "256 projects, instance 3, replica 1"
set ylabel "Front size"
plot "Parsed/r1s_C256_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r1_C256_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r1s_C256_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r1_C256_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 3, replica 2"
set ylabel "Front size"
plot "Parsed/r2s_C256_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C256_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r2s_C256_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C256_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
set yrange [170:270]
set title "256 projects, instance 3, replica 3"
set ylabel "Front size"
plot "Parsed/r3s_C256_3.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r3_C256_3.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [3650:3920]
set ylabel "Budget"
plot "Parsed/r3s_C256_3.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r3_C256_3.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
unset multiplot
