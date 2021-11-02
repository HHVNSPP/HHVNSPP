set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 1"
set yrange [49500.0:341000.0]
plot "Parsed/r2_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 2"
set yrange [4500.0:286000.0]
plot "Parsed/r2_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 3"
set yrange [18000.0:253000.00000000003]
plot "Parsed/r2_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 4"
set yrange [4050.0:80850.0]
plot "Parsed/r2_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 5"
set yrange [27000.0:105600.00000000001]
plot "Parsed/r2_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 6"
set yrange [4050.0:33000.0]
plot "Parsed/r2_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 7"
set yrange [16200.0:231000.00000000003]
plot "Parsed/r2_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 8"
set yrange [86400.0:369600.00000000006]
plot "Parsed/r2_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 9"
set yrange [27000.0:323400.0]
plot "Parsed/r2_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Budget"
set yrange [581850000.0:825000000.0000001]
plot "Parsed/r2_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_30_2_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r2_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
