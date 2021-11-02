set term postscript eps size 4, 4 color
set output "setC128_2_2.eps"
set xrange [0.6:121.78999999999998]
set multiplot layout 2, 1
set logscale x
set boxwidth 0.06 absolute
set style fill solid border -1
                    set xtics 1, 2
set xlabel "Iteration"
set yrange [90:140]
set ylabel "Front size"
plot "Parsed/r2s_C128_2.txt" u (0.7 * ($1 + 0.1)):8:7:11:10 t "with" with candlesticks lt -1 lw 1 lc rgb "#336699" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#336699" ,\
     "Parsed/r2_C128_2.txt" u (1.2 * ($1 + 0.1)):8:7:11:10 t "without" with candlesticks lt -1 lw 1 lc rgb "#330099" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):9:9:9:9 notitle with candlesticks lt -1 lw 2 lc rgb "#330099" 
set yrange [1700:2050]
set ylabel "Budget"
plot "Parsed/r2s_C128_2.txt" u (0.7 * ($1 + 0.1)):3:2:6:5 t "with" with candlesticks lt -1 lw 1 lc rgb "#996633" whiskerbars, \
     "" u (0.7 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#996633" ,\
     "Parsed/r2_C128_2.txt" u (1.2 * ($1 + 0.1)):3:2:6:5 t "without" with candlesticks lt -1 lw 1 lc rgb "#990033" whiskerbars, \
     "" u (1.2 * ($1 + 0.1)):4:4:4:4 notitle with candlesticks lt -1 lw 2 lc rgb "#990033" 
