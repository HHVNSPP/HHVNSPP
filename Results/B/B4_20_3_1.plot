set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 1"
set yrange [18000.0:247500.00000000003]
plot "Parsed/r1_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 2"
set yrange [27000.0:253000.00000000003]
plot "Parsed/r1_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 3"
set yrange [40500.0:330000.0]
plot "Parsed/r1_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 4"
set yrange [13500.0:313500.0]
plot "Parsed/r1_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Budget"
set yrange [421425000.0:534600000.00000006]
plot "Parsed/r1_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set term postscript eps font ",12" size 2, 6 color
set key off
set logscale x
set boxwidth 0.1 absolute
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20_3_1.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r1_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
